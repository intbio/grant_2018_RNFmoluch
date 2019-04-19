### TEST

<html lang="en">
<head>
  <meta charset="utf-8">
</head>
<body>
  <script src="https://unpkg.com/ngl@0.10.4/dist/ngl.js"></script>
  <script>
    document.addEventListener("DOMContentLoaded", function () {
      var stage = new NGL.Stage("viewport");
      stage.loadFile("only_nucl_init_chains.pdb", {defaultRepresentation: true});
    });
  </script>
  <div id="viewport" style="width:500px; height:500px;"></div>
</body>
</html>
