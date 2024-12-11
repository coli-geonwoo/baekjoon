
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        //빵 a 패티 b 양상추 c 토마토 d
        // 조건1. 위와 아래에 있는 재료는 빵
        // 조건2. 인접한 재료는 같을 수 없다.
        // 조건3. 가진 재료로만 햄버거를 만들어야 한다.

        int n = Integer.parseInt(br.readLine());
        Map<Character, Integer> countMap = new HashMap<>();
        Map<Character, Integer> realCount = new HashMap<>();
        st = new StringTokenizer(br.readLine());
        countMap.put('a', Integer.parseInt(st.nextToken()));
        realCount.put('a', 0);
        countMap.put('b', Integer.parseInt(st.nextToken()));
        realCount.put('b', 0);
        countMap.put('c', Integer.parseInt(st.nextToken()));
        realCount.put('c', 0);
        countMap.put('d', Integer.parseInt(st.nextToken()));
        realCount.put('d', 0);

        char[] hamburger = br.readLine().toCharArray();

        boolean flag = true;

        //조건1.
        if(!(hamburger[0] == 'a' && hamburger[hamburger.length - 1] == 'a')){
            flag=false;
        }else {
            char before = ' ';
            for (int i = 0; i < hamburger.length; i++) {
                realCount.put(hamburger[i], realCount.get(hamburger[i])+1);
                //조건1
                if (before == hamburger[i] || realCount.get(hamburger[i]) > countMap.get(hamburger[i])) {
                    flag=false;
                    break;
                }
                before = hamburger[i];
            }
        }
        if(flag){
            bw.write("Yes\n");
        }else{
            bw.write("No\n");
        }

        bw.flush();
        bw.close();
    }
}
