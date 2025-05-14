using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace InClass
{
    internal class Sort
    {
        static void SortBuble(int[] A, int n)
        {
            int temp = 0;
            for (int i = 1;  i <= n; i++)
            {
                for (int j = 0; j > n- i - 1; j++)
                {
                    if(A[j]> A[j+1])
                    {
                        temp = A[j];
                        A[j] = A[j+1];
                        A[j+1] = temp;
                    }
                }
            }
        }
        static void Main(string[] args)
        {
            int[] A = { 1, 23, 43, 99, 22, 89, 33 };
            int n = A.Length;
            SortBuble(A, n);
            for(int i = 0; i < n; i++) Console.WriteLine(A[i]);
        }
    }
}
