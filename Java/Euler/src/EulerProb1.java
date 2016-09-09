class EulerProb1 extends Functor
{
    /**
     * If we list all the natural numbers below 10 that are multiples of 3 or
     * 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
     * Find the sum of all the multiples of 3 or 5 below 1000.
     */
    private int max;

    EulerProb1(int max) {this.max = max;}

    public String run()
    {
        int [] sign  = {1, 1, -1};
        int [] scale = {3, 5, 15};
        int result = 0;
        for (int i = 0; i < sign.length; ++i)
            result += sign[i] * Progressions.arithmeticSum(this.max/scale[i],
                                                           scale[i]);
        return String.valueOf(result);
    }
}
