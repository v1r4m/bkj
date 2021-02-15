import java.util.Scanner;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.ArrayList;
import java.util.Queue;
import java.util.HashSet;
import java.io.IOException;

//failed. this code is O(N^logN)
//you have to use segmented tree instead of this algorithm

class P9426{
    private static int N;
    private static int K;
    private static HashSet<Integer> set1 = new HashSet<Integer>();
    private static HashSet<Integer> set2 = new HashSet<Integer>();

    public static void main(String[] args) throws IOException{
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        K = sc.nextInt();
        int[] Karr = new int[K];
        int[] Narr = new int[N];
        for(int i = 0; i<K;i++){
            int tmp=sc.nextInt();
            Karr[i]=tmp;
            Narr[i]=tmp;
        }
        set2.
        Arrays.sort(Karr);
        for(int i = 0; i<K/2-1;i++){
            set1.add(Karr[i]);
        }
        for(int i = K/2-1; i<K; i++){
            set2.add(Karr[i]);
        }
        for(int i = K; i<N; i++){
            Narr[i]=sc.nextInt();
            int goIn = Narr[i];
            int goOut = Narr[i-K];
        }
        sc.close();
    }
    public static int update(int goIn, int goOut){
        if(goIn<set2.getFirst()&&goOut<set2.getFirst()){
            return set2.getFirst();
        }
        else if(goIn>=set2.getFirst()&&goOut>=set2.getFirst()){
            return set2.getFirst();
        }

    }
}


