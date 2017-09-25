'use strict';

const $ = id => document.getElementById(id);

function visualize(json) {
  console.log(json);

  const instance = new sigma({
    graph: json.graph,
    renderer: {
      container: 'graph-container',
      type: 'canvas',
      skipErrors: true,
      labelThreshold: 0,
      labelSize: 'proportional'
    }
  });

  instance.startForceAtlas2({
    worker: true,
    barnesHutOptimize: true,
    adjustSizes: true,
    slowDown: 20,
    strongGravityMode: true
  });

  const drag = sigma.plugins.dragNodes(instance, instance.renderers[0]);
  drag.bind('startdrag', event => {
    if (instance.isForceAtlas2Running()) {
      instance.killForceAtlas2()
    }
  });
}

const xhr = new XMLHttpRequest();
xhr.open('GET', 'graph.json');
xhr.onreadystatechange = () => {
  if (xhr.readyState === XMLHttpRequest.DONE) {
    visualize(JSON.parse(xhr.responseText));
  }
}

xhr.send();
