class EulerProb2 extends Functor
{
    /**
     * Each new term in the Fibonacci sequence is generated by adding the
     * previous two terms. By starting with 1 and 2, the first 10 terms will be:
     * 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
     * By considering the terms in the Fibonacci sequence whose values do not
     * exceed four million, find the sum of the even-valued terms.
     */
    private int max;

    EulerProb2(int max) {this.max = max;}

    public String run()
    {
        int sum = 0;
        for (int next, prev = 1, current = 2; current <= this.max; )
        {
            sum     += current;

            next    = current + prev;
            prev    = current + next;
            current = prev    + next;
        }
        return String.valueOf(sum);
    }
}
