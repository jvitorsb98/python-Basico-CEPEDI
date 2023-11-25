#include<bits/stdc++.h>

typedef long long int ll;

void fibo(int N){
    ll a = 0 , b=1;
    if(N == 1 ){
        printf("%lld\n",a);
    } else if(N==2){
        printf("%lld\n",a);
        printf("%lld\n",b);
    }

    for(int i = 0 ; i < N ; i++){
        printf("%lld\n",a);
        b = a+b;
        a = a +b;
        b = a-b;
        a = a-b;
    }

}

int main(){

    int N = 100000;

    fibo(N);


}