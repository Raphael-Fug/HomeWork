using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HomeWork17._04._25
{
    internal class pt2
    {
        static void Main()
        {
            int a = Convert.ToInt32(Console.ReadLine());
            int b = Convert.ToInt32(Console.ReadLine());
            int c = Convert.ToInt32(Console.ReadLine());
            if (a == 0)
            {
                if (b == 0) Console.WriteLine(c == 0 ? "Vô số nghiệm" : "Vô nghiệm");
                else Console.WriteLine($"Có 1 nghiệm là {-c / (double)b}");
            }
            else
            {
                double Delta = Math.Pow(b, 2) - 4 * a * c;
                if (Delta < 0) Console.WriteLine("Vô nghiệm");
                else if (Delta == 0) Console.WriteLine($"Nghiệm là x = {-b/2.0*a}");
                else Console.WriteLine($"Phương trình có hai nghiệm phân biệt là {(-b - Math.Sqrt(Delta)) / (2.0 * a)} và {(-b + Math.Sqrt(Delta)) / (2.0 * a)}");
            }

        }
    }
}
