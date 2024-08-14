

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int t;
    static int n;
    static int [] data;
    static int [] answer;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        t = Integer.parseInt(st.nextToken());

        for (int i = 0; i < t; i++) {
            st = new StringTokenizer(br.readLine());
            n = Integer.parseInt(st.nextToken());
            data = new int[n];
            answer = new int[n];

            st = new StringTokenizer(br.readLine());

            for (int j = 1; j < n+1; j++) {
                data[j-1]= Integer.parseInt(st.nextToken());
                answer[j-1]= j;
            }
            System.out.println(turn());
        }
    }

    static int turn() {
        int count = 0;

        while(!isAnswer()) {
            for (int i = 1; i < n; i++) {
                if (data[i - 1] > data[i]) {
                    int temp = data[i];
                    data[i] = data[i - 1];
                    data[i - 1] = temp;
                    count++;
                }
            }
        }

        return count;
    }

    static boolean isAnswer(){
        for (int i = 0; i < n; i++) {
            if(answer[i] != data[i]){
                return false;
            }
        }
        return true;
    }
}

