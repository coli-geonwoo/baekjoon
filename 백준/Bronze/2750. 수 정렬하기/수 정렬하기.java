
import static java.util.Comparator.comparing;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        long n = Long.parseLong(br.readLine());
        List<Long> numbers = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            numbers.add(Long.parseLong(br.readLine()));
        }

        numbers.sort(comparing(Long::longValue));
        for (int i = 0; i < n; i++) {
            bw.write(numbers.get(i) + System.lineSeparator());
        }

        bw.flush();
    }
}

