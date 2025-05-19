using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Sort_New
{
    internal class Heap_Sort
    {
        static void MaxHeapNode(int[] A, int n, int i)
        {
            int left = 2 * i + 1; // Chỉ số của nút trái
            int right = 2 * i + 2; // Chỉ số của nút phải
            int maxIndex = i; // Đặt maxIndex là chỉ số của nút hiện tại

            // Kiểm tra xem nút trái có lớn hơn nút hiện tại không
            if (left < n && A[left] > A[maxIndex])
            {
                maxIndex = left;
            }

            // Kiểm tra xem nút phải có lớn hơn nút hiện tại không
            if (right < n && A[right] > A[maxIndex])
            {
                maxIndex = right;
            }

            // Nếu nút lớn nhất không phải là nút hiện tại, hoán đổi và tiếp tục heapify
            if (maxIndex != i)
            {
                // Hoán đổi
                int temp = A[i];
                A[i] = A[maxIndex];
                A[maxIndex] = temp;

                // Gọi đệ quy để heapify nút bị ảnh hưởng
                MaxHeapNode(A, n, maxIndex);
            }
        }

        static void MaxHeap(int[] A, int n)
        {
            // Xây dựng heap tối đa từ giữa mảng trở về đầu
            for (int i = n / 2 - 1; i >= 0; i--)
            {
                MaxHeapNode(A, n, i);
            }
        }

        static void Sort(int[] A, int n)
        {
            if (n == 1)
                return;

            MaxHeap(A, n); // Xây dựng heap tối đa
            // Hoán đổi phần tử lớn nhất với phần tử cuối cùng
            int temp = A[0];
            A[0] = A[n - 1];
            A[n - 1] = temp;

            Sort(A, n - 1); // Gọi đệ quy với kích thước giảm
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
            Sort(A, n);
            Console.WriteLine("Array after sort:");
            foreach (int i in A)
            {
                Console.Write(i + " ");
            }
        }
    }
}
