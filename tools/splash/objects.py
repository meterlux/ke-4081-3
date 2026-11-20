"""Late-night drafting table, c. 1952: two compositions (landscape + portrait) from one object library."""
import math,random,sys
from deer2 import deer
FONT='DejaVu Sans Condensed, DejaVu Sans, sans-serif'
MONO='DejaVu Sans Mono, monospace'
def g(inner,tf='',flt=None,op=None):
    a=f' transform="{tf}"' if tf else ''
    a+=f' filter="url(#{flt})"' if flt else ''
    a+=f' opacity="{op}"' if op is not None else ''
    return f'<g{a}>{inner}</g>'
def T(x,y,s,size,fill='#222',anchor='start',fam=FONT,extra=''):
    return f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" font-family="{fam}" fill="{fill}" text-anchor="{anchor}" {extra}>{s}</text>'

DEFS='''<defs>
 <filter id="grain" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="2" seed="7"/><feColorMatrix values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .2 0"/><feComposite in2="SourceGraphic" operator="in"/></filter>
 <filter id="fiber" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".012 .04" numOctaves="3" seed="11"/><feColorMatrix values="0 0 0 0 .35  0 0 0 0 .3  0 0 0 0 .2  0 0 0 .14 0"/><feComposite in2="SourceGraphic" operator="in"/></filter>
 <filter id="hammer" x="0" y="0" width="100%" height="100%"><feTurbulence type="turbulence" baseFrequency=".06" numOctaves="2" seed="5"/><feColorMatrix values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 .18 -.02"/><feComposite in2="SourceGraphic" operator="in"/></filter>
 <filter id="woodgrain" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".004 .09" numOctaves="3" seed="2"/><feColorMatrix values="0 0 0 0 .1  0 0 0 0 .05  0 0 0 0 0  0 0 0 .5 0"/><feComposite in2="SourceGraphic" operator="in"/></filter>
 <filter id="b0" x="-5%" y="-30%" width="110%" height="160%"><feDropShadow dx="14" dy="22" stdDeviation="16" flood-color="#000" flood-opacity=".6"/><feGaussianBlur stdDeviation=".5"/></filter>
 <filter id="b1" x="-10%" y="-10%" width="120%" height="120%"><feDropShadow dx="10" dy="16" stdDeviation="12" flood-color="#000" flood-opacity=".55"/><feGaussianBlur stdDeviation="2.2"/></filter>
 <filter id="b2" x="-10%" y="-10%" width="120%" height="120%"><feDropShadow dx="6" dy="10" stdDeviation="9" flood-color="#000" flood-opacity=".45"/><feGaussianBlur stdDeviation="3.4"/></filter>
 <filter id="b3" x="-15%" y="-15%" width="130%" height="130%"><feDropShadow dx="8" dy="12" stdDeviation="12" flood-color="#000" flood-opacity=".5"/><feGaussianBlur stdDeviation="7"/></filter>
 <filter id="b4" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="11"/></filter>
 <filter id="glow" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="30"/></filter>
 <linearGradient id="chrome" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7d858b"/><stop offset=".25" stop-color="#eef1f3"/><stop offset=".5" stop-color="#aab1b6"/><stop offset=".78" stop-color="#e4e8ea"/><stop offset="1" stop-color="#6c7378"/></linearGradient>
 <linearGradient id="chromeH" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#7d858b"/><stop offset=".3" stop-color="#eef1f3"/><stop offset=".55" stop-color="#aab1b6"/><stop offset=".8" stop-color="#e4e8ea"/><stop offset="1" stop-color="#6c7378"/></linearGradient>
 <linearGradient id="green" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#173f13"/><stop offset=".25" stop-color="#3f8a33"/><stop offset=".42" stop-color="#7cbf68"/><stop offset=".55" stop-color="#3a7e2e"/><stop offset="1" stop-color="#11300e"/></linearGradient>
 <linearGradient id="ivory" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f7efda"/><stop offset=".5" stop-color="#f1e8cf"/><stop offset="1" stop-color="#e3d8b9"/></linearGradient>
 <linearGradient id="maho" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#6b3a1d"/><stop offset="1" stop-color="#2e170a"/></linearGradient>
 <linearGradient id="oak" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#b98a52"/><stop offset=".45" stop-color="#9a6b39"/><stop offset="1" stop-color="#4f3218"/></linearGradient>
 <linearGradient id="walnut" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2b1a10"/><stop offset="1" stop-color="#4a2e1b"/></linearGradient>
 <linearGradient id="bp" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#21497f"/><stop offset=".55" stop-color="#173a6c"/><stop offset="1" stop-color="#112d57"/></linearGradient>
 <filter id="bpmottle" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".008" numOctaves="4" seed="9"/><feColorMatrix values="0 0 0 0 .7  0 0 0 0 .8  0 0 0 0 1  0 0 0 .35 -.08"/><feComposite in2="SourceGraphic" operator="in"/></filter>
 <filter id="rough" x="-3%" y="-3%" width="106%" height="106%"><feTurbulence type="fractalNoise" baseFrequency=".05" numOctaves="2" seed="3" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="5"/></filter>
 <filter id="smudge" x="-20%" y="-20%" width="140%" height="140%"><feTurbulence type="fractalNoise" baseFrequency=".035" numOctaves="3" seed="21" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="26"/><feGaussianBlur stdDeviation="3"/></filter>
 <filter id="sh0" x="-10%" y="-30%" width="120%" height="160%"><feDropShadow dx="14" dy="22" stdDeviation="16" flood-color="#000" flood-opacity=".7"/></filter>
 <filter id="sh1" x="-15%" y="-15%" width="130%" height="130%"><feDropShadow dx="10" dy="16" stdDeviation="12" flood-color="#000" flood-opacity=".6"/></filter>
 <filter id="sh2" x="-10%" y="-10%" width="120%" height="120%"><feDropShadow dx="6" dy="10" stdDeviation="9" flood-color="#000" flood-opacity=".55"/></filter>
 <linearGradient id="lens" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#4f6b46"/><stop offset=".5" stop-color="#22341f"/><stop offset="1" stop-color="#3b5233"/></linearGradient>
 <linearGradient id="brass" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7a5a14"/><stop offset=".4" stop-color="#f0d07a"/><stop offset="1" stop-color="#6e5214"/></linearGradient>
 <radialGradient id="bulb" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#fffbe8"/><stop offset=".35" stop-color="#ffe7a8"/><stop offset="1" stop-color="#ffb347" stop-opacity="0"/></radialGradient>
 <radialGradient id="dial" cx="50%" cy="45%" r="55%"><stop offset="0" stop-color="#2a2a2a"/><stop offset="1" stop-color="#0d0d0d"/></radialGradient>
</defs>'''

# ---------------- objects (each drawn around its own origin) ----------------
def slide_rule(L,Hh):
    o=[]
    x0,x1=0.075*L,0.925*L;S=x1-x0
    yT,yS0,yS1,yB=0,0.31*Hh,0.66*Hh,Hh
    o.append(f'<rect x="0" y="{yB-2}" width="{L}" height="{Hh*.09:.1f}" fill="url(#maho)"/>')
    o.append(f'<rect x="0" y="0" width="{L}" height="{Hh}" fill="url(#ivory)"/>')
    o.append(f'<rect x="0" y="0" width="{L}" height="{Hh}" fill="#000" filter="url(#grain)" opacity=".5"/>')
    o.append(f'<rect x="-{L*.012}" y="{yS0+2}" width="{L*1.024}" height="{yS1-yS0-4}" fill="#f6eedb"/>')
    for yy in (yS0,yS1):
        o.append(f'<rect x="0" y="{yy-1.5}" width="{L}" height="3" fill="#5a3a1f" fill-opacity=".55"/><rect x="0" y="{yy+1.5}" width="{L}" height="1.2" fill="#fff" fill-opacity=".6"/>')
    rows=[(yS0*.5,True,'k',0),(yS0,True,'k',0.497),(yS0,False,'k',0.497),(yS0+(yS1-yS0)*.5,True,'r',None),(yS1,True,'k',0),(yS1,False,'k',0),(yS1+(yB-yS1)*.55,False,'k',None)]
    fs=Hh*.075
    for (yb,up,ink,shift) in rows:
        col='#2a2520' if ink=='k' else '#b3392b'
        p=[];labs=[]
        for i in range(0,901):
            v=1+9*i/900
            if i%2 and v>2: continue
            if i%5 and v>4: continue
            x=math.log10(v)
            if shift: x=(x-shift)%1
            if shift is None: x=1-x
            X=x0+S*x
            maj=abs(v-round(v))<1e-9; half=abs(v*2-round(v*2))<1e-9
            L_=Hh*(.12 if maj else (.085 if half else .05))
            y2=yb-L_ if up else yb+L_
            p.append(f'M{X:.1f},{yb:.1f}V{y2:.1f}')
            if maj and i<900: labs.append((X,str(int(round(v)))))
        o.append(f'<path d="{"".join(p)}" stroke="{col}" stroke-width="{max(1,Hh*.007):.2f}" fill="none"/>')
        for X,t in labs:
            yy=(yb-Hh*.12-fs*.25) if up else (yb+Hh*.12+fs*.95)
            o.append(T(X,yy,t,f'{fs:.1f}',col,'middle'))
    # scale names at the left margin
    for yb,name in ((yS0*.55,'LL02'),(yS0*.9,'DF'),(yS0+12,'CF'),(yS0+(yS1-yS0)*.55,'CI'),(yS1-6,'C'),(yS1+20,'D'),(yB-10,'LL3')):
        o.append(T(x0-Hh*.12,yb,name,f'{fs*.95:.1f}','#2a2520','end'))
    # brackets
    for bx in (L*.012,L*.962):
        o.append(f'<rect x="{bx}" y="-{Hh*.04}" width="{L*.026}" height="{Hh*1.08}" rx="4" fill="url(#chromeH)"/>')
        for sy in (Hh*.15,Hh*.85): o.append(f'<circle cx="{bx+L*.013}" cy="{sy}" r="{Hh*.045}" fill="#c9c3ae" stroke="#6f6a5c" stroke-width="1.5"/>')
    # cursor
    cx,cw=0.47*L,0.105*L
    o.append(f'<rect x="{cx-cw/2}" y="-{Hh*.12}" width="{cw}" height="{Hh*1.24}" rx="{Hh*.06}" fill="#dff0f2" fill-opacity=".16" stroke="#cfd5d8" stroke-width="{Hh*.03}"/>')
    o.append(f'<rect x="{cx-cw/2-4}" y="-{Hh*.14}" width="{cw+8}" height="{Hh*.1}" rx="6" fill="url(#chrome)"/><rect x="{cx-cw/2-4}" y="{Hh*1.04}" width="{cw+8}" height="{Hh*.1}" rx="6" fill="url(#chrome)"/>')
    o.append(f'<path d="M{cx},{-Hh*.04} V{Hh*1.04}" stroke="#111" stroke-width="2"/>')
    o.append(f'<path d="M{cx-cw/2+cw*.18},{-Hh*.05} L{cx-cw/2+cw*.42},{Hh*1.03}" stroke="#fff" stroke-opacity=".18" stroke-width="{cw*.12}"/>')
    o.append(T(L*.945,yS0+(yS1-yS0)*.62,'K+E',f'{fs*1.5:.1f}','#b3392b','middle','DejaVu Serif, serif','font-style="italic"'))
    return ''.join(o)

def sheet(w,h,kind,seed=0):
    r=random.Random(seed);o=[]
    kind='blue'  # every shop drawing is a blueprint
    base='url(#bp)'
    o.append(f'<rect width="{w}" height="{h}" fill="{base}"/>')
    o.append(f'<rect width="{w}" height="{h}" fill="#9ec0ff" filter="url(#bpmottle)"/>')
    o.append(f'<rect width="{w}" height="{h}" fill="none" stroke="#7fa3e0" stroke-opacity=".35" stroke-width="{min(w,h)*.03:.0f}"/>')
    ink='#dfeaff'
    sw=3.2
    o.append(f'<rect x="{w*.03}" y="{h*.035}" width="{w*.94}" height="{h*.93}" fill="none" stroke="{ink}" stroke-width="{sw*1.6}" opacity=".85"/>')
    # title block
    tx,ty,tw,th=w*.62,h*.82,w*.35,h*.145
    o.append(f'<g stroke="{ink}" fill="none" stroke-width="{sw}" opacity=".8"><rect x="{tx}" y="{ty}" width="{tw}" height="{th}"/><path d="M{tx},{ty+th*.33}H{tx+tw}M{tx},{ty+th*.66}H{tx+tw}M{tx+tw*.55},{ty+th*.33}V{ty+th}"/></g>')
    return o,ink,sw,(tx,ty,tw,th)

def drawing_turbojet(w,h):
    o,ink,sw,(tx,ty,tw,th)=sheet(w,h,'vellum',1)
    cy=h*.42;x0=w*.08;x1=w*.86
    st=f'stroke="{ink}" fill="none" stroke-linecap="round"'
    # casing profile (top and bottom mirrored)
    prof=[(0,.16),(.08,.2),(.18,.2),(.36,.19),(.44,.22),(.62,.22),(.7,.18),(.84,.14),(1,.11)]
    for sgn in (-1,1):
        pts=" ".join(f"{x0+(x1-x0)*a:.0f},{cy+sgn*h*b:.0f}" for a,b in prof)
        o.append(f'<polyline points="{pts}" {st} stroke-width="{sw*1.8}"/>')
    # compressor stages + turbine
    for i in range(12):
        x=x0+(x1-x0)*(.1+i*.022)
        hh=h*(.18-.004*i)
        o.append(f'<path d="M{x:.0f},{cy-hh:.0f}V{cy-h*.05:.0f}M{x:.0f},{cy+h*.05:.0f}V{cy+hh:.0f}" {st} stroke-width="{sw}"/>')
    for i in range(6):
        x=x0+(x1-x0)*(.45+i*.025)
        o.append(f'<rect x="{x:.0f}" y="{cy-h*.2:.0f}" width="{(x1-x0)*.012:.0f}" height="{h*.4:.0f}" {st} stroke-width="{sw}"/>')
    for i in range(3):
        x=x0+(x1-x0)*(.66+i*.03)
        o.append(f'<path d="M{x:.0f},{cy-h*.17:.0f}V{cy+h*.17:.0f}" {st} stroke-width="{sw*1.6}"/>')
    o.append(f'<path d="M{x0-20},{cy}H{x1+30}" {st} stroke-width="{sw*.8}" stroke-dasharray="40 10 6 10"/>')
    o.append(f'<rect x="{x0+(x1-x0)*.05:.0f}" y="{cy-h*.05:.0f}" width="{(x1-x0)*.75:.0f}" height="{h*.1:.0f}" {st} stroke-width="{sw}"/>')
    # dimensions
    o.append(f'<path d="M{x0},{cy+h*.3}H{x1} M{x0},{cy+h*.24}V{cy+h*.33} M{x1},{cy+h*.24}V{cy+h*.33}" {st} stroke-width="{sw*.8}"/>')
    o.append(T((x0+x1)/2,cy+h*.29,'145.75',h*.03,ink,'middle'))
    o.append(T(tx+tw*.04,ty+th*.25,'TURBOJET — GENERAL ARRANGEMENT',th*.17,ink))
    o.append(T(tx+tw*.04,ty+th*.58,'J47 · SEC. A–A',th*.2,ink))
    o.append(T(tx+tw*.04,ty+th*.9,'DR. J.J.L.',th*.17,ink));o.append(T(tx+tw*.6,ty+th*.9,'11-3-52',th*.17,ink))
    o.append(T(w*.06,h*.1,'NOTES: 1. ALL DIMS IN INCHES  2. BREAK SHARP EDGES',h*.022,ink))
    return ''.join(o)

def drawing_wingrib(w,h):
    o,ink,sw,(tx,ty,tw,th)=sheet(w,h,'white',2)
    st=f'stroke="{ink}" fill="none" stroke-linecap="round"'
    # airfoil rib
    pts=[]
    for i in range(61):
        t=i/60;x=w*.08+w*.8*t
        yt=h*.36-h*.22*(1.4845*math.sqrt(t)-.63*t-1.758*t*t+1.4215*t**3-.5075*t**4)
        pts.append(f'{x:.0f},{yt:.0f}')
    for i in range(60,-1,-1):
        t=i/60;x=w*.08+w*.8*t
        yb=h*.36+h*.07*(1.4845*math.sqrt(t)-.63*t-1.758*t*t+1.4215*t**3-.5075*t**4)
        pts.append(f'{x:.0f},{yb:.0f}')
    o.append(f'<polygon points="{" ".join(pts)}" {st} stroke-width="{sw*1.8}"/>')
    for k,(cx,r) in enumerate([(.26,.045),(.4,.05),(.54,.045),(.67,.035),(.78,.025)]):
        o.append(f'<circle cx="{w*cx:.0f}" cy="{h*.34:.0f}" r="{w*r:.0f}" {st} stroke-width="{sw*1.3}"/>')
    o.append(f'<path d="M{w*.05},{h*.34}H{w*.92}" {st} stroke-width="{sw*.8}" stroke-dasharray="36 9 6 9"/>')
    o.append(T(tx+tw*.04,ty+th*.25,'WING RIB — STA. 112',th*.18,ink))
    o.append(T(tx+tw*.04,ty+th*.58,'NACA 64A010',th*.2,ink))
    return ''.join(o)

def drawing_blue(w,h):
    o,ink,sw,(tx,ty,tw,th)=sheet(w,h,'blue',3)
    st=f'stroke="{ink}" fill="none" stroke-linecap="round" opacity=".85"'
    cx,cy=w*.3,h*.45
    teeth=[]
    for i in range(160):
        a=2*math.pi*i/160;r=h*(.27 if i%4 in(1,2) else .25)
        teeth.append(f'{cx+r*math.cos(a):.0f},{cy+r*math.sin(a):.0f}')
    o.append(f'<polygon points="{" ".join(teeth)}" {st} stroke-width="{sw*1.6}"/>')
    for r in (.08,.17):o.append(f'<circle cx="{cx:.0f}" cy="{cy:.0f}" r="{h*r:.0f}" {st} stroke-width="{sw*1.4}"/>')
    o.append(T(tx+tw*.04,ty+th*.25,'TRACTOR WORKS · WATERLOO, IOWA',th*.16,ink,extra='opacity=".9"'))
    return ''.join(o)

def drawing_sepia(w,h):
    o,ink,sw,_=sheet(w,h,'sepia',4)
    for i in range(14):
        y=h*(.12+i*.05)
        o.append(f'<path d="M{w*.06},{y:.0f}H{w*.9}" stroke="{ink}" stroke-width="{sw}" opacity=".35"/>')
    return ''.join(o)

def tape(x,y,rot,s=1):
    return f'<rect x="{x-38*s}" y="{y-26*s}" width="{76*s}" height="{52*s}" fill="#e9d9a8" fill-opacity=".72" transform="rotate({rot} {x} {y})"/>'

def thermos(L=620,D=150):
    o=[]
    # body along +x, lid at x<0
    o.append(f'<rect x="0" y="{-D/2}" width="{L}" height="{D}" rx="{D*.22}" fill="url(#green)"/>')
    o.append(f'<rect x="0" y="{-D/2}" width="{L}" height="{D}" rx="{D*.22}" fill="#000" filter="url(#hammer)"/>')
    o.append(f'<rect x="{L-D*.3}" y="{-D*.48}" width="{D*.34}" height="{D*.96}" rx="{D*.2}" fill="url(#chrome)"/>')
    for xx in (D*.25,L-D*.55): o.append(f'<rect x="{xx}" y="{-D/2}" width="9" height="{D}" fill="#e8c547"/>')
    # shoulder + neck
    o.append(f'<path d="M0,{-D/2} C{-D*.25},{-D/2} {-D*.28},{-D*.36} {-D*.32},{-D*.34} L{-D*.32},{D*.34} C{-D*.28},{D*.36} {-D*.25},{D/2} 0,{D/2} Z" fill="url(#green)"/>')
    # cup-lid: wider, chrome, with rolled rim and ribbed band
    cl=D*1.0
    o.append(f'<rect x="{-D*.32-cl}" y="{-D*.58}" width="{cl}" height="{D*1.16}" rx="{D*.1}" fill="url(#chrome)"/>')
    for k in range(5): o.append(f'<rect x="{-D*.32-cl+D*.16+k*D*.05}" y="{-D*.58}" width="{D*.02}" height="{D*1.16}" fill="#5e666c" fill-opacity=".5"/>')
    o.append(f'<rect x="{-D*.32-cl-D*.06}" y="{-D*.62}" width="{D*.1}" height="{D*1.24}" rx="{D*.05}" fill="url(#chrome)"/>')
    o.append(f'<rect x="{-D*.32-cl-D*.06}" y="{-D*.62}" width="{D*.1}" height="{D*1.24}" rx="{D*.05}" fill="none" stroke="#4a5055" stroke-width="2"/>')
    o.append(f'<g transform="translate({L*.48},0) rotate(0)"><ellipse rx="{D*.42}" ry="{D*.3}" fill="#e8c547"/><ellipse rx="{D*.38}" ry="{D*.26}" fill="#2f6e26"/>{deer(0,1,D*.0075,"#f2cf4a")}</g>')
    o.append(f'<rect x="{-D*.3}" y="{-D*.38}" width="{L+D*.2}" height="{D*.08}" fill="#fff" fill-opacity=".18"/>')
    return ''.join(o)

def clock(R=150):
    o=[]
    o.append(f'<rect x="{-R*1.12}" y="{-R*1.12}" width="{R*2.24}" height="{R*2.24}" rx="{R*.18}" fill="#1b1d1f"/>')
    for sx in (-1,1):
        for sy in (-1,1): o.append(f'<circle cx="{sx*R*.92}" cy="{sy*R*.92}" r="{R*.07}" fill="#8b8f92"/><path d="M{sx*R*.92-R*.05},{sy*R*.92} h{R*.1}" stroke="#333" stroke-width="3"/>')
    o.append(f'<circle r="{R*1.0}" fill="#3a3d40"/><circle r="{R*.9}" fill="url(#dial)"/>')
    for i in range(60):
        a=i*math.pi/30;L_=R*(.12 if i%5==0 else .05)
        o.append(f'<path d="M{R*.86*math.sin(a):.1f},{-R*.86*math.cos(a):.1f} L{(R*.86-L_)*math.sin(a):.1f},{-(R*.86-L_)*math.cos(a):.1f}" stroke="#e9e4cf" stroke-width="{3 if i%5==0 else 1.5}"/>')
    for n in range(1,13):
        a=n*math.pi/6
        o.append(T(R*.62*math.sin(a),-R*.62*math.cos(a)+R*.07,str(n),R*.19,'#e9e4cf','middle',FONT,'font-weight="bold"'))
    o.append(T(0,R*.36,'8 DAY',R*.1,'#a9a490','middle'))
    def hand(ang,l,wd,col):
        return f'<path d="M0,{R*.08} L{-wd},0 L0,{-l} L{wd},0 Z" fill="{col}" transform="rotate({ang})"/>'
    o.append(hand(352,R*.48,R*.05,'#efe9d2'));o.append(hand(282,R*.72,R*.035,'#efe9d2'));o.append(hand(150,R*.78,R*.01,'#d24a2a'))
    o.append(f'<circle r="{R*.05}" fill="#999"/><ellipse cx="{-R*.3}" cy="{-R*.4}" rx="{R*.5}" ry="{R*.2}" fill="#fff" fill-opacity=".07" transform="rotate(-30)"/>')
    return ''.join(o)

def jet(s=1):
    # swept-wing fighter, top view, nose toward -y
    o=[]
    al='#b9c0c5'
    o.append(f'<ellipse cx="0" cy="40" rx="150" ry="70" fill="#2d1c10"/>')                    # stand base
    o.append('<rect x="-8" y="-40" width="16" height="90" fill="#3a2a1a"/>')
    wing="M-12,-30 L-250,120 L-250,150 L-30,70 Z M12,-30 L250,120 L250,150 L30,70 Z"
    o.append(f'<path d="{wing}" fill="{al}"/>')
    o.append('<path d="M-10,190 L-110,250 L-110,268 L-12,232 Z M10,190 L110,250 L110,268 L12,232 Z" fill="#a9b0b5"/>')
    o.append('<path d="M0,-260 C24,-250 34,-200 34,-120 L30,230 C26,262 14,272 0,274 C-14,272 -26,262 -30,230 L-34,-120 C-34,-200 -24,-250 0,-260 Z" fill="url(#chromeH)"/>')
    o.append('<ellipse cx="0" cy="-258" rx="16" ry="8" fill="#1a1a1a"/><path d="M0,-200 C12,-200 16,-170 14,-140 L-14,-140 C-16,-170 -12,-200 0,-200 Z" fill="#2e3b45"/>')
    o.append('<path d="M-4,170 L0,200 L4,170 Z M0,150 L-3,250 L3,250 Z" fill="#9aa1a6"/>')
    for sx in (-1,1):
        x=sx*165
        o.append(f'<circle cx="{x}" cy="100" r="28" fill="#1f3a8a"/><rect x="{x-56}" y="94" width="112" height="13" fill="#f3f3f3"/><rect x="{x-56}" y="99" width="112" height="3" fill="#b22"/><circle cx="{x}" cy="100" r="22" fill="#1f3a8a"/>')
        o.append(f'<path d="M{x},{80} L{x+5},{95} L{x+20},{95} L{x+8},{104} L{x+13},{119} L{x},{110} L{x-13},{119} L{x-8},{104} L{x-20},{95} L{x-5},{95} Z" fill="#fff"/>')
    o.append(T(0,40,'U.S. AIR FORCE',12,'#333','middle',FONT,'transform="rotate(90 0 40)"'))
    o.append(T(-150,140,'FU-178',13,'#333','middle',FONT,'transform="rotate(-31 -150 140)"'))
    return f'<g transform="scale({s})">{"".join(o)}</g>'

def logbook(w=420,h=560):
    o=[]
    o.append(f'<rect x="8" y="10" width="{w}" height="{h}" rx="10" fill="#e9e1cc"/>')                  # page block edge
    o.append(f'<rect x="0" y="0" width="{w}" height="{h}" rx="10" fill="#3d4732"/>')
    o.append(f'<rect x="0" y="0" width="{w}" height="{h}" rx="10" fill="#000" filter="url(#fiber)"/>')
    o.append(f'<rect x="0" y="0" width="26" height="{h}" fill="#2c3423"/>')
    o.append(f'<rect x="{w*.12}" y="{h*.1}" width="{w*.76}" height="{h*.28}" fill="none" stroke="#d9cfa8" stroke-width="3" stroke-opacity=".7"/>')
    o.append(T(w/2,h*.2,"PILOT'S",w*.1,'#e2d7ad','middle',MONO,'font-weight="bold" letter-spacing="4" opacity=".85"'))
    o.append(T(w/2,h*.31,'FLIGHT LOG',w*.1,'#e2d7ad','middle',MONO,'font-weight="bold" letter-spacing="3" opacity=".85"'))
    o.append(T(w/2,h*.48,'U.S. AIR FORCE',w*.055,'#cfc49b','middle',MONO,'letter-spacing="3" opacity=".7"'))
    o.append(T(w/2,h*.9,'AF FORM 5',w*.045,'#cfc49b','middle',MONO,'opacity=".6"'))
    return ''.join(o)

def aviators(s=1):
    o=[]
    lens="M0,0 C30,-8 92,-8 104,8 C114,26 100,74 64,82 C30,88 2,60 -2,30 C-4,16 -4,4 0,0 Z"
    o.append(f'<path d="{lens}" fill="url(#lens)" fill-opacity=".92" stroke="#c9a54a" stroke-width="4"/>')
    o.append(f'<path d="{lens}" fill="url(#lens)" fill-opacity=".92" stroke="#c9a54a" stroke-width="4" transform="translate(250,0) scale(-1,1)"/>')
    o.append('<path d="M104,10 C120,-2 130,-2 146,10" fill="none" stroke="#c9a54a" stroke-width="4"/><path d="M100,-2 C118,-12 132,-12 150,-2" fill="none" stroke="#c9a54a" stroke-width="3"/>')
    o.append('<path d="M0,6 L-120,28 C-140,32 -150,46 -146,60" fill="none" stroke="#c9a54a" stroke-width="4"/><path d="M250,6 L370,28 C390,32 400,46 396,60" fill="none" stroke="#c9a54a" stroke-width="4"/>')
    o.append('<path d="M14,10 C40,4 70,6 84,16" stroke="#fff" stroke-opacity=".35" stroke-width="5" fill="none"/>')
    return f'<g transform="scale({s})">{"".join(o)}</g>'

def tsquare(L=1500):
    o=[]
    o.append(f'<rect x="0" y="-70" width="58" height="420" rx="6" fill="#1b1b1b"/><rect x="6" y="-62" width="12" height="404" fill="#444"/>')
    o.append(f'<rect x="58" y="0" width="{L}" height="64" fill="#c99b5c"/><rect x="58" y="0" width="{L}" height="64" fill="#000" filter="url(#woodgrain)"/>')
    o.append(f'<rect x="58" y="-2" width="{L}" height="14" fill="#b8d8d2" fill-opacity=".45"/><rect x="58" y="52" width="{L}" height="14" fill="#b8d8d2" fill-opacity=".45"/>')
    for sx in (90,140): o.append(f'<circle cx="{sx}" cy="32" r="6" fill="#d8c8a0"/>')
    return ''.join(o)

def notepad(w=520,h=700):
    o=[]
    o.append(f'<rect x="6" y="8" width="{w}" height="{h}" fill="#bfcab3"/>')
    o.append(f'<rect width="{w}" height="{h}" fill="#dfe8cf"/>')
    gp=[f'M{x},{70}V{h}' for x in range(0,w,20)]+[f'M0,{y}H{w}' for y in range(70,h,20)]
    o.append(f'<path d="{"".join(gp)}" stroke="#7fa37a" stroke-width="1" stroke-opacity=".35"/>')
    o.append(f'<rect width="{w}" height="60" fill="#5b4a33"/><rect y="56" width="{w}" height="6" fill="#3a2e1e"/>')
    o.append(T(w/2,40,'ENGINEERING COMPUTATION',20,'#e9dfc4','middle',MONO,'font-weight="bold" letter-spacing="2"'))
    lines=['Thrust  F = 5200 lb','W/S = 13 400 / 288 = 46.5','q = ½ρV²  →  0.00238 × 590²','  = 414 psf','CL = W / (qS)','   = 13 400 / (414 × 288)','   = 0.112  ✓  (slide rule)','Re = 9.4 × 10⁶']
    for i,t in enumerate(lines):
        o.append(T(30,130+i*58,t,26,'#555','start','DejaVu Sans, sans-serif',f'font-style="italic" opacity=".78" transform="rotate(-.6 30 {130+i*58})"'))
    return ''.join(o)

def leadholder(L=520):
    return (f'<rect x="0" y="-11" width="{L*.62}" height="22" rx="4" fill="#24402a"/><rect x="0" y="-11" width="{L*.62}" height="7" fill="#fff" fill-opacity=".18"/>'
            f'<rect x="{L*.62}" y="-12" width="{L*.22}" height="24" fill="url(#chrome)"/>'
            + ''.join(f'<rect x="{L*.62+k*7}" y="-12" width="2" height="24" fill="#555" fill-opacity=".5"/>' for k in range(int(L*.22/7)))
            + f'<path d="M{L*.84},-8 L{L*.95},-3 L{L*.95},3 L{L*.84},8 Z" fill="url(#chrome)"/><path d="M{L*.95},-2 L{L},0 L{L*.95},2 Z" fill="#333"/>'
            f'<rect x="-{L*.06}" y="-9" width="{L*.06}" height="18" rx="5" fill="url(#chrome)"/>')

def pencil(L=600,col='#e8b923'):
    return (f'<rect x="0" y="-11" width="{L*.86}" height="22" fill="{col}"/><rect x="0" y="-11" width="{L*.86}" height="7" fill="#fff" fill-opacity=".25"/><rect x="0" y="4" width="{L*.86}" height="7" fill="#000" fill-opacity=".15"/>'
            f'<path d="M{L*.86},-11 L{L*.97},-1 L{L*.97},1 L{L*.86},11 Z" fill="#e1b98a"/><path d="M{L*.95},-2 L{L},0 L{L*.95},2 Z" fill="#333"/>'
            f'<rect x="-{L*.07}" y="-12" width="{L*.07}" height="24" fill="url(#brass)"/><rect x="-{L*.13}" y="-11" width="{L*.06}" height="22" rx="6" fill="#c98a7e"/>')

def triangle(s=1):
    return f'<path transform="scale({s})" d="M0,0 L0,620 L360,620 Z M50,150 L50,570 L290,570 Z" fill="#c8a24a" fill-opacity=".28" fill-rule="evenodd" stroke="#8a6a20" stroke-opacity=".6" stroke-width="5"/>'

def lamp(s=1):
    o=[]
    o.append('<path d="M-20,-200 L-300,-470 L-620,-300" fill="none" stroke="url(#chromeH)" stroke-width="20" stroke-linecap="round" stroke-linejoin="round"/>')
    o.append('<path d="M-40,-215 L-290,-455" stroke="#8b9399" stroke-width="6" stroke-dasharray="8 6"/><circle cx="-300" cy="-470" r="22" fill="url(#chromeH)"/>')
    o.append('<path d="M-70,-200 C-70,-232 70,-232 70,-200 L200,-10 C200,40 -200,40 -200,-10 Z" fill="#163222"/>')
    o.append('<path d="M-70,-200 C-70,-232 70,-232 70,-200 L200,-10 C200,40 -200,40 -200,-10 Z" fill="#000" filter="url(#hammer)"/>')
    o.append('<path d="M-40,-206 L-150,-20" stroke="#6f9a78" stroke-opacity=".55" stroke-width="16" stroke-linecap="round"/>')
    o.append('<rect x="-26" y="-250" width="52" height="40" rx="8" fill="url(#chromeH)"/>')
    o.append('<ellipse cx="0" cy="-8" rx="200" ry="56" fill="#3a5a44"/><ellipse cx="0" cy="-2" rx="188" ry="48" fill="#fff3cf"/><ellipse cx="0" cy="-2" rx="110" ry="30" fill="url(#bulb)"/>')
    return f'<g transform="scale({s})">{"".join(o)}</g>'

def compass(s=1):
    return f'<g transform="scale({s})"><path d="M0,0 L-80,300 M0,0 L80,300" stroke="url(#chromeH)" stroke-width="14" stroke-linecap="round"/><path d="M-62,210 H62" stroke="#9aa1a6" stroke-width="6"/><circle cy="210" r="12" fill="#ccc"/><circle r="26" fill="url(#chromeH)"/><rect x="-8" y="-70" width="16" height="50" rx="6" fill="#8b9399"/></g>'

def coffee_ring(x,y,r):
    return (f'<circle cx="{x}" cy="{y}" r="{r}" fill="none" stroke="#6b3e1c" stroke-opacity=".32" stroke-width="{r*.1:.0f}"/>'
            f'<circle cx="{x+5}" cy="{y+4}" r="{r*.96}" fill="none" stroke="#6b3e1c" stroke-opacity=".15" stroke-width="{r*.05:.0f}"/>')

def crumbs(x0,y0,x1,y1,n,seed):
    r=random.Random(seed);o=[]
    for i in range(n):
        x=r.uniform(x0,x1);y=r.uniform(y0,y1)
        o.append(f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="{r.uniform(2,6):.1f}" ry="{r.uniform(1.5,3.5):.1f}" fill="#c98a7e" opacity=".6"/>')
    return ''.join(o)

# ---------------- compositions ----------------
def scene(W,H,P):
    o=[f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',DEFS]
    by=P['boardTop'];fy=P['front']
    # back of the desk (walnut, in shadow) and the board
    o.append(f'<rect width="{W}" height="{H}" fill="#120c08"/>')
    o.append(g(f'<rect width="{W}" height="{by}" fill="url(#walnut)"/><rect width="{W}" height="{by}" fill="#000" filter="url(#woodgrain)"/>',flt='b4'))
    o.append(g(f'<rect y="{by}" width="{W}" height="{fy-by}" fill="#9fb09a"/><rect y="{by}" width="{W}" height="{fy-by}" fill="#000" filter="url(#grain)"/>'
               f'<rect y="{by-10}" width="{W}" height="14" fill="url(#chrome)"/>',flt='b3'))
    o.append(g(f'<rect y="{fy}" width="{W}" height="{H-fy}" fill="url(#oak)"/><rect y="{fy}" width="{W}" height="{H-fy}" fill="#000" filter="url(#woodgrain)"/><rect y="{fy+18}" width="{W}" height="10" fill="#3a2410" opacity=".7"/>',flt='b2'))
    # back objects
    for kind,x,y,rot,s in P['back']:
        body={'jet':jet(s),'clock':clock(150*s),'lamp':lamp(s),'logbook':logbook()+g(aviators(.9),'translate(70,190) rotate(-8)'),'book2':g(logbook(),'scale(.9)')}[kind]
        o.append(g(body,f'translate({x},{y}) rotate({rot})',{'jet':'b4','clock':'b3','lamp':'b2'}.get(kind,'b3')))
    # the stacked shop drawings, fanned
    for kind,x,y,w,h,rot in P['sheets']:
        f={'turbojet':drawing_turbojet,'wingrib':drawing_wingrib,'blue':drawing_blue,'sepia':drawing_sepia}[kind]
        tp=tape(30,30,8)+tape(w-30,30,-6)+tape(30,h-30,-4)+tape(w-30,h-30,10)
        o.append(g(f(w,h)+tp,f'translate({x},{y}) rotate({rot})','b2'))
    for x,y,r in P['rings']: o.append(g(coffee_ring(x,y,r),flt='b2'))
    o.append(g(crumbs(*P['crumbs'],40,9),flt='b2'))
    for kind,x,y,rot,s in P['mid']:
        body={'tsq':tsquare(P.get('tsqL',1500)),'triangle':triangle(s),'notepad':notepad(),'compass':compass(s),'logbook':logbook()+g(aviators(.9),'translate(60,200) rotate(-8)'),
              'thermos':thermos(),'lead':leadholder(),'pencil':pencil(),'pencilR':pencil(560,'#c24a2a')}[kind]
        o.append(g(body,f'translate({x},{y}) rotate({rot}) scale({s if kind in ("notepad","thermos","logbook","lead","pencil","pencilR","tsq") else 1})','b1' if kind in('thermos','lead','pencil','pencilR') else 'b2'))
    # the slide rule: in focus
    x,y,rot,L,Hh=P['rule']
    o.append(g(slide_rule(L,Hh),f'translate({x},{y}) rotate({rot})','b0'))
    # late-night lamp light: warm pool, deep falloff
    lx,ly,rx,ry=P['light']
    o.append(f'<defs><radialGradient id="pool" gradientUnits="userSpaceOnUse" cx="{lx}" cy="{ly}" r="{rx}" gradientTransform="translate({lx} {ly}) scale(1 {ry/rx}) translate({-lx} {-ly})">'
             '<stop offset="0" stop-color="#000" stop-opacity="0"/><stop offset=".45" stop-color="#05040a" stop-opacity=".12"/><stop offset=".78" stop-color="#05040a" stop-opacity=".55"/><stop offset="1" stop-color="#030305" stop-opacity=".8"/></radialGradient>'
             f'<radialGradient id="warm" gradientUnits="userSpaceOnUse" cx="{lx}" cy="{ly}" r="{rx*.8}"><stop offset="0" stop-color="#ffcf7a" stop-opacity=".22"/><stop offset="1" stop-color="#ffcf7a" stop-opacity="0"/></radialGradient></defs>')
    o.append(f'<rect width="{W}" height="{H}" fill="#ffd9a0" fill-opacity=".14" style="mix-blend-mode:multiply"/>')
    o.append(f'<rect width="{W}" height="{H}" fill="url(#warm)" style="mix-blend-mode:screen"/>')
    o.append(f'<rect width="{W}" height="{H}" fill="url(#pool)"/>')
    for kind,x,y,rot,s in P['back']:
        if kind=='lamp': o.append(f'<ellipse cx="{x}" cy="{y+20*s}" rx="{230*s}" ry="{90*s}" fill="#ffe7b0" opacity=".7" filter="url(#glow)" transform="rotate({rot} {x} {y})"/>')
    o.append(f'<rect width="{W}" height="{H}" fill="#000" filter="url(#grain)" opacity=".6"/>')
    o.append('</svg>')
    return '\n'.join(o)

LAND=dict(boardTop=250,front=1040,
  back=[('jet',1580,150,-62,.62),('clock',2170,190,0,.9),('lamp',420,250,-6,.85)],
  sheets=[('sepia',430,330,1600,740,-3.5),('blue',560,285,1560,720,2.6),('wingrib',470,345,1580,700,-1.4),('turbojet',600,300,1460,680,.9)],
  rings=[(1880,600,80)],crumbs=(900,700,1400,780),
  mid=[('tsq',-20,640,0,1),('logbook',70,300,-12,.85),('triangle',700,330,-18,.9),('thermos',2040,520,-28,1),('notepad',1720,760,7,.9),('lead',1700,730,-10,1),('pencil',260,1010,-2,1),('pencilR',1080,1020,-1,1)],
  rule=(60,790,-1.5,2300,165),light=(1050,700,1500,900))
PORT=dict(boardTop=640,front=2310,
  back=[('clock',230,330,0,1.0),('jet',690,440,-28,.6),('lamp',860,470,8,.75)],
  sheets=[('sepia',70,760,980,1400,-3.5),('blue',130,720,950,1380,3),('wingrib',50,800,1000,1360,-1.6),('turbojet',140,750,900,1340,1.2)],
  rings=[(840,1180,70)],crumbs=(200,1450,700,1520),
  mid=[('tsq',-30,1450,0,1),('logbook',-110,820,-14,.8),('thermos',860,1130,64,.85),('triangle',600,1500,12,.75),('notepad',560,1990,-8,.9),('compass',170,1880,-30,.9),('lead',590,1960,-14,1),('pencil',40,2350,-2,1),('pencilR',560,2360,-1,1)],
  rule=(-230,2080,-19,1720,150),light=(560,1450,1200,1500))
if __name__=='__main__':
    open('land.svg','w').write(scene(2400,1100,LAND))
    open('port.svg','w').write(scene(1100,2400,PORT))
