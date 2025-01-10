using SixLabors.ImageSharp;
using SixLabors.ImageSharp.PixelFormats;
using SixLabors.ImageSharp.Processing;
using System.Numerics;

const int resolution = 1000;
const int maxCoord = resolution - 1;
const int iterations = 100;
/*(double X, double Y) point = (0, 0);*/
const double pointX = 0;
const double pointY = 0;
const double bounds = 2;
const double upperBoundX = pointX + bounds;
const double lowerBoundX = pointX - bounds;
const double upperBoundY = pointY + bounds;
const double lowerBoundY = pointY - bounds;

using Image<Rgba32> image = new(resolution, resolution);

static double ScaleRange(double x, int minInput, int maxInput, double minScale, double maxScale)
{
  int inputRange = maxInput - minInput;
  double scaleRange = maxScale - minScale;
  double scaledNum = (scaleRange*((x-minInput)/inputRange))-(scaleRange/2);
  return scaledNum;
}

static bool CheckComplexNumber(double a, double b)
{
  /*a -= 0.5;*/
  /*b -= 0.5;*/
  /*a = a / ((resolution - 1) / 4) - 2;*/
  /*b = b / ((resolution - 1) / 4) - 2;*/
  a = ScaleRange(a-0.5, 0, maxCoord, lowerBoundX, upperBoundX);
  b = ScaleRange(b-0.5, 0, maxCoord, lowerBoundY, upperBoundY);
  a += pointX;
  b += pointY;
  Complex z = new Complex(0, 0);
  Complex c = new Complex(a, b);
  for (int i = 0; i < iterations; i++) {
    z = z * z + c;
    if (z.Magnitude > 2) return false;
  }
  return true;
}

double loops = 0;
for (int x = 0; x < resolution; x++) {
  for (int y = 0; y < resolution; y++) {
    if (CheckComplexNumber(x, y)) {
      image[x, y] = Color.Black;
      /*image[x, maxCoord - y] = Color.Black;*/
    } else {
      image[x, y] = Color.White;
      /*image[x, maxCoord - y] = Color.White;*/
    }
  }
  loops++;
  Console.WriteLine(loops / resolution * 100);
}

image.SaveAsPng("test.png");
