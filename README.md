# JJL

A touch simulator of the K&E 4081-3 Log Log Duplex Decitrig (20-scale version), built for iPhone.

- **Learn**: 15 guided lessons with "More" pop-ups, "Show me" demos and hands-on "Your turn" checks
- **Practice**: 14 problem types with hints and animated walkthroughs
- **Test**: 10 timed problems, scored for slide-rule accuracy, with best scores saved
- **Expert**: full-screen rule only

Gestures: drag either fixed strip sideways to move the whole rule under the cursor, drag the slide sideways to move the slide (even under the glass), swipe up or down to roll the rule over (the roll follows your finger), pinch to zoom, and tap a scale name to see what it does. Dragging is speed-sensitive: slow movement is geared down to about 1/3 for fine settings, normal speed is 1:1, and fast strokes are geared up (to 3.5×) so one stroke can cross the rule. In Expert mode, the lightbulb in the corner returns to Learn.

The rule's surface and slide ends come from photos of the actual rule (`textures.js`): perspective-corrected, with the printed ink and the cursor removed, then renewed to look like a new rule with only a faint patina. The scales are drawn on top mathematically, so every reading is exact.

Orientation: by default the app always runs in landscape; if the phone is upright (or rotation-locked) the whole app turns sideways. The phone button (shown when the phone is upright) switches to the upright view instead: the rule fills the screen height at its natural proportions, heavily cropped at the sides, so the scales and hairline are large.

It is two files (`index.html` and `textures.js`). On iPhone, open it in Safari, tap Share, then Add to Home Screen, and it runs full screen.
