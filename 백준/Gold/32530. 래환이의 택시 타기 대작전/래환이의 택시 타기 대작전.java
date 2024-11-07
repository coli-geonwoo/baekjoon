
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.time.Duration;
import java.time.LocalTime;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.List;

//25393. 교집합 만들기(골5)
public class Main {
    static int n;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());

        List<LocalTime> times = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            LocalTime time = LocalTime.parse(br.readLine(), DateTimeFormatter.ofPattern("HH:mm"));
//            System.out.println(time);
            times.add(time);
        }

        //시간 순으로 정렬
        times.sort(LocalTime::compareTo);
        List<Taxi> taxis = new ArrayList<>();

        for (LocalTime time : times) {
            if (taxis.isEmpty()) {
                taxis.add(new Taxi(time.plusMinutes(10L)));
            } else {
                boolean flag = false;
                for (Taxi taxi : taxis) {
                    if (taxi.canRide(time)) {
                        taxi.people++;
                        flag = true;
                        break;
                    }
                }

                if (!flag) {
                    taxis.add(new Taxi(time.plusMinutes(10L)));
                }
            }
        }

        System.out.println(taxis.size());

//        for (Taxi taxi : taxis) {
//            System.out.println("taxi.people = " + taxi.people);;
//            System.out.println("taxi.time = " + taxi.time);;
//        }


    }

    static class Taxi {
        final LocalTime time;
        int people;

        public Taxi(LocalTime time) {
            this.time = time;
            this.people = 1;
        }

        public boolean canRide(LocalTime target) {
            return people < 3 && Math.abs(Duration.between(time, target).toMinutes()) <= 10;
        }
    }

}
