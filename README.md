# Some of my (very) small coding projects

---

## Mandelbrot Set

![Generated Mandelbrot Set](https://github.com/Zynthoil/Code/blob/master/Mandelbrot-Set/Mandelbrot-Set-C)

Generates a Mandelbrot Set in either ascii, pixels or coloured pixels. Uses recursive function.

The ascii geneation is slightly warped (characters are taller than they are wide).

Quite inefficient, but works and isn't too complex (unlike the numbers used! (see what I did there?)).

---

## Sierpinski Carpet

![Generated Sierpinski Carpet](https://github.com/Zynthoil/Code/blob/master/Sierpinski-Carpet/Sierpinski-Carpet-high-res.png)

Generates a Sierpinski Carpet with the chaos game. Essentially:
- Pick a random starting point (don't place this one though).
- Pick a random corner or edge midpoint.
- Place a point 2/3 of the distance from the point to the chosen corner/edge.
- Repeat with the new point.

I could of course generate this much faster normally, but I though the chaos game approach was interesting.

---

## Sierpinski Triangle

I made this after making the Sierpinski Carpet, which was a good start due to its rectangular nature.

Generates a Sierpinski Triangle with the chaos game. Essentially:
- Choose initial starting point as the center of the screen (I didn't want to try generated a random point within the bounds of the triangle).
- Pick a random corner.
- Place a point 1/2 of the distance from the point to the chosen corner.
- Repeat with the new point.

I also made some changes with this one to make a GIF of the generation. Currently only works at small scales, as the GIF is made by storing all iterations images in a list, which is demanding on the RAM.
