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
        long sum = this.max;
        return String.valueOf(sum);
    }
}
