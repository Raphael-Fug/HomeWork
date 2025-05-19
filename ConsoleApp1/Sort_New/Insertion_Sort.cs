using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sort_New
{
    internal class Insertion_Sort
    {
        static void Insertion(int[] A, int n)
        {
            for (int i = 1; i < n; i++)
            {
                int key = A[i];
                int j = i - 1;
                while (j >= 0 && A[j] < key)
                {
                    A[j+1] = A[j];
                    j--;
                }
                A[j + 1] = key;
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
            Insertion(A, n);
            Console.WriteLine("Array after sort:");
            foreach (int i in A)
            {
                Console.Write(i + " ");
            }
        }
    }
}
