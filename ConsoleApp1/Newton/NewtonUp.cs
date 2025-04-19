using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Newton
{
    //Lỗi chạy sai vãi cả L

    public class NewtonUp
    {
        public double ActionNewtonUp(double[] x, double[] y, double c, int n)
        {
            double[] delta = new double[n + 1];

            // Tính các delta ban đầu
            for (int i = 0; i <= n; i++)
            {
                delta[i] = y[i];
            }

            // Tính bảng sai phân
            for (int i = 1; i <= n; i++)
            {
                for (int j = n; j >= i; j--)
                {
                    delta[j] = delta[j] - delta[j - 1];
                }
            }

            // Tính t = (x - x0)
            double t = c - x[0];
            double result = y[0];
            double temp = 1;

            for (int i = 1; i <= n; i++)
            {
                temp *= (t - (i - 1));
                result += (delta[i] / GiaiThua(i)) * temp;
            }

            return result;
        }

        private int GiaiThua(int n)
        {
            if (n <= 1) return 1;
            return n * GiaiThua(n - 1);
        }


    }
}