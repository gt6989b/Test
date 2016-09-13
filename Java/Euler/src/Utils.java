import java.util.ArrayList;
import java.util.stream.LongStream;

interface Functor
{
    String run();
}

class Primes
{
    static ArrayList<Long> sieve(int max)
    {
        int     numPrimes = 1 + (int) Math.floor(max/Math.log(max)),
                numIters  = max - 1;
        long [] numbers
                = LongStream.iterate(2, n -> n+1).limit(numIters).toArray();

        ArrayList<Long> primes = new ArrayList<>(numPrimes);
        int i;
        for (i = 0; i < numbers.length/2; ++i)
        {
            long prime = numbers[i];
            if (prime > 0)
            {
                primes.add(prime);
                for (int j = i + (int)prime; j < numbers.length; j += prime)
                    numbers[j] = 0L;
            }
        }
        for (; i < numbers.length; ++i)
        {
            if (numbers[i] > 0)
                primes.add(numbers[i]);
        }

        return primes;
    }
}

class Progressions
{
    static int arithmeticSum(int numTerms, int stepSize)
    {
        return stepSize * numTerms * (numTerms + 1) / 2;
    }
}