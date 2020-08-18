import java.util.Scanner;

public class P2921{
    public static void main(String[] args){
        int N;
        int answer = 0;
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        sc.close();
        for(int i = 0;i<=N;i++){
            for(int j =i;j<=N;j++){
                answer = answer+i+j;
            }
        }
        System.out.print(answer);
    }
}