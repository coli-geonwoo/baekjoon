
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.StringTokenizer;

//29808 너의 수능 점수가 궁금해
public class Main {
    static int num;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        num = Integer.parseInt(br.readLine());
        List<Score> scores = new LinkedList<>();
        for (int i = 0; i < 201; i++) {
            for (int j = 0; j < 201; j++) {
                Score score = new Score(i,j);
                if(score.result()){
                    scores.add(score);
                }
            }
        }

        System.out.println(scores.size());
        for (Score score : scores) {
            score.print();
        }
    }

    static class Score{
        int diff1;
        int diff2;

        public Score(int diff1, int diff2) {
            this.diff1 = diff1;
            this.diff2 = diff2;
        }

        boolean result(){
            if((diff1*508 + diff2*212)*4763 == num){
                return true;
            }

            if((diff1*108 + diff2*212)*4763 == num){
                return true;
            }

            if((diff1*508 + diff2*305)*4763 == num){
                return true;
            }

            if((diff1*108 + diff2*305)*4763 == num){
                return true;
            }
            return false;
        }

        void print(){
            System.out.println(diff1 + " " + diff2);
        }
    }

}