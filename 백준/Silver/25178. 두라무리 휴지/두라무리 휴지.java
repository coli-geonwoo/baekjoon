
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
    static int n;
    static char[] origin;
    static char[] destination;


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        origin = br.readLine().toCharArray();
        destination = br.readLine().toCharArray();

        if (check()) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }

    }

    static boolean check() {
        return check1() && check2() && check3();
    }

    static boolean check1() {
        return (origin[0] == destination[0] && origin[n - 1] == destination[n - 1]);
    }

    static boolean check2() {
        StringBuilder sb1 = new StringBuilder();
        StringBuilder sb2 = new StringBuilder();

        for (int i = 0; i < n; i++) {
            if (!moeum(origin[i])) {
                sb1.append(origin[i]);
            }

            if (!moeum(destination[i])) {
                sb2.append(destination[i]);
            }
        }

        return sb1.toString().equals(sb2.toString());
    }

    static boolean moeum(char c) {
        return (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u');
    }

    static boolean check3() {
        Arrays.sort(origin);
        Arrays.sort(destination);

        for (int i = 0; i < n; i++) {
            if (origin[i] != destination[i]) {
                return false;
            }
        }
        return true;
    }
}