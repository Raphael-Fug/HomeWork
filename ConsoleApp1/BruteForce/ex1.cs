using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BruteForce
{
    internal class ex1
    {
        static void Sum(int[] nums, int x)
        {
            for (int i = 0; i < nums.Length; i++)
            {
                for (int j = 0; j < nums.Length; j++)
                {
                    if (x == nums[j] + nums[i]) Console.WriteLine($"[{i}, {j}]"); 
                }
            }
        }
        static void Main(string[] args)
        {
            Console.Write("Nhập số lượng mảng: ");
            int n = Convert.ToInt32(Console.ReadLine());
            int[] nums = new int[n];
            for (int i = 0;i < n; i++)
            {
                Console.Write($"Phần tử thứ {i}: ");
                nums[i] = Convert.ToInt32(Console.ReadLine());
            }
            Console.Write("Phần tử cần tìm: ");
            int x = Convert.ToInt32(Console.ReadLine());
            Sum(nums, x);
        }
    }
}
