using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Search
{
    internal class LinearSearch
    {
        static int Linear(int[] A, int k)
        {
            int n = A.Length;
            for (int i = 0; i < n; i++)
            {
                if (A[i] == k) return i;
            }
            return -1;
        }
        static void Main(string[] args)
        {
            Console.Write("Nhập số lượng mảng: ");
            int n = Convert.ToInt32(Console.ReadLine());
            int[] A = new int[n];
            for (int i = 0; i < 10; i++)
            {
                Console.Write($"Nhập giá trị A{i+1}: ");
                A[i] = Convert.ToInt32(Console.ReadLine());
            }
            Console.Write("Nhập giá trị K cần tìm: ");
            int k = Convert.ToInt32(Console.ReadLine());
            int Value = Linear(A, k);
            Console.WriteLine($"Vị trí: {Value}");

        }
    }
}
