using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CodeChef
{
    class Program
    {
        static void Main(string[] args)
        {
            int N = 0;
            N = int.Parse(Console.ReadLine());
            string input = null;
            input = Console.ReadLine();
            var temp1=input.Split(' ').Select(a=>Convert.ToInt32(a));
            List<int> temp=new List<int>();
            foreach (var item in temp1)
            {
                temp.Add(item);
            }
            List<int> result = new List<int>();
            for (int i=temp.Count-1;i>0; i--)
            {
                //if (temp.Find((int j) => { return j == i; }) > 0)
                if (!temp.Contains(i+1))
                {
                    //Console.WriteLine(i + 1);
                    result.Add(i + 1);
                }
            }
            result.Sort();
            foreach (var item in result)
            {
                Console.Write(item);
                Console.Write(" ");
            }
        }
    }
}
