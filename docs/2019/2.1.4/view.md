### Визуализация результатов докинга пептида LANA на кислотный лоскут нуклеосомы в программном пакете CabsDock
[Назад](https://intbio.org/grant_2018_RNFmoluch/year2.html)

<html lang="en">
<head>
  <meta charset="utf-8">
</head>
<body>
 
 
  <script src="https://unpkg.com/ngl@2.0.0-dev.35/dist/ngl.js"></script>
  <script>
    document.addEventListener("DOMContentLoaded", function () {
      var stage = new NGL.Stage("viewport",{ backgroundColor:"#FFFFFF" });
      stage.loadFile("1kx5_ntm.pdb").then(function (nucl) {
        var aspectRatio = 2;
        var radius = 1.5;

        nucl.addRepresentation('cartoon', {
           "sele": ":A :E", "color": 0x94b4d1,"aspectRatio":aspectRatio, "radius":radius,"radiusSegments":1,"capped":0 });
        nucl.addRepresentation('cartoon', {
           "sele": ":B :F", "color": 0x94d19c,"aspectRatio":aspectRatio, "radius":radius,"radiusSegments":1,"capped":0 });
        nucl.addRepresentation('cartoon', {
           "sele": ":C :G", "color": 0xd6d989,"aspectRatio":aspectRatio, "radius":radius,"radiusSegments":1,"capped":0 });
        nucl.addRepresentation('cartoon', {
           "sele": ":D :H", "color": 0xd98989,"aspectRatio":aspectRatio, "radius":radius,"radiusSegments":1,"capped":0 });
        nucl.addRepresentation('cartoon', {
           "sele": "nucleic", "color": 0xd6d6d6,"aspectRatio":aspectRatio, "radius":radius,"radiusSegments":1,"capped":0 });
        nucl.addRepresentation('base', {
           "sele": "nucleic", "color": 0xd6d6d6});
           
       nucl.autoView();
      });
      stage.loadFile("0_sum.mrc").then(function (o) {
        o.addRepresentation("surface", {
          colorScheme: "uniform",
          colorValue: 0xef3e3e,
          isolevel: 20,
          isolevelType: 'value',
          opacity:0.4
        })
        o.autoView()
      });
      
      stage.loadFile("N_sum.mrc").then(function (o) {
        o.addRepresentation("surface", {
          colorScheme: "uniform",
          colorValue: 0x3e5def,
          isolevel: 20,
          isolevelType: 'value',
          opacity:0.4
        })
        o.autoView()
      });
      
      stage.loadFile("c_sum.mrc").then(function (o) {
        o.addRepresentation("surface", {
          colorScheme: "uniform",
          colorValue: 0xefea3e,
          isolevel: 20,
          isolevelType: 'value',
          opacity:0.4
        })
        o.autoView()
      });
      
    });
  </script>
  <div id="viewport" style="width:500px; height:500px;"></div>
</body>
</html>
