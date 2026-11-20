# JJL

A touch simulator of the K&E 4081-3 Log Log Duplex Decitrig (20-scale version), built for iPhone.

- **Learn**: 15 guided lessons with "More" pop-ups, "Show me" demos and hands-on "Your turn" checks
- **Practice**: 14 problem types with hints and animated walkthroughs
- **Test**: 10 timed problems, scored for slide-rule accuracy, with best scores saved
- **Expert**: full-screen rule only

Gestures: drag either fixed strip sideways to move the whole rule under the cursor, drag the slide sideways to move the slide (even under the glass), swipe up or down to roll the rule over (the roll follows your finger), pinch to zoom, and tap a scale name to see what it does. Dragging is speed-sensitive: slow movement is geared down to about 1/3 for fine settings, normal speed is 1:1, and fast strokes are geared up (to 3.5×) so one stroke can cross the rule. In Expert mode, the lightbulb in the corner returns to Learn.

The rule's surface and slide ends come from photos of the actual rule (`textures.js`): perspective-corrected, with the printed ink and the cursor removed, then renewed to look like a new rule with only a faint patina. The scales are drawn on top mathematically, so every reading is exact.

Orientation follows how the phone is held. Sideways shows the full rule; upright shows the large, cropped close-up. With rotation lock on, the app reads the motion sensor (iPhone asks once for permission, on the first tap) and turns itself the right way round. Settings → Screen offers Automatic (default), Sideways or Upright.

It is two files (`index.html` and `textures.js`). On iPhone, open it in Safari, tap Share, then Add to Home Screen, and it runs full screen.

## Intro screen

Each launch opens on a title page over a late-night, jet-age drafting table (`splash-land.jpg` sideways, `splash-port.jpg` upright): a messy desk of blueprints with the slide rule and a worn spiral pocket notepad in focus, and a T-square, pilot's flight log with aviator sunglasses, swept-wing jet model, cockpit clock, lidded thermos, blueprint roll and architect's lamp falling away out of focus. The title is bold architect's hand lettering, the rest is vintage typewriter, and J.J.L. is on a burgundy embossed label. "Add to Home Screen" (shown only in the browser) plays a step-by-step guide for iPhone and Android.

The scene is generated from `tools/splash/scene.py` (SVG, using the objects in `objects.py`), rendered with `tools/splash/render.js` (Playwright), and finished by `tools/splash/compose.py`, which adds depth of field and film grain.
