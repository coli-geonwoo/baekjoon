import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Deque;
import java.util.List;
import java.util.StringTokenizer;

//30701. 돌아온 똥게임 실3
public class Main {
    static long roomCnt;
    static long health;
    static Deque<Integer> weapons;
    static List<Integer> monsters = new ArrayList<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");

        roomCnt = Integer.parseInt(s[0]);
        health = Integer.parseInt(s[1]);
        List<Integer> temp = new ArrayList<>();

        for (int i = 0; i < roomCnt; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            if (Integer.parseInt(st.nextToken()) == 1) {
                monsters.add(Integer.parseInt(st.nextToken()));
            } else {
                temp.add(Integer.parseInt(st.nextToken()));
            }
        }

        Collections.sort(monsters);
        Collections.sort(temp);

        weapons = new ArrayDeque<>(temp);

        long result = 0;

        for (long monster : monsters) {
            if (monster < health) {
                result++;
                health += monster;
            } else {
                while (!weapons.isEmpty() && health <= monster) {
                    int product = weapons.pollFirst();
                    health *= product;
                    result++;
                }

                if(health > monster){
                    result++;
                }else{
                    break;
                }
            }
        }
        System.out.println(result + weapons.size());
    }
}

