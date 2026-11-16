# Paints plain stone colour over the visitors standing in front of three west-face panels.
# Usage: python3 paint.py <assets/sculpture dir> <output dir>
import sys
from PIL import Image, ImageDraw, ImageFilter
import numpy as np
D,out=sys.argv[1].rstrip('/')+'/',sys.argv[2].rstrip('/')+'/'
JOBS={
 'west-panel-N1.jpg':[[(0,226),(22,227),(35,236),(40,252),(41,259),(66,259),(72,246),(85,232),(100,222),(125,217),(152,216),(174,228),(187,246),(193,266),(197,283),(222,283),(233,305),(0,305)],
                      [(260,224),(271,206),(280,200),(280,305),(252,305)]],
 'west-panel-N2.jpg':[[(144,305),(149,276),(156,267),(183,267),(196,271),(213,271),(215,258),(223,236),(245,221),(245,305)]],
 'west-panel-N3.jpg':[[(213,305),(220,293),(233,285),(252,285),(263,293),(271,305)]],
}
def blur(arr,r): return np.asarray(Image.fromarray(np.clip(arr+128,0,255).astype('uint8')).filter(ImageFilter.GaussianBlur(r))).astype(float)-128
rng=np.random.default_rng(11)
for name,polys in JOBS.items():
    im=Image.open(D+name).convert('RGB'); w,h=im.size; a=np.asarray(im).astype(float)
    m=Image.new('L',(w,h),0); d=ImageDraw.Draw(m)
    for p in polys: d.polygon(p,fill=255)
    hard=np.asarray(m)>0
    overall=np.median(a[180:][~hard[180:]],axis=0)             # the stone's usual colour in the lower part of the panel
    col=np.zeros((w,3)); has=np.zeros(w,bool); tops=np.zeros(w,int)
    for x in range(w):
        ys=np.where(hard[:,x])[0]
        if len(ys)==0: continue
        top=ys.min(); tops[x]=top; has[x]=True
        col[x]=a[max(0,top-24):max(1,top-5),x,:].mean(axis=0)   # the stone just above the person in this column
    xs=np.where(has)[0]; fill=a.copy()
    for x in xs:
        lo,hi=max(0,x-22),min(w,x+23); c=col[lo:hi][has[lo:hi]].mean(axis=0)
        fill[tops[x]:,x][hard[tops[x]:,x]]=0.5*c+0.5*overall
    # plain grain and mottling made from noise, so nothing carved is invented
    grain=blur(rng.normal(0,13,(h,w,1)).repeat(3,2),1.1)+blur(rng.normal(0,60,(h,w,1)).repeat(3,2),5)
    fill=np.clip(fill+grain*hard[:,:,None],0,255)
    soft=m.filter(ImageFilter.GaussianBlur(1.8))
    Image.composite(Image.fromarray(fill.astype('uint8')),im,soft).save(out+name,quality=93,subsampling=0)
    print(name,'painted',int(hard.sum()),'of',w*h,'pixels (%.1f%%)'%(100*hard.sum()/(w*h)))
