package oops;

class Person{
    Person(String name,int age){
        this.name=name;
        this.age=age;
    }
    public void info(){
        System.out.println(this.name);
        System.out.println(this.age);
    }
}
public class OOPS {
    public static void main(String[] args){
        Person P1=new Person("someshwar",18);
        P1.info();


    }
    
}
