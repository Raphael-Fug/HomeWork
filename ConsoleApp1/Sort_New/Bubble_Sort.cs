using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sort_New
{
    internal class Bubble_Sort
    {
        static void Bubble(int[] A, int n)
        {
            for (int i = 0; i < n; i++)
            {
                int count = 0;
                for (int j = 0; j < n - i -1; j++)
                {
                    if (A[j] > A[j+1])
                    {
                        int temp = A[j];
                        A[j] = A[j + 1];
                        A[j + 1] = temp;
                        count++;
                    }
                    if (count == 0) break;
                }
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
            Bubble(A, n);
            Console.WriteLine("Array after sort:");
            foreach (int i in A)
            {
                Console.Write(i + " ");
            }
        }
    }
}
