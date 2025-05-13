using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BruteForce
{
    internal class ex2
    {
        static int Max(int[] A)
        {
            int max = int.MaxValue;
            foreach (int i in A)
            {
                if (A[i] > max) max = A[i]; 
            }
            return max;
        }
        public static int Min(int[] A)
        {
            int min = int.MinValue;
            foreach (int i in A)
            {
                if (A[i] < min) min = A[i];
            }
            return min;
        }
        static void Main(string[] args)
        {
            Console.Write("Nhập số lượng mảng: ");
            int n = Convert.ToInt32(Console.ReadLine());
            int[] nums = new int[n];
            for (int i = 0; i < n; i++)
            {
                Console.Write($"Phần tử thứ {i}: ");
                nums[i] = Convert.ToInt32(Console.ReadLine());
            }

        }
    }
}
