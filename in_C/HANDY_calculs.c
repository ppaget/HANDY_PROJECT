// Notre fichier calculs de HANDY depuis fichier textes

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

void readFile(char * FileName, struct Struct_variables * variables, struct Struct_params * params, int size) {
/* This function reads a text file of our initial conditions : 4 variables and 10 parameters.
It stocks the values in the two structures corresponding to the two types of arguments
(variables and parameters). */ 

    FILE * file = fopen(FileName, "r");
    if (file == NULL) printf("Error: file does not exist");

    int n = 0;
    double val;
    char line[100];
    while (fgets(line, 100, file) != NULL) {

        char * espace = strchr(line,' ') ;
        val = atof(espace) ; 

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
/* This function calculates the new four variables from the variables just before.
Incremeting with differential functions defined in the paper, using Euler method.*/

    // giving name for variables to make the program lighter
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

    //why
    double wth = (r * xc_prev) + (k * r * xe_prev) ; //dépend du temps
    double cc ;
    double ce ;
    double ac ;
    double ae ;

    if (wth != 0) {
        cc = fmin(1, w_prev/wth) * s * xc_prev ;
        ce = fmin(1, w_prev/wth) * k * s * xe_prev ;
    }
    else {
        cc = s * xc_prev ;
        ce = k * s * xe_prev ;
    }
    if (s * xc_prev != 0) {
        ac = am + (fmax(0, 1 - (cc / (s * xc_prev))) * (aM - am)) ;
    }
    else {
        ac = am ;
    } 
    if (s * xe_prev != 0) {
        ae = am + (fmax(0, 1 - (ce / (s * xe_prev))) * (aM - am)) ;
    }
    else {
        ae = am ;
    }

    // why
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

    // Addition of values of structure n°i+1
    variables[i+1].xc = xc_next ;
    variables[i+1].xe = xe_next ;
    variables[i+1].n = n_next ;
    variables[i+1].w = w_next ;
}

double findMax(struct Struct_variables * variables, char variable_name, int t) {
/* This function finds the maximum value for each of our 4 variable. It is then used
for the normalisation. */ 

    if (variable_name == 'c') {
        double mx = 0 ;
        for (int i = 0; i < t; i++) {
            double val = variables[i].xc ;
            mx = fmax(mx, val);
        }
        return mx ;
    }
    if (variable_name == 'e') {
        double mx = 0 ;
        for (int i = 0; i < t; i++) {
            double val = variables[i].xe ;
            mx = fmax(mx, val);
        }
        return mx ;
    }

    if (variable_name == 'n') {
        double mx = 0 ;
        for (int i = 0; i < t; i++) {
            double val = variables[i].n ;
            mx = fmax(mx, val);
        }
        return mx ;
    }

    if (variable_name == 'w') {
        double mx = 0 ;
        for (int i = 0; i < t; i++) {
            double val = variables[i].w ;
            mx = fmax(mx, val);
        }
        return mx ;
    }
    return 0 ;
}

void runAuto(struct Struct_variables * variables, struct Struct_params * params, int t) {
/* This function fulfills our tab_variables following the time using our
euleur function and normalizes each value. */

    for (int i = 0 ; i < t-1 ; i++) {
        euler(variables, params, i) ;
    }

    //normalisation
    double mx_XC = findMax(variables, 'c', t) ; 
    double mx_XE = findMax(variables, 'e', t) ;
    double mx_N = findMax(variables, 'n', t) ;
    double mx_W = findMax(variables, 'w', t) ;

    for (int i = 0 ; i < t ; i++) {
        variables[i].xc = (variables[i].xc / mx_XC) ;
        variables[i].xe = (variables[i].xe / mx_XE) ;
        variables[i].n = (variables[i].n / mx_N) ;
        variables[i].w = (variables[i].w / mx_W) ;
    }
}

void finalFile(char * FileName, struct Struct_variables * variables, int t) {
/* This function creates the final file containing all datas to send to python
(one variable per column). */
;

    FILE * file = fopen(FileName, "w");
    if (file == NULL) printf("Error: can not open file.\n");


    for (int i=0 ; i<t ; i++) {  // line break implemented for each i 
        fprintf(file, "%f, %f, %f, %f\n", variables[i].xc, variables[i].xe, variables[i].n, variables[i].w);
    } // Warning : frpintf writes strings and not doubles into the file -> Need to convert in python file 

    fclose(file);
}

int main(int argc, char const *argv[]) {
/* This is our main function. It reads a text file.
Then calculates datas. Creates a final file to send the datas to Python. */
;

    int t = 1000;
    struct Struct_variables tab_variables[t] ;// = tableau de t structures de types struct_vari
    struct Struct_params parameters ; //1 seule car les variables ne changent pas
    int size = 13; //taille des params (j'ai enlevé le temps à la fin)

    readFile("params_stable_equitable_2.txt",tab_variables, &parameters, 15);
    runAuto(tab_variables, &parameters, t);
    finalFile("results_python.txt", tab_variables, t) ;

    //lien avec python ? fin
    
    return 0;
}



// pour euler : mieux de faire une copie ou d'appeler variables[i] ?
// pour améliorer : fichier plus précis donc modifier lecture
// anciens fichiers textes
// template pyhton pour définir fonction