### Визуализация результатов докинга пептида LANA на кислотный лоскут нуклеосомы в программном пакете CabsDock
[Назад](https://intbio.org/grant_2018_RNFmoluch/year2.html)

<html lang="en">
<head>
  <meta charset="utf-8">
</head>
<body>
  <p style="color:#94b4d1;font-size:22px;font-family:verdana;font-weight: bold;text-shadow: -1px 0 black, 0 1px black, 1px 0 black, 0 -1px black;display: inline">H3</p> 
  <p style="color:#94d19c;font-size:22px;font-family:verdana;font-weight: bold;text-shadow: -1px 0 black, 0 1px black, 1px 0 black, 0 -1px black;display: inline">H4</p>
  <p style="color:#d6d989;font-size:22px;font-family:verdana;font-weight: bold;text-shadow: -1px 0 black, 0 1px black, 1px 0 black, 0 -1px black;display: inline">H2A</p>
  <p style="color:#d98989;font-size:22px;font-family:verdana;font-weight: bold;text-shadow: -1px 0 black, 0 1px black, 1px 0 black, 0 -1px black;display: inline">H2B</p>
  <p style="color:#d6d6d6;font-size:22px;font-family:verdana;font-weight: bold;text-shadow: -1px 0 black, 0 1px black, 1px 0 black, 0 -1px black;display: inline">ДНК</p>
  <p style="color:#ffffff;font-size:22px;font-family:verdana;font-weight: bold;text-shadow: -1px 0 black, 0 1px black, 1px 0 black, 0 -1px black">LANA</p>
  
  <p style="color:#1f77b4;font-size:22px;font-family:verdana;font-weight: bold;text-shadow: -1px 0 black, 0 1px black, 1px 0 black, 0 -1px black;display: inline">Поза # 0</p>
  <p style="color:#xff7f0e;font-size:22px;font-family:verdana;font-weight: bold;text-shadow: -1px 0 black, 0 1px black, 1px 0 black, 0 -1px black;display: inline">Поза # 1</p>
  <p style="color:#2ca02c;font-size:22px;font-family:verdana;font-weight: bold;text-shadow: -1px 0 black, 0 1px black, 1px 0 black, 0 -1px black;display: inline">Поза # 2</p>
  <p style="color:#d62728;font-size:22px;font-family:verdana;font-weight: bold;text-shadow: -1px 0 black, 0 1px black, 1px 0 black, 0 -1px black;display: inline">Поза # 3</p>
  <p style="color:#9467bd;font-size:22px;font-family:verdana;font-weight: bold;text-shadow: -1px 0 black, 0 1px black, 1px 0 black, 0 -1px black;display: inline">Поза # 4</p>
  <br>
  <p style="color:#8c564b;font-size:22px;font-family:verdana;font-weight: bold;text-shadow: -1px 0 black, 0 1px black, 1px 0 black, 0 -1px black;display: inline">Поза # 5</p>
  <p style="color:#e377c2;font-size:22px;font-family:verdana;font-weight: bold;text-shadow: -1px 0 black, 0 1px black, 1px 0 black, 0 -1px black;display: inline">Поза # 6</p>
  <p style="color:#7f7f7f;font-size:22px;font-family:verdana;font-weight: bold;text-shadow: -1px 0 black, 0 1px black, 1px 0 black, 0 -1px black;display: inline">Поза # 7</p>
  <p style="color:#bcbd22;font-size:22px;font-family:verdana;font-weight: bold;text-shadow: -1px 0 black, 0 1px black, 1px 0 black, 0 -1px black;display: inline">Поза # 8</p>
  <p style="color:#17becf;font-size:22px;font-family:verdana;font-weight: bold;text-shadow: -1px 0 black, 0 1px black, 1px 0 black, 0 -1px black;display: inline">Поза # 9</p>
 
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
           
        nucl.addRepresentation('tube', {
           "sele": ":K", "color": 0xffffff,"aspectRatio":aspectRatio, "radius":0.5,"radiusSegments":1,"capped":0 });
        nucl.addRepresentation('tube', {
           "sele": ":L", "color": 0x1f77b4,"aspectRatio":aspectRatio, "radius":0.5,"radiusSegments":1,"capped":0 });
        nucl.addRepresentation('tube', {
           "sele": ":M", "color": 0xff7f0e,"aspectRatio":aspectRatio, "radius":0.5,"radiusSegments":1,"capped":0 });
        nucl.addRepresentation('tube', {
           "sele": ":N", "color": 0x2ca02c,"aspectRatio":aspectRatio, "radius":0.5,"radiusSegments":1,"capped":0 });
        nucl.addRepresentation('tube', {
           "sele": ":O", "color": 0xd62728,"aspectRatio":aspectRatio, "radius":0.5,"radiusSegments":1,"capped":0 });
        nucl.addRepresentation('tube', {
           "sele": ":P", "color": 0x9467bd,"aspectRatio":aspectRatio, "radius":0.5,"radiusSegments":1,"capped":0 });
        nucl.addRepresentation('tube', {
           "sele": ":Q", "color": 0x8c564b,"aspectRatio":aspectRatio, "radius":0.5,"radiusSegments":1,"capped":0 });
        nucl.addRepresentation('tube', {
           "sele": ":R", "color": 0xe377c2,"aspectRatio":aspectRatio, "radius":0.5,"radiusSegments":1,"capped":0 });
        nucl.addRepresentation('tube', {
           "sele": ":S", "color": 0x7f7f7f,"aspectRatio":aspectRatio, "radius":0.5,"radiusSegments":1,"capped":0 });
        nucl.addRepresentation('tube', {
           "sele": ":T", "color": 0xbcbd22,"aspectRatio":aspectRatio, "radius":0.5,"radiusSegments":1,"capped":0 });
        nucl.addRepresentation('tube', {
           "sele": ":U", "color": 0x17becf,"aspectRatio":aspectRatio, "radius":0.5,"radiusSegments":1,"capped":0 });

        nucl.autoView();
      });
    });
  </script>
  <div id="viewport" style="width:500px; height:500px; border: thin solid black"></div>
</body>
</html>
