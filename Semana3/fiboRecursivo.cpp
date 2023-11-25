#include<bits/stdc++.h>

using namespace std;

typedef long long ll;


ll fibonacci(ll i ){
    if(i == 0 ){
        return 0;
    }else if (i == 1 ){
        return 1;
    }
    
    return fibonacci(i-1)+fibonacci(i-2);
}

int main(){

    ll i = 0;

    for( i = 0 ; i < 50 ; i++){
        printf("%lld\n",fibonacci(i));
    }


    return 0;
}