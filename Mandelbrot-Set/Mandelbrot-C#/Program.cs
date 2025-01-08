using SixLabors.ImageSharp;
using SixLabors.ImageSharp.PixelFormats;
using SixLabors.ImageSharp.Processing;

using System.Numerics;

const int resolution = 30000;
const int maxCoord = resolution - 1;

using Image<Rgba32> image = new(resolution, resolution);

static bool CheckComplexNumber(double a, double b)
{
  a -= 0.5;
  b -= 0.5;
  a = a / ((resolution - 1) / 4) - 2;
  b = b / ((resolution - 1) / 4) - 2;
  Complex z = new Complex(0, 0);
  Complex c = new Complex(a, b);
  for (int i = 0; i < 100; i++) {
    z = z * z + c;
    if (z.Magnitude > 2) return false;
  }
  return true;
}

float loops = 0;
for (int x = 0; x < resolution; x++) {
  for (int y = 0; y < resolution / 2; y++) {
    if (CheckComplexNumber(x, y)) {
      image[x, y] = Color.Black;
      image[x, maxCoord - y] = Color.Black;
    } else {
      image[x, y] = Color.White;
      image[x, maxCoord - y] = Color.White;
    }
  }
  loops++;
  Console.WriteLine(loops / resolution * 100);
}

image.SaveAsPng("test.png");
