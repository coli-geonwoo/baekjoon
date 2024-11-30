
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        long n = Long.parseLong(br.readLine());
        long result = 0;

        if(n==2){
            result=1;
        }else if(n==3){
            result=3;
        }else{
            result = (n-2)*2 +1 + (n-1);
        }
        bw.write(String.valueOf(result));
        bw.flush();
    }
}
