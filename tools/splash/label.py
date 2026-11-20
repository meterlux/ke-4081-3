# Embossed label tape, drawn: one continuous strip, square-cut ends, fixed-pitch glyphs centred on it.
PITCH=24; CAP=24; SW=4.8
def glyph(c,x0,y0):
    h=SW/2; t=y0+h; b=y0+CAP-h
    if c=='J':  # stem on the right, short squared hook
        s=x0+16; l=x0+5.5; r=2.2
        return f'<path d="M{s},{t} V{b-r} Q{s},{b} {s-r},{b} H{l+r} Q{l},{b} {l},{b-r} V{b-5.6}" fill="none"/>'
    if c=='L':
        s=x0+6.5
        return f'<path d="M{s},{t} V{b} H{x0+17.5}" fill="none"/>'
    if c=='.':
        return f'<rect x="{x0+PITCH/2-3.1}" y="{y0+CAP-6.2}" width="6.2" height="6.2" rx="1.2" stroke="none"/>'
    raise ValueError(c)
def label(text='J.J.L.',W=236,H=50):
    n=len(text); tw=n*PITCH
    x0=(W-tw)/2+1.2; y0=(H-CAP)/2+.4          # optical centring: the periods sit low, nudge right a hair
    gl=''.join(glyph(c,x0+i*PITCH,y0) for i,c in enumerate(text))
    return f'''<svg class="dymo" viewBox="-6 -6 {W+12} {H+14}" width="{W+12}" height="{H+14}" role="img" aria-label="{text}">
  <defs>
    <linearGradient id="dyTape" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#5a1020"/><stop offset=".07" stop-color="#8b2639"/><stop offset=".2" stop-color="#6d1628"/><stop offset=".85" stop-color="#560d1d"/><stop offset="1" stop-color="#3a0712"/>
    </linearGradient>
    <linearGradient id="dyGloss" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".22" stop-color="#fff" stop-opacity=".13"/><stop offset=".36" stop-color="#fff" stop-opacity="0"/><stop offset=".74" stop-color="#fff" stop-opacity=".05"/><stop offset="1" stop-color="#fff" stop-opacity="0"/>
    </linearGradient>
    <filter id="dyTex" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency=".6" numOctaves="2" seed="4"/>
      <feColorMatrix values="0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 .05 0"/><feComposite in2="SourceGraphic" operator="in"/></filter>
    <filter id="dyEmboss" x="-20%" y="-30%" width="140%" height="160%">
      <feGaussianBlur in="SourceAlpha" stdDeviation="1.15" result="b"/>
      <feSpecularLighting in="b" surfaceScale="2" specularConstant=".5" specularExponent="14" lighting-color="#fff" result="s"><feDistantLight azimuth="235" elevation="40"/></feSpecularLighting>
      <feComposite in="s" in2="SourceAlpha" operator="in" result="s2"/>
      <feDiffuseLighting in="b" surfaceScale="1.6" diffuseConstant="1.15" lighting-color="#fff" result="d"><feDistantLight azimuth="235" elevation="50"/></feDiffuseLighting>
      <feComposite in="d" in2="SourceAlpha" operator="in" result="d2"/>
      <feBlend in="SourceGraphic" in2="d2" mode="multiply" result="m"/>
      <feComposite in="s2" in2="m" operator="arithmetic" k2=".35" k3="1" result="lit"/>
      <feOffset in="SourceAlpha" dx=".7" dy="1.5" result="o"/><feGaussianBlur in="o" stdDeviation=".7" result="ob"/>
      <feFlood flood-color="#22030a" flood-opacity=".55"/><feComposite in2="ob" operator="in" result="sh"/>
      <feMerge><feMergeNode in="sh"/><feMergeNode in="lit"/></feMerge>
    </filter>
  </defs>
  <rect x="0" y="0" width="{W}" height="{H}" rx="1.6" fill="url(#dyTape)"/>
  <rect x="0" y="0" width="{W}" height="{H}" rx="1.6" fill="#000" filter="url(#dyTex)"/>
  <rect x="0" y="0" width="{W}" height="{H}" rx="1.6" fill="url(#dyGloss)"/>
  <path d="M1,1.6 H{W-1}" stroke="#c46176" stroke-opacity=".4" stroke-width="1.1"/>
  <path d="M1,{H-.8} H{W-1}" stroke="#1d0309" stroke-opacity=".7" stroke-width="1.5"/>
  <g filter="url(#dyEmboss)" fill="#ecc9d0" stroke="#ecc9d0" fill-opacity=".94" stroke-opacity=".94" stroke-width="{SW}" stroke-linejoin="round" stroke-linecap="butt">{gl}</g>
</svg>'''
if __name__=='__main__':
    open('label.svg.html','w').write(label())
