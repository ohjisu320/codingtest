import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        for (int i = 0 ; i < n ; i++) {
            String oxString = br.readLine();
            int len_ox = oxString.length();
            int result = 0;
            int j = 0; // idx
            int k = 1; // plus
            while (j < len_ox) {
                if ( oxString.charAt(j) == 'O') {
                    result += k;
                    k += 1;
                } else {
                    k = 1;
                }
                j += 1;
            }
            System.out.println(result);

        }
    }
}