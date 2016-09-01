class EulerProb1 extends Functor
{
    private int max;

    EulerProb1(int max) {this.max = max;}

    private int arithmeticSum(int numTerms, int stepSize)
    {
        return stepSize * numTerms * (numTerms + 1) / 2;
    }

    public String run()
    {
        int [] sign  = {1, 1, -1};
        int [] scale = {3, 5, 15};
        int result = 0;
        for (int i = 0; i < sign.length; ++i)
            result += sign[i] * this.arithmeticSum(this.max/scale[i], scale[i]);
        return String.valueOf(result);
    }
}
