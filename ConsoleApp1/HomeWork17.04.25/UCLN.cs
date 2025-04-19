using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HomeWork17._04._25
{
    internal class UCLN
    {

        static void Main(string[] args)
        {
            int a = Convert.ToInt32(Console.ReadLine());
            int b = Convert.ToInt32(Console.ReadLine());
            if (a == 0 && b == 0) Console.WriteLine(a);
            else
            {
                while (a != b)
                {
                    if (a > b) a = a - b;
                    else b = b - a;
                }
                Console.WriteLine(a);   
            }
        }
    }
}
