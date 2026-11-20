"""Depth of field: keep the working area sharp, blur the rest progressively."""
import sys
from PIL import Image,ImageFilter,ImageDraw,ImageChops
from scene3 import FOCUS
for f in ('land','port'):
    im=Image.open(f+'.png').convert('RGB')
    cx,cy,rx,ry=FOCUS[f]
    soft=im.filter(ImageFilter.GaussianBlur(5)); far=im.filter(ImageFilter.GaussianBlur(13))
    def mask(k):
        m=Image.new('L',im.size,0);d=ImageDraw.Draw(m)
        d.ellipse([cx-rx*k,cy-ry*k,cx+rx*k,cy+ry*k],fill=255)
        return m.filter(ImageFilter.GaussianBlur(min(rx,ry)*.45*k))
    out=Image.composite(soft,far,mask(1.9))
    out=Image.composite(im,out,mask(1.0))
    # film grain
    noise=Image.effect_noise(im.size,26).convert('L').point(lambda v:128+(v-128)*.35)
    out=ImageChops.overlay(out,Image.merge('RGB',(noise,noise,noise)))
    out.save(f'splash-{f}.jpg',quality=80,optimize=True,progressive=True)
    out.resize((out.width//3,out.height//3),Image.LANCZOS).save(f'prev-{f}.jpg',quality=85)
