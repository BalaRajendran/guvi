#include<stdio.h>
#include<conio.h>
int main(){
    int a[100],n,k,temp,i,j;
    scanf("%d%d",&n,&k);
    for(i=0;i<n;i++){
        scanf("%d",&a[i]);
    }
     for(i=0;i<n;i++){
         //printf("%d-i ",i);
        for(j=i;j<n;j++){
           /// printf("%d-j ",j);
         if(a[i]>a[j]){
             temp=a[i];
             a[i]=a[j];
             a[j]=temp;
         }
        }
     }
printf("%d ",a[k-1]);
}
