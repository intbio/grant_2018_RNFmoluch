
### Траектория молекулярной динамики димера гистонов Н2А/Н2В с участком ДНК 30 пар нуклеотидов
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
      stage.loadFile("sys_ref.pdb").then(function (nucl) {
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
        NGL.autoLoad("sys_md_skip20.xtc").then(function (frames) {
          nucl.addTrajectory(frames);
          var traj = nucl.trajList[0].trajectory;
          var player = new NGL.TrajectoryPlayer( traj,{step: 1, timeout: 20, direction : "bounce"});
          player.play();
        });  
        nucl.autoView();
      });
    });
  </script>
  <div id="viewport" style="width:500px; height:500px;"></div>
</body>
</html>
