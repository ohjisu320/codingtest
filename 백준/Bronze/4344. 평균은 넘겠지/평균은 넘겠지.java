import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int C = sc.nextInt();
        for (int tc = 0; tc < C; tc ++) {
            int N = sc.nextInt();
            int[] students = new int[N];
            

            int sum = 0;
            for (int i = 0; i < N; i++) {
                students[i] = sc.nextInt();
                sum += students[i];
            }

            double avg = sum / (double) N ;

            int count = 0;
            for (int student : students) {
                if (student > avg) {
                    count++;
                }
            }

            double ratio = (count * 100.0) / N;
            System.out.println(String.format("%.3f%%", ratio));

        }
    }
}