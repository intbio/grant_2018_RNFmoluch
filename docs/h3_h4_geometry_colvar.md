### Интерактивная визуализация геометрических коллективных переменных в гистонах H3-H3
[Назад](index.md)

<html lang="en">
<head>
  <meta charset="utf-8">
</head>
<body>
 
 
  <script src="https://unpkg.com/ngl@2.0.0-dev.35/dist/ngl.js"></script>
  <script>
    document.addEventListener("DOMContentLoaded", function () {
      var stage = new NGL.Stage("viewport",{ backgroundColor:"#FFFFFF" });
      stage.loadFile("assets/h3_h4_tetramer_ref.pdb").then(function (nucl) {
        var aspectRatio = 2;
        var radius = 1.5;
        var subdiv = 5;
        nucl.addRepresentation('cartoon', {
           "sele": ":A :E", "color": 0x020AED,"aspectRatio":aspectRatio, "radius":radius,"radiusSegments":1,"capped":0,"opacity":0.25,"subdiv":subdiv });
        nucl.addRepresentation('cartoon', {
           "sele": ":B :F", "color": "green","aspectRatio":aspectRatio, "radius":radius,"radiusSegments":1,"capped":0,"opacity":0.25,"subdiv":subdiv });
        nucl.addRepresentation('cartoon', {
           "sele": ":C :G", "color": 0xE0F705,"aspectRatio":aspectRatio, "radius":radius,"radiusSegments":1,"capped":0,"opacity":0.25,"subdiv":subdiv });
        nucl.addRepresentation('cartoon', {
           "sele": ":D :H", "color": 0xCE0000,"aspectRatio":aspectRatio, "radius":radius,"radiusSegments":1,"capped":0,"opacity":0.25,"subdiv":subdiv });
        nucl.addRepresentation('cartoon', {
           "sele": "nucleic", "color": "grey","aspectRatio":aspectRatio, "radius":radius,"radiusSegments":1,"capped":0,"opacity":0.25,"subdiv":subdiv });
        nucl.addRepresentation('base', {
           "sele": "nucleic","color": "grey","opacity":0.25});
        nucl.autoView();
        var shape = new NGL.Shape("shape", { disableImpostor: true, radialSegments: 10 });
        shape.addArrow([98.53,  86.59, 69.27 ],[  77.95,120.46, 55.35], [ 0.6,0.6,0.0 ], 1.5);
        shape.addArrow([88.71059861644235, 116.09167992120595, 70.34512048861993 ],[ 84.68191960368208, 78.12231950913258, 78.28850863916509], [ 0.3,0.8,0.0 ], 1.5);
        shape.addArrow([47.93630510150841,  88.96455241383129, 55.589396784705464],[ 73.60507384052082, 121.5008964260798, 62.408533807798584], [ 0.6,0.6,0.0 ], 1.5);
        shape.addArrow([61.94507672836827, 115.82610350425895, 48.549008289439506],[60.216034043658645, 76.86463814070632,   48.6699550510372], [ 0.3,0.8,0.0 ], 1.5);
        shape.addSphere([ 108.81999969482422, 82.2655029296875, 78.23849487304688 ], [ 1,0,0 ],2);
        shape.addSphere([ 97.74500274658203, 129.56399536132812, 63.884498596191406], [ 1,0,0 ],2);
        shape.addSphere([ 54.92850112915039, 131.3939971923828, 51.90049743652344], [ 1,0,0 ],2);
        shape.addSphere([ 37.087501525878906, 83.96499633789062, 47.64400100708008], [ 1,0,0 ],2);
        shape.addCylinder([108.81999969482422, 82.2655029296875, 78.23849487304688],[97.74500274658203, 129.56399536132812, 63.884498596191406], [ 0.6,0.1,0.6 ], 1);
        shape.addCylinder([97.74500274658203, 129.56399536132812, 63.884498596191406],[54.92850112915039, 131.3939971923828, 51.90049743652344], [ 0.6,0.1,0.6 ], 1);
        shape.addCylinder([54.92850112915039, 131.3939971923828, 51.90049743652344],[37.087501525878906, 83.96499633789062, 47.64400100708008], [ 0.6,0.1,0.6 ], 1);
        var shapeComp = stage.addComponentFromObject(shape)
        shapeComp.addRepresentation("buffer")
        shapeComp.autoView()
        
      });
    });
  </script>
  <div id="viewport" style="width:500px; height:500px;"></div>
</body>
</html>
