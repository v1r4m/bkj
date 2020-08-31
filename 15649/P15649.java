import java.util.Scanner;

//I tried to sole this using choose&mix, but I figured out choosing itself is mixing...
//the problem was i couldn't think of backtracking with choosing algorithm, so i thought
//choose somehow and mix.. and then I came up with choosing with backtracking makes it all easy.
//what it makes this problem hard is that the output should be descendent.


public class P15649{
    private int n;
    private int m;
    private int[] arr;
    private boolean[] visited;
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        P15649 P = new P15649(n,m);
        sc.close();
        P.choose(0);
    }
    P15649(int n, int m){
        this.n = n;
        this.m = m;
        this.arr = new int[m];
        this.visited = new boolean[n+1];
    }
    public void choose(int index){
        if(index==this.m){
            for(int i=0;i<this.arr.length;i++){
                System.out.print(this.arr[i]+" ");
            }
            System.out.println();
            return;
            //we do not need index =0; because it will go back...
        }
        for(int i=1;i<=this.n;i++){  //visited - backtracking
            if(!this.visited[i]){
                this.visited[i]=true;
                this.arr[index] = i;
                choose(index+1);
                this.visited[i]=false;
            }

        }
    }
    public void mix(int[] array, int i){ //not in use
        if(i == this.m){
            for(int j=0;j<array.length;j++){
                System.out.print(array[j]+" ");
            }
            System.out.println();
            return;
        }
        else{
            for(int j =i;j<array.length;j++){
                int temp;
                temp = array[i];
                array[i]=array[j];
                array[j]=temp;
                this.mix(array, i+1);
                int temp2;
                temp2 = array[i];
                array[i]=array[j];
                array[j]=temp2;
            }
        }
    }
}