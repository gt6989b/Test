import java.util.*;
import java.util.stream.IntStream;
import java.util.stream.LongStream;

class EulerProb4 extends Functor
{
    /**
     * A palindromic number reads the same both ways. The largest palindrome
     * made from the product of two 2-digit numbers is 9009 = 91 × 99. Find
     * the largest palindrome made from the product of two 3-digit numbers.
     */
    private long max;

    EulerProb4(long max) {this.max = max;}

    /**
     * Check string for being a palindrome.
     * - http://componentsprogramming.com/palindromes/
     * - http://stackoverflow.com/questions/4138827/check-string-for-palindrome
     *
     * @param str String to check for palindrome property
     * @return True iff it is a palindrome
     */
    static boolean isPalindrome(String str)
    {
        int n = str.length();
        for (int i = 0; i < n/2; ++i) {
            if (str.charAt(i) != str.charAt(n-i-1)) return false;
        }
        return true;
    }
    public String run()
    {
        int answer = -1, low = -1, high = -1;
        for (int i = 999; i > 99; --i)
        {
            for (int j = i - 1; j > 99; --j)
            {
                int product = i * j;
                if (isPalindrome(String.valueOf(product)) && product > answer) {
                    answer = product;
                    low = j;
                    high = i;
                }
            }
        }
        return (answer >= 0)
                ? String.valueOf(answer) + " = " + String.valueOf(low)
                                         + " * " + String.valueOf(high)
                : "No palindrome in 3-digit product exists";
    }
}
