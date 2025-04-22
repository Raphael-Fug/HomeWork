using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Search
{
    internal class JumbSearch
    {
        static int Search(int[] A, int k)
        {
            int n = A.Length;
            int step = (int)Math.Sqrt(Math.Floor(Math.Sqrt(n)));
            int i = 0;
            int jumb = i + step;
            while (i <= n && A[jumb] < k)
            {
                jumb += step;
                i += step;
            }
            if (jumb > n) jumb = n - 1;
            while (A[i] < k)
            {
                i ++;
                if (i >= n || i > jumb) return -1; 
            }
            if (A[i] == k) return i;
            else return -1;
        }
    }
}
