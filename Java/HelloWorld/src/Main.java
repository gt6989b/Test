abstract class Functor
{
    public abstract String run();
}

class LoopSum
{
    private int sum;

         LoopSum  (int initValue) {this.sum = initValue;}
    void increment(int number)    {this.sum += number;}
    int  getSum   ()              {return this.sum;}
}

class EulerProb1 extends Functor
{
    private int max;

    EulerProb1(int max)
    {
        this.max = max;
    }

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
        return result.asString();
    }
}

public class Main
{
    static void runEuler()
    {
        int numProblems = 2;

        Functor [] problemArray = new Functor[numProblems];
        problemArray[0] = new EulerProb1(999);
        problemArray[1] = new EulerProb2(4000000);

        for (int i = 0; i < numProblems; ++i)
            System.out.println("Problem " + i + ": " + problemArray[i].run());
    }

    public static void main(String[] args)
    {
        System.out.println("Hello, world!");

        LoopSum counter = new LoopSum(0);
        for (short i = 1; i < 11; ++i)
            counter.increment(i);

        System.out.println(counter.getSum());

        Main.runEuler();
    }
}

