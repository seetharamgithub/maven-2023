class FibonacciExample2{  
 static int n1=0,n2=1,n3=0;    
 static void printFibonacci(int count){    
    if(count>0){    
         n4 = n1 + n2 + n3;    
         n1 = n2;    
         n2 = n3; 
         n3 = n1;
         System.out.print(" "+n3);   
         printFibonacci(count-1); 
my first fibnacci program   
     }    
 }    
 public static void main(String args[]){    
  int count=10; 
  maven-2023   
  System.out.print(n1+" "+n2+" "n3+);//printing 0 and 1    
  printFibonacci(count-2);//n-2 because 2 numbers are already printed   
 }  
}  
