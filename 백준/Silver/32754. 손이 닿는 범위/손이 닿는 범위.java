
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        st= new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int r = Integer.parseInt(st.nextToken());
        int result =0 ;

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());

            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());
            int x3 = Integer.parseInt(st.nextToken());
            int y3 = Integer.parseInt(st.nextToken());
            int x4 = Integer.parseInt(st.nextToken());
            int y4 = Integer.parseInt(st.nextToken());

            if( isAnswer(x1, y1, x2, y2, x3, y3, x4, y4, r)){
                result++;
            }

        }
        bw.write(String.valueOf(result));
        bw.flush();
    }

    private static boolean isAnswer(
            int x1, int y1,
            int x2, int y2,
            int x3, int y3,
            int x4, int y4,
            int r){
        double px = (double) (x1+x2+x3+x4) /4 ;
        double py = (double) (y1+y2+y3+y4) /4 ;

        double cr = distance(px, py, x1, y1); //외접원의 반지름
        double d = distance(px, py, 0, 0);
        return d<=r || cr +r >=d;
    }

    private static double distance(double x1, double y1, double x2, double y2){
        return Math.sqrt(Math.pow(Math.abs(x1-x2), 2) + Math.pow(Math.abs(y1-y2), 2));
    }
}
