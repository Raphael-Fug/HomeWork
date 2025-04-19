using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HomeWork17._04._25
{
    internal class Hpt2
    {
        static void Main()
        {
            double[] a = new double[2]; 
            double[] b = new double[2]; 
            double[] c = new double[2]; 
            for (int i = 0; i < 2; i++)
            {
                Console.WriteLine($"Nhập hệ số cho phương trình {i + 1} (ax + by = c):");
                Console.Write($"Nhập a{i + 1}: ");
                a[i] = Convert.ToDouble(Console.ReadLine());
                Console.Write($"Nhập b{i + 1}: ");
                b[i] = Convert.ToDouble(Console.ReadLine());
                Console.Write($"Nhập c{i + 1}: ");
                c[i] = Convert.ToDouble(Console.ReadLine());
            }
            double D = a[0] * b[1] - a[1] * b[0]; 
            double Dx = c[0] * b[1] - c[1] * b[0]; 
            double Dy = a[0] * c[1] - a[1] * c[0]; 

            if (D == 0)
            {
                Console.WriteLine(Dx == 0 && Dy == 0 ? "Vô số nghiệm" : "Vô nghiệm");
            }
            else
            {
                double x = Dx / D; 
                double y = Dy / D;
                Console.WriteLine($"Nghiệm của hệ phương trình là: x = {x}, y = {y}");
            }
        }
    }
}
