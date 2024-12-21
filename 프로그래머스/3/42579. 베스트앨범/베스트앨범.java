import java.util.*;

class Solution {
    public int[] solution(String[] genres, int[] plays) {
        //많이 재생된 장르 > 노래 > 고유번호
        Map<String, List<Song>> songs = new HashMap<>();
        Map<String, Integer> cnt = new HashMap<>();
        int n = genres.length;

        
        for(int i=0; i<n; i++){
            String genre = genres[i];
            int play = plays[i];
            Song s = new Song(play, i);
            
            songs.putIfAbsent(genre, new ArrayList<>());
            cnt.putIfAbsent(genre, 0);
            cnt.put(genre, cnt.get(genre)+play);
            List<Song> temp = songs.get(genre);
            temp.add(s);
            songs.put(genre, temp);
        }
        
        //cnt 값 기준 내림차순 정렬
        List<Map.Entry<String, Integer>> genreCnts = new LinkedList<>(cnt.entrySet());
        genreCnts.sort((o1, o2)-> cnt.get(o2.getKey()) - cnt.get(o1.getKey())); //내림차순
        List<Integer>temp = new ArrayList<>();

        for(Map.Entry<String, Integer> entry : genreCnts){
            String genre = entry.getKey();
            List<Song> ss = songs.get(genre);
            ss.sort(Comparator.comparing(Song::getPlay).thenComparing(Song::getNum));
            
            for(int i =0; i<Math.min(ss.size(),2); i++){
                temp.add(ss.get(i).num);
            }
        }
        int [] answer = new int[temp.size()];
        for(int i=0; i<temp.size(); i++){
            answer[i] = temp.get(i);
        }
        
        return answer;
    }
    
    static class Song {
        int plays;
        int num;
        
        public Song(int plays, int num){
            this.plays = plays;
            this.num= num;
        }
        
        public int getPlay(){
            return -plays;
        }
        
        public int getNum(){
            return num;
        }
                
    }
}