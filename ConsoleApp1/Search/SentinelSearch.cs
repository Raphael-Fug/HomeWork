using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Search
{
    internal class SentinelSearch
    {
        static int Sentinel(int[] A, int k)
        {
            int n = A.Length;
            A[n + 1] = k;
            int i = 1;
            while (A[i] != n) i ++;
            return (i < n) ? i : -1;
        }
        static void Main(string[] args)
        {
            Console.Write("Nhập số lượng mảng: ");
            int n = Convert.ToInt32(Console.ReadLine());
            int[] A = new int[n];
            for (int i = 0; i < 10; i++)
            {
                Console.Write($"Nhập giá trị A{i + 1}: ");
                A[i] = Convert.ToInt32(Console.ReadLine());
            }
            Console.Write("Nhập giá trị K cần tìm: ");
            int k = Convert.ToInt32(Console.ReadLine());
            int Value = Sentinel(A, k);
            Console.WriteLine($"Vị trí: {Value}");
        }
    }
}
