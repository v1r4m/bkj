import java.util.Scanner;
import java.util.Arrays;
import java.io.IOException;

class P9426{
    private static int N;
    private static int K;
    public static void main(String[] args) throws IOException{
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        K = sc.nextInt();
        int result = 0;
        int tt = N-K+1;
        int[][] arr = new int[tt][K];
        for(int i = 0;i<K;i++){
            int tmp = sc.nextInt();
            for(int j = 0; j <i+1;j++){
                arr[j][i-j]=tmp;
            }
        }
        for(int i = K-1; i < N-K; i++){
            int tmp=sc.nextInt();
            for(int j = 0 ; j <K;j++){
                arr[i+j-1][K-j-1] = tmp;
            }
        }
        for(int i = 1; i<K;i++){ //7
            int tmp = sc.nextInt();
            for(int j =0;j<K-i;j++){
                arr[tt-K+i+j][K-j-1] = tmp;
            }
        }
        sc.close();
        for(int i = 0; i<tt; i++){
            Arrays.sort(arr[i]);
            result = result+arr[i][K/2];
        }
        System.out.print(result);
    }
}
