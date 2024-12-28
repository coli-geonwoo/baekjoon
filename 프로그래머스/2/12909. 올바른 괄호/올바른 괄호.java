import java.util.*;

class Solution {
    boolean solution(String s) {
        boolean answer = true;
        char[] arr = s.toCharArray();
        List<Character> carr = new ArrayList<>();
        
        for(int i=0; i<arr.length; i++){
            if(arr[i] == '('){
                carr.add(arr[i]);
            }else{
                if(carr.isEmpty() || carr.get(carr.size()-1)== ')'){
                    answer=false;
                    break;
                }
                carr.remove(carr.size()-1);
            }
        }
        
        if(!carr.isEmpty()){
            answer=false;
        }
    

        return answer;
    }
}