import java.util.*;

//정렬이 곧 연관도 순이라는 사실
class Solution {
    public boolean solution(String[] phone_book) {
        boolean answer = true;
        Arrays.sort(phone_book);
        
        for(int i=0; i<phone_book.length-1; i++){
            String num1 = phone_book[i];
            String num2 = phone_book[i+1];
            
            if(num2.startsWith(num1)){
                answer=false;
                break;
            }
        }
        
      
        return answer;
    }
}