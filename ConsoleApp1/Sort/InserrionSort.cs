using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sort
{
    internal class InserrionSort
    {
        static void Insertion(int[] A)
        {
            for (int i = 1; i < A.Length; i++)
            {
                int j = i;
                while (j > 0 && A[j] <= A[j - 1])
                {
                    int temp = A[j];
                    A[j] = A[j - 1];
                    A[j - 1] = temp;
                    j--;
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
            Insertion(A);
            for (int i = 0; i < n; i++)
            {
                Console.Write(A[i] + " ");
            }
        }
    }
}
