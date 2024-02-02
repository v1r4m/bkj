import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st;

        int T = Integer.parseInt(br.readLine());
        int N = Integer.parseInt(br.readLine());
        int[] A = new int[N + 1];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            A[i + 1] = A[i] + Integer.parseInt(st.nextToken());
        }

        int M = Integer.parseInt(br.readLine());
        int[] B = new int[M + 1];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i++) {
            B[i + 1] = B[i] + Integer.parseInt(st.nextToken());
        }

        int[] aSum = new int[N*(N + 1) / 2];
        int[] bSum = new int[M*(M + 1) / 2];

        int cnt = 0;
        for (int i = 0; i < N; i++) {
            for (int j = i + 1; j <= N; j++) {
                aSum[cnt++] = A[j] - A[i];
            }
        }

        cnt = 0;
        for (int i = 0; i < M; i++) {
            for (int j = i + 1; j <= M; j++) {
                bSum[cnt++] = B[j] - B[i];
            }
        }

        Arrays.sort(aSum);
        Arrays.sort(bSum);

        int left = 0;
        int right = bSum.length - 1;
        int result = 0;
        while (left < aSum.length && right >= 0) {
            int sum = aSum[left] + bSum[right];

            if (sum < T) {
                left++;
            } else if (sum > T) {
                right--;
            } else {
                int tR = right;
                int tL = left;
                result++;

                while (--tR >= 0) {
                    if (aSum[left] + bSum[tR] == T) {
                        result++;
                    } else {
                        break;
                    }
                }

                while (++tL < aSum.length) {
                    if (aSum[tL] + bSum[right] == T) {
                        result++;
                    } else {
                        break;
                    }
                }

                left = tL;
                right = tR;
            }
        }
        System.out.print(result);

    }
}