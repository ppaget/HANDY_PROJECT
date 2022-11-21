#include <stdio.h>

struct Struct_vari {
    double xc; //commoners population
    double xe; //elites population
    double n; //nature 
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

struct Struct_Data {
    char name;
    double value; // pointeur pour avoir tableaux des valeurs en fonction du temps 
} ;
// pour pouvoir faire Data[i].name = Data[i].value, ie pour associer la valeur au nom 


int readFile(char * nomFichier, struct Struct_params * tableparams, struct Struct_vari * tablevari, int size) { // On peut mettre le nom de struct qu'on veut ??
    // Ouvrir le fichier
    FILE * file = fopen(nomFichier, "r"); // pointer
    if (file == NULL) return -1;  //si fichier n'existe pas

    // Lire ligne par ligne
    int n = 0;
    double val;
    char line[100];
    while (fgets(line, 100, file) != NULL) { //read and store char (max 100 char) into buffer. at the end-> NULL
        // recup la valeur de la ligne strch, atof
        char * espace =strchr(line,' ');
        if (*(espace+1) != ' '){  // Si le caractère d'après n'est pas un espace, on peut transfèrer en chiffres 
            val = atof(espace+1); // arrondir à 2 chiffres après virgule 
        }    
        else {
            val=atof(espace+2); // arrondir à 2 chiffres après virgule 
        }
        
        // dijonction des cas pour chaque valeur de n
        if (n == 0) tablevari->xc = val;
        if (n == 1) tablevari->xe = val ;
        if (n == 2) tablevari->n = val ;
        if (n == 3) tablevari->w = val ; // Finir pour les paramètres 

        if (n == 4) 
        n = n + 1; // if ok is 1
        
        if (n>size) break ; // ici, size=15
    }
    fclose(file);
}

int main(int argc, char const *argv[]){
    struct Struct_vari vari[1000] ; //= tableau de 1500 structures de types struct_vari
    struct Struct_params params ;

    //option avec struct data (name+value)
    struct Struct_Data data[10] ;
    readFile("params_default.txt", vari, &params, 15); 
    return 0;
}


