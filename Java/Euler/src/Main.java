public class Main
{
    public static void main(String[] args)
    {
        System.out.println("Solving Euler Project Problems");

        String result;
        int numProblems = 7;

        Functor [] problemArray = new Functor[numProblems];
        problemArray[0] = new EulerProb1(999);
        problemArray[1] = new EulerProb2(4000000);
        problemArray[2] = new EulerProb3(600851475143L);
        problemArray[3] = new EulerProb4(-1);
        problemArray[6] = new EulerProb7(10000, 120000);

        for (int i = 0; i < numProblems; ++i)
        {
            result = problemArray[i] == null
                    ? "Not run"
                    : problemArray[i].run();
            System.out.println("Problem " + (i+1) + ": " + result);
        }
    }
}
