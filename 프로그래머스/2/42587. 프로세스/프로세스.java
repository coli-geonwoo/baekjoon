import java.util.*;
import java.io.*;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        
        //복사하고 정렬
        int n = priorities.length;
        Deque<Num> nums = new ArrayDeque<>();
        
        for(int i=0; i<n; i++){
            Num a= new Num(priorities[i], i);
            System.out.println("a : " + a.num +" "+ a.location);               
            nums.add(a);
        }
        
        Arrays.sort(priorities);; //정렬        
        int idx =n-1; //중요도 순위
        int cnt =1;
        
        
        while(!nums.isEmpty()){
            Num k = nums.pollFirst();
            if(priorities[idx] == k.num){
                if(k.location ==location){
                    answer=cnt;
                    break;
                }
                idx--;
                cnt++;
                
            }else{
                nums.addLast(k);
            }
        }
        
        return answer;
        
    }

    static class Num{
        int num;
        int location;
        
        public Num(int num, int location){
            this.num =num;
            this.location=location;
        }
    }
               
               
}