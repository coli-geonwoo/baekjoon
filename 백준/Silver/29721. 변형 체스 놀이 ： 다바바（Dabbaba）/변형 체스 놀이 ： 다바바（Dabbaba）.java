
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Objects;
import java.util.Set;

public class Main {

    public static void main(String[] args) throws IOException {

        class Data {
            private int x;
            private int y;

            public Data(int x, int y) {
                this.x = x;
                this.y = y;
            }

            @Override
            public boolean equals(Object o) {
                if (this == o) return true;
                if (o == null || getClass() != o.getClass()) return false;
                Data data = (Data) o;
                return x == data.x && y == data.y;
            }

            @Override
            public int hashCode() {
                return Objects.hash(x, y);
            }
        }
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int result = 0;

        String[] s = br.readLine().split(" ");
        int size = Integer.parseInt(s[0]);
        int cnt = Integer.parseInt(s[1]);

        int[] dx = {-2, 2, 0, 0};
        int[] dy = {0, 0, -2, 2};

        Set<Data> board = new HashSet<>();
        Set<Data> start  = new HashSet<>();
        for (int i = 0; i < cnt; i++) {
            String[] inputs = br.readLine().split(" ");

            int sx = Integer.parseInt(inputs[0]);
            int sy = Integer.parseInt(inputs[1]);
            start.add(new Data(sx, sy));

            for(int j=0; j<4; j++){
                int nx = sx +dx[j];
                int ny = sy+dy[j];

                if(nx<=0 || ny<=0 || nx>size || ny>size){
                    continue;
                }

                board.add(new Data(nx, ny));
            }
        }
        board.removeAll(start);
        System.out.println(board.size());
    }
}
