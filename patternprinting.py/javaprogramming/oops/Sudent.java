package oops;

class Student{
    String name;
    int age;
    int roll_no;

    public void info(){
        System.out.println(name);
        System.out.println(age);
        System.out.println(roll_no);

    }

}

public class Sudent {
    public static void main(String[] args){
        Student s1=new Student();
        s1.name="someshwar";
        s1.age=18;
        s1.roll_no=40;
        s1.info();


    }
    
}
