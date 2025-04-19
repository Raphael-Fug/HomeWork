using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    public class LagrangeInterpolation
    {
        public double Lagrange(double[] x, double[] y, int Max, double c)
        {
            double P = 0.0;
            for (int i = 0; i < Max; i++)
            {
                double l = 1;
                for (int k = 0; k < Max; k++)
                {
                    if (k != i)
                    {
                        l *= (c - x[k]) / (x[i] - x[k]);
                    }
                }
                P += y[i] * l;
            }
            return P;
        }
    }
}
