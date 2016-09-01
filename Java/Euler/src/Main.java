abstract class Functor
{
    public abstract String run();
}

public class Main
{
    public static void main(String[] args)
    {
        System.out.println("Solving Euler Project Problems");

        int numProblems = 2;

        Functor [] problemArray = new Functor[numProblems];
        problemArray[0] = new EulerProb1(999);
        problemArray[1] = new EulerProb2(4000000);

        for (int i = 0; i < numProblems; ++i)
            System.out.println("Problem " + i + ": " + problemArray[i].run());
    }
}
