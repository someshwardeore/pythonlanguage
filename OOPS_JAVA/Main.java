class Student{
    String name;
    int age;
    int roll_no;
    //constructor
    Student(String name,int age,int roll_no){
        this.name=name;
        this.age=age;
        this.roll_no=roll_no;
    }
    //method
    public void info(){
        System.out.println(this.name);
        System.out.println(this.age);
        System.out.println(this.roll_no);
    }

}
//main class
public class Main{
    public static void main(String[] args){
        Student s1=new Student("someshwar",18,40);
        s1.info();

    }
}