using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sort
{
    internal class BubleSort
    {
        static void Buble(int[] A)
        {
            for (int i = 0;  i < A.Length - 1; i++)
            {
                for (int j = 0; j < A.Length - 1; j++)
                {
                    if (A[j] > A[j + 1])
                    {
                        int temp = A[j];
                        A[j] = A[j + 1];
                        A[j + 1] = temp;
                    }
                }    
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
            Buble(A);
            for (int i = 0; i < n; i++)
            {
                Console.Write(A[i] + " ");
            }
        }
    }
}
