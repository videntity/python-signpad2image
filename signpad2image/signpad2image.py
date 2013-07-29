#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4
from PIL import Image, ImageDraw
import json, sys, os, exceptions

try:
   from django.conf import settings
   BLANK_IMAGE=settings.BLANK_SIG_IMAGE
   NO_SIG_IMAGE=settings.NO_SIG_IMAGE   
except ImportError:
   BLANK_IMAGE="blanksig.png"
   NO_SIG_IMAGE="nosig.png"
  

j="""[{"lx":32,"ly":13,"mx":32,"my":12},{"lx":32,"ly":11,"mx":32,"my":13},{"lx":31,"ly":11,"mx":32,"my":11},{"lx":30,"ly":11,"mx":31,"my":11},{"lx":29,"ly":11,"mx":30,"my":11},{"lx":28,"ly":11,"mx":29,"my":11},{"lx":26,"ly":11,"mx":28,"my":11},{"lx":23,"ly":11,"mx":26,"my":11},{"lx":21,"ly":11,"mx":23,"my":11},{"lx":19,"ly":11,"mx":21,"my":11},{"lx":17,"ly":11,"mx":19,"my":11},{"lx":15,"ly":11,"mx":17,"my":11},{"lx":13,"ly":11,"mx":15,"my":11},{"lx":12,"ly":12,"mx":13,"my":11},{"lx":11,"ly":12,"mx":12,"my":12},{"lx":10,"ly":13,"mx":11,"my":12},{"lx":9,"ly":13,"mx":10,"my":13},{"lx":8,"ly":14,"mx":9,"my":13},{"lx":7,"ly":14,"mx":8,"my":14},{"lx":6,"ly":15,"mx":7,"my":14},{"lx":6,"ly":16,"mx":6,"my":15},{"lx":5,"ly":17,"mx":6,"my":16},{"lx":3,"ly":18,"mx":5,"my":17},{"lx":2,"ly":19,"mx":3,"my":18},{"lx":2,"ly":20,"mx":2,"my":19},{"lx":1,"ly":21,"mx":2,"my":20},{"lx":1,"ly":22,"mx":1,"my":21},{"lx":0,"ly":23,"mx":1,"my":22},{"lx":0,"ly":24,"mx":0,"my":23},{"lx":0,"ly":25,"mx":0,"my":24},{"lx":0,"ly":26,"mx":0,"my":25},{"lx":0,"ly":27,"mx":0,"my":26},{"lx":0,"ly":28,"mx":0,"my":27},{"lx":0,"ly":29,"mx":0,"my":28},{"lx":1,"ly":29,"mx":0,"my":29},{"lx":1,"ly":30,"mx":1,"my":29},{"lx":2,"ly":30,"mx":1,"my":30},{"lx":3,"ly":30,"mx":2,"my":30},{"lx":4,"ly":30,"mx":3,"my":30},{"lx":5,"ly":30,"mx":4,"my":30},{"lx":6,"ly":30,"mx":5,"my":30},{"lx":7,"ly":30,"mx":6,"my":30},{"lx":8,"ly":30,"mx":7,"my":30},{"lx":8,"ly":29,"mx":8,"my":30},{"lx":10,"ly":29,"mx":8,"my":29},{"lx":11,"ly":28,"mx":10,"my":29},{"lx":12,"ly":28,"mx":11,"my":28},{"lx":12,"ly":27,"mx":12,"my":28},{"lx":13,"ly":27,"mx":12,"my":27},{"lx":14,"ly":27,"mx":13,"my":27},{"lx":15,"ly":26,"mx":14,"my":27},{"lx":16,"ly":26,"mx":15,"my":26},{"lx":16,"ly":25,"mx":16,"my":26},{"lx":17,"ly":25,"mx":16,"my":25},{"lx":18,"ly":24,"mx":17,"my":25},{"lx":18,"ly":23,"mx":18,"my":24},{"lx":19,"ly":23,"mx":18,"my":23},{"lx":19,"ly":22,"mx":19,"my":23},{"lx":20,"ly":22,"mx":19,"my":22},{"lx":20,"ly":20,"mx":20,"my":22},{"lx":21,"ly":20,"mx":20,"my":20},{"lx":21,"ly":19,"mx":21,"my":20},{"lx":22,"ly":19,"mx":21,"my":19},{"lx":22,"ly":18,"mx":22,"my":19},{"lx":23,"ly":18,"mx":22,"my":18},{"lx":23,"ly":19,"mx":23,"my":18},{"lx":22,"ly":19,"mx":23,"my":19},{"lx":22,"ly":20,"mx":22,"my":19},{"lx":21,"ly":21,"mx":22,"my":20},{"lx":21,"ly":22,"mx":21,"my":21},{"lx":20,"ly":23,"mx":21,"my":22},{"lx":19,"ly":24,"mx":20,"my":23},{"lx":19,"ly":26,"mx":19,"my":24},{"lx":18,"ly":27,"mx":19,"my":26},{"lx":17,"ly":28,"mx":18,"my":27},{"lx":17,"ly":30,"mx":17,"my":28},{"lx":16,"ly":31,"mx":17,"my":30},{"lx":16,"ly":32,"mx":16,"my":31},{"lx":16,"ly":33,"mx":16,"my":32},{"lx":16,"ly":34,"mx":16,"my":33},{"lx":17,"ly":34,"mx":16,"my":34},{"lx":17,"ly":35,"mx":17,"my":34},{"lx":18,"ly":35,"mx":17,"my":35},{"lx":20,"ly":36,"mx":18,"my":35},{"lx":22,"ly":36,"mx":20,"my":36},{"lx":24,"ly":36,"mx":22,"my":36},{"lx":26,"ly":36,"mx":24,"my":36},{"lx":29,"ly":36,"mx":26,"my":36},{"lx":31,"ly":36,"mx":29,"my":36},{"lx":34,"ly":36,"mx":31,"my":36},{"lx":37,"ly":35,"mx":34,"my":36},{"lx":40,"ly":34,"mx":37,"my":35},{"lx":42,"ly":33,"mx":40,"my":34},{"lx":44,"ly":32,"mx":42,"my":33},{"lx":47,"ly":31,"mx":44,"my":32},{"lx":49,"ly":30,"mx":47,"my":31},{"lx":51,"ly":29,"mx":49,"my":30},{"lx":52,"ly":28,"mx":51,"my":29},{"lx":54,"ly":27,"mx":52,"my":28},{"lx":55,"ly":26,"mx":54,"my":27},{"lx":56,"ly":25,"mx":55,"my":26},{"lx":57,"ly":24,"mx":56,"my":25},{"lx":57,"ly":23,"mx":57,"my":24},{"lx":58,"ly":22,"mx":57,"my":23},{"lx":59,"ly":20,"mx":58,"my":22},{"lx":59,"ly":19,"mx":59,"my":20},{"lx":59,"ly":18,"mx":59,"my":19},{"lx":60,"ly":18,"mx":59,"my":18},{"lx":60,"ly":17,"mx":60,"my":18},{"lx":60,"ly":16,"mx":60,"my":17},{"lx":60,"ly":15,"mx":60,"my":16},{"lx":59,"ly":15,"mx":60,"my":15},{"lx":59,"ly":14,"mx":59,"my":15},{"lx":58,"ly":14,"mx":59,"my":14},{"lx":58,"ly":13,"mx":58,"my":14},{"lx":57,"ly":13,"mx":58,"my":13},{"lx":56,"ly":13,"mx":57,"my":13},{"lx":55,"ly":13,"mx":56,"my":13},{"lx":54,"ly":13,"mx":55,"my":13},{"lx":53,"ly":13,"mx":54,"my":13},{"lx":52,"ly":13,"mx":53,"my":13},{"lx":51,"ly":13,"mx":52,"my":13},{"lx":50,"ly":13,"mx":51,"my":13},{"lx":48,"ly":14,"mx":50,"my":13},{"lx":46,"ly":15,"mx":48,"my":14},{"lx":44,"ly":16,"mx":46,"my":15},{"lx":42,"ly":17,"mx":44,"my":16},{"lx":40,"ly":19,"mx":42,"my":17},{"lx":39,"ly":21,"mx":40,"my":19},{"lx":37,"ly":22,"mx":39,"my":21},{"lx":36,"ly":24,"mx":37,"my":22},{"lx":36,"ly":25,"mx":36,"my":24},{"lx":35,"ly":27,"mx":36,"my":25},{"lx":35,"ly":28,"mx":35,"my":27},{"lx":35,"ly":29,"mx":35,"my":28},{"lx":35,"ly":30,"mx":35,"my":29},{"lx":35,"ly":31,"mx":35,"my":30},{"lx":36,"ly":31,"mx":35,"my":31},{"lx":37,"ly":31,"mx":36,"my":31},{"lx":38,"ly":31,"mx":37,"my":31},{"lx":39,"ly":31,"mx":38,"my":31},{"lx":40,"ly":31,"mx":39,"my":31},{"lx":41,"ly":31,"mx":40,"my":31},{"lx":42,"ly":31,"mx":41,"my":31},{"lx":44,"ly":31,"mx":42,"my":31},{"lx":46,"ly":31,"mx":44,"my":31},{"lx":49,"ly":31,"mx":46,"my":31},{"lx":51,"ly":31,"mx":49,"my":31},{"lx":54,"ly":30,"mx":51,"my":31},{"lx":55,"ly":30,"mx":54,"my":30},{"lx":57,"ly":30,"mx":55,"my":30},{"lx":59,"ly":29,"mx":57,"my":30},{"lx":60,"ly":29,"mx":59,"my":29},{"lx":61,"ly":28,"mx":60,"my":29},{"lx":62,"ly":28,"mx":61,"my":28},{"lx":63,"ly":27,"mx":62,"my":28},{"lx":64,"ly":26,"mx":63,"my":27},{"lx":65,"ly":26,"mx":64,"my":26},{"lx":67,"ly":25,"mx":65,"my":26},{"lx":69,"ly":24,"mx":67,"my":25},{"lx":70,"ly":23,"mx":69,"my":24},{"lx":72,"ly":21,"mx":70,"my":23},{"lx":74,"ly":20,"mx":72,"my":21},{"lx":75,"ly":20,"mx":74,"my":20},{"lx":77,"ly":19,"mx":75,"my":20},{"lx":79,"ly":18,"mx":77,"my":19},{"lx":81,"ly":17,"mx":79,"my":18},{"lx":82,"ly":17,"mx":81,"my":17},{"lx":84,"ly":17,"mx":82,"my":17},{"lx":85,"ly":17,"mx":84,"my":17},{"lx":86,"ly":17,"mx":85,"my":17},{"lx":86,"ly":18,"mx":86,"my":17},{"lx":85,"ly":18,"mx":86,"my":18},{"lx":84,"ly":18,"mx":85,"my":18},{"lx":83,"ly":18,"mx":84,"my":18},{"lx":83,"ly":19,"mx":83,"my":18},{"lx":82,"ly":19,"mx":83,"my":19},{"lx":80,"ly":19,"mx":82,"my":19},{"lx":78,"ly":20,"mx":80,"my":19},{"lx":77,"ly":21,"mx":78,"my":20},{"lx":75,"ly":22,"mx":77,"my":21},{"lx":74,"ly":23,"mx":75,"my":22},{"lx":73,"ly":24,"mx":74,"my":23},{"lx":71,"ly":24,"mx":73,"my":24},{"lx":70,"ly":25,"mx":71,"my":24},{"lx":70,"ly":26,"mx":70,"my":25},{"lx":69,"ly":27,"mx":70,"my":26},{"lx":69,"ly":28,"mx":69,"my":27},{"lx":68,"ly":29,"mx":69,"my":28},{"lx":68,"ly":30,"mx":68,"my":29},{"lx":68,"ly":31,"mx":68,"my":30},{"lx":69,"ly":31,"mx":68,"my":31},{"lx":70,"ly":31,"mx":69,"my":31},{"lx":71,"ly":31,"mx":70,"my":31},{"lx":72,"ly":31,"mx":71,"my":31},{"lx":74,"ly":31,"mx":72,"my":31},{"lx":76,"ly":31,"mx":74,"my":31},{"lx":79,"ly":31,"mx":76,"my":31},{"lx":82,"ly":31,"mx":79,"my":31},{"lx":84,"ly":31,"mx":82,"my":31},{"lx":85,"ly":30,"mx":84,"my":31},{"lx":87,"ly":29,"mx":85,"my":30},{"lx":88,"ly":29,"mx":87,"my":29},{"lx":88,"ly":28,"mx":88,"my":29},{"lx":89,"ly":27,"mx":88,"my":28},{"lx":89,"ly":26,"mx":89,"my":27},{"lx":89,"ly":25,"mx":89,"my":26},{"lx":90,"ly":25,"mx":89,"my":25},{"lx":90,"ly":26,"mx":90,"my":25},{"lx":90,"ly":27,"mx":90,"my":26},{"lx":90,"ly":28,"mx":90,"my":27},{"lx":89,"ly":29,"mx":90,"my":28},{"lx":89,"ly":31,"mx":89,"my":29},{"lx":88,"ly":32,"mx":89,"my":31},{"lx":88,"ly":34,"mx":88,"my":32},{"lx":88,"ly":35,"mx":88,"my":34},{"lx":88,"ly":36,"mx":88,"my":35},{"lx":88,"ly":37,"mx":88,"my":36},{"lx":89,"ly":37,"mx":88,"my":37},{"lx":90,"ly":37,"mx":89,"my":37},{"lx":90,"ly":36,"mx":90,"my":37},{"lx":92,"ly":35,"mx":90,"my":36},{"lx":94,"ly":33,"mx":92,"my":35},{"lx":95,"ly":31,"mx":94,"my":33},{"lx":98,"ly":28,"mx":95,"my":31},{"lx":100,"ly":26,"mx":98,"my":28},{"lx":102,"ly":24,"mx":100,"my":26},{"lx":104,"ly":22,"mx":102,"my":24},{"lx":106,"ly":21,"mx":104,"my":22},{"lx":107,"ly":21,"mx":106,"my":21},{"lx":108,"ly":20,"mx":107,"my":21},{"lx":109,"ly":20,"mx":108,"my":20},{"lx":110,"ly":20,"mx":109,"my":20},{"lx":110,"ly":21,"mx":110,"my":20},{"lx":111,"ly":21,"mx":110,"my":21},{"lx":111,"ly":22,"mx":111,"my":21},{"lx":112,"ly":23,"mx":111,"my":22},{"lx":113,"ly":23,"mx":112,"my":23},{"lx":114,"ly":24,"mx":113,"my":23},{"lx":115,"ly":25,"mx":114,"my":24},{"lx":116,"ly":26,"mx":115,"my":25},{"lx":118,"ly":27,"mx":116,"my":26},{"lx":121,"ly":28,"mx":118,"my":27},{"lx":123,"ly":28,"mx":121,"my":28},{"lx":126,"ly":29,"mx":123,"my":28},{"lx":129,"ly":29,"mx":126,"my":29},{"lx":132,"ly":30,"mx":129,"my":29},{"lx":135,"ly":30,"mx":132,"my":30},{"lx":138,"ly":30,"mx":135,"my":30},{"lx":139,"ly":30,"mx":138,"my":30},{"lx":141,"ly":30,"mx":139,"my":30},{"lx":142,"ly":30,"mx":141,"my":30},{"lx":143,"ly":30,"mx":142,"my":30},{"lx":143,"ly":29,"mx":143,"my":30},{"lx":144,"ly":29,"mx":143,"my":29}]"""

def s2if(jsonsig, output_image="signature.png", input_image=BLANK_IMAGE,
            pincolor=(0,0,255)):
    #Decode valid json or return None
    try:
        l=json.loads(jsonsig)
    except(exceptions.ValueError):
        return None
    #Make sure its a signature or return None
    if not l[0].has_key('lx') or not l[0].has_key('my'):
        return None
    #create a blank image from out template
    im = Image.open(input_image)
    #create a drawing object
    draw = ImageDraw.Draw(im)
    #iterate over our list of points and draw corresponding lines
    for i in l:
        draw.line((i['lx'], i['ly'], i['mx'], i['my']), fill=pincolor, width=1)
    #delete our draw object (cleanup and free the memory)
    del draw 

    # save image
    im.save(output_image, "PNG")
    #get its path
    BASE_DIR = os.path.dirname(os.path.abspath(output_image))
    IMAGE_PATH = os.path.join(BASE_DIR, output_image)
    return IMAGE_PATH
    

def s2i(jsonsig, input_image=BLANK_IMAGE, pincolor=(0,0,255),
        force_no_sig_image=False, nosig_image=NO_SIG_IMAGE):
    
      
    if force_no_sig_image==True:
        im = Image.open(nosig_image)
        return im
    #Decode valid json or return None
    try:
        l=json.loads(jsonsig)
    except(exceptions.ValueError):
        im = Image.open(nosig_image)
        return im
    #Make sure its a signature or return None
    if not l[0].has_key('lx') or not l[0].has_key('my'):
        im = Image.open(nosig_image)
        return im
    #create a blank image from out template
    im = Image.open(input_image)
    #create a drawing object
    draw = ImageDraw.Draw(im)
    #iterate over our list of points and draw corresponding lines
    for i in l:
        draw.line((i['lx'], i['ly'], i['mx'], i['my']), fill=pincolor, width=1)
    #delete our draw object (cleanup and free the memory)
    del draw 
    
    # save image
    #im.save(output_image, "PNG")
    return im

    
if __name__ == "__main__":
    
    try:
        #jsonsig =  sys.argv[1]
        output_image =  sys.argv[1]
        image_path=s2if(j, output_image)
        print "New signature image written to: %s " % (image_path)
    except:
        print sys.exc_info()
