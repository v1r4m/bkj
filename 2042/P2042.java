import java.util.Scanner;
import java.io.IOException;
import java.lang.Math;

class P2042{
    public static void main(String[] args) throws IOException{
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int K = sc.nextInt();
        int [] arr = new int[N];

        for(int i = 0 ; i < N; i++){
            arr[i]=sc.nextInt();
        }

        sc.close();

        Tree tr = new Tree(arr);
    }
}

class Tree{
    private int tree[];
    private int log;
    Tree(int[] arr){
        log = (int)Math.pow(2.0,log2(arr.length));
        int[] tree = new int[log];
        init(arr, 0, arr.length-1, 1);
        
    }
    private static double log2(int base){
        return (Math.log10(base)/Math.log10(2));
    }
    private int init(int[] arr, int left, int right, int node){
        if(left==right){
            return tree[node]=arr[left];
        }
        int mid = (left+right)/2;
        tree[node] += init(arr, left, mid, node*2);
        tree[node] += init(arr, mid+1, right, node*2+1);

        return tree[node];
    }
}