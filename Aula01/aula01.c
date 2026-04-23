#include <stdio.h>

int main(){

    // Variaveis
    int idade = 19;

    printf("Mostrando a idade: %d", idade);

    if(idade > 18){
        printf("Permitido comprar bebida");
    }else{
        printf("Não permitido");
    }

    idade > 18 ? printf("Permitido comprar bebida") : printf("Não Permitido");


    for(int i = 0; i < 10; i++){
        printf("Contagem: %d", i);
    }

    return 0;
}