import java.util.Scanner;

public class Switch{
    public static void main(String[] args){
        while (true){
        System.out.println("Enter day from (sunday - saturday) :");
        Scanner sc=new Scanner(System.in);
        String day=sc.next();
        
        switch(day){
            case "sunday": System.out.println("watch movie and fun");
            break;
            case "monday": System.out.println("practice python");
            break;                         
            case "tuesday": System.out.println("study git and github");
            break;           
            case "wednesday": System.out.println("learn java");
            break;           
            case "thursday": System.out.println("DSA and python practice");
            break;  
            case "friday": System.out.println("math 3");
            break;           
            case "saturday": System.out.println("work on mini project");
            break;           
            default: System.out.println("invalid day");
        }
        }
    }
}