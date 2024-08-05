

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

//1855. 암호
public class Main {
    static int n;
    static int m;
    static char[][] matrix;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        m = Integer.parseInt(br.readLine());
        char[] data = br.readLine().toCharArray();

        n = data.length / m;
        matrix = new char[n][m];

        for (int i = 0; i < data.length; i++) {
            if ((i/m) % 2 == 0) {
                matrix[i/ m][i % m] = data[i];
            } else {
                matrix[i/ m][m - 1 - i % m] = data[i];
            }
        }

        String result = "";
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                result+= matrix[j][i];
            }
        }
        System.out.println(result);


    }


}

