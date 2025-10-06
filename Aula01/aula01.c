#include <stdio.h>

int main(){

    // Variaveis
    int idade = 16;

    printf("Mostrando a idade: %d", idade);

    if(idade > 12){
        printf("Ja passou da validade, segundo Daniel");
    }else{
        printf("Ta boa ainda, segundo Daniel");
    }

    idade > 12 ? printf("Ja passou da validade, segundo Daniel") : printf("Ta boa ainda, segundo Daniel");


    for(int i = 0; i < 10; i++){
        printf("Contagem: %d", i);
    }

    return 0;
}