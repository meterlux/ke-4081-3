BODY=("M24,29 C30,25 44,24 56,25 C64,25 70,24 74,22 C78,19 81,14 84,9 L86,6 L90,6 L98,10 L97,13 L90,14 "
 "C87,17 85,22 83,28 C82,31 80,33 77,34 L66,36 C56,37 46,37 38,35 C34,34 30,33 27,32 Z "
 "M25,29 L17,23 L20,30 Z "
 "M78,32 L90,34 L99,41 L97,43 L88,37 L76,36 Z "
 "M73,34 L83,39 L89,47 L87,48 L80,41 L70,37 Z "
 "M36,33 L22,40 L6,46 L5,44 L20,37 L30,31 Z "
 "M41,35 L28,44 L12,52 L11,50 L25,42 L35,34 Z")
ANT="M86,7 C84,0 80,-4 73,-6 M81,-2 L82,-9 M77,-4 L76,-10 M89,6 C90,0 93,-3 97,-5 M92,-1 L94,-7"
def deer(x,y,s,fill,rot=0,op=1):
    return (f'<g transform="translate({x},{y}) rotate({rot}) scale({s}) translate(-52,-22)" opacity="{op}">'
            f'<path d="{BODY}" fill="{fill}"/><path d="{ANT}" fill="none" stroke="{fill}" stroke-width="1.8" stroke-linecap="round"/></g>')
