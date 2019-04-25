### Интерактивная визуализация геометрических коллективных переменных в гистонах H3-H4
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
      stage.loadFile("assets/h3_h4_dimer_ref.pdb").then(function (nucl) {
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

        shape.addSphere([ 77.92430114746094, 66.87095642089844, 63.1876220703125 ], [ 1,0,0 ],2);
        shape.addSphere([ 87.07524108886719, 80.8552474975586, 58.24094772338867], [ 1,0,0 ],2);
        shape.addSphere([ 75.97905731201172, 113.1738052368164, 52.34953308105469], [ 1,0,0 ],2);
        shape.addSphere([ 62.5819091796875, 122.89144134521484, 46.09333801269531], [ 1,0,0 ],2);
        shape.addSphere([ 82.69573211669922, 97.38047790527344, 55.3990478515625], [ 1,0,0 ],2);
        shape.addCylinder([77.92430114746094, 66.87095642089844, 63.1876220703125], [87.07524108886719, 80.8552474975586, 58.24094772338867], [ 0.6,0.1,0.6 ], 1);
        shape.addCylinder([87.07524108886719, 80.8552474975586, 58.24094772338867], [75.97905731201172, 113.1738052368164, 52.34953308105469], [ 0.6,0.1,0.6 ], 1);
        shape.addCylinder([75.97905731201172, 113.1738052368164, 52.34953308105469], [62.5819091796875, 122.89144134521484, 46.09333801269531], [ 0.6,0.1,0.6 ], 1);
        shape.addCylinder([77.92430114746094, 66.87095642089844, 63.1876220703125], [82.69573211669922, 97.38047790527344, 55.3990478515625], [ 0.6,0.6,0.1 ], 1);
        shape.addCylinder([82.69573211669922, 97.38047790527344, 55.3990478515625], [62.5819091796875, 122.89144134521484, 46.09333801269531], [ 0.6,0.6,0.1 ], 1);
        var shapeComp = stage.addComponentFromObject(shape);
        shapeComp.addRepresentation("buffer");
                
      });
    });
  </script>
  <div id="viewport" style="width:500px; height:500px;"></div>
</body>
</html>
