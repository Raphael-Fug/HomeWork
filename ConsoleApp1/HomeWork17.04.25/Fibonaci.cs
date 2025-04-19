using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HomeWork17._04._25
{
    internal class Fibonaci
    {
        public static void Main()
        {
            int F0 = 0;
            int F1 = 1;
            int Fn = 0;
            int n = Convert.ToInt32(Console.ReadLine());
            if (n == 0) Console.WriteLine(F0);
            else if (n == 1) Console.WriteLine(F1);
            else
            {
                for (int i = 2; i <= n; i++)
                {
                    Fn = F0 + F1;
                    F0 = F1;
                    F1 = Fn;
                    //if (i == n) break;
                }
                Console.WriteLine(Fn);
            }
               
        }
    }
}
