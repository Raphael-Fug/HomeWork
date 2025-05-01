using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sort
{
    internal class SelectionSort
    {
        static void Selection(int[] A)
        {
            int n = A.Length;
            for (int i = 0;  i < n-1; i++)
            {
                int i_min = i;
                int v_min = A[i];
                for (int j = i; j < n; j++)
                {
                    if (A[j] < v_min)
                    {
                        v_min = A[j];
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
            Console.Write("Nhập số lượng mảng: ");
            int n = Convert.ToInt32(Console.ReadLine());
            int[] A = new int[n];
            for (int i = 0; i < n; i++)
            {
                Console.Write($"Nhập giá trị A{i + 1}: ");
                A[i] = Convert.ToInt32(Console.ReadLine());
            }
            Selection(A);
            for (int i = 0; i < n; i++)
            {
                Console.Write(A[i] + " ");
            }
        }
    }
}
