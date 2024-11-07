import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.time.Duration;
import java.time.LocalTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;

public class Main {
    static int n;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long sum = 0;
        int n = Integer.parseInt(br.readLine());
        char [] chars = br.readLine().toCharArray();

        for(char c : chars){
            sum += c - '0';
        }
        System.out.println(sum);

    }

}
