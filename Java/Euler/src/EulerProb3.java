import java.util.*;
import java.util.stream.IntStream;
import java.util.stream.LongStream;

class EulerProb3 extends Functor
{
    /**
     * The prime factors of 13195 are 5, 7, 13 and 29.
     * What is the largest prime factor of the number 600851475143?
     */
    private long max;

    EulerProb3(long max) {this.max = max;}

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

    public String run()
    {
        ArrayList<Long> primes = sieve((int) Math.floor(Math.sqrt(this.max)));
        int primeIndex = primes.size() - 1;
        for (; primeIndex >= 0; --primeIndex)
            if (this.max % primes.get(primeIndex) == 0)
                break;

        Long answer= (primeIndex >= 0) ? primes.get(primeIndex) : this.max;
        return answer.toString();
    }
}
