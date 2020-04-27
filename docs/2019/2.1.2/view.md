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
      stage.loadFile("all_peptides_cabs.pdb").then(function (nucl) {
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
        nucl.addRepresentation('cartoon', {
           "sele": ":V", "tube": 0xffffff,"aspectRatio":aspectRatio, "radius":0.5,"radiusSegments":1,"capped":0 });
        nucl.addRepresentation('cartoon', {
           "sele": ":L", "tube": 0x1f77b4,"aspectRatio":aspectRatio, "radius":0.5,"radiusSegments":1,"capped":0 });
        nucl.addRepresentation('cartoon', {
           "sele": ":M", "tube": 0xff7f0e,"aspectRatio":aspectRatio, "radius":0.5,"radiusSegments":1,"capped":0 });
        nucl.addRepresentation('cartoon', {
           "sele": ":N", "tube": 0x2ca02c,"aspectRatio":aspectRatio, "radius":0.5,"radiusSegments":1,"capped":0 });
        nucl.addRepresentation('cartoon', {
           "sele": ":O", "tube": 0xd62728,"aspectRatio":aspectRatio, "radius":0.5,"radiusSegments":1,"capped":0 });
        nucl.addRepresentation('cartoon', {
           "sele": ":P", "tube": 0x9467bd,"aspectRatio":aspectRatio, "radius":0.5,"radiusSegments":1,"capped":0 });
        nucl.addRepresentation('cartoon', {
           "sele": ":Q", "tube": 0x8c564b,"aspectRatio":aspectRatio, "radius":0.5,"radiusSegments":1,"capped":0 });
        nucl.addRepresentation('cartoon', {
           "sele": ":R", "tube": 0xe377c2,"aspectRatio":aspectRatio, "radius":0.5,"radiusSegments":1,"capped":0 });
        nucl.addRepresentation('cartoon', {
           "sele": ":S", "tube": 0x7f7f7f,"aspectRatio":aspectRatio, "radius":0.5,"radiusSegments":1,"capped":0 });
        nucl.addRepresentation('cartoon', {
           "sele": ":T", "tube": 0xbcbd22,"aspectRatio":aspectRatio, "radius":0.5,"radiusSegments":1,"capped":0 });
        nucl.addRepresentation('cartoon', {
           "sele": ":U", "tube": 0x17becf,"aspectRatio":aspectRatio, "radius":0.5,"radiusSegments":1,"capped":0 });

        nucl.autoView();
      });
    });
  </script>
  <div id="viewport" style="width:500px; height:500px;"></div>
</body>
</html>
