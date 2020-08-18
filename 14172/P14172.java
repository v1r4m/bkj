import java.util.Scanner;
import java.util.ArrayList;
import java.util.Arrays;

public class P14172{

    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        Dfsclass dfs = new Dfsclass(N);
        for(int i = 0; i < N; i++){
            dfs.listadd(new int[]{sc.nextInt(), sc.nextInt(), sc.nextInt()});
        }
        sc.close();
        for(int i = 0; i<N; i++){
            for(int j = 0; j<N;j++){
                if(i!=j&&Math.sqrt(Math.pow((dfs.listget(i,0)-dfs.listget(j,0)),2)+Math.pow((dfs.listget(i,1)-dfs.listget(j,1)),2))<=dfs.listget(i,2)){
                    dfs.arraytrue(i,j);
                }
            }
        }
        int maxcount = 0;
        for(int i =0; i<N; i++){
            dfs.dfs(i);
            if(maxcount<dfs.getcount()){
                maxcount = dfs.getcount();
            }
            dfs.initcount();
            dfs.initvisitedArray();
        }
        System.out.print(maxcount);
    }
}

class Dfsclass{
    private int N;
    private ArrayList<int[]> list = new ArrayList<int[]>();
    private boolean[][] array;
    private boolean[] visitedArray;
    private int count;

    public Dfsclass(int n){
        this.N = n;
        this.array = new boolean[n][n];
//        Arrays.fill(this.array, false); //already false
        this.visitedArray = new boolean[n];
//        Arrays.fill(this.visitedArray, false); //already false
        this.count = 0;
    }

    public int getcount(){
        return this.count;
    }

    public void initcount(){
        this.count = 0;
    }

    public void listadd(int[] arr){
        this.list.add(arr);
    }

    public void arraytrue(int index1, int index2){
        this.array[index1][index2] = true;
    }

    public int listget(int index1, int index2){
        return this.list.get(index1)[index2];
    }

    public void initvisitedArray(){
        Arrays.fill(this.visitedArray,false);
    }

    public void dfs(int vIdx){
        this.visitedArray[vIdx] = true;
        count++;
        for(int i = 0; i <this.N; i++){
            if(this.array[vIdx][i] && !this.visitedArray[i]){
                dfs(i);
            }
        }
    }
}