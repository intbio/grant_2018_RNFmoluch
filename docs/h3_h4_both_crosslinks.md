### Интерактивная визуализация димера гистонов H3-H4 с цистеиновыми сшивками
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
      stage.loadFile("assets/h3-h4_tm_mutated_s-s_adjusted_.pdb").then(function (nucl) {
        var aspectRatio = 2;
        var radius = 1.5;
        nucl.addRepresentation('cartoon', {
           "sele": ":A :E", "color": 0x020AED,"aspectRatio":aspectRatio, "radius":radius,"radiusSegments":1,"capped":0 });
        nucl.addRepresentation('cartoon', {
           "sele": ":B :F", "color": "green","aspectRatio":aspectRatio, "radius":radius,"radiusSegments":1,"capped":0 });
        nucl.addRepresentation('cartoon', {
           "sele": ":C :G", "color": 0xE0F705,"aspectRatio":aspectRatio, "radius":radius,"radiusSegments":1,"capped":0 });
        nucl.addRepresentation('cartoon', {
           "sele": ":D :H", "color": 0xCE0000,"aspectRatio":aspectRatio, "radius":radius,"radiusSegments":1,"capped":0 });
        nucl.addRepresentation('cartoon', {
           "sele": "nucleic", "color": "grey","aspectRatio":aspectRatio, "radius":radius,"radiusSegments":1,"capped":0 });
        nucl.addRepresentation('licorice', {
           "sele": "not (.N .O .C) and (104:A 43:B 81:B 82:A)","radius": 0.6});
        nucl.autoView();
        var shape = new NGL.Shape("shape", { disableImpostor: true, radialSegments: 10 })
       shape.addArrow([ 50, 70, 40 ], [ 65.729,  83.095,  21.864 ], [ 1, 0.3, 0.2 ], 0.7)
       shape.addArrow([ 80, 120, 10 ], [ 62.087, 107.969,   3.767 ], [ 1, 0.3, 0.2 ], 0.7)
       shape.addText([ 50, 70, 40 ], [ 0, 0, 0 ], 6, "82H3-81H4")
       shape.addText([ 80, 120, 10 ], [ 0, 0, 0 ], 6, "104H3-43H4")
       var shapeComp = stage.addComponentFromObject(shape)
       shapeComp.addRepresentation("buffer", { wireframe: false })
        
      });
    });
  </script>
  <div id="viewport" style="width:1024px; height:800px;"></div>
</body>
</html>
