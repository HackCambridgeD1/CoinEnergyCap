class Visuals extends HTMLElement {
  connectedCallback() {
    this.innerHTML = `
      <div>         
        jjjjjj   
      </div>
    `;
  }
}

customElements.define('visual-component', Visuals);


var svgCircles = $('.wrapper svg circle');

// animating example
var i = 0;
setInterval(function() {
  "use strict";
  if(i <= 100){
     miProgressbar(svgCircles, i);
    i++;
  }
}, 50);

svgCircles.each(function() {
  "use strict";
  var $this = $(this),
    $parent = $this.parent(),
    SVG = miSVGdata($this);

  $this.attr('r', SVG.radius);
  $parent.css({
    'top': SVG.strokeWidth / 2,
    'left': SVG.strokeWidth / 2
  });
  $parent.attr('viewBox', '0 0 ' + SVG.svgWidth + ' ' + SVG.svgHeight);
  $parent.attr('width', SVG.svgWidth);
  $parent.attr('height', SVG.svgHeight);
});

function miProgressbar(element, ratio) {
  "use strict";
  var SVG = miSVGdata(element);
  element.css({
    'stroke-dasharray': SVG.circum * ratio / 100 + ' ' + SVG.circum
  });
}

function miSVGdata(element) {
  "use strict";
  var svgParent = element.parent(),
    strokeWidth = parseInt(element.attr('stroke-width'), 10),
    img = element.parents('.wrapper').find('img'),
    svgWidth = parseInt(img.attr('width'), 10) + strokeWidth,
    svgHeight = parseInt(img.attr('height'), 10) + strokeWidth,
    circum, radius, svgObj;

  img.css({
    top: strokeWidth,
    left: strokeWidth
  });
  radius = svgWidth / 2 - strokeWidth / 2;
  circum = parseInt(2 * radius * 3.14, 10);
  svgObj = {
    svgWidth: svgWidth,
    svgHeight: svgHeight,
    parent: svgParent,
    strokeWidth: strokeWidth,
    radius: radius,
    circum: circum
  };
  return svgObj;
}