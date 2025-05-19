using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sort_New
{
    internal class Merge_Sort
    {
        static void Sort(int[] A, int n, int p, int r)
        {
            if (p < r)
            {
                int q = (p + r) / 2;
                Sort(A, n, p, q);
                Sort(A, n, q + 1, r);
                Merge(A, n, p, q, r);
            }
        }
        static void Merge(int[] A, int n, int p, int q, int r)
        {
            int[] B = new int[r-p+1];
            int k = 0;
            int i = p;
            int j = q+1;
            while (i <= q && j <= r)
            {
                if (A[i] < A[j])
                {
                    B[k] = A[i];
                    i ++;
                    k ++;
                }
                else
                {
                    B[k] = A[j];
                    j ++;
                    k ++;
                }
            }
            while (i <= q)
            {
                B[k] = A[i];
                i++;
                k++;
            }
            while (j <= r)
            {
                B[k] = A[j];
                j++;
                k++;
            }
            for(int z = 0; z < B.Length; z++)
            {
                A[p+z] = B[z];
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
            //Merge(A, n);
            Sort(A, n, 0, n-1);
            Console.WriteLine("Array after sort:");
            foreach (int i in A)
            {
                Console.Write(i + " ");
            }
        }
    }
}
