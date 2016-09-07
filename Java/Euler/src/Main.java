abstract class Functor
{
    public abstract String run();
}

public class Main
{
    public static void main(String[] args)
    {
        System.out.println("Solving Euler Project Problems");

        int numProblems = 3;

        Functor [] problemArray = new Functor[numProblems];
        problemArray[0] = new EulerProb1(999);
        problemArray[1] = new EulerProb2(4000000);
        problemArray[2] = new EulerProb3(600851475143L);

        for (int i = 0; i < numProblems; ++i)
            System.out.println("Problem " + i + ": " + problemArray[i].run());
    }
}
