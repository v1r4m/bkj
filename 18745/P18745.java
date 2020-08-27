////// fail ///////


import java.util.Scanner;

public class P18745{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[][][] array1 = new int[N][][];
        int[] array2 = new int[N];
        for(int i = 0;i<N;i++){
            int n = sc.nextInt();
            array1[i] = new int[n][2];
            int m = sc.nextInt();
            array2[i] = m;
            for(int j =0;j<n;j++){
                array1[i][j][0]=sc.nextInt();
                array1[i][j][1]=sc.nextInt();
            }
        }
        sc.close();
        for(int i=0;i<N;i++){
            int count = 0;
            firstloop:
            for(int j =0;j<Integer.MAX_VALUE;j++){
                int temp1 = 0;
                int temp2 = 0;
                for(int k=0;k<array1[i].length;k++){
                    temp1 = temp1+array1[i][k][0]*(int)Math.pow(j, array1[i][k][1]);
                }
                for(int k =0;k<array2[i];k++){
                    temp2 = temp2+(int)Math.pow(j,k);
                }
                if(temp1%temp2==0){
                    count++;
                }
                if(temp2>temp1){

                }

            }
        }

    }
}