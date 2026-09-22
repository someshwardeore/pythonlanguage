import java.util.Scanner;
public class CheckNum {
    public static void main(String[] args){
        while (true){
            System.out.println("Enter any number :");
            Scanner sc=new Scanner(System.in);
            int num=sc.nextInt();
        
            if(num%2==0){
                System.out.println("even");
            }

            else{
                System.out.println("ood");
            }
        }
    }
    
}