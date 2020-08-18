import java.util.Scanner;
import java.util.Arrays;

public class P10427{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[][] array = new int[N][];
        for(int i = 0; i<N; i++){
            int num = sc.nextInt();
            array[i] = new int[num];
            for(int j = 0; j<num; j++){
                array[i][j] = sc.nextInt();
            }
        }
        sc.close();
        for(int i =0;i<N;i++){
            Arrays.sort(array[i]);
        }
        int[] answer = new int[N];
        //n=1 -> always zero
        //n=2
        for(int i =0;i<N;i++){
            int sec = -1;
            for(int j =0;j<array[i].length-1;j++){
                if(sec==-1||sec>array[i][j+1]-array[i][j])
                sec = array[i][j+1]-array[i][j];
            }
            answer[i] = answer[i]+sec;
            //n=3
            for(int j = 2;j<array[i].length-1;j++){ // 3,4,5,....,n-1
                sec = -1;
                int thr = 0;
                for(int k = 0; k<array[i].length-j;k++){
                    thr = array[i][k+j]*j;
                    for(int l = 0; l<j;l++){
                        thr = thr - array[i][k+l];
                    }
                    if(sec==-1 || sec>thr) sec = thr;
                }
                answer[i]=answer[i]+sec;
            }
            //n=n
            int sum= 0;
            for(int j = 0; j<array[i].length;j++){
                sum = sum+array[i][j];
            }
            answer[i]=answer[i]+array[i][array[i].length-1]*array[i].length - sum;
            System.out.println(answer[i]);
        }
    }
}