using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace InClass
{
    internal class Bac
    {
        static string Bac1(int a, int b)
        {
            if (a == 0) return (b == 0) ? "Vô số nghiệm" : "Vô nghiệm";
            else return $"Có 1 nghiệm là: {-b/a}";
        }
        static void Main(string[] args)
        {
            int a = Convert.ToInt32(Console.ReadLine());
            int b = Convert.ToInt32(Console.ReadLine());
            Bac1(a, b);
        }
    }
}
