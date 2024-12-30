import java.util.*;

class Solution {
    
    static Map<Integer, Deque<Integer>> map;
    static int [] visited = new int [1000001];
    static int [] start;
    static int [] end;
    
    public int[] solution(int[][] edges) {
        int[] answer = new int [4];
        start = new int [1000001]; // i에서 출발한 정점의 개수
        end = new int [1000001]; //j에서 출발한 정점의 개수
        map = new HashMap<>();
        
        int maxNode =0;
        
        for(int i=0; i<edges.length; i++){
            int[] arr = edges[i];
            int s = arr[0];
            int e = arr[1];
            start[s]++;
            end[e]++;
            map.putIfAbsent(s, new ArrayDeque<>());
            map.get(s).add(e);
            
            maxNode = Math.max(maxNode, s);
            maxNode = Math.max(maxNode, e);
        }
        
        int startNode =-1;
        
        for(int i=1; i<maxNode+1; i++){
            if(start[i]>=2 && end[i]==0){
                startNode=i;
                break;
            }
        }
        
        visited[startNode]=1;
        Deque<Integer> nodes = map.get(startNode);
        
        for(int n : nodes){
            answer[bfs(n)]++;
        }
        
        answer[0] = startNode;
    
        return answer;
    }
    
    
    static int bfs(int startNode){
        
        Deque<Integer> nodes = map.get(startNode);
        
        if(nodes ==null){
            return 2;
        }
        
        while(!nodes.isEmpty()){
            int n = nodes.pop();
            
            if(start[n]+end[n]>=4){
                return 3;
            }
            
            if(end[n]==0 || start[n]==0) {
                return 2;
            }
            
            Deque<Integer> next = map.get(n);
            visited[n]=1;
            
            if(next==null){
                continue;
            }
            
            for(int nn : next){
                if(visited[nn]==0){
                    nodes.add(nn);
                }
            }
        }
        
        return 1;
    }
}