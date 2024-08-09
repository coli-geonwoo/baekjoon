

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringJoiner;
import java.util.StringTokenizer;

//1855. 암호
public class Main {
    static int n;
    static int k;
    static int q;
    static int m;
    static int[] sleep;
    static int[] student;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        n = Integer.parseInt(s[0]);
        k = Integer.parseInt(s[1]);
        q = Integer.parseInt(s[2]);
        m = Integer.parseInt(s[3]);

        student = new int[n + 3];
        sleep = new int[n + 3];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < k; i++) {
            sleep[Integer.parseInt(st.nextToken())] = 1;
        }

        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < q; i++) {
            int num = Integer.parseInt(st.nextToken());
            if (sleep[num] == 1) {
                continue;
            }

            for (int j = num; j < n + 3; j += num) {
                if (sleep[j] == 1) {
                    continue;
                }
                student[j] = 1;
            }
        }

//        for (int i = 0; i < n + 3; i++) {
//            System.out.print(student[i] + " ");
//        }
//        System.out.println();

        for (int i = 1; i < n + 3; i++) {
            student[i] += student[i - 1];
        }

//        for (int i = 0; i < n + 3; i++) {
//            System.out.print(student[i] + " ");
//        }
//        System.out.println();

        StringJoiner sj = new StringJoiner(System.lineSeparator());
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());

            sj.add(String.valueOf((end - start +1) - (student[end] - student[start - 1])));
        }
        System.out.println(sj);
    }


}

