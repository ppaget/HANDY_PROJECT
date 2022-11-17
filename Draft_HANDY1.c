#include <stdio.h>

struct Struct_vari {
    double xc; //commoners population
    double xe; //elites population
    double y; //nature 
    double w; //wealth 
};

struct Struct_params {
    double min_deathrate;
    double max_deathrate;
    double c_birthrate;
    double e_birthrate;
    double y_rege ;
    double y_capacity ;
    double sub_salary ; // Consumption
    double y_depletion ;
    double delta_consumption;
    double min_consumption ;
    int time ; //in years 

} ;

struct Data {
    char name;
    double value;
} ;

int lireFichier(char * nomFichier, struct Struct_vari * tableauARemplir, int longueur) { // On peut mettre le nom de struct qu'on veut ??
    // Ouvrir le fichier
    FILE * file = fopen(nomFichier, "r"); // pointer
    if (file == NULL) return -1;  //si fichier n'existe pas

    // Lire ligne par ligne
    int n = 0;
    char buffer[100];
    while (fgets(buffer, 100, file) != NULL) { //read and store char (max 100 char) into buffer. at the end-> NULL
        if (n >= longueur) break; //tu choisis longueur
        int ok = lireLigne(buffer, &tableauARemplir[n]);  //accede a ladresse n du tableau de structures = la structure n qui sera modifiée
        if (ok) n = n + 1;  // if ok is 1
    }
    fclose(file);
    return n;  // nombre de lignes ok pour paramètres en input 
}

int lireLigne(char * ligne, struct DataSet * data){

        // Création tableau pour stocker chiffres à la fin 
        char Data[15];

        // Définition des positions respectives des 2 virgules 
        char *tab1 = strchr(ligne, '\t');
        char *tab2 = strchr(tab1 + 1, '\t');

        //Condition d'invalidité de la ligne 
        if (tab1==NULL) {
            printf("0\nLigne non valide !\n");
            return 0 ;
        }
        else {
        
        //Conversion de la valeur txt en nombre ; pas besoin de convertir les autres colonnes 
        double v = atof(tab1+1) ; 

        //Remplissage de la structure avec les coordonnées en chiffres 
        data -> value = v ;
        data -> name = tab1 ;

        printf("%s,%.5f\t\n", tab1, v);
        return 1; 
        }
    }

int main(int argc, char const *argv[]){
    struct Struct_params params[1500] ;//= tableau de 1500 structures de types struct_params
    struct Struct_vari vari ;


    return 0;
}


// #define MAX 16

// int main (void){
//     FILE *file;
//     int primNum;
//     int secNum;
//     int listOfNumers[16];
//     int numberOfLines = MAX;
//     int i = 0;

//     file = fopen("file.txt", "rt");

//     fscanf(file, "%*f;%*c;%d;%s",  , myString);

//     if (file == NULL)
//     {
//         printf("Error\n");
//         return 1;
//     }

//     fscanf(file, "%d %d\n", &primNum, &secNum);

//     printf("\n1st Number: %d",primNum);
//     printf("\n2nd Number: %d",secNum);

//     printf("List of Numbers");

//     for(i=0;i<numberOfLines;i++){
//         //Count the number from the second line onwards
//     }

//     fclose(file);
//     return 0;
// }  