import java.util.Scanner;
import java.util.Arrays;

public class P2098{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        Dp dp = new Dp(N);
        for(int i = 0; i<N; i++){
            for(int j =  0; j<N; j++){
                int a = sc.nextInt();
                dp.setdp(i,j,a);
            }
        }
        sc.close();
        System.out.print(dp.filla(0,1));
    }
}

class Dp{
    private int[][] array;
    private int[][] dpa;
    private int N;
    private static int INF = 16 * 1_000_000;

    Dp(int N){
        this.array = new int[N][N];
        this.dpa = new int[N][(int)Math.pow(2,N)];
        for(int i =0; i<N;i++){
            Arrays.fill(this.dpa[i],INF);
        }
        this.N = N;
    }

    public void setdp(int i, int j, int a){
        this.array[i][j]=a;
    }


    /*"check no road or visited" once on bigger size filla function,
    and another time in for(N) loop for "check no road or visited"
    this function does mapping nxn array & calling the shortest path
    mapping is for(N) loop, and calling is return;
    dpa[current][visited] = you are in current node, visited visited, and saves the shortest value of going back to 0.
    */

    public int filla(int current, int visited){
        if(visited == Math.pow(2,this.N)-1){
            if(this.array[current][0]==0) return INF; //if returning road not exists
            return this.array[current][0];
        }
        if(this.dpa[current][visited]!=INF){ //if visited
            return this.dpa[current][visited];
        }
        for(int i =0;i<this.N;i++){
            if(this.array[current][i] == 0 || (visited & (1 << i)) != 0) continue; //no road or visited

            int next = visited | (1 << i);

            this.dpa[current][visited] = Math.min(this.dpa[current][visited],this.filla(i,next)+this.array[current][i]);
        }
        return this.dpa[current][visited];
    }
}