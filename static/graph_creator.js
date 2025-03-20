
let html_element = document.getElementById("svg_data")
html_element.innerHTML = ""

let dimensions = html_element.getBoundingClientRect()

const width = dimensions.width;
const height = dimensions.height;
const svg = d3.select("svg");

let nodes = [];
let links = [];
let selectedNode = null;
let tempLink = null;

const simulation = d3.forceSimulation(nodes)
    .force("link", d3.forceLink(links).id(d => d.id).distance(100))
    .force("charge", d3.forceManyBody().strength(-5))
    //.force("center", d3.forceCenter(width / 2, height / 2));

function update() {
    svg.selectAll("line").remove();
    svg.selectAll("circle").remove();

    // Draw links
    svg.selectAll("line")
        .data(links)
        .enter().append("line")
        .on("click", handleLinkClick);

    // Draw nodes
    const node = svg.selectAll("circle")
        .data(nodes)
        .enter().append("circle")
        .attr("r", 10)
        .style("fill", d => d.isGen ? "red" : "blue")
        .call(drag(simulation))
        .on("click", handleNodeClick)
        .on("contextmenu", handle_node_right_click);

    svg.selectAll(".link-label").remove();

        // Draw link distances
    const linkLabels = svg.selectAll(".link-label")
        .data(links)
        .enter().append("text")
        .attr("class", "link-label")
        .attr("font-size", "12px")
        .text(d => d.distance);

    svg.selectAll(".node-label").remove()

    const node_label = svg.selectAll(".node-label")
        .data(nodes)
        .enter().append("text")
        .attr("class", "node-label")
        .attr("font-size", "12px")
        .text(d => d.id)

    simulation.nodes(nodes).on("tick", () => {
        svg.selectAll("line")
            .attr("x1", d => d.source.x)
            .attr("y1", d => d.source.y)
            .attr("x2", d => d.target.x)
            .attr("y2", d => d.target.y);

        svg.selectAll("circle")
            .attr("cx", d => d.x)
            .attr("cy", d => d.y);

        svg.selectAll(".link-label")
            .attr("x", d => (d.source.x + d.target.x) / 2) 
            .attr("y", d => (d.source.y + d.target.y) / 2)
            .text(d => d.distance);

        svg.selectAll(".node-label")
            .attr("x", d => d.x + 12)
            .attr("y", d => d.y + 4)
            .text(d => d.id)

    });

    simulation.force("link").links(links);
    simulation.alpha(1).restart();

}

// Create link between nodes
function handleNodeClick(event, d) {
    if (!selectedNode) {
        // Select first node
        console.log(d)
        selectedNode = d;
        // Draw link
        tempLink = svg.append("line")
            .attr("stroke", "gray")
            .attr("stroke-dasharray", "5,5");

        // Follow mouse 
        svg.on("mousemove", (event) => {
            if (tempLink) {
                let [x, y] = d3.pointer(event, svg.node()) // Coords of svg

                // Adjust coords
                let adjustedX = x 
                let adjustedY = y 

                tempLink
                    .attr("x1", selectedNode.x)
                    .attr("y1", selectedNode.y)
                    .attr("x2", adjustedX)
                    .attr("y2", adjustedY)
            }
        });


    // If is node
    } else if (selectedNode !== d) {
        // Get distance of link
        let distance = parseFloat(prompt("Ingrese la distancia del enlace:", "100"));

        // Validate distance
        if (isNaN(distance) || distance <= 0) {
            alert("Distancia inválida. Se usará la distancia por defecto (100).");
            distance = 100;
        }

        // Add link
        links.push({ source: selectedNode, target: d, distance: distance });

        // Update visuals
        selectedNode = null;
        tempLink.remove();
        tempLink = null;
        svg.on("mousemove", null);

        update();
    }
}

function handle_node_right_click(event, elem){
    event.preventDefault()
    // Change color of node and change data in graph
    nodes[elem.id].isGen = !nodes[elem.id].isGen
    if (nodes[elem.id].isGen){
        d3.select(this).style("fill", "red")
    }else{
        d3.select(this).style("fill", "blue")
    }
    
}

//Change distance of link when click
function handleLinkClick(event, d) {
    event.stopPropagation(); // Only link will get this event

    let newDistance = parseFloat(prompt("Ingrese la nueva distancia del enlace:", d.distance));

    if (!isNaN(newDistance) && newDistance > 0) {
        d.distance = newDistance; // Update distance of link
        // Update simulation
        simulation.force("link").distance(link => link.distance); 
        simulation.alpha(1).restart(); 
    } else {
        alert("Distancia inválida. Debe ser un número mayor que 0.");
    }
}


// Simulation of force with dragable elements
simulation.force("link", d3.forceLink(links).id(d => d.id).distance(d => d.distance));


    function drag(simulation) {
        function dragstarted(event, d) {
            if (!event.active) simulation.alphaTarget(0.3).restart();
            d.fx = d.x;
            d.fy = d.y;
        }

        function dragged(event, d) {
            d.fx = event.x;
            d.fy = event.y;
        }

        function dragended(event, d) {
            if (!event.active) simulation.alphaTarget(0);
            d.fx = null;
            d.fy = null;
        }

        return d3.drag()
            .on("start", dragstarted)
            .on("drag", dragged)
            .on("end", dragended);
    }

    svg.on("dblclick", (event) => {
        const newNode = { id: nodes.length, x: event.clientX, y: event.clientY, isGen: false };
        nodes.push(newNode);
        update();
});


const form_graph = document.getElementById("form_graph")

form_graph.addEventListener('submit', async () => {
    event.preventDefault()
    
    let data = {
        max_dist : document.getElementById("max_dist").value,
        link : links,
        node : nodes
    }

    let response = await fetch("/api/algorithms/ftlrp_checker", {
        method: 'POST',
        headers:{
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    })
    is_sol = await response.json()
    console.log(is_sol)
    console.log(nodes)
    if(is_sol == true){
        document.getElementById("isSol").innerHTML = "Yes"
        document.getElementById("sol_g").innerHTML = get_gen_nodes(nodes)
    }else{
        show_data(is_sol)
    }
    
})

function get_gen_nodes(data){
    reg_nodes = []
    data.forEach(element => {
        if (element.isGen){
            reg_nodes.push(element.id)
        }
    });
    return reg_nodes
}

function show_data(data){
    if(data.solution != null){
      document.getElementById("isSol").innerHTML = "No"
      document.getElementById("sol_g").innerHTML = data.solution
      document.getElementById("time_sol").innerHTML = data.time_to_solve + " sec"
    }else{
      document.getElementById("isSol").innerHTML = "There is no solution"
      document.getElementById("sol_g").innerHTML = "..."
      document.getElementById("time_sol").innerHTML = "..."
    }
}

update();
