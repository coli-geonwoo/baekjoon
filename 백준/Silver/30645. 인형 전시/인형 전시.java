
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Deque;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {
    static int n;
    static int k;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        n = Integer.parseInt(s[0]);
        k = Integer.parseInt(s[1]);

        int dollCount = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        List<Integer> dolls = new ArrayList<>();
        for (int i = 0; i < dollCount; i++) {
            dolls.add(Integer.parseInt(st.nextToken()));
        }
        Collections.sort(dolls);

        Map<Integer, Integer> map = new HashMap<>();
        int result=0;

        for(int num : dolls){
            if(map.containsKey(num) && map.get(num)>=k){
            }else if(map.containsKey(num)){
                map.put(num, map.get(num)+1);
                result+=1;
            }else{
                map.put(num, 1);
                result+=1;
            }
        }
        System.out.println(Math.min(result, n*k));
    }

}