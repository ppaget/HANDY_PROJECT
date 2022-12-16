// Fichier pour des essais ou se rappeler ce qu'on a enlevé

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

double double_round(double value, int decimal_places) {
    double rounded ;
    double shift = pow(10, decimal_places);

    rounded = round(value*shift)/shift;
    return rounded ;
}

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


// void runge_kutta4(struct Struct_params * params, struct Struct_vari * vari, int t) {

//     double h ;
//     double k1_xc ;
//     double k2_xc ;
//     double k3_xc ;
//     double k4_xc ;

//     for (int i = 0 ; i < t ; i++) {

//         // double xc = params[i].xc ;
//         // double xe = params[i].xe ;
//         // double n = params[i].n ;
//         // double w = params[i].w ;

//         k1_xc = f_xc(i, params[i].xc) ;
//         k2_xc = f_xc(i + h/2, params[i].xc + h/2*k1_xc) ;
//         k3_xc = f_xc(i + h/2, params[i].xc + h/2*k2_xc) ;
//         k4_xc = f_xc(i + h, params[i].xc + h*k3_xc) ;

//         params[i].xc = params[i].xc + h/6 * (k1_xc + 2*k2_xc + 2*k3_xc + k4_xc) ;
//     }
// }

// double f_xc(t,xc) {

//     double wth = (r * xc) + (k * r * xe) ;
//     xc * (bc - (am + max(0,1-min(1,w/wth))(aM-am))) ;
// }


    // if (strcmp(condition, eg_f) == 0) {
    //     const char * file_path = argv[2] ;
    //     readFile(file_path, tab_variables, &parameters, size);
    //     runAuto(tab_variables, &parameters, t, 75000, 1, 4);
    //     finalFile("in_C/results_python_file.txt", tab_variables, &parameters, t) ;
    //     system("python in_Python/fen2.py --fileName in_C/results_python_file.txt --scenario eg") ;
    // }
    // else if (strcmp(condition, eq_f) == 0) {
    //     const char * file_path = argv[2] ;
    //     readFile(file_path, tab_variables, &parameters, size);
    //     runAuto(tab_variables, &parameters, t, 60000, 1, 4);
    //     finalFile("in_C/results_python_file.txt", tab_variables, &parameters, t) ;
    //     system("python in_Python/fen2.py --fileName in_C/results_python_file.txt --scenario eq") ;
    // }
    // else if (strcmp(condition, un_f) == 0) {
    //     const char * file_path = argv[2] ;
    //     readFile(file_path, tab_variables, &parameters, size);
    //     runAuto(tab_variables, &parameters, t, 79000, 1, 4);
    //     finalFile("in_C/results_python_file.txt", tab_variables, &parameters, t) ;
    //     system("python in_Python/fen2.py --fileName in_C/results_python_file.txt --scenario un") ;
    // }



    // else if (strcmp(condition, eg_c) == 0) {
    //     parameters.k = 0;
    //     double d = atof(argv[2]) ;
    //     parameters.d = d_optimal * d ;
    //     tab_variables[0].xc = 100 ;
    //     tab_variables[0].xe = 0 ;
    //     valuesDefault(tab_variables, &parameters) ;
    //     runAuto(tab_variables, &parameters, t, 2, 20);
    //     finalFile("in_C/results_python_cursors.txt", tab_variables, &parameters, t) ;
    //     system("python in_Python/fen3.py --fileCursors in_C/results_python_cursors.txt --fileBasic in_C/results_python_file.txt --scenario eg") ;
    // }
    // else if (strcmp(condition, eq_c) == 0) {
    //     parameters.k = 1;
    //     double d = atof(argv[2]) ;
    //     parameters.d = d_optimal * d ;
    //     tab_variables[0].xc = 100 ;
    //     tab_variables[0].xe = 10 ;
    //     valuesDefault(tab_variables, &parameters) ;
    //     runAuto(tab_variables, &parameters, t, 1, 20);
    //     finalFile("in_C/results_python_cursors.txt", tab_variables, &parameters, t) ;
    //     system("python in_Python/fen3.py --fileCursors in_C/results_python_cursors.txt --fileBasic in_C/results_python_file.txt --scenario eq") ;
    // }
    // else if (strcmp(condition, un_c) == 0) {
    //     double k = atof(argv[3]) ;
    //     parameters.k = k;
    //     double d = atof(argv[2]) ;
    //     parameters.d = d_optimal * d ;
    //     double xe = atof(argv[4]) ;
    //     tab_variables[0].xc = 100 ;
    //     tab_variables[0].xe = xe ;
    //     valuesDefault(tab_variables, &parameters) ;
    //     runAuto(tab_variables, &parameters, t, 2, 4);
    //     finalFile("in_C/results_python_cursors.txt", tab_variables, &parameters, t) ;
    //     system("python in_Python/fen3.py --fileCursors in_C/results_python_cursors.txt --fileBasic in_C/results_python_file.txt --scenario un") ;
    // }


//if ((strcmp(condition, eg_c) == 0) || (strcmp(condition, eq_c) == 0) || (strcmp(condition, un_c) == 0)) {