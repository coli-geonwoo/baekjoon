
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int l = Integer.parseInt(st.nextToken())-1;
        int r = Integer.parseInt(st.nextToken())-1;

        boolean flag = true;

        List<Integer> nums = new LinkedList<>();
        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            nums.add(Integer.parseInt(st.nextToken()));
        }

        List<Integer> left = nums.subList(0, l);
        List<Integer> middle = nums.subList(l, r + 1);
        List<Integer> right = nums.subList(r + 1, nums.size());

        int leftMax, middleMax, middleMin, rightMin = 0;

        if (!left.isEmpty()) {
            leftMax = Collections.max(left);
        } else {
            leftMax = 0;
        }

        if (!middle.isEmpty()) {
            middleMax = Collections.max(middle);
            middleMin = Collections.min(middle);
        } else {
            middleMax = middleMin = leftMax;
        }

        if (!right.isEmpty()) {
            rightMin = Collections.min(right);
        } else {
            rightMin = middleMax;
        }

        if (!(leftMax <= middleMin && middleMax <= rightMin)) {
            flag = false;
        }

        if (flag) {
            bw.write("1");
        } else {
            bw.write("0");
        }
        bw.flush();
        bw.close();


    }
}
