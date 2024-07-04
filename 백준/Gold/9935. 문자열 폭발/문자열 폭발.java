import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {

    private static int len;
    private static char [] stack;


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine();
        String bomb = br.readLine();
        len = bomb.length();
        stack = new char[s.length()];

        int index = 0;

        for (char a : s.toCharArray()) {
            stack[index++] = a;
            if (index >= len
                    && String.valueOf(Arrays.copyOfRange(stack, Math.max(0, index - len), index))
                    .equals(bomb)
            ) {
                for (int j = Math.max(0, index - len); j < index; j++) {
                    stack[j] = ' ';
                }
                index -= len;

            }
        }

        while(remove(stack, bomb)){};

        String result = String.valueOf(stack).trim();
        if(result.length() ==0){
            System.out.println("FRULA");
        }else{
            System.out.println(result);
        }
    }

    private static boolean remove(char [] stack, String bomb){
        if (stack.length >= len
                && String.valueOf(Arrays.copyOfRange(stack, Math.max(0, stack.length - len), stack.length))
                .equals(bomb)
        ) {
            for (int j = Math.max(0, stack.length - len); j < stack.length; j++) {
                stack[j] = ' ';
            }
            return true;
        }
        return false;
    }
}
