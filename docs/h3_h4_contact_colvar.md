### Интерактивная визуализация контактной коллективной переменной в гистонах H3-H4
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
        var radius = 1;
        var subdiv = 5;
        nucl.addRepresentation('cartoon', {
           "sele": ":A :E", "color": 0x020AED,"aspectRatio":aspectRatio, "radius":radius,"radiusSegments":1,"capped":0,"subdiv":subdiv });
        nucl.addRepresentation('cartoon', {
           "sele": ":B :F", "color": "green","aspectRatio":aspectRatio, "radius":radius,"radiusSegments":1,"capped":0,"subdiv":subdiv });
        nucl.addRepresentation('cartoon', {
           "sele": ":C :G", "color": 0xE0F705,"aspectRatio":aspectRatio, "radius":radius,"radiusSegments":1,"capped":0,"subdiv":subdiv });
        nucl.addRepresentation('cartoon', {
           "sele": ":D :H", "color": 0xCE0000,"aspectRatio":aspectRatio, "radius":radius,"radiusSegments":1,"capped":0,"opacity":0.25,"subdiv":subdiv });
        nucl.addRepresentation('cartoon', {
           "sele": "nucleic", "color": "grey","aspectRatio":aspectRatio, "radius":radius,"radiusSegments":1,"capped":0,"opacity":0.25,"subdiv":subdiv });
        nucl.addRepresentation('hyperball', {
           "sele": "(:A and ( 62 70 103 121 124 99)) or (:B and ( 26 34 58))","color": "yellow"});
        nucl.addRepresentation('hyperball', {
           "sele":" (:B and (29  49 50  57))","color": "red"});    
        nucl.addRepresentation('contact', { 
          "sele":" (:B and (29  49 50  57)) or (:A and ( 62 70 103 121 124 99)) or (:B and ( 26 34 58))", 
          hydrophobic:true,backboneHydrogenBond: false,hydrogenBond: false, maxHydrophobicDist:4.5,
           "color": "yellow", radius:0.2});  
        
        nucl.autoView(); 
      });
    });
  </script>
  <div id="viewport" style="width:500px; height:500px;"></div>
</body>
</html>
