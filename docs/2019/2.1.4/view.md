### Визуализация области наилучших взаимодействий, обнаруженных при помощи Peptogrid2, область выделена желтым
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
  <p style="color:#efea3e;font-size:18px;font-family:verdana;font-weight: bold;text-shadow: -1px 0 black, 0 1px black, 1px 0 black, 0 -1px black">Изоповерхность оценочной функции Peptogrid</p>
 
 
  <script src="https://unpkg.com/ngl@2.0.0-dev.35/dist/ngl.js"></script>
  <script>
    document.addEventListener("DOMContentLoaded", function () {
      var stage = new NGL.Stage("viewport",{ backgroundColor:"#FFFFFF" });
      stage.setSpin(true);
      stage.loadFile("c_sum.mrc").then(function (o) {
        o.addRepresentation("surface", {
          colorScheme: "uniform",
          colorValue: 0xefea3e,
          isolevel: 20,
          smooth: 2,
          isolevelType: 'value',
          opacity:0.4
        })
        o.autoView()
      });
  
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
      function addElement (el) {
        Object.assign(el.style, {
          zIndex: 10
        })
        stage.viewer.container.appendChild(el)
      }

      function createElement (name, properties, style) {
        var el = document.createElement(name)
        Object.assign(el, properties)
        Object.assign(el.style, style)
        return el
      }
      var centerButton = createElement("input", {
        type: "button",
        value: "Автовращение",
        onclick: function () {
          stage.toggleSpin()
        }
      }, { top: "12px", left: "12px" })
      addElement(centerButton)      
      
    });
  </script>
  <div id="viewport" style="width:500px; height:500px; border: thin solid black"></div>

</body>
</html>
