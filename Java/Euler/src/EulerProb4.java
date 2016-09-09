import java.util.*;
import java.util.stream.IntStream;
import java.util.stream.LongStream;

class EulerProb4 extends Functor
{
    /**
     * The prime factors of 13195 are 5, 7, 13 and 29.
     * What is the largest prime factor of the number 600851475143?
     */
    private long max;

    EulerProb4(long max) {this.max = max;}

    public String run()
    {
        int answer = -1;
        return String.valueOf(answer);
    }
}
