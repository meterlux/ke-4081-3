"""Late-night drafting table, c. 1952 — messy desk of blueprints with one working area in focus.
Renders two compositions (landscape, portrait). Depth of field is applied afterwards in compose.py."""
import math,random
from objects import *

def curl(x,y,w,h,corner,s):
    # dog-eared/curled corner: lighter back of the sheet showing
    if corner=='br': p=f'M{w},{h-s} L{w-s},{h} L{w-s*.15},{h-s*.15} Z'
    else: p=f'M{w-s},0 L{w},{s} L{w-s*.15},{s*.15} Z'
    return f'<path d="{p}" fill="#c9d6ea"/><path d="{p}" fill="url(#bp)" opacity=".35"/>'

def pocket_pad(w=270,h=380,seed=5):
    r=random.Random(seed);o=[]
    edge=f'M8,0 H{w-6} Q{w},2 {w},14 V{h-18} Q{w-2},{h} {w-16},{h} H14 Q2,{h-2} 0,{h-20} V10 Q1,1 8,0 Z'
    o.append(f'<path d="{edge}" fill="#6b5232" transform="translate(5,6)"/>')                       # cardboard back
    o.append(f'<g filter="url(#rough)"><path d="{edge}" fill="#ebdcb4"/>'
             f'<path d="{edge}" fill="#000" filter="url(#fiber)" opacity=".9"/></g>')
    rules=''.join(f'M14,{y}H{w-10}' for y in range(70,h-14,22))
    o.append(f'<path d="{rules}" stroke="#7b9bc0" stroke-width="1.3" stroke-opacity=".55"/><path d="M38,40V{h-8}" stroke="#c0605a" stroke-opacity=".5" stroke-width="1.4"/>')
    # torn stubs of pages long gone, then the spiral
    o.append(f'<path d="M6,6 H{w-8} L{w-10},20 L{w-30},14 L{w-60},22 L{w-100},15 L{w-150},23 L{w-200},14 L40,21 L8,16 Z" fill="#f2e6c4" opacity=".9"/>')
    for i in range(14):
        x=16+i*((w-30)/13)
        o.append(f'<circle cx="{x:.1f}" cy="10" r="4.2" fill="#2a1d10"/><path d="M{x-5:.1f},10 C{x-6:.1f},-10 {x+6:.1f},-10 {x+5:.1f},10" fill="none" stroke="url(#chromeH)" stroke-width="3.4"/>')
    # handwritten figures in graphite
    lines=[('LH spar cap',0),('7075-T6  t=.156',0),('M = 41 800 in-lb',0),('fb = Mc/I = 38 900',1),('MS = +.12 ✓',0),('rivet pitch 1.0',0),('ck w/ JJL Mon.',2)]
    for i,(t,ind) in enumerate(lines):
        y=88+i*44
        o.append(T(46+ind*12,y,t,25,'#4a4a52','start',"Caveat, cursive",f'opacity=".85" transform="rotate({r.uniform(-1.6,.8):.1f} 46 {y})"'))
    o.append(f'<path d="M44,{88+4*44+10} q60,8 130,-2" stroke="#4a4a52" stroke-width="2" fill="none" opacity=".7"/>')
    # wear: greasy thumbprints, coffee crescent, dog-ear, scuffs
    o.append(f'<g filter="url(#smudge)"><ellipse cx="{w*.78}" cy="{h*.84}" rx="34" ry="44" fill="#3a2d22" opacity=".28"/><ellipse cx="{w*.2}" cy="{h*.55}" rx="22" ry="30" fill="#3a2d22" opacity=".18"/></g>')
    o.append(f'<path d="M{w*.55},{h*.95} a70,70 0 0,1 {w*.4},-{h*.2}" stroke="#6b3e1c" stroke-opacity=".35" stroke-width="7" fill="none"/>')
    o.append(f'<path d="M{w-34},{h} L{w},{h-38} L{w-14},{h-14} Z" fill="#d7c59b"/><path d="M{w-34},{h} L{w},{h-38}" stroke="#9a8558" stroke-width="1.2"/>')
    for k in range(18):
        x=r.uniform(10,w-10);y=r.uniform(30,h-10)
        o.append(f'<path d="M{x:.0f},{y:.0f} l{r.uniform(-14,14):.0f},{r.uniform(-4,4):.0f}" stroke="#5a4a30" stroke-opacity=".18" stroke-width="1"/>')
    return ''.join(o)

def bp_roll(L=900,D=90):
    return (f'<rect x="0" y="{-D/2}" width="{L}" height="{D}" rx="{D*.12}" fill="#173a6c"/>'
            f'<rect x="0" y="{-D/2}" width="{L}" height="{D*.3}" fill="#fff" fill-opacity=".12"/><rect x="0" y="{D*.2}" width="{L}" height="{D*.3}" fill="#000" fill-opacity=".25"/>'
            f'<ellipse cx="{L}" cy="0" rx="{D*.18}" ry="{D/2}" fill="#dfe8f5"/><ellipse cx="{L}" cy="0" rx="{D*.1}" ry="{D*.3}" fill="none" stroke="#173a6c" stroke-width="3"/><ellipse cx="{L}" cy="0" rx="{D*.04}" ry="{D*.13}" fill="none" stroke="#173a6c" stroke-width="2"/>'
            f'<rect x="{L*.3}" y="{-D/2-2}" width="8" height="{D+4}" fill="#b8915a"/>')

def crumple(R=70,seed=3):
    r=random.Random(seed);pts=[]
    for i in range(16):
        a=i*math.pi/8;rr=R*r.uniform(.75,1.05);pts.append(f'{rr*math.cos(a):.0f},{rr*math.sin(a):.0f}')
    o=f'<polygon points="{" ".join(pts)}" fill="#e9e3d2"/>'
    for i in range(9):
        a=r.uniform(0,6.3);b=r.uniform(0,6.3)
        o+=f'<path d="M{R*.7*math.cos(a):.0f},{R*.7*math.sin(a):.0f} L{r.uniform(-15,15):.0f},{r.uniform(-15,15):.0f} L{R*.8*math.cos(b):.0f},{R*.8*math.sin(b):.0f}" stroke="#a49c88" stroke-width="2" fill="none"/>'
    return o

def clip(): return '<path d="M0,0 h60 a12,12 0 0,1 0,24 h-52 a8,8 0 0,1 0,-16 h44" fill="none" stroke="url(#chromeH)" stroke-width="3.5"/>'

def scene(W,H,P):
    o=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',DEFS]
    by,fy=P['boardTop'],P['front']
    o.append(f'<rect width="{W}" height="{H}" fill="#0c0806"/>')
    o.append(f'<rect width="{W}" height="{by}" fill="url(#walnut)"/><rect width="{W}" height="{by}" fill="#000" filter="url(#woodgrain)"/>')
    o.append(f'<rect y="{by}" width="{W}" height="{fy-by}" fill="#8fa08a"/><rect y="{by}" width="{W}" height="{fy-by}" fill="#000" filter="url(#grain)"/><rect y="{by-10}" width="{W}" height="14" fill="url(#chrome)"/>')
    o.append(f'<rect y="{fy}" width="{W}" height="{H-fy}" fill="url(#oak)"/><rect y="{fy}" width="{W}" height="{H-fy}" fill="#000" filter="url(#woodgrain)"/>')
    LIB={'jet':lambda s:jet(s),'clock':lambda s:clock(150*s),'lamp':lambda s:lamp(s),'roll':lambda s:bp_roll(),'thermos':lambda s:thermos(),
         'logbook':lambda s:logbook()+g(aviators(.9),'translate(60,200) rotate(-8)'),'tsq':lambda s:tsquare(P.get('tsqL',1500)),'triangle':lambda s:triangle(1),
         'compass':lambda s:compass(1),'lead':lambda s:leadholder(),'pencil':lambda s:pencil(),'pencilR':lambda s:pencil(560,'#c24a2a'),
         'pad':lambda s:pocket_pad(),'crumple':lambda s:crumple(),'clip':lambda s:clip(),'aviators':lambda s:aviators(1)}
    def put(items,flt):
        for kind,x,y,rot,s in items:
            o.append(g(LIB[kind](s),f'translate({x},{y}) rotate({rot}) scale({s})',flt))
    put(P['back'],'sh1')
    for i,(kind,x,y,w,h,rot) in enumerate(P['sheets']):
        f={'turbojet':drawing_turbojet,'wingrib':drawing_wingrib,'blue':drawing_blue,'sepia':drawing_sepia}[kind]
        tp=tape(30,30,8)+tape(w-30,h-30,10) if i%2 else tape(w-30,30,-6)
        o.append(g(f(w,h)+curl(0,0,w,h,'br' if i%2 else 'tr',60+i*15)+tp,f'translate({x},{y}) rotate({rot})','sh2'))
    for x,y,r in P['rings']: o.append(coffee_ring(x,y,r))
    o.append(crumbs(*P['crumbs'],50,9))
    put(P['mid'],'sh2')
    x,y,rot,L,Hh=P['rule']
    o.append(g(slide_rule(L,Hh),f'translate({x},{y}) rotate({rot})','sh0'))
    put(P['top'],'sh1')
    lx,ly,rx,ry=P['light']
    o.append(f'<defs><radialGradient id="pool" gradientUnits="userSpaceOnUse" cx="{lx}" cy="{ly}" r="{rx}" gradientTransform="translate({lx} {ly}) scale(1 {ry/rx}) translate({-lx} {-ly})">'
             '<stop offset="0" stop-color="#000" stop-opacity="0"/><stop offset=".45" stop-color="#05040a" stop-opacity=".15"/><stop offset=".78" stop-color="#05040a" stop-opacity=".5"/><stop offset="1" stop-color="#020203" stop-opacity=".74"/></radialGradient>'
             f'<radialGradient id="warm" gradientUnits="userSpaceOnUse" cx="{lx}" cy="{ly}" r="{rx*.75}"><stop offset="0" stop-color="#ffc977" stop-opacity=".3"/><stop offset="1" stop-color="#ffc977" stop-opacity="0"/></radialGradient></defs>')
    o.append(f'<rect width="{W}" height="{H}" fill="#ffd9a0" fill-opacity=".12" style="mix-blend-mode:multiply"/>')
    o.append(f'<rect width="{W}" height="{H}" fill="url(#warm)" style="mix-blend-mode:screen"/>')
    o.append(f'<rect width="{W}" height="{H}" fill="url(#pool)"/>')
    for kind,x,y,rot,s in P['back']:
        if kind=='lamp': o.append(f'<ellipse cx="{x}" cy="{y+20*s}" rx="{230*s}" ry="{90*s}" fill="#ffe7b0" opacity=".35" filter="url(#glow)" transform="rotate({rot} {x} {y})"/>')
    o.append('</svg>')
    return '\n'.join(o)

LAND=dict(boardTop=210,front=1050,
  back=[('roll',260,175,-4,1),('jet',1560,120,-70,.55),('clock',2190,170,0,.85),('lamp',420,150,14,.8)],
  sheets=[('wingrib',-220,250,1500,720,-9),('blue',1180,200,1400,760,7),('sepia',340,560,1300,620,4.5),('turbojet',720,300,1420,680,-2.5)],
  rings=[(1560,520,78),(610,860,64)],crumbs=(1250,700,1600,820),
  mid=[('tsq',-60,930,-4,1),('logbook',-120,560,16,.85),('triangle',1700,420,-26,1),('thermos',1950,620,-34,1),('crumple',2280,960,0,1),('clip',1430,980,20,1),('clip',300,640,-35,1),('compass',2050,300,40,1)],
  rule=(140,760,-3.2,2050,150),
  top=[('pad',1330,800,8,1),('pencil',1300,1050,-17,1),('lead',380,1010,4,1)],
  light=(1150,700,1600,900))
PORT=dict(boardTop=560,front=2320,
  back=[('clock',220,300,0,1.0),('jet',720,380,-24,.58),('lamp',880,520,6,.72),('roll',-80,560,-3,.9)],
  sheets=[('wingrib',-260,640,1000,1340,-8),('blue',320,700,1000,1300,9),('sepia',-120,1500,1000,900,5),('turbojet',40,760,980,1330,-3)],
  rings=[(860,1240,70),(260,1650,56)],crumbs=(300,1900,800,2000),
  mid=[('tsq',-60,1300,-6,1),('logbook',-140,880,15,.78),('thermos',880,1100,70,.8),('triangle',620,1500,18,.75),('crumple',960,2160,0,1),('clip',140,2240,-30,1),('compass',840,1700,-20,.9)],
  rule=(-330,2110,-23,1760,150),
  top=[('pad',610,1900,10,1),('pencil',560,2270,-48,1),('lead',60,2330,-6,1)],
  light=(560,1650,1200,1700))
FOCUS={'land':(1180,860,760,320),'port':(520,1920,560,480)}
if __name__=='__main__':
    open('land.svg','w').write(scene(2400,1100,LAND));open('port.svg','w').write(scene(1100,2400,PORT))
