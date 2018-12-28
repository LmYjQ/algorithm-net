$(function(){
  $.get('/graph', function(result) {
    var style = [
      { selector: 'node[label = "Person"]',
      css: {'background-color': '#6FB1FC','content': 'data(name)'},
    },
      { selector: 'node[label = "Movie"]', 
      css: {'background-color': '#F5A45D','content': 'data(title)'}, 
    },
    { selector: 'edge', 
    css: {'background-color': '#F5A45D','content': 'data(relationship)'}, 
  }
    ];

    var cy = cytoscape({
      container: document.getElementById('cy'),
      style: style,
      layout: { name: 'cose', fit: false },      
      elements: result.elements
    });
  }, 'json');  
});
