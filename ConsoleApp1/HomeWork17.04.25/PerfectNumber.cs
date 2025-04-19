using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace HomeWork17._04._25
{
    internal class PerfectNumber
    {
        static void Main()
        {
            int a = Convert.ToInt32(Console.ReadLine());
            int[] Uoc = new int[a];
            int count = 0;
            int Value = 0;
            for (int i = 1; i < a; i++)
            {
                if (a % i == 0)
                {
                    Uoc[count] = i;
                    count++;
                }
            }
            foreach (int item in Uoc)
            {
                Value += item;
            }
            Console.WriteLine(Value == a ? "SHH" : "Không HH");
        }
    }
}
