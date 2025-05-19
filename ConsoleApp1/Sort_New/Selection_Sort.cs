
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sort_New
{
    internal class Selection_Sort
    {
        static void Selection(int[] A, int n)
        {
            for (int i = 0; i < n; i++)
            {
                int i_min = i;
                int V_min = A[i];
                for (int j = i; j < n; j++)
                {
                    if (A[j] < V_min)
                    {
                        V_min = A[j];
                        i_min = j;
                    }
                }
                int temp = A[i];
                A[i] = A[i_min];
                A[i_min] = temp;
            }
        }
        static void Main(string[] args)
        {
            Console.Write("Input n: ");
            int n = Convert.ToInt32(Console.ReadLine());
            int[] A = new int[n];
            Console.WriteLine("ADD item of array:");
            for (int i = 0; i < n; i++)
            {
                Console.Write($"Array[{i}]");
                A[i] = Convert.ToInt32(Console.ReadLine());
            }
            Selection(A, n);
            Console.WriteLine("Array after sort:");
            foreach (int i in A)
            {
                Console.Write(i + " ");
            }
        }
    }
}
