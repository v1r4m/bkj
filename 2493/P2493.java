import java.util.ArrayList;
import java.util.Stack;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class P2493{
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int topNum = Integer.parseInt(bf.readLine());
        String[] temp = bf.readLine().split(" ");
        ArrayList<Integer> top = new ArrayList<Integer>();
        ArrayList<Integer> result = new ArrayList<Integer>();
        Stack<Tower> towerStack = new Stack<Tower>();
        for(int i = 0; i<topNum; i++){
            top.add(Integer.parseInt(temp[i]));
        }
        result.add(0);//tower number 0's result is always 0;
        for(int i = 0; i < topNum-1;i++){
            if(top.get(i)>=top.get(i+1)){ //when it gets smaller
                result.add(i+1); //i+1 => i but it shows in i+1
                towerStack.push(new Tower(top.get(i), i));
            }
            else{ // when it gets bigger
                if(towerStack.isEmpty()){
                    result.add(0);
                    continue;
                }
                else{
                    while(!towerStack.isEmpty()&&top.get(i+1)>towerStack.peek().getData()){
                        towerStack.pop();
                    }
                    if(towerStack.isEmpty()){
                        result.add(0);
                    }
                    else{
                        result.add(towerStack.peek().getIndex()+1); // it starts with 1 not 0 so we adjust it 
                    }
                }

            }
        }
        for(int i = 0; i < result.size(); i++){
            System.out.print(result.get(i)+" ");
        }
    }
}

class Tower{
    private int data;
    private int index;
    Tower(int data, int index){
        this.data = data;
        this.index = index;
    }
    public int getData(){
        return this.data;
    }
    public int getIndex(){
        return this.index;
    }
}