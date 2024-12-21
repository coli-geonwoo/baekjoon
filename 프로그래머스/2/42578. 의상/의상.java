import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        Map<String, Integer> countMap = new HashMap<>();
        for(String [] cloth : clothes){
            String op = cloth[1];
            countMap.putIfAbsent(op, 0);
            countMap.put(op, countMap.get(op)+1);
        }
        
        int result=1;
        Set<String> keys = countMap.keySet();
        if(keys.isEmpty()){
            result=0;
        }else{
            for(String key: keys){
                int c = countMap.get(key);
                result *= (c+1);
            }
            result-=1;
        }
        
        return result;
    }
}