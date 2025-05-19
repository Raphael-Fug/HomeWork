using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sort_New
{
    internal class Quick_Sort
    {
        static int Partition(int[] A, int left, int right)
        {
            int pivot = A[right]; // Chọn phần tử cuối làm pivot
            int i = left - 1; // Vị trí cho phần tử nhỏ hơn pivot

            for (int j = left; j < right; j++)
            {
                // So sánh phần tử hiện tại với pivot
                if (A[j] <= pivot)
                {
                    i++;
                    // Hoán đổi A[i] và A[j]
                    int temp = A[i];
                    A[i] = A[j];
                    A[j] = temp;
                }
            }

            // Hoán đổi A[i + 1] và A[right] (pivot)
            int tempPivot = A[i + 1];
            A[i + 1] = A[right];
            A[right] = tempPivot;

            return i + 1; // Trả về chỉ số của pivot
        }

        static void Sort(int[] A, int left, int right)
        {
            if (left < right)
            {
                int pivotIndex = Partition(A, left, right); // Lấy chỉ số của pivot
                Sort(A, left, pivotIndex - 1); // Sắp xếp nửa bên trái
                Sort(A, pivotIndex + 1, right); // Sắp xếp nửa bên phải
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
            Sort(A, 0, n-1);
            Console.WriteLine("Array after sort:");
            foreach (int i in A)
            {
                Console.Write(i + " ");
            }
        }
    }
}
