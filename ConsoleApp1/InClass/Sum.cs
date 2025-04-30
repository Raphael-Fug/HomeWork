using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace InClass
{
    internal class Sum
    {
        static int Tong(int n)
        {
            return (n * (1 + n) / 2);
        }
        //static int Tong(int n)
        //{
        //    for (int i = 1; i <= n; i ++)

        //}
        static void Main()
        {
            int n = Convert.ToInt32(Console.ReadLine());
            Console.WriteLine(Tong(n));
        }
    }
}
