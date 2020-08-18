import java.util.Scanner;

public class P1022{
    private static int max(int a, int b){
        if(a>b) return a;
        else if(a<b) return b;
        else return a;
    }
    private static int absolute(int a){
        if(a>0) return a;
        else if(a<0) return -1*a;
        else return 0;
    }
    private static int data(int x, int y){
        int mile = 0;
        int data = 0;
        mile = max(absolute(x),absolute(y)); //mile is always positive(+)>0
        if(mile == -1*y)        data = (mile*2)*(mile*2)+1+((-1*mile)-x);
        else if(mile == -1*x)   data = (mile*2)*(mile*2)+1+(y-(-1*mile));
        else if(mile == y)      data = (2*mile+1)*(2*mile+1) - (mile-x); 
        else if(mile == x){ //&& mile!=y
            data = (2*mile-1)*(2*mile-1)+mile-y;
        }
        return data;
    }
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int dy1 = sc.nextInt();
        int dx1 = sc.nextInt();
        int dy2 = sc.nextInt();
        int dx2 = sc.nextInt();
        sc.close();
        int digit = 0;
        int maximum = max(data(dx2,dy2),max(data(dx1, dy1), data(dx1, dy2)));
        digit = (int)(Math.log10(maximum)+1);
        for(int y = dy1; y<dy2+1; y++){
            for(int x = dx1; x<dx2+1; x++){
                String f = "%"+digit+"d";
                String data = String.format(f, P1022.data(x,y));
                if(x != dx2)    System.out.print(data+" ");
                else            System.out.println(data);
            }
        }
    }
}