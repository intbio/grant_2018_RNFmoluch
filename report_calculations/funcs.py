import os
import urllib.request
import json
import nglview as nv
import MDAnalysis as mda


def view_nucl(*args,gui=False,colors='nucl',size=(800,600),aspectRatio=2,radius=1.5):
    if type(args[0]) == mda.core.universe.Universe:
        nuclMD=args[0]
    else:
        nuclMD=mda.Universe(*args)
    #prot = nuclMD.select_atoms("protein")
    show=nv.show_mdanalysis(nuclMD,gui=gui)
    if colors=='nucl':
        show.representations = [
        {"type": "cartoon", "params": {
            "sele": ":A :E", "color": 0x020AED,"aspectRatio":aspectRatio, "radius":radius,"radiusSegments":1,"capped":0
        }},
        {"type": "cartoon", "params": {
            "sele": ":B :F", "color": "green","aspectRatio":aspectRatio, "radius":radius,"radiusSegments":1,"capped":0
        }},
        {"type": "cartoon", "params": {
            "sele": ":C :G", "color": 0xE0F705,"aspectRatio":aspectRatio, "radius":radius,"radiusSegments":1,"capped":0
        }},
        {"type": "cartoon", "params": {
            "sele": ":D :H", "color": 0xCE0000,"aspectRatio":aspectRatio, "radius":radius,"radiusSegments":1,"capped":0
        }},
        {"type": "cartoon", "params": {
            "sele": "nucleic", "color": "grey","aspectRatio":aspectRatio, "radius":radius,"radiusSegments":1,"capped":0
        }},
        {"type": "base", "params": {
            "sele": "nucleic", "color": "grey",
        }},
        ]
    else:
        show.representations = [
        {"type": "cartoon", "params": {
            "sele": "protein", "color": colors,"aspectRatio":aspectRatio, "radius":radius,"radiusSegments":1,"capped":0
        }},
        {"type": "base", "params": {
            "sele": "nucleic", "color": colors,
        }},
        ]
    show.camera = 'orthographic'
    show._remote_call('setSize',target='Widget',args=['%dpx'%size[0],'%dpx'%size[1]])
    return show

def nv_save_image(view,image_name):
    view.render_image(factor=12)
    data=str.encode(view._image_data)
    #view._display_image()
    fh = open(image_name, "wb")
    fh.write(base64.decodebytes(data))
    fh.close()


def get_files_from_git(gitapiurl,savefoldername):
    os.mkdir(savefoldername)
    json_url = urllib.request.urlopen(gitapiurl)
    data = json.loads(json_url.read())
    for d in data:
        if(d['type']=='file'):
            print("Downloading "+os.path.join(savefoldername,d['name']))
            urllib.request.urlretrieve(d['download_url'],os.path.join(savefoldername,d['name']))
        if(d['type']=='dir'):
            get_files_from_git(d['url'],os.path.join(savefoldername,d['name']))

  
