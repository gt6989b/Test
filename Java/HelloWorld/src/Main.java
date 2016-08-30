class LoopSum
{
    private int sum;

         LoopSum  (int initValue) {this.sum = initValue;}
    void increment(int number)    {this.sum += number;}
    int  getSum   ()              {return this.sum;}
}

public class Main
{
    public static void main(String[] args)
    {
        System.out.println("Hello, world!");

        LoopSum counter = new LoopSum(0);
        for (short i = 1; i < 11; ++i)
            counter.increment(i);

        System.out.println(counter.getSum());
    }
}

