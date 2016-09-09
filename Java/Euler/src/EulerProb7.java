import java.util.ArrayList;

class EulerProb7 extends Functor
{
    /**
     * By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
     * see that the 6th prime is 13. What is the 10,001-st prime number?
     */
    private int maxPrime;
    private int primeIndex;

    EulerProb7(int primeIndex, int maxPrime)
    {
        this.primeIndex = primeIndex;
        this.maxPrime   = maxPrime;
    }

    public String run()
    {
        ArrayList<Long> primes = Primes.sieve(this.maxPrime);
        return primes.get(this.primeIndex).toString();
    }
}
