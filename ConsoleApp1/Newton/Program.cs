using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Newton
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.Write("Nhap bac cua phuong thuc: ");
            int n = Convert.ToInt32(Console.ReadLine());
            double[] x = new double[n + 1];
            double[] y = new double[n + 1];

            for (int i = 0; i <= n; i++)
            {
                Console.Write($"Nhap gia tri x{i}: ");
                x[i] = Convert.ToDouble(Console.ReadLine());
                Console.Write($"Nhap gia tri y{i}: ");
                y[i] = Convert.ToDouble(Console.ReadLine());
            }

            Console.Write("Nhap gia tri c: ");
            double c = Convert.ToDouble(Console.ReadLine());

            NewtonUp newton = new NewtonUp();
            double kq = newton.ActionNewtonUp(x, y, c, n);
            Console.WriteLine($"Ket qua: P = {kq}");
        }
    }
}
