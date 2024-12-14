
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Deque;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        //트리는 기본적으로 이분 그래프 > n번의 워프가 가능함
        // 만약 차수가 n-1인 노드가 존재 == 트리의 지름이 2 이하인 그래프의 존재 > n-1

        int n  = Integer.parseInt(br.readLine());

        int [] degree = new int[n+1];
        boolean flag = true;

        for (int i = 0; i < n-1; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            degree[a]++;
            degree[b]++;

            if(degree[a]==n-1 || degree[b]==n-1){
                flag=false;
            }
        }

        if(flag){
            bw.write(String.valueOf(n));
        }else{
            bw.write(String.valueOf(n-1));
        }

        bw.flush();
        bw.close();
    }
}
