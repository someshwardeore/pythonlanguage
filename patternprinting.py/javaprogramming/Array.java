import java.util.Scanner;
public class Array {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        //declare integer array
        int[] marks=new int[5];
        //Take input
        for(int i=0; i<5; i++){
            System.out.println("Enter element of array "+(i+1));
            marks[i]=sc.nextInt();
        }
        System.out.println();
        //Display elements
        for(int i=0; i<5; i++){
            System.out.println(marks[i]);
        }
    }
}
