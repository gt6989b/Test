class EulerProb2 extends Functor
{
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
