using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Search
{
    internal class Binary
    {
        static int Search(int[] A, int K)
        {
            int left = 0;
            int right = A.Length;
            while (left <= right)
            {
                int mid = (left + right) / 2;
                if (A[mid] == K) return mid;
                else if (A[mid] > K) right = mid - 1;
                else left = mid + 1;
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
                Console.Write($"Nhập giá trị A{i + 1}: ");
                A[i] = Convert.ToInt32(Console.ReadLine());
            }
            Console.Write("Nhập giá trị K cần tìm: ");
            int k = Convert.ToInt32(Console.ReadLine());
            int Value = Search(A, k);
            Console.WriteLine($"Vị trí: {Value}");
        }
    }
}
