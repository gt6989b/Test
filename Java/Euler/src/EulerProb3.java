import java.util.ArrayList;

class EulerProb3 extends Functor
{
    /**
     * The prime factors of 13195 are 5, 7, 13 and 29.
     * What is the largest prime factor of the number 600851475143?
     */
    private long max;

    EulerProb3(long max) {this.max = max;}

    public String run()
    {
        ArrayList<Long> primes
                = Primes.sieve((int) Math.floor(Math.sqrt(this.max)));
        int primeIndex = primes.size() - 1;
        for (; primeIndex >= 0; --primeIndex)
            if (this.max % primes.get(primeIndex) == 0)
                break;

        Long answer= (primeIndex >= 0) ? primes.get(primeIndex) : this.max;
        return answer.toString();
    }
}
