import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static int n;
    static int m;
    static Sinho[] sinhos;


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] s = br.readLine().split(" ");
        n = Integer.parseInt(s[0]);
        m = Integer.parseInt(s[1]);
        sinhos = new Sinho[m];

        for (int i = 0; i < m; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());

            sinhos[i] = new Sinho(
                    Integer.parseInt(st.nextToken()),
                    Integer.parseInt(st.nextToken()),
                    Integer.parseInt(st.nextToken())
            );
        }

        Arrays.sort(sinhos);

        long result = n;

        if (m != 0) {
            result = sinhos[0].cal(0, 0);

            for (int i = 1; i < m; i++) {
                result = sinhos[i].cal(result, sinhos[i - 1].meter);
            }
            result += n - sinhos[m - 1].meter;
        }

        System.out.println(result);
    }

    static class Sinho implements Comparable<Sinho> {
        int meter;
        int cycle;
        int startTime;

        Sinho(int meter, int cycle, int startTime) {
            this.meter = meter;
            this.cycle = cycle;
            this.startTime = startTime;
        }

        long cal(long time, long beforeMeter) {
            time += (meter - beforeMeter);

            if (time <= startTime) {
                return startTime;
            }
            
            if((time/cycle)%2==1){
                if(time%cycle<startTime){
                    return time;
                }else{
                    return ((time/cycle)+1)*cycle + startTime;
                }
            }else{
                if(time%cycle>=startTime){
                    return time;
                }
                return time + (startTime - time%cycle);
                
            }
        }

        @Override
        public int compareTo(Sinho o) {
            return Integer.compare(meter, o.meter);
        }
    }


}