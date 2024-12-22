import java.util.*;

class Solution {
    public int solution(int[] citations) {
        // n편중 h번이상 인용된 논문이 h편 이상이고, 
        // h의 최대값
        
        Arrays.sort(citations);
        int left = 0;
        int right = 1000;
        int answer =0;
        
        while(left<=right){
            int mid = (left+right)/2;
            
            if(sequence(citations, mid)){
                answer = mid;
                left= mid+1;
            }else{
                right = mid-1;
            }
        
        }
        
        return answer;
    }
    
    static boolean sequence(int [] citations, int hIndex){
        int left = 0;
        int right = citations.length-1;
        int result =0;
        
        while(left<=right){
            int mid = (left+right)/2;
            if(citations[mid]>=hIndex){
                right = mid-1;
        
            }else{
                result=mid;
                left = mid+1;
            }
        }
        System.out.println(hIndex + " " + result);
        
        if(citations[result]>=hIndex){
            return citations.length>=hIndex;
        }
        
        return (citations.length-1-result)>=hIndex;
    }
}