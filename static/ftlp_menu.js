
const form_graph = document.getElementById("form_graph")

const svg = d3.select("svg"),
      width = +svg.attr("width"),
      height = +svg.attr("height");

form_graph.addEventListener('submit', async (event) => {
    //Avoid to send graph directly
    event.preventDefault()

    let formData = new FormData(form_graph)
    let data = Object.fromEntries(formData.entries())

    try{

        //Send data to server api
        let response = await fetch('/api/algorithms/ftlrp',{
            method: 'POST',
            headers:{
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        })

        if (response.ok){
            solution = await response.json()
            document.getElementById("graph").innerHTML = ""
            show_graph(solution.graph)
            show_regenerators(solution.solution)
        }else{
            console.error("Ocurrio un error")
        }

    }catch(error){
        console.error(error)
    }

})

function show_regenerators(solution_node){
    if(solution_node != null){
        solution_node.forEach(element => {
            d3.selectAll(".node")
            .filter((d) => {return d.id == element})
            .style("fill", "red")
        });
    }
}

function show_graph(graph){
    
  // Create Force Simulation
  const simulation = d3.forceSimulation(graph.nodes)
  .force("link", d3.forceLink(graph.links).id(d => d.id).distance(100))
  .force("charge", d3.forceManyBody().strength(-200))
  .force("center", d3.forceCenter(width / 2, height / 2));

  // Show links
  const link = svg.append("g")
  .attr("class", "links")
  .selectAll("line")
  .data(graph.links)
  .join("line")
  .attr("class", "link");

  // Draw Nodes
  const node = svg.append("g")
  .attr("class", "nodes")
  .selectAll("circle")
  .data(graph.nodes)
  .join("circle")
  .attr("class", "node")
  .attr("r", 10)
  .call(drag(simulation));

  // Add names to nodes
  const labels = svg.append("g")
  .selectAll("text")
  .data(graph.nodes)
  .join("text")
  .attr("x", 12)
  .attr("y", 4)
  .text(d => d.id);

  // Update positions of nodes
  simulation.on("tick", () => {
  link
    .attr("x1", d => d.source.x)
    .attr("y1", d => d.source.y)
    .attr("x2", d => d.target.x)
    .attr("y2", d => d.target.y);

  node
    .attr("cx", d => d.x)
    .attr("cy", d => d.y);

  labels
    .attr("x", d => d.x + 12)
    .attr("y", d => d.y + 4);
  });

  // Dragable functions
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

}
