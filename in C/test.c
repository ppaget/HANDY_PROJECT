#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int main(int argc, char * argv[]) {
    FILE * fichier = fopen("resultats", "w");


// Ecrire
    double valeur = 0.661;
    fprintf(fichier, "Valeur: %0.3f\n", valeur);

// Fermer le fichier
    fclose(fichier);

        

    return 0;    
} 