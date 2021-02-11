import java.util.Scanner;
import java.util.LinkedList;
import java.util.ArrayList;
import java.util.Iterator;
import java.util.Queue;

public class P9470{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int nN = sc.nextInt();
        ArrayList<Integer>[][] adjList = new ArrayList[nN][];
        for(int i =0;i<nN;i++){
            if(i==sc.nextInt()){
                int nV = sc.nextInt();
                int nE = sc.nextInt();
                Ar A = new Ar(nV);
                adjList[i] = new ArrayList[nV+1];
                boolean[] visited = new boolean[nV+1];
                for(int j=1;j<=nV;j++){
                    adjList[i][j] = new ArrayList<Integer>();
                }
                for(int j=0;j<nE;j++){
                    int v1 = sc.nextInt();
                    int v2 = sc.nextInt();
                    adjList[i][v2].add(v1); //this is inverse order, it would look nice if I replace its vector
                }
                dfs(A, nV, adjList[i],visited); //nV = root
                //visited init
            }
        }
        sc.close();
    }
    public static void dfs(Ar a, int v, ArrayList[] arr, boolean[] visited){
        visited[v] = true;
        //do something
        Iterator<Integer> iter = arr[v].listIterator();
        if(iter.hasNext()){
            int n = iter.next();
            if(!visited[n]){
                dfs(a, n,arr,visited);
            }
        }
        else{
            a.setArray(v,1);
            return;
        }
    }
    public static int filla(Ar a, int v, ArrayList[] arr, boolean[] visited){
        visited[v]=true;
        Queue<Integer> q = new LinkedList<Integer>();

        return 0;
        

    }
}

class Ar{
    private int[] array;
    Ar(int n){
        int[] array = new int[n];
    }
    public int getArray(int n){
        return this.array[n];
    }
    public void setArray(int n, int a){
        this.array[n] = a;
        return;
    }
}