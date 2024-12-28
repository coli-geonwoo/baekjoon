import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int n = progresses.length;
        int [] remainDays = new int[n];
        
        for(int i=0; i<remainDays.length; i++){
            if((100-progresses[i])%speeds[i]==0){
                remainDays[i]= (100-progresses[i])/speeds[i];
                continue;
            }
            remainDays[i]= (100-progresses[i])/speeds[i] +1;
        }
        
        //System.out.println(Arrays.toString(remainDays));
        
        int max = remainDays[0];
        int cnt =0;
        List<Integer> answer = new ArrayList<>();
        
        for(int i=0; i<n; i++){
            if(remainDays[i]> max){
                max = remainDays[i];
                answer.add(cnt);
                cnt=1;
                continue;
            }
            cnt++;
        }
        
        answer.add(cnt);
        
        int [] result = new int[answer.size()];
        
        for(int i=0; i<answer.size(); i++){
            result[i] = answer.get(i);
        }
        
            
        return result;
    }
}