#include<stdio.h>
//#include<conio.h>
int main()
{
    int a, b;
    printf("Enter 1st value :");
    scanf("%d",&a);
    printf("Enter 2nd value :");
    scanf("%d",&b);
    
    if(a>b){
        printf("number %d is greater than number %d",a,b);}
    else if(a==b){
	   printf("Numbers are equal.");}
    else{
        printf("Largest Number is: %d", b);}
    return 0;
    //getch();
}
