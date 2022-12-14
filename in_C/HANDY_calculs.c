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

void readFile(const char * FileName, struct Struct_variables * variables, struct Struct_params * params, int size) {
/* This function reads a text file of our initial conditions : 4 variables and 10 parameters.
It stocks the values in the two structures corresponding to the two types of arguments
(variables and parameters). */ 

    FILE * file = fopen(FileName, "r");
    if (file == NULL) printf("Error: file does not exist"); //ne fonctionne pas

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

void paramsDefault(struct Struct_params * params) {
    params->am = 0.01 ;
    params->aM = 0.07 ;
    params->bc = 0.03 ;
    params->be = 0.03 ;
    params->g = 0.01 ;
    params->l = 100 ;
    params->s = 0.0005 ;
    // params->d = 0.00000667 ;
    // params->k = 0 ;
    params->r = 0.005 ;
}

void euler(struct Struct_variables * variables, struct Struct_params * params, int i) {
/* This function calculates the new four variables from the variables just before.
Incremeting with differential functions defined in the paper, using Euler method.*/

    // giving name for variables to make the program lighter
    double xc_prev = variables[i].xc ;
    double xe_prev = variables[i].xe ;
    double n_prev = variables[i].n ;
    double w_prev = variables[i].w ;

    double am = params->am ; //healthy value 
    double aM = params->aM ; //max value when population starts to starve
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
    double cc ; //consumption rate of commoners
    double ce ; //consumption rate of elites
    double ac ; //death rate of commoners
    double ae ; //death rate of elites
    double zh = (g*(aM-am))/(s*(aM-bc))*pow((l/2),2) ; //pour egalitarian
    double zhg = (g*(aM-am))/(s*(aM-bc))*pow((l/2),2) ; //pour equitable 
    // printf("%f\n", zh) ;

    if (wth != 0) {
        cc = fmin(1, w_prev/wth) * s * xc_prev ;
        ce = fmin(1, w_prev/wth) * k * s * xe_prev ; //k = 0 ou k=1
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

//Mettre normalisation clean : en argument de la fonction
//Déterminer comment normaliser selon les graphs 

    for (int i = 0 ; i < t-1 ; i++) {
        euler(variables, params, i) ;
    }

    //normalisation
    double mx_XC = findMax(variables, 'c', t) ; 
    double mx_XE = findMax(variables, 'e', t) ;
    double mx_N = findMax(variables, 'n', t) ;
    double mx_W = findMax(variables, 'w', t) ;
    

    for (int i = 0 ; i < t ; i++) {
        if (mx_XC == 0) variables[i].xc = 0 ;
        else variables[i].xc = (variables[i].xc / 75000 / 2) ;
        if (mx_XE == 0) variables[i].xe = 0 ;
        else variables[i].xe = (variables[i].xe / 75000 / 2) ;
        if (mx_N == 0) variables[i].n = 0 ;
        else variables[i].n = (variables[i].n / params[0].l) ;
        if (mx_W == 0) variables[i].w = 0 ;
        else variables[i].w = (variables[i].w / params[0].l / 40) ;
    }
}

void finalFile(char * FileName, struct Struct_variables * variables, struct Struct_params * params, int t) {
/* This function creates the final file containing all datas to send to python
(one variable per column). */
;

    FILE * file = fopen(FileName, "w");
    if (file == NULL) printf("Error: can not open file.\n");

    fprintf(file, "%s, %f, %f, %f, %f\n%s, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f\n", "Variables at t=0", variables->xc, variables->xe, variables->n, variables->w, "Parameters", params->am, params->aM, params->bc, params->be, params->g, params->l, params->s, params->d, params->k, params->r);

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
    struct Struct_variables tab_variables[t] ;
    struct Struct_params parameters ; 
    int size = 13 ;


    const char * condition = argv[1] ;

    double d_star = 6.67e-6 ;

    // const char * condition = "eg_f" ;
    // printf("%s\n", condition) ;
    
    char * eg_f = "eg_f" ;
    char * eq_f = "eq_f" ;
    char * un_f = "un_f" ;
    char * eg_c = "eg_c" ;
    char * eq_c = "eq_c" ;
    char * un_c = "un_c" ;

    if (strcmp(condition, eg_f) == 0) {
        printf("%s\n", condition) ;
        const char * file_path = argv[2] ;
        // const char * file_path = "/Users/macbookpro/Desktop/BA3/BA3-CMT/PROJECT/HANDY_PROJECT/Text/HANDY_egalitarian_basic.txt" ;
        readFile(file_path, tab_variables, &parameters, size);
        runAuto(tab_variables, &parameters, t);
        finalFile("results_python_file.txt", tab_variables, &parameters, t) ;
        system("python ../in_Python/fen2.py --fileName results_python_file.txt --scenario egalitarian") ;
    }
    else if (strcmp(condition, eq_f) == 0) {
        const char * file_path = argv[2] ;
        readFile(file_path, tab_variables, &parameters, size);
        runAuto(tab_variables, &parameters, t);
        finalFile("results_python_file.txt", tab_variables, &parameters, t) ;
        system("python ../in_Python/fen2.py --fileName results_python_file.txt --scenario equitable") ;
    }
    else if (strcmp(condition, un_f) == 0) {
        const char * file_path = argv[2] ;
        readFile(file_path, tab_variables, &parameters, size);
        runAuto(tab_variables, &parameters, t);
        finalFile("results_python_file.txt", tab_variables, &parameters, t) ;
        system("python ../in_Python/fen2.py --fileName results_python_file.txt --scenario unequal") ;
    }

    else if (strcmp(condition, eg_c) == 0) {
        parameters.k = 0;
        double d = atof(argv[3]) ;
        parameters.d = d_star * d ;
        tab_variables[0].xc = 100 ;
        tab_variables[0].xe = 0 ;
        tab_variables[0].n = 100 ;
        tab_variables[0].w = 0 ;
        paramsDefault(&parameters) ;
        runAuto(tab_variables, &parameters, t);
        finalFile("results_python_cursors.txt", tab_variables, &parameters, t) ;
        system("python ../in_Python/fen3.py --fileCursors results_python_cursors.txt --fileBasic results_python_file.txt --scenario egalitarian") ;
    }
    else if (strcmp(condition, eq_c) == 0) {
        parameters.k = 1;
        double d = atof(argv[3]) ;
        parameters.d = d_star * d ;
        tab_variables[0].xc = 100 ;
        tab_variables[0].xe = 10 ;
        tab_variables[0].n = 100 ;
        tab_variables[0].w = 0 ;
        paramsDefault(&parameters) ;
        runAuto(tab_variables, &parameters, t);
        finalFile("results_python_cursors.txt", tab_variables, &parameters, t) ;
        system("python ../in_Python/fen3.py --fileCursors results_python_cursors.txt --fileBasic results_python_file.txt --scenario equitable") ;
    }
    else if (strcmp(condition, un_c) == 0) {
        double k = atof(argv[2]) ;
        parameters.k = k;
        double d = atof(argv[3]) ;
        parameters.d = d_star * d ;
        tab_variables[0].xc = 100 ;
        tab_variables[0].xe = 0.2 ;
        tab_variables[0].n = 100 ;
        tab_variables[0].w = 0 ;
        paramsDefault(&parameters) ;
        runAuto(tab_variables, &parameters, t);
        finalFile("results_python_cursors.txt", tab_variables, &parameters, t) ;
        system("python ../in_Python/fen3.py --fileCursors results_python_cursors.txt --fileBasic results_python_file.txt --scenario unequal") ;
    }

    //readFile("/Users/macbookpro/Desktop/BA3/BA3-CMT/PROJECT/HANDY_PROJECT/Text/HANDY_egalitarian_basic.txt", tab_variables, &parameters, 15);
    // readFile("/Users/peppa/Desktop/Ba3/CMT/PROJECT/HANDY_PROJECT/Text/HANDY_unequal_basic.txt", tab_variables, &parameters, 15);
    // runAuto(tab_variables, &parameters, t);
    // finalFile("results_python_file.txt", tab_variables, &parameters, t) ;

    return 0;
}

