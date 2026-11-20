import math,random
random.seed(1952)
W=H=2000
o=[]
A=o.append
from deer2 import deer
A(f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<defs>
 <radialGradient id="lamp" cx="30%" cy="22%" r="85%"><stop offset="0" stop-color="#fff2cf" stop-opacity=".55"/><stop offset=".45" stop-color="#ffe7b0" stop-opacity=".12"/><stop offset="1" stop-color="#000" stop-opacity="0"/></radialGradient>
 <radialGradient id="vig" cx="50%" cy="48%" r="72%"><stop offset=".55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#05080a" stop-opacity=".72"/></radialGradient>
 <linearGradient id="board" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#9fb59b"/><stop offset="1" stop-color="#6d826d"/></linearGradient>
 <linearGradient id="bp" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#2a5ba3"/><stop offset=".6" stop-color="#1f4787"/><stop offset="1" stop-color="#173a72"/></linearGradient>
 <linearGradient id="wood" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#a8743f"/><stop offset=".5" stop-color="#8a5a2c"/><stop offset="1" stop-color="#5e3a1a"/></linearGradient>
 <linearGradient id="chrome" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#8b9399"/><stop offset=".3" stop-color="#f4f6f7"/><stop offset=".55" stop-color="#b9c0c5"/><stop offset=".8" stop-color="#eef1f3"/><stop offset="1" stop-color="#7b838a"/></linearGradient>
 <linearGradient id="green" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#1f4e1b"/><stop offset=".35" stop-color="#3f8a33"/><stop offset=".55" stop-color="#5aa349"/><stop offset=".75" stop-color="#367c2b"/><stop offset="1" stop-color="#1a4316"/></linearGradient>
 <linearGradient id="pencil" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#2a6223"/><stop offset=".33" stop-color="#4d963f"/><stop offset=".34" stop-color="#367c2b"/><stop offset=".66" stop-color="#2e6e25"/><stop offset=".67" stop-color="#245a1e"/><stop offset="1" stop-color="#173d13"/></linearGradient>
 <linearGradient id="brass" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#8a6a1c"/><stop offset=".35" stop-color="#f2d27a"/><stop offset=".7" stop-color="#c49a32"/><stop offset="1" stop-color="#6e5214"/></linearGradient>
 <linearGradient id="ivory" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#f3ead2"/><stop offset="1" stop-color="#e6dcbf"/></linearGradient>
 <radialGradient id="coffee" cx="45%" cy="40%" r="60%"><stop offset="0" stop-color="#6b3d1e"/><stop offset=".7" stop-color="#3b200e"/><stop offset="1" stop-color="#26150a"/></radialGradient>
 <filter id="grain" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="2" seed="7"/><feColorMatrix values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .22 0"/><feComposite in2="SourceGraphic" operator="in"/></filter>
 <filter id="mottle" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".006" numOctaves="3" seed="3"/><feColorMatrix values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 .16 0"/><feComposite in2="SourceGraphic" operator="in"/></filter>
 <filter id="soft" x="-5%" y="-5%" width="110%" height="110%"><feGaussianBlur stdDeviation="7"/></filter>
 <filter id="obj" x="-10%" y="-10%" width="120%" height="120%"><feDropShadow dx="10" dy="16" stdDeviation="12" flood-color="#000" flood-opacity=".5"/><feGaussianBlur stdDeviation="2.8"/></filter>
 <filter id="paper" x="-5%" y="-5%" width="110%" height="110%"><feDropShadow dx="6" dy="10" stdDeviation="10" flood-color="#000" flood-opacity=".35"/><feGaussianBlur stdDeviation="6.5"/></filter>
</defs>
''')
# ---------- drafting board (green vinyl cover) + oak edge
A('<g filter="url(#soft)">')
A(f'<rect width="{W}" height="{H}" fill="url(#board)"/>')
A(f'<rect width="{W}" height="{H}" fill="#000" filter="url(#grain)"/>')
A('<rect y="1868" width="2000" height="132" fill="url(#wood)"/><rect y="1862" width="2000" height="8" fill="#c9cfd3"/>')
A('</g>')
# ---------- blueprint
bp=[]
B=bp.append
B('<g transform="rotate(-6 860 860)" filter="url(#paper)">')
B('<rect x="250" y="410" width="1220" height="880" fill="url(#bp)"/>')
B('<rect x="250" y="410" width="1220" height="880" fill="#000" filter="url(#mottle)"/>')
ln='stroke="#e8f0ff" fill="none" stroke-linecap="round"'
B(f'<g {ln} stroke-opacity=".88">')
B('<rect x="282" y="442" width="1156" height="816" stroke-width="3"/>')
gx,gy=640,830
pts=[]
N=38
for i in range(N*4):
    a=2*math.pi*i/(N*4)
    k=i%4
    r=232 if k in (1,2) else 212
    pts.append(f'{gx+r*math.cos(a):.1f},{gy+r*math.sin(a):.1f}')
B(f'<polygon points="{" ".join(pts)}" stroke-width="2.6"/>')
for r,w in ((196,1.4),(74,2.4),(36,2.2)):
    B(f'<circle cx="{gx}" cy="{gy}" r="{r}" stroke-width="{w}"/>')
for i in range(6):
    a=2*math.pi*i/6+.3
    B(f'<circle cx="{gx+138*math.cos(a):.1f}" cy="{gy+138*math.sin(a):.1f}" r="30" stroke-width="2.2"/>')
B(f'<circle cx="{gx}" cy="{gy}" r="138" stroke-width="1.2" stroke-dasharray="26 8 4 8"/>')
B(f'<path d="M{gx-280},{gy} H{gx+280} M{gx},{gy-280} V{gy+280}" stroke-width="1.3" stroke-dasharray="34 9 5 9"/>')
B(f'<path d="M{gx-6},{gy-36} h12 v-12 h-12 z" stroke-width="2"/>')
# dimension line under the gear
B(f'<path d="M{gx-232},{gy+250} V{gy+330} M{gx+232},{gy+250} V{gy+330} M{gx-232},{gy+310} H{gx+232}" stroke-width="1.4"/>')
B(f'<path d="M{gx-232},{gy+310} l22,-7 v14 z M{gx+232},{gy+310} l-22,-7 v14 z" fill="#e8f0ff" stroke-width="1"/>')
B(f'<path d="M{gx+170},{gy-170} L{gx+300},{gy-290} H{gx+430}" stroke-width="1.4"/>')
# section view
sx=990
B(f'<rect x="{sx}" y="{gy-232}" width="70" height="464" stroke-width="2.4"/>')
B(f'<rect x="{sx-30}" y="{gy-74}" width="130" height="148" stroke-width="2.4"/>')
for i in range(-20,26):
    y0=gy-232+i*22
    B(f'<path d="M{sx},{y0+70} L{sx+70},{y0}" stroke-width="1" stroke-opacity=".55"/>')
B(f'<path d="M{sx+35},{gy-290} V{gy+290}" stroke-width="1.2" stroke-dasharray="30 8 4 8"/>')
# title block
tx,ty=1110,1130
B(f'<rect x="{tx}" y="{ty}" width="328" height="128" stroke-width="2.4"/>')
for yy in (ty+34,ty+68,ty+98): B(f'<path d="M{tx},{yy} H{tx+328}" stroke-width="1.4"/>')
B(f'<path d="M{tx+180},{ty+68} V{ty+128}" stroke-width="1.4"/>')
B('</g>')
tf='font-family="DejaVu Sans Condensed, DejaVu Sans, sans-serif" fill="#e8f0ff" fill-opacity=".9"'
B(f'<text x="{tx+12}" y="{ty+24}" font-size="17" {tf} letter-spacing="1.5">TRACTOR WORKS · WATERLOO, IOWA</text>')
B(f'<text x="{tx+12}" y="{ty+58}" font-size="21" {tf} letter-spacing="1">DRIVE GEAR · 38 TEETH</text>')
B(f'<text x="{tx+12}" y="{ty+90}" font-size="15" {tf}>DR. J.J.L.</text><text x="{tx+192}" y="{ty+90}" font-size="15" {tf}>3-14-52</text>')
B(f'<text x="{tx+12}" y="{ty+120}" font-size="15" {tf}>SCALE: FULL</text><text x="{tx+192}" y="{ty+120}" font-size="15" {tf}>R-4081</text>')
B(f'<text x="{gx-60}" y="{gy+300}" font-size="24" {tf}>Ø 9.250</text>')
B(f'<text x="{gx+310}" y="{gy-300}" font-size="20" {tf}>38 T  4 DP  20° PA</text>')
B(f'<text x="300" y="1240" font-size="15" {tf} letter-spacing="2">ALL DIMENSIONS IN INCHES · BREAK SHARP EDGES</text>')
# fold creases
for x in (660,1060):
    B(f'<path d="M{x},410 V1290" stroke="#000" stroke-opacity=".18" stroke-width="3"/><path d="M{x+3},410 V1290" stroke="#fff" stroke-opacity=".12" stroke-width="2"/>')
B('<path d="M250,850 H1470" stroke="#000" stroke-opacity=".16" stroke-width="3"/><path d="M250,853 H1470" stroke="#fff" stroke-opacity=".1" stroke-width="2"/>')
B('</g>')
o+=bp
# ---------- tracing vellum with a graphite wheel elevation and a coffee ring
A('<g transform="rotate(8 1520 1520)" filter="url(#paper)">')
A('<rect x="1060" y="1130" width="940" height="760" fill="#efe9da" opacity=".97"/>')
A('<rect x="1060" y="1130" width="940" height="760" fill="#000" filter="url(#grain)" opacity=".6"/>')
A('<g stroke="#4a4a4a" fill="none" stroke-opacity=".75" stroke-linecap="round">')
cx,cy=1460,1500
for r,w in ((250,2.2),(214,1.4),(90,2),(54,1.6)): A(f'<circle cx="{cx}" cy="{cy}" r="{r}" stroke-width="{w}"/>')
for i in range(8):
    a=2*math.pi*i/8
    A(f'<path d="M{cx+90*math.cos(a):.0f},{cy+90*math.sin(a):.0f} L{cx+214*math.cos(a):.0f},{cy+214*math.sin(a):.0f}" stroke-width="5" stroke-opacity=".35"/>')
A(f'<path d="M{cx-300},{cy} H{cx+300} M{cx},{cy-300} V{cy+300}" stroke-width="1" stroke-dasharray="26 8 4 8"/>')
A(f'<path d="M{cx+250},{cy-60} H{cx+390} M{cx+250},{cy+60} H{cx+390} M{cx+370},{cy-60} V{cy+60}" stroke-width="1.2"/>')
A('</g>')
A(f'<text x="{cx+300}" y="{cy+110}" font-size="22" font-family="DejaVu Sans, sans-serif" fill="#4a4a4a" fill-opacity=".7" transform="rotate(-1 {cx} {cy})">2.375</text>')
A('<circle cx="1760" cy="1290" r="74" fill="none" stroke="#7a4a22" stroke-opacity=".35" stroke-width="9"/>')
A('<circle cx="1766" cy="1296" r="70" fill="none" stroke="#7a4a22" stroke-opacity=".18" stroke-width="4"/>')
A('</g>')
# ---------- 30/60 triangle, clear with a green edge tint
A('<g transform="rotate(14 330 1500)" filter="url(#paper)">')
A('<path d="M110,1180 L110,1820 L480,1820 Z M160,1330 L160,1770 L410,1770 Z" fill="#9fd6b4" fill-opacity=".28" fill-rule="evenodd" stroke="#2f7a52" stroke-opacity=".55" stroke-width="5"/>')
A('</g>')
# ---------- the slide rule, lying across the top
A('<g transform="translate(40 455) rotate(-2.5)" filter="url(#obj)">')
A('<rect x="0" y="0" width="1560" height="112" rx="3" fill="url(#ivory)"/>')
A('<rect x="0" y="36" width="1560" height="40" fill="#f6eed8"/><rect x="0" y="35" width="1560" height="1.5" fill="#6b4a2a" fill-opacity=".5"/><rect x="0" y="76" width="1560" height="1.5" fill="#6b4a2a" fill-opacity=".5"/>')
A('<rect x="0" y="112" width="1560" height="10" fill="#5a3518"/>')
t=[]
for row,(y,up) in enumerate(((34,True),(40,False),(74,True),(80,False))):
    for i in range(1,400):
        x=90+1380*math.log10(1+9*i/400)
        L=10 if i%40==0 else (6 if i%10==0 else 3.5)
        y2=y-L if up else y+L
        t.append(f'M{x:.1f},{y} V{y2:.1f}')
A(f'<path d="{" ".join(t)}" stroke="#2a2520" stroke-width="1.1" stroke-opacity=".8"/>')
A('<rect x="1490" y="-6" width="56" height="134" rx="4" fill="url(#chrome)"/><rect x="14" y="-6" width="56" height="134" rx="4" fill="url(#chrome)"/>')
A('<rect x="760" y="-14" width="150" height="150" rx="10" fill="#d8ecf0" fill-opacity=".22" stroke="#d9dee2" stroke-width="7"/><path d="M835,-14 V136" stroke="#111" stroke-width="2"/>')
A('</g>')
# ---------- steel thermos (green enamel) with a small deer decal, and its cup
A('<g transform="translate(1790 760) rotate(58)" filter="url(#obj)">')
A('<rect x="-100" y="-380" width="200" height="820" rx="40" fill="url(#green)"/>')
A('<rect x="-100" y="-380" width="200" height="820" rx="40" fill="#000" filter="url(#grain)" opacity=".7"/>')
A('<rect x="-92" y="-452" width="184" height="92" rx="12" fill="url(#chrome)"/><rect x="-74" y="-488" width="148" height="42" rx="10" fill="url(#chrome)"/>')
for k in range(6): A(f'<rect x="-92" y="{-446+k*14}" width="184" height="3" fill="#6f777d" fill-opacity=".45"/>')
A('<rect x="-100" y="-322" width="200" height="11" fill="#e8c547"/><rect x="-100" y="392" width="200" height="11" fill="#e8c547"/>')
A('<g transform="rotate(-90)"><ellipse cx="60" cy="0" rx="96" ry="64" fill="#e8c547"/><ellipse cx="60" cy="0" rx="88" ry="56" fill="#2f6e26"/>')
A(deer(60,2,1.45,'#f2cf4a'))
A('</g>')
A('</g>')
A('<g filter="url(#obj)"><circle cx="1600" cy="1200" r="92" fill="url(#chrome)"/><circle cx="1600" cy="1200" r="76" fill="url(#coffee)"/><ellipse cx="1578" cy="1172" rx="30" ry="12" fill="#fff" fill-opacity=".18"/></g>')
# ---------- bow compass on the vellum
A('<g transform="translate(1180 1690) rotate(-28)" filter="url(#obj)">')
A('<path d="M0,0 L-70,240 M0,0 L70,240" stroke="url(#chrome)" stroke-width="13" stroke-linecap="round"/><path d="M-70,240 l-6,30 M70,240 l4,30" stroke="#333" stroke-width="5"/>')
A('<path d="M-55,170 H55" stroke="#9aa1a6" stroke-width="5"/><circle cx="0" cy="170" r="12" fill="url(#chrome)"/>')
A('<circle cx="0" cy="0" r="22" fill="url(#chrome)"/><rect x="-7" y="-60" width="14" height="44" rx="5" fill="#8b9399"/>')
A('</g>')
# ---------- the pencil: green, gold-stamped, with a leaping deer
A('<g transform="translate(980 1428) rotate(-4)" filter="url(#obj)">')
A('<rect x="-560" y="-16" width="1080" height="32" fill="url(#pencil)"/>')
A('<path d="M520,-16 L612,0 L520,16 Z" fill="#dcb27e"/><path d="M520,-16 L612,0 L520,-1 Z" fill="#e9c695"/><path d="M590,-4 L622,0 L590,4 Z" fill="#2e2e2e"/>')
A('<path d="M520,-16 q6,8 0,16 q6,8 0,16" fill="none" stroke="#2a6223" stroke-width="3"/>')
A('<rect x="-626" y="-18" width="66" height="36" fill="url(#brass)"/>')
for k in range(4): A(f'<rect x="{-620+k*14}" y="-18" width="4" height="36" fill="#6e5214" fill-opacity=".5"/>')
A('<rect x="-688" y="-16" width="64" height="32" rx="10" fill="#c98a7e"/><rect x="-688" y="-16" width="64" height="10" rx="6" fill="#e0a89c" fill-opacity=".7"/>')
A('<text x="-420" y="7" font-size="17" font-family="DejaVu Sans Condensed, DejaVu Sans, sans-serif" font-weight="bold" fill="#e8c547" letter-spacing="2.5">MOLINE · ILL. · DRAFTING 2H</text>')
A(deer(-40,-1,0.42,'#e8c547'))
A('</g>')
# ---------- eraser crumbs
for i in range(26):
    x=random.uniform(560,1150);y=random.uniform(1300,1380)
    A(f'<ellipse cx="{x:.0f}" cy="{y:.0f}" rx="{random.uniform(2,5):.1f}" ry="{random.uniform(1.5,3):.1f}" fill="#c98a7e" opacity=".55" transform="rotate({random.uniform(0,180):.0f} {x:.0f} {y:.0f})"/>')
# ---------- light + vignette
A(f'<rect width="{W}" height="{H}" fill="url(#lamp)" style="mix-blend-mode:screen"/>')
A(f'<rect width="{W}" height="{H}" fill="#ffdcae" fill-opacity=".16" style="mix-blend-mode:multiply"/>')
A(f'<rect width="{W}" height="{H}" fill="url(#vig)"/>')
A(f'<rect width="{W}" height="{H}" fill="#000" filter="url(#grain)" opacity=".55"/>')
A('</svg>')
open('scene.svg','w').write('\n'.join(o))
