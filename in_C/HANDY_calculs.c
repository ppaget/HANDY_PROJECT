// File that contains all our calculus.

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
    int CC ;
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
        if (n == 13) params->CC = val ;

        n = n + 1 ;
        
        if (n>size) break ;
    }
    fclose(file);

    // double eta = (params->aM-params->bc)/(params->aM-params->am) ;
    // int CC = (params->g/params->d)*(params->l-(params->s*eta/params->d)) ;
    // // printf("%d\n", CC) ;
    // params->CC = CC ;
}

void valuesDefault(struct Struct_variables *variables, struct Struct_params * params, char*scenario, int CC_c, double d_optimal) {

    char * eg = "eg" ;
    char * eq = "eq" ;
    char * un = "un" ;
    double eta ;
    if ((strcmp(scenario, eg) == 0) || (strcmp(scenario, eq) == 0)) {
        if (strcmp(scenario, eg) == 0) {
        variables[0].xe = 0 ;
        params->k=0 ;
        }
        else {
            variables[0].xe = 25 ;
            params->k=1 ;
        } 
    variables[0].xc = 100 ;
    params->bc = 0.03 ;
    params->be = 0.03 ;
    eta = 2/3 ;
    }

    else {
        variables[0].xc = 1e4 ;
        variables[0].xe = 3e3 ;
        params->k=10 ;
        params->bc = 6.5e-2 ;
        params->be = 2e-2 ;
        eta = 1/12 ;
    }

    params->am = 0.01 ;
    params->aM = 0.07 ;
    params->g = 0.01 ;
    params->l = 100 ;
    params->s = 0.0005 ;
    params->r = 0.005 ;
    params->CC = CC_c ;

    double d_c = (params->g*params->l+sqrt(pow(params->g*params->l,2)-4*CC_c*eta*params->s*params->g))/(2*CC_c) ;

    if (strcmp(scenario, eg) == 0) {
        params->d= d_c * d_optimal ;
    }
    else if (strcmp(scenario, eq) == 0) {
        params->d= d_c * 1.25 * d_optimal ;
    } 
    else {
        params->d= d_c * 0.95 * d_optimal ;
    }
    
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

void runAuto(struct Struct_variables * variables, struct Struct_params * params, int t, int mx_CC, double x_factor, int w_factor) {
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

    // double rapport = mx_W / mx_XC ;
    // printf("%f\n", rapport) ;
    
    // int mx_CC = 75000 ;

    for (int i = 0 ; i < t ; i++) {
        if (mx_XC == 0) variables[i].xc = 0 ;
        else variables[i].xc = (variables[i].xc / mx_CC / x_factor) ;
        if (mx_XE == 0) variables[i].xe = 0 ;
        else variables[i].xe = (variables[i].xe / mx_CC / x_factor) ;
        if (mx_N == 0) variables[i].n = 0 ;
        else variables[i].n = (variables[i].n / params[0].l) ;
        if (mx_W == 0) variables[i].w = 0 ;
        else variables[i].w = (variables[i].w / params[0].l / w_factor) ;
    }
}

void finalFile(char * FileName, struct Struct_variables * variables, struct Struct_params * params, int t, double x_factor, int w_factor) {
/* This function creates the final file containing all datas to send to python
(one variable per column). */

    FILE * file = fopen(FileName, "w");
    if (file == NULL) printf("Error: can not open file.\n");

    fprintf(file, "%s, %f, %f, %f, %f\n%s, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %d, %d\n", "Variables at t=0", variables->xc, variables->xe, variables->n, variables->w, "Parameters", params->am, params->aM, params->bc, params->be, params->g, params->l, params->s, params->d, params->k, params->r, x_factor, w_factor, params->CC);

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
    int size = 14 ;

    // readFile("/Users/macbookpro/Desktop/BA3/BA3-CMT/PROJECT/HANDY_PROJECT/Text/HANDY_unequal_basic.txt", tab_variables, &parameters, size);    
    // runAuto(tab_variables, &parameters, t, 1, 4);
    // finalFile("results_python_file.txt", tab_variables, &parameters, t) ;

    const char * condition = argv[1] ;

    double d_optimal = 6.67e-6 ;

    char * eg_f = "eg_f" ;
    char * eq_f = "eq_f" ;
    char * un_f = "un_f" ;
    char * eg_c = "eg_c" ;
    char * eq_c = "eq_c" ;
    char * un_c = "un_c" ;

    if ((strcmp(condition, eg_f) == 0) || (strcmp(condition, eq_f) == 0) || (strcmp(condition, un_f) == 0)) {
        puts("entered");
        const char * file_path = argv[2] ;
        char * scenario = "aa";
        double x_factor ;
        int w_factor ;
        if (strcmp(condition, eg_f) == 0) {
            puts("entered");
            printf("%s/n", condition);
            x_factor = 1 ;
            w_factor = 4 ;
            strcpy(scenario, "eg");
            puts("lol")
        }
        else if (strcmp(condition, eq_f) == 0) {
            x_factor = 1 ;
            w_factor = 4 ;
            strcpy(scenario, "eq");
        }
        else {
            x_factor = 1 ;
            w_factor = 4 ;
            strcpy(scenario, "un");
        }
        puts("fini");
        readFile(file_path, tab_variables, &parameters, size);
        runAuto(tab_variables, &parameters, t, parameters.CC, x_factor, w_factor);
        puts("file");
        finalFile("in_C/results_python_file.txt", tab_variables, &parameters, t, x_factor, w_factor) ;

        char runFen2[500] = "python in_Python/fen2.py --fileName in_C/results_python_file.txt --scenario ";
        // char sc[5] = scenario;
        strcat(runFen2, scenario);
        system(runFen2) ;
    }

    else {
        puts("cursors");
        double CC_c = atof(argv[2]) ;
        printf("%f\n", CC_c);
        char * scenario ;
        double x_factor ;
        int w_factor ;
        if (strcmp(condition, eg_c) == 0) {
            strcpy(scenario, "eg");
            if (CC_c>=0.7 && CC_c<=1.0) {
                puts("first");
                x_factor = 1 ;
                w_factor = 4 ;
            }
            else {
                x_factor = 2 ;
                w_factor = 20 ;
            }
        }
        else if (strcmp(condition, eq_f) == 0) {
            strcpy(scenario, "eq");
            x_factor = 1 ;
            w_factor = 20 ;
        }
        else {
            strcpy(scenario, "un");
            x_factor = 0.2 ;
            w_factor = 4 ;
        }
    valuesDefault(tab_variables, &parameters, scenario, CC_c, d_optimal);
    runAuto(tab_variables, &parameters, t, parameters.CC, x_factor, w_factor);
    finalFile("in_C/results_python_file.txt", tab_variables, &parameters, t, x_factor, w_factor) ;

    char runFen3[500] = "python in_Python/fen3.py --fileCursors in_C/results_python_cursors.txt --fileBasic in_C/results_python_file.txt --scenario ";
    // char sc[5] = scenario;
    strcat(runFen3, scenario);
    system(runFen3) ;
    }

    return 0;

}

