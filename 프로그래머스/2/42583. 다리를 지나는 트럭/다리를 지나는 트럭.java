import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int second = 0;
        int bridge_weight = 0;
        Deque<Truck> trucks = new ArrayDeque<>();
        Deque<Truck> bridges = new ArrayDeque<>();
        
        //트럭을 하나씩 대기조에 넣음
        for(int i=0; i<truck_weights.length; i++){
            trucks.add(new Truck(truck_weights[i]));
        }
        
        while(!(trucks.isEmpty() && bridges.isEmpty())) {
            if(!bridges.isEmpty() && bridges.peekFirst().location == bridge_length){
                Truck t = bridges.pollFirst();
                bridge_weight  -=t.weight;
            }
            
            Truck waitTruck = trucks.peekFirst();
            
            if(!trucks.isEmpty() && waitTruck.weight+bridge_weight <= weight){
                Truck freshTruck = trucks.pollFirst();
                bridge_weight += freshTruck.weight;
                bridges.add(freshTruck);
            }
            
            for(Truck t : bridges){
                t.location++;
            }
            second++;
        }
        
        
        return second;
    }
    
    static class Truck{
        int weight;
        int location;
        
        public Truck(int weight){
            this.weight = weight;
            this.location = 0;
        }
    }
}