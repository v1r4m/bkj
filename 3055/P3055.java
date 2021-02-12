import java.io.IOException;
import java.util.Queue;
import java.util.LinkedList;
import java.util.Scanner;

class P3055{
    static private boolean visited[][];
    static private boolean koMap[][];
    static private int waterMap[][];
    static private int Bx;
    static private int By;
    static private int X;
    static private int Y;
    static private Queue<Node> water = new LinkedList<Node>();
    public static void main(String[] args) throws IOException{
        Scanner sc = new Scanner(System.in);
        String tmp[] = sc.nextLine().split(" ");
        Y = Integer.parseInt(tmp[0]);
        X = Integer.parseInt(tmp[1]);
        int Kx = 0;
        int Ky = 0;

        visited = new boolean[X][Y];
        koMap = new boolean[X][Y];
        waterMap = new int[X][Y];
        for(int i = 0; i<Y; i++){
            String temp = sc.nextLine();
            for(int j = 0;j<X;j++){
                visited[j][i]=false;
                waterMap[j][i]=Integer.MAX_VALUE; // infinity
                switch(temp.charAt(j)){
                    case 83: //S
                        Kx = j;
                        Ky = i;
                        koMap[j][i]=true;
                        break;
                    case 46: //.
                        koMap[j][i]=true;
                        break;
                    case 42: //*
                        koMap[j][i]=false;
                        water.add(new Node(j, i, 0));
                        waterMap[j][i]=0;
                        break;
                    case 88: //X
                        koMap[j][i]=false;
                        break;
                    case 68: //D
                        Bx = j;
                        By = i;
                        koMap[j][i]=true;
                        break;
                    default:
                        System.out.print("Unknown Token");
                        break;
                }
            }
        }
        sc.close();
        water_bfs();
        ko_bfs(Kx,Ky);
    }

    public static void ko_bfs(int start, int end){
        Queue<Node> ko = new LinkedList<Node>();
        ko.add(new Node(start, end, 0));
        visited[start][end]= true;
        boolean flag = false;
        while(!ko.isEmpty()){
            Node node = ko.poll();
//            visited[node.getX()][node.getY()]=true;

            //to up
            if((node.getY()-1>=0&&koMap[node.getX()][node.getY()-1])&&
                (!visited[node.getX()][node.getY()-1]&&waterMap[node.getX()][node.getY()-1]>node.getDepth()+1)){
                ko.add(new Node(node.getX(),node.getY()-1,node.getDepth()+1));
                visited[node.getX()][node.getY()-1]=true;
            }

            //to down
            if((node.getY()+1<Y&&koMap[node.getX()][node.getY()+1])&&
                (!visited[node.getX()][node.getY()+1]&&waterMap[node.getX()][node.getY()+1]>node.getDepth()+1)){
                ko.add(new Node(node.getX(),node.getY()+1,node.getDepth()+1));
                visited[node.getX()][node.getY()+1]=true;
            }
            
            //to right
            if((node.getX()+1<X&&koMap[node.getX()+1][node.getY()])&&
                (!visited[node.getX()+1][node.getY()]&&waterMap[node.getX()+1][node.getY()]>node.getDepth()+1)){
                ko.add(new Node(node.getX()+1,node.getY(),node.getDepth()+1));
                visited[node.getX()+1][node.getY()]=true;
            }

            //to left
            if((node.getX()-1>=0&&koMap[node.getX()-1][node.getY()])&&
                (!visited[node.getX()-1][node.getY()]&&waterMap[node.getX()-1][node.getY()]>node.getDepth()+1)){
                ko.add(new Node(node.getX()-1,node.getY(),node.getDepth()+1));
                visited[node.getX()-1][node.getY()]=true;
            }

            if(visited[Bx][By]){
                System.out.print(node.getDepth()+1);
                flag = true;
                break; //?
            }

        }
        if(!flag){
            System.out.print("KAKTUS");
        }
    }


    public static void water_bfs(){
        while(!water.isEmpty()){
            Node node = water.poll();
//            waterMap[node.getX()][node.getY()]=0;

            //to up
            if(node.getY()-1>=0&&koMap[node.getX()][node.getY()-1]&&!(node.getX()==Bx&&node.getY()-1==By)){
                if(waterMap[node.getX()][node.getY()-1]>node.getDepth()+1){
                    waterMap[node.getX()][node.getY()-1]=node.getDepth()+1;
                    water.add(new Node(node.getX(), node.getY()-1, node.getDepth()+1));
                }
                else{ 
                }
            }
            
            //to down
            if(node.getY()+1<Y&&koMap[node.getX()][node.getY()+1]&&!(node.getX()==Bx&&node.getY()+1==By)){
                if(waterMap[node.getX()][node.getY()+1]>node.getDepth()+1){
                    waterMap[node.getX()][node.getY()+1]=node.getDepth()+1;
                    water.add(new Node(node.getX(), node.getY()+1, node.getDepth()+1));
                }
                else{ 
                }
            }
            
            //to left
            if(node.getX()-1>=0&&koMap[node.getX()-1][node.getY()]&&!(node.getX()-1==Bx&&node.getY()==By)){
                if(waterMap[node.getX()-1][node.getY()]>node.getDepth()+1){
                    waterMap[node.getX()-1][node.getY()]=node.getDepth()+1;
                    water.add(new Node(node.getX()-1, node.getY(), node.getDepth()+1));
                }
                else{ 
                }
            }

            //to right
            if(node.getX()+1<X&&koMap[node.getX()+1][node.getY()]&&!(node.getX()+1==Bx&&node.getY()==By)){
                if(waterMap[node.getX()+1][node.getY()]>node.getDepth()+1){
                    waterMap[node.getX()+1][node.getY()]=node.getDepth()+1;
                    water.add(new Node(node.getX()+1, node.getY(), node.getDepth()+1));
                }
                else{ 
                }
            }
        }
    }
}

class Node{
    private int x;
    private int y;
    private int depth;
    Node(int x, int y, int depth){
        this.x = x;
        this.y = y;
        this.depth = depth;
    }
    public int getX(){
        return this.x;
    }
    public int getY(){
        return this.y;
    }
    public int getDepth(){
        return this.depth;
    }
}