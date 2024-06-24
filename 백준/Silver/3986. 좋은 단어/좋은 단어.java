import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int result = 0;

        for (int i = 0; i < n; i++) {
            String[] split = br.readLine().split("");
            List<String> nums = new ArrayList<>();
            boolean flag = true;

            for (String s : split) {
                if (nums.isEmpty()) {
                    nums.add(s);
                } else {
                    if (s.equals(nums.get(nums.size() - 1))) {
                        nums.remove(nums.size() - 1);
                    } else {
                        nums.add(s);
                    }
                }
            }

            if (nums.isEmpty()) {
                result++;
            }
        }
        System.out.println(result);
    }
}
