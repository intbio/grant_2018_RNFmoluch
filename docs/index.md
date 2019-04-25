### TEST

<html lang="en">
<head>
  <meta charset="utf-8">
</head>
<body>
  
  Интерактивные материалы к отчету
за 2018-2019 годы 
по проекту
“Структурная динамика нуклеосом и их взаимодействий: поиск подходов для диагностики и лечения онкологических заболеваний.”
  
  <script src="https://unpkg.com/ngl@0.10.4/dist/ngl.js"></script>
  <script>
    document.addEventListener("DOMContentLoaded", function () {
      var stage = new NGL.Stage("viewport",{ backgroundColor:"#FFFFFF" });
      stage.loadFile("only_nucl_init_chains.pdb").then(function (nucl) {
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
        nucl.addRepresentation('base', {
           "sele": "nucleic", "color": "grey"});
        nucl.autoView();
        NGL.autoLoad("md_10drames.dcd").then(function (frames) {
          nucl.addTrajectory(frames);
          var traj = nucl.trajList[0].trajectory;
          var player = new NGL.TrajectoryPlayer( traj,{step: 1, timeout: 500});
          player.play();
        });      
      });
    });
  </script>
  <div id="viewport" style="width:500px; height:500px;"></div>
</body>
</html>
