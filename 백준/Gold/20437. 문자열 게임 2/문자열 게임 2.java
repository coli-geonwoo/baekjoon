import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());

        for (int i = 0; i < t; i++) {
            Map<Character, List<Integer>> numbers = new HashMap<Character, List<Integer>>();

            char[] input = br.readLine().toCharArray();
            int k = Integer.parseInt(br.readLine());

            int short_length = Integer.MAX_VALUE;
            int long_length = -1;
            boolean flag = true;

            for (int j = 0; j < input.length; j++) {
                char c = input[j];
                if (!numbers.containsKey(c)) {
                    numbers.put(c, new ArrayList<>());
                    numbers.get(c).add(j + 1);
                } else {
                    numbers.get(c).add(j + 1);
                }

                List<Integer> indexs = numbers.get(c);

                if (indexs.size() >= k) {
                    flag = false;
                    long_length = Math.max(long_length, j + 1 - indexs.get(indexs.size()-k)+1);
                    short_length = Math.min(short_length, j + 1 - indexs.get(indexs.size()-k)+1);
                }
            }

            if (!flag) {
                System.out.println(short_length + " " + long_length);
            } else {
                System.out.println(-1);
            }
        }
    }
}
