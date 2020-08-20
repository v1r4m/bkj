import java.util.Scanner;

//very massive code
//if you want to slove this problem, you have to check case of upper slope/down slope. 
//down slope is not that hard problem, but the upper slope is the hard one because you have to check the previous block.
//want to make this code cleaner if chance comes.

public class P14890 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int L = sc.nextInt();
        int[][][] array = new int[N][N][3];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                array[i][j][0] = sc.nextInt();
            }
        }
        sc.close();
        int count = 0;
        boolean flag = false;
        if (L == 1) {
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N - 1; j++) {
                    if (array[i][j][0] - array[i][j + 1][0] == 1) {
                        array[i][j + 1][1] = 1;
                    } else if (array[i][j][0] - array[i][j+1][0] == -1 && array[i][j][1] == 0) { //upper slope
                        array[i][j][1] = 1;
                    } else if (array[i][j][0] == array[i][j+1][0]) {} else {
                        count--;
                        break;
                    }
                }
                count++;
            }
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N - 1; j++) {
                    if (array[j][i][0] - array[j + 1][i][0] == 1) {
                        array[j + 1][i][2] = 1;
                    } else if (array[j][i][0] - array[j+1][i][0] == -1 && array[j][i][2] == 0) {
                        array[j][i][2] = 1;
                    } else if (array[j][i][0] == array[j+1][i][0]) {} else {
                        count--;
                        break;
                    }
                }
                count++;
            }
        } else {
            for (int i = 0; i < N; i++) {
                firstloop: //means of break firstloop; = this line is boomed
                    for (int j = 0; j < N - 1; j++) {
                        int abs = array[i][j][0] - array[i][j + 1][0];
                        if (abs > 1 || abs <-1) {
                            flag = false;
                            count--;
                            break firstloop;
                        } else if (abs == -1) {
                            if(flag){
                                flag = false;
                                count--;
                                break firstloop;
                            }
                            if (j - L < -1) {
                                flag = false;
                                count--;
                                break firstloop;
                            }
                            for (int f = 0; f < L; f++) {
                                if (array[i][j - f][1] != 0) {
                                    flag = false;
                                    count--;
                                    break firstloop;
                                }
                            }
                            for (int f = 1; f < L; f++) { // j-1, j-2 .... L-1s check
                                if (array[i][j - f][0] - array[i][j - f + 1][0] != 0) {
                                    flag = false;
                                    count--;
                                    break firstloop;
                                }
                            }
                            for (int f = 1; f <= L; f++) { // j-1, j-2 .... L-1s check
                                array[i][j-L+f][1]=f;
                            }
                        } else if ((array[i][j][1] == 0 ||array[i][j][1]==L)&& abs == 1) { // down slope start
                            if (j + L < N) {
                                array[i][j + 1][1]++; //=1
                                flag = true;
                            } else {
                                flag = false;
                                count--;
                                break firstloop;
                            }
                        } else if (array[i][j][1] < L && abs == 1) {
                            flag = false;
                            count--;
                            break firstloop;
                        } else if (array[i][j][1] == 0 && abs == 0) {}
                        else if (array[i][j][1] == L - 1 && abs == 0) {
                            array[i][j + 1][1] = array[i][j][1] + 1;
                            flag = false;
                        } else if (array[i][j][1] < L && abs == 0) {
                            array[i][j + 1][1] = array[i][j][1] + 1;
                        }
                    }
                if (!flag) count = count + 1;
                flag = false;
            }
            for (int i = 0; i < N; i++) {
                firstloop: for (int j = 0; j < N - 1; j++) {
                    int abs = array[j][i][0] - array[j + 1][i][0];
                    if (abs > 1 || abs <-1) {
                        flag = false;
                        count--;
                        break firstloop;
                    } else if (abs == -1) { //upper slope
                        if(flag){
                            flag = false;
                            count--;
                            break firstloop;
                        }
                        if (j - L < -1) {
                            flag = false;
                            count--;
                            break firstloop;
                        }
                        for (int f = 0; f < L; f++) {
                            if (array[j - f][i][2] != 0) {
                                flag = false;
                                count--;
                                break firstloop;
                            }
                        }
                        for (int f = 1; f < L; f++) { // j-1, j-2 .... L-1s check
                            if (array[j - f][i][0] - array[j - f + 1][i][0] != 0) {
                                flag = false;
                                count--;
                                break firstloop;
                            }
                        }
                        for (int f = 1; f < L; f++) { // j-1, j-2 .... L-1s check
                            array[j-L+f][i][2]=f;
                        }
                    } else if ((array[j][i][2] == 0||array[j][i][2]==L) && abs == 1) { // down slope start
                        if (j + L < N) {
                            array[j + 1][i][2]++;
                            flag = true;
                        } else {
                            flag = false;
                            count--;
                            break firstloop;
                        }
                    } else if (array[j][i][2] < L && abs == 1) {
                        flag = false;
                        count--;
                        break firstloop;
                    } else if (array[j][i][2] == 0 && abs == 0) {}
                    else if (array[j][i][2] == L - 1 && abs == 0) {
                        array[j + 1][i][2] = array[j][i][2] + 1;
                        flag = false;
                    } else if (array[j][i][2] < L && abs == 0) {
                        array[j + 1][i][2] = array[j][i][2] + 1;
                    }
                }
                if (!flag) count = count + 1;
                flag = false;
            }
        }
        System.out.print(count);
    }
}