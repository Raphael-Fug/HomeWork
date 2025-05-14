using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace InClass
{
    internal class ex1
    {
        static int GiaiThua(int x)
        {
            if (x == 1 || x == 0) return 1;
            return GiaiThua(x - 1) * x;
        }
        static int Fibonanci(int n)
        {
            if (n <= 2) return 1;
            return Fibonanci(n - 1) + Fibonanci(n - 2);
        }
        static void Main()
        {
            Console.Write("nhập n: ");
            int x = Convert.ToInt32(Console.ReadLine());
            //Console.WriteLine($"Đáp án là {GiaiThua(x)}");
            Console.WriteLine($"Fibonanci thứ n: {Fibonanci(x)}");

        }
    }
}
