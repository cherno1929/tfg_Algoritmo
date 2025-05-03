
const form_benchmark = document.getElementById("form_benchmarck")
var graphs
var algorithm_type

form_benchmark.addEventListener('submit', async (event) => {
    //Avoid to send data directly
    event.preventDefault()

    //Entract data from form
    let form_data  = new FormData(form_benchmark)
    let data = Object.fromEntries(form_data.entries())

    // Check if all data is correct
    // ...

    //Send data to server
    try{

        show_hide_loading_animation()

        let response = await fetch('/api/benchmarks/general', {
            method : 'POST',
            headers:{
                'Content-Type': 'application/json',
            },
            body : JSON.stringify(data)
        })

        if (response.ok){
            solution = await response.json()
            graphs = solution
            console.log(graphs)
            algorithm_type = graphs[-1]
            delete graphs[-1]
            show_hide_loading_animation()
            draw_line_graphics(graph_to_linear_data(graphs), "#line_graphic")
            draw_line_graphics(graph_to_error_data(graphs), "#error_graphic")
            draw_bar_graphics(graph_to_node_link_data(graphs), "#nl_graphic")
            draw_table(graphs)
        }
        
    }catch(error){
        console.error(error)
    }

})

function show_hide_loading_animation(){
    elements = ["line_graphic", "nl_graphic", "error_graphic", "loading_animation_1", "loading_animation_2", "loading_animation_3"]
    elements.forEach(element => {
        show_hide_element(document.getElementById(element))
    });
}

function show_hide_element(element){
    if(element.style.display === "block"){
        element.style.display = "none"
    }else{
        element.style.display = "block"
    }
}

function draw_table(solutions){
    let table = document.getElementById("table_graph")
    table.innerHTML = ""
    line_count = 0
    if (algorithm_type == 'g'){
        algorithm_type = 'Greedy'
    } else if (algorithm_type == 'o'){
        algorithm_type = 'Optimal'
    }else{
        algorithm_type = 'Random'
    }
    draw_table_line(solutions)
}

var line_count = 0

function draw_table_line(solutions){
    let table = document.getElementById("table_graph")
    for (let n_sol in solutions){
        solutions[n_sol].forEach(element => {
            table.innerHTML += `<tr>
                                    <th scope="row">${line_count}</th>
                                    <td>${element.graph.nodes.length}</th>
                                    <td>${element.graph.links.length}</td>
                                    <td>${algorithm_type}</td>
                                    <td>${element.solution != null ? '[' + element.solution + ']' : element.solution}</td>
                                    <td>${element.time_to_solve}</td>
                                  </tr>`
            line_count++
        });
        if(line_count > 100){
            break
        }
    }
}

function graph_to_error_data(data){
    let info = []
    for (let key in data){
        n_error = 0
        data[key].forEach(element => {
            if (element.solution == null){
                n_error += 1
            }
        });
        info.push({x : parseInt(key), y : (n_error / data[key].length * 100)})
    }
    return info
}

function graph_to_linear_data(data){
    let info = []
    let n_sample = Number(document.getElementById("n_sample").value)
    for (let key in data){
        time_to_process = 0
        data[key].forEach(element => {
            if (element.solution != null){
                time_to_process += element.time_to_solve
            }
        });
        time_to_process /= n_sample
        info.push({x : parseInt(key), y : time_to_process})
    }
    return info
}

function graph_to_node_link_data(data){
    let info = []
    for (let key in data){
        n_link = 0
        data[key].forEach(element => {
            n_link += element.graph.links.length
        });
        n_link /= data[key].length
        info.push({x : parseInt(key), y : n_link})
    }
    return info
}

function draw_bar_graphics(data, svg_id){
    
    let html_element = document.getElementById(svg_id.substr(1, svg_id.length))
    html_element.innerHTML = ""
    
    let dimensions = html_element.getBoundingClientRect()

    const width = dimensions.width;
    const height = dimensions.height;
    const margin = { top: 30, right: 30, bottom: 70, left: 50 };

    // Create svg
    const svg = d3.select(svg_id)
        .append("svg")
        .attr("width", width)
        .attr("height", height);

    // Create dimensions of svg
    const x = d3.scaleBand()
        .domain(data.map(d => d.x)) 
        .range([margin.left, width - margin.right])
        .padding(0.2); 

    const y = d3.scaleLinear()
        .domain([0, d3.max(data, d => d.y)]) 
        .nice() 
        .range([height - margin.bottom, margin.top]); 

    // Draw bars
    svg.selectAll(".bar")
        .data(data)
        .enter().append("rect")
        .attr("class", "bar")
        .attr("x", d => x(d.x))
        .attr("y", d => y(d.y))
        .attr("width", x.bandwidth())  
        .attr("height", d => height - margin.bottom - y(d.y)); 

    // Add axis
    svg.append("g")
        .attr("transform", `translate(0,${height - margin.bottom})`)
        .call(d3.axisBottom(x))  // Axi X
        .selectAll("text")
        .attr("transform", "rotate(-45)")
        .style("text-anchor", "end")
        //.text("Nº Nodes")

    svg.append("g")
        .attr("transform", `translate(${margin.left},0)`)
        .call(d3.axisLeft(y))
        //.text("Nº Errors") // Axi Y

    // Add names
    svg.selectAll(".label")
        .data(data)
        .enter().append("text")
        .attr("class", "label")
        .attr("x", d => x(d.x) + x.bandwidth() / 2) 
        .attr("y", d => y(d.y) - 5) 
        .text(d => d.y)
        .style("fill", "black");
}

function draw_line_graphics(data, svg_id){

    let id = svg_id.substr(1, svg_id.length)
    document.getElementById(id).innerHTML = ""
    const svgReal = document.getElementById(id).getBoundingClientRect()

    const width = svgReal.width
    const height = svgReal.height
    const margin = { top: 20, right: 30, bottom: 30, left: 40 }

    const xScale = d3.scaleLinear()
    .domain(d3.extent(data, d => d.x)) 
    .range([margin.left, width - margin.right]); 

    const yScale = d3.scaleLinear()
    .domain([0, d3.max(data, d => d.y)])
    .range([height - margin.bottom, margin.top]); 


    const svg = d3.select(svg_id);

    // Add axis
    svg.append("g")
        .attr("transform", `translate(0,${height - margin.bottom})`)
        .call(d3.axisBottom(xScale))
        //.text("Nº Nodes")

    svg.append("g")
        .attr("transform", `translate(${margin.left},0)`)
        .call(d3.axisLeft(yScale))
        //.text(svg_id => svg_id === "#line_graphic" ? "Time (sec)" : "")

    const line = d3.line()
        .x(d => xScale(d.x))
        .y(d => yScale(d.y))

    // Add lines
    svg.append("path")
        .datum(data) 
        .attr("fill", "none")
        .attr("stroke", "steelblue")
        .attr("stroke-width", 2)
        .attr("d", line); 

}

function modificar_formulario(){
    let type_algorithm = document.getElementById("select-algorithm").value
    if (type_algorithm === "r"){
        document.getElementById("option_algorithm").innerHTML = `<p>Propability of activating a node</p>
                                    <input type="number" id="ramdom_activation" name="ramdom_activation" value="20">`
    }else if (type_algorithm === "g"){
        document.getElementById("option_algorithm").innerHTML = `<p>Porcentage of destrion</p>
                                    <input type="number" id="greedy_destruction" name="greedy_destruction" value="5">`
    }
}

function download_graphs(){
    let header = "Numero Nodes;Numero Links;Algorithm;Solution;Time to solve\n"
    let lines = ""
    for (let key in graphs){
        graphs[key].forEach(element => {
            lines += key + ";" + element.graph.links.length + ";" + algorithm_type + ";" + element.solution +";" + element.time_to_solve.toLocaleString('es-ES') + "\n"
        });
    }

    const csvString = header + lines
    const blob = new Blob([csvString], { type: "text/csv;charset=utf-8;" });
    const url = URL.createObjectURL(blob);


    const link = document.createElement("a");
    link.href = url;
    link.download = "grafos.csv";
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
    URL.revokeObjectURL(url); // Free url
}