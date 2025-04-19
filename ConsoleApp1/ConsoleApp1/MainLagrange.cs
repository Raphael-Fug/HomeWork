using System;

namespace ConsoleApp1
{
    internal class MainLagrange
    {
        static void Main(string[] args)
        {
            Console.Write("Nhập số lượng giá trị: ");
            int Max = Convert.ToInt32(Console.ReadLine());
            double[] x = new double[Max];
            double[] y = new double[Max];
            for (int i = 0; i < Max; i++)
            {
                Console.Write($"Nhập giá trị x{i}: ");
                x[i] = Convert.ToDouble(Console.ReadLine());
                Console.Write($"Nhập giá trị y{i}: ");
                y[i] = Convert.ToDouble(Console.ReadLine());
            }
            Console.Write("Nhập giá trị c: ");
            double c = Convert.ToDouble(Console.ReadLine());
            LagrangeInterpolation interpolation = new LagrangeInterpolation();
            double kq = interpolation.Lagrange(x, y, Max, c);
            Console.WriteLine($"Kết quả là: {kq}");
        }
    }
}

