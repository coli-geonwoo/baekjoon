
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String [] s = br.readLine().split(" ");
        PriorityQueue<Integer> pq =  new PriorityQueue<Integer>();

        for(String num : s){
            pq.add(Integer.parseInt(num));
        }

        List<List<Integer>> rooms = new ArrayList<>();
        rooms.add(new ArrayList<>());

        while(!pq.isEmpty()){
            int k = pq.poll();
            boolean flag = false;

            for(List<Integer> room : rooms){
                if(room.size() <=k){
                    flag=true;
                    room.add(k);
                    break;
                }
            }

            if(!flag){
                List<Integer> freshRoom = new ArrayList<>();
                freshRoom.add(k);

                rooms.add(freshRoom);

            }
        }

        System.out.println(rooms.size());
    }
}
