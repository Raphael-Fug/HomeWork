using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HomeWork17._04._25
{
    internal class Prime
    {
        static void Main(string[] args)
        {
            int a = Convert.ToInt32(Console.ReadLine());
            if (a <= 1) Console.WriteLine("Ko là snt");
            else
            {
                bool IsPrime = true;
                for (int i = 2; i <= Math.Sqrt(a); i++)
                {
                    if (a % i == 0) IsPrime = false;
                }
                Console.WriteLine(IsPrime ? "SNT" : "Không SNT");
            }

        }
    }
}
