#include <stdio.h>
void InsertionSort(int arr[],int n)
{ int last;
int idx;
int i;
    for( i=1;i<n;i++)
    {
      last=arr[i];
       idx=i-1;
      while(idx>=0 && arr[idx]>last)
      {
          arr[idx+1]=arr[idx];
          
            idx--;
        } 
          arr[idx+1]=last;
        
      for(int i=0;i<n;i++){
          printf("%d ",arr[i]);
      }
      printf("\n");
    }
    
     
  
    
}

int main()
{
    int n;
    scanf("%d",&n);
    int arr[n];
    for(int i=0;i<n;i++)
    {
        scanf("%d",&arr[i]);
    }
    InsertionSort(arr,n);

    return 0;
}
