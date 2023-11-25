#include<bits/stdc++.h>

using namespace std;

typedef long long ll;

ll memo[200000];

ll fibonacci(ll i ){
    if(i == 0 ){
        return 0;
    }else if (i == 1 ){
        return 1;
    }
    
    ll& pdm = memo[i];
    if(pdm!= -1 ){
        return pdm;
    }

    return pdm = fibonacci(i-1)+fibonacci(i-2);
}

int main(){

    ll i = 0;

    memset(memo,-1,sizeof memo);

    for( i = 0 ; i < 100 ; i++){
        printf("%lld\n",fibonacci(i));
    }


    return 0;
}