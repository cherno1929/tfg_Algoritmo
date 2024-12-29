
const form_graph = document.getElementById("form_graph")

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
            redrawGraph(solution.graph)
        }else{
            console.error("Ocurrio un error")
        }

    }catch(error){
        console.error(error)
    }

})

function redrawGraph(graph) {
    let svg = d3.select('svg')
    let width = +svg.attr("width")
    let height = +svg.attr("height")

    const simulation = d3.forceSimulation(graph.nodes)
        .force('link', d3.forceLink(graph.links).id(d => d.id).distance(100))
        .force('charge', d3.forceManyBody().strength(-100))
        .force('center', d3.forceCenter(width / 2, height / 2))

    const link = svg.selectAll('.link')
        .data(graph.links)
        .enter().append('line')
        .attr('class', 'link')

    const node = svg.selectAll('.node')
        .data(graph.nodes)
        .enter().append('circle')
        .attr('class', 'node')
        .attr('r', 10)
        .call(d3.drag()
            .on('start', dragstart)
            .on('drag', dragged)
            .on('end', dragend))

    node.append('title')
        .text(d => d.id)

    simulation.on('tick', () => {
        link
            .attr('x1', d => d.source.x)
            .attr('y1', d => d.source.y)
            .attr('x2', d => d.target.x)
            .attr('y2', d => d.target.y)

        node
            .attr('cx', d => d.x)
            .attr('cy', d => d.y)
    });

}

function dragstart(event) {
    if (!event.active) simulation.alphaTarget(0.3).restart();
    event.subject.fx = event.subject.x;
    event.subject.fy = event.subject.y;
}

function dragged(event) {
    event.subject.fx = event.x;
    event.subject.fy = event.y;
}

function dragend(event) {
    if (!event.active) simulation.alphaTarget(0);
    event.subject.fx = null;
    event.subject.fy = null;
}     