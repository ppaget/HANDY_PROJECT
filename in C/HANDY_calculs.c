// Notre fichier calculs de HANDY

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

struct Struct_variables {
    double xc ;
    double xe ;
    double n ;
    double w ;
} ;
struct Struct_params {
    double am ;
    double aM ;
    double bc ;
    double be ;
    double g ;
    double l ;
    double s ;
    double d ;
    double k ;
    double r ;
} ;

void readfile(char * FileName, struct Struct_variables * variables, struct Struct_params * params, int size) {
""" This function reads a text file of our initial conditions : 4 variables and 10 parameters. """
""" It stocks the values in the two structures corresponding to the two types of arguments (variables and parameters). """
;

    FILE * file = fopen(FileName, "r");
    if (file == NULL) printf("Error: file does not exist");

    // Lire ligne par ligne
    int n = 0;
    double val;
    char line[100];
    while (fgets(line, 100, file) != NULL) { //read and store char (max 100 char) into buffer. at the end-> NULL
        // recup la valeur de la ligne strch, atof
        char * espace =strchr(line,' ');
        if (*(espace+1) != ' '){  // Si le caractère d'après n'est pas un espace, on peut transfèrer en chiffres 
            val = atof(espace+1);
            //val = double_round(val,6); // arrondit à 2 chiffres après virgule 
        }    
        else {
            val=atof(espace+2);
            //val = double_round(val,6); // arrondit à 2 chiffres après virgule 
        }
        
        // disjonction des cas pour chaque valeur de n
        if (n == 0) variables->xc = val ;
        if (n == 1) variables->xe = val ;
        if (n == 2) variables->n = val ;
        if (n == 3) variables->w = val ; 

        if (n == 4) params->am = val ;
        if (n == 5) params->aM = val ;
        if (n == 6) params->bc = val ;
        if (n == 7) params->be = val ;
        if (n == 8) params->g = val ;
        if (n == 9) params->l = val ;
        if (n == 10) params->s = val ;
        if (n == 11) params->d = val ;
        if (n == 12) params->k = val ;
        if (n == 13) params->r = val ;

        n = n + 1 ;
        
        if (n>size) break ;
    }
    fclose(file);
}

void euler(struct Struct_variables * variables, struct Struct_params * params, int i) {
""" This function calculates the new four variables from the variables just before. """
""" Incremeting with differential functions defined in the paper, using Euler method. """
;

    double xc_prev = variables[i].xc ;
    double xe_prev = variables[i].xe ;
    double n_prev = variables[i].n ;
    double w_prev = variables[i].w ;

    double am = params->am ;
    double aM = params->aM ;
    double bc = params->bc ;
    double be = params->be ;
    double g = params->g ;
    double l = params->l ;
    double s = params->s ;
    double d = params->d ;
    double k = params->k ;
    double r = params->r ;

    double wth = (r * xc_prev) + (k * r * xe_prev) ; //dépend du temps
    double cc ;
    double ce ;
    double ac ;
    double ae ;

    if (wth != 0) {
        double cc = fmin(1, w_prev/wth) * s * xc_prev ;
        double ce = fmin(1, w_prev/wth) * k * s * xe_prev ;
    }
    else {
        double cc = s * xc_prev ;
        double ce = k * s * xe_prev ;
    }
    if (s * xc_prev != 0) {
        double ac = am + (fmax(0, 1 - (cc / (s * xc_prev))) * (aM - am)) ;
    }
    else {
        double ac = am ;
    } 
    if (s * xe_prev != 0) {
        double ae = am + (fmax(0, 1 - (ce / (s * xe_prev))) * (aM - am)) ;
    }
    else {
        double ae = am ;
    }

    double dxc = (bc * xc_prev) - (ac * xc_prev) ;
    double dxe = (be * xe_prev) - (ae * xe_prev) ;
    double dn = (g * n_prev * (l - n_prev)) - (d * xc_prev * n_prev) ;
    double dw = (d * xc_prev * n_prev) - cc - ce ;

    double xc_next = xc_prev + dxc ;
    if (xc_next < 0) xc_next = 0 ;
    double xe_next = xe_prev + dxe ;
    if (xe_next < 0) xe_next = 0 ;
    double n_next = n_prev + dn ;
    if (n_next < 0) n_next = 0 ;
    double w_next = w_prev + dw ;
    if (w_next < 0) w_next = 0 ;

    //ajout des valeurs à ma strucutre n°i+1
    variables[i+1].xc = xc_next ;
    variables[i+1].xe = xe_next ;
    variables[i+1].n = n_next ;
    variables[i+1].w = w_next ;
}

double XC_findMax(struct Struct_variables * vari, int t) {

    double mx = 0 ;

    for (int i = 0; i < t; i++) {
        double val = vari[i].xc ;
        mx = fmax(mx, val);

    }
    return mx ;

}

double XE_findMax(struct Struct_variables * vari, int t) {

    double mx = 0 ;

    for (int i = 0; i < t; i++) {
        double val = vari[i].xe ;
        mx = fmax(mx, val);

    }
    return mx ;

}

double N_findMax(struct Struct_variables * vari, int t) {

    double mx = 0 ;

    for (int i = 0; i < t; i++) {
        double val = vari[i].n ;
        mx = fmax(mx, val);

    }
    return mx ;

}

double W_findMax(struct Struct_variables * vari, int t) {

    double mx = 0 ;

    for (int i = 0; i < t; i++) {
        double val = vari[i].w ;
        mx = fmax(mx, val);

    }
    return mx ;

}

void run_auto(struct Struct_variables * variables, struct Struct_params * params, int t) {
""" This function fulfills our tab_variables following the time using our """
""" euleur function and normalizes each value. """
;

    for (int i = 0 ; i < t ; i++) {
        euler(variables, params, i) ;
    }

    //normalisation
    double mx_XC = XC_findMax(variables, t) ; 
    double mx_XE = XE_findMax(variables, t) ;
    double mx_N = N_findMax(variables, t) ;
    double mx_W = W_findMax(variables, t) ;

    for (int i = 0 ; i < t ; i++) {
        variables[i].xc = (variables[i].xc / mx_XC) ;
        variables[i].xe = (variables[i].xe / mx_XE) ;
        variables[i].n = (variables[i].n / mx_N) ;
        variables[i].w = (variables[i].w / mx_W) ;
    }
}

void finalfile(char * FileName, struct Struct_variables * variables, int t) {
""" This function creates the final file containing all datas to send to python """
""" (one variable per column) """
;

    FILE * file = fopen(FileName, "w");
    if (file == NULL) printf("Error: can not open file.\n");


    for (int i=0 ; i<t ; i++) {  //va à la ligne à chaque fois normalement
        fprintf(file, "%f, %f, %f, %f\n", variables[i].xc, variables[i].xe, variables[i].n, variables[i].w);
    }

    fclose(file);
}

int main(int argc, char const *argv[]) {
"""This is our main function. It reads a text file. Then calculates datas. Creates a final file to send the datas to Python. """
;

    int t = 1000;
    struct Struct_variables tab_variables[t] ;// = tableau de t structures de types struct_vari
    struct Struct_params parameters ; //1 seule car les variables ne changent pas
    int size = 14; //taille des params (j'ai enlevé le temps à la fin)

    readfile("params_stable_equitable_2.txt",tab_variables, &parameters, 15);
    run_auto(tab_variables, &parameters, t);
    finalfile("results_python.txt", tab_variables, t) ;

    //lien avec python ?
    
    return 0;
}


// modifier tous les textes de parametres
// findMax en structure ?
// pour euler : mieux de faire une copie ou d'appeler variables[i]
// courbe inclusive