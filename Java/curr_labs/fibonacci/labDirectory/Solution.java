import java.util.*;


public class Solution {
    final static int MAX_INPUT = 2000;
    int[] lookup;

    Solution()
    {
        this.lookup = new int[MAX_INPUT+1];
        Arrays.fill(lookup, -1);
        lookup[0] = 0;
        lookup[1] = 1;
    }

  public static void main(String[] args) {
        Solution sol = new Solution(); 
        System.out.println(sol.lookup_fibonacci(Integer.parseInt(args[0])));
  }

  public int naive_fibonacci(int n)
  {
    if(n<0)
    {
        throw new ArithmeticException("Given n is negative");
    }
    if(n>MAX_INPUT)
    {
        throw new ArithmeticException("Given n is greater than MAX_INPUT");
    }
    if(n==0){return 0;}
    if(n==1) {return 1;}

    return naive_fibonacci(n-1) + naive_fibonacci(n-2);
    
  }

  public int lookup_fibonacci(int n)
  {
    if(n<0)
    {
        throw new ArithmeticException("Given n is negative");
    }
    if(n>MAX_INPUT)
    {
        throw new ArithmeticException("Given n is greater than MAX_INPUT");
    }
    if(this.lookup[n] == -1)
    {
        // store in lookup array and return it
        this.lookup[n] = lookup_fibonacci(n-1) + lookup_fibonacci(n-2);
        return this.lookup[n];
    }
    // return the corresponding value in lookup
    return this.lookup[n];
  }


}