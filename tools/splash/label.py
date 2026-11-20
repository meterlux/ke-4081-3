"""Embossed label tape (J.J.L.), modelled on classic embossing-tool labels:
thin raised strokes whitened by the stretch, with the tape colour showing as a groove down the middle
of each stroke; fixed pitch; one flat glossy strip with square-cut ends; text centred."""
CAP=21; PITCH=21; SW=3.6
def glyph(c,x0,y0):
    h=SW/2; t=y0; b=y0+CAP
    if c=='J':          # stem on the right, short hook with a slightly squared drop
        s=x0+14.5; l=x0+4; r=3.2
        return f'M{s},{t} V{b-r} Q{s},{b} {s-r},{b} H{l+r} Q{l},{b} {l},{b-r} V{b-6}',None
    if c=='L':
        return f'M{x0+5},{t} V{b} H{x0+16}',None
    if c=='.':
        return None,(x0+PITCH/2,b-1.1)
def label(text='J.J.L.',W=230,H=48,tape='#6a1426'):
    n=len(text); tw=(n-1)*PITCH+16
    x0=(W-tw)/2-2; y0=(H-CAP)/2
    paths=[];dots=[]
    for i,c in enumerate(text):
        p,d=glyph(c,x0+i*PITCH,y0)
        if p: paths.append(p)
        if d: dots.append(d)
    P=' '.join(paths)
    def strokes(dx,dy,col,w,op):
        s=f'<path d="{P}" transform="translate({dx},{dy})" fill="none" stroke="{col}" stroke-width="{w}" stroke-opacity="{op}" stroke-linejoin="round" stroke-linecap="round"/>'
        s+=''.join(f'<circle cx="{x+dx}" cy="{y+dy}" r="{w/2+.4:.2f}" fill="{col}" fill-opacity="{op}"/>' for x,y in dots)
        return s
    return f'''<svg class="dymo" viewBox="-6 -6 {W+12} {H+14}" width="{W+12}" height="{H+14}" role="img" aria-label="{text}">
  <defs>
    <linearGradient id="dyTape" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#4f0d1b"/><stop offset=".06" stop-color="#7d1f33"/><stop offset=".16" stop-color="{tape}"/><stop offset=".9" stop-color="#5c1020"/><stop offset="1" stop-color="#3a0712"/>
    </linearGradient>
    <linearGradient id="dyGloss" x1="0" y1="0" x2="1" y2=".25">
      <stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".2" stop-color="#fff" stop-opacity=".1"/><stop offset=".3" stop-color="#fff" stop-opacity="0"/><stop offset="1" stop-color="#fff" stop-opacity="0"/>
    </linearGradient>
    <filter id="dySoft" x="-5%" y="-20%" width="110%" height="140%"><feGaussianBlur stdDeviation=".35"/></filter>
  </defs>
  <rect x="0" y="0" width="{W}" height="{H}" fill="url(#dyTape)"/>
  <rect x="0" y="0" width="{W}" height="{H}" fill="url(#dyGloss)"/>
  <path d="M0,1 H{W}" stroke="#c46176" stroke-opacity=".35" stroke-width="1"/>
  <g filter="url(#dySoft)">
    {strokes(.7,1.1,'#1c0207',SW+.6,.55)}
    {strokes(0,0,'#f4e7e9',SW,.97)}
    {strokes(.35,.45,tape,SW*.3,.85)}
    {strokes(-.45,-.5,'#ffffff',SW*.28,.55)}
  </g>
</svg>'''
if __name__=='__main__':
    open('label.svg.html','w').write(label())
