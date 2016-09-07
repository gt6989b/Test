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
        int     numPrimes = 1 + (int) Math.floor(max/Math.log(max));
        long [] numbers = LongStream.iterate(2, n -> n+1).limit(max).toArray();

        ArrayList<Long> primes = new ArrayList<>(numPrimes);
        for (int i = 0; i < numbers.length/2; ++i)
        {
            if (numbers[i] > 0)
            {
                primes.add(numbers[i]);
                for (int j = 2 * i; j < numbers.length / 2; ++j)
                    numbers[j] = 0L;
            }
        }

        return primes;
    }

    public String run()
    {
        ArrayList<Long> primes = sieve((int) Math.floor(Math.sqrt(this.max)));
        int primeIndex = primes.size() - 1;
        for (; primeIndex >= 0; --i)
            if (this.max % primes.get(i) == 0)
                break;

        Long answer= (primeIndex >= 0) ? primes.get(primes.size()-1) : this.max;
        return answer.toString();
    }
}
