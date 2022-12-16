// File that contains all of our calculus.

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
    double CC ;
} ;

void readFile(const char * FileName, struct Struct_variables * variables, struct Struct_params * params, int size) {
/* Reads text file of our initial conditions : 4 variables and 10 parameters.
Stocks the values in corresponding structures.
Args: FileName: given file
      variables: all datas from beginning
      params: all parameters
      size: to stop loop.
*/

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
        if (n == 14) params->CC = val ;

        n = n + 1 ;
        
        if (n>size) break ;
    }
    fclose(file);
}

void valuesDefault(struct Struct_variables *variables, struct Struct_params * params, char*scenario, double CC_c, double d_optimal) {
/* Fulfills parameters and first variable values according to type of scenario.
Calculates parameter d from carrying capacity.
Args: variables: datas
      params: all parameters
      scenario: type of scenario
      CC_c: carrying capacity from cursors
      d_optimal: factor to find d.
*/
    char * eg = "eg" ;
    char * eq = "eq" ;
    char * un = "un" ;
    double eta = 2/3 ;
    if (strcmp(scenario, eg) == 0) {
    variables[0].xe = 0 ;
    params->k=0 ;
    }
    else if (strcmp(scenario, eq) == 0){
        variables[0].xe = 25 ;
        params->k=1 ;
    } 
    else {
        variables[0].xe = 0.001 ;
        params->k = 100 ;
    }
    variables[0].xc = 100 ;
    variables[0].n = 100 ;
    variables[0].w = 0 ;
    params->am = 0.01 ;
    params->aM = 0.07 ;
    params->bc = 0.03 ;
    params->be = 0.03 ;
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
/* Calculates new four variables (i+1) from the variables just before (i).
Incremeting with differential functions using Euler method.
Args: variables: all datas from beginning
      params: all parameters
      i: index for structure
*/

    // Giving name for variables to make the program lighter
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

    double wth = (r * xc_prev) + (k * r * xe_prev) ; //dépend du temps
    double cc ; //consumption rate of commoners
    double ce ; //consumption rate of elites
    double ac ; //death rate of commoners
    double ae ; //death rate of elites

    // Values needed to calculate
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

    // Euler's method
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

    // Addition of values to structure n°i+1
    variables[i+1].xc = xc_next ;
    variables[i+1].xe = xe_next ;
    variables[i+1].n = n_next ;
    variables[i+1].w = w_next ;
}

void runAuto(struct Struct_variables * variables, struct Struct_params * params, int t, int x_factor, int w_factor) {
/* Fulfills tab_variables over time using Euler method
and normalizes each value.
Args: variables: all datas from beginning
      params: all parameters
      t: time
      x_factor: normalisation for populations
      w_factor: normalisation for wealth
*/

    // Calls euler each time
    for (int i = 0 ; i < t-1 ; i++) {
        euler(variables, params, i) ;
    }

    // Normalisation depending on variable
    int mxx_CC = 75000 ;

    for (int i = 0 ; i < t ; i++) {
        variables[i].xc = (variables[i].xc / mxx_CC / x_factor) ;
        variables[i].xe = (variables[i].xe / mxx_CC / x_factor) ;
        variables[i].n = (variables[i].n / params[0].l) ;
        variables[i].w = (variables[i].w / params[0].l / w_factor) ;
    }
}

void finalFile(char * FileName, struct Struct_variables * variables, struct Struct_params * params, int t, int x_factor, int w_factor) {
/* Creates final file containing all datas from tab_variables to send to Python.
Contains a header with variables at t=0 and fixed parameters.
Four variables (one per column) overtime.
Args: FileName: file will be created
      variables: all datas from beginning
      params: all parameters
      t: time
      x_factor: normalisation for populations
      w_factor: normalisation for wealth
*/

    FILE * file = fopen(FileName, "w");
    if (file == NULL) printf("Error: can not open file.\n");

    // Header
    fprintf(file, "%s, %f, %f, %f, %f\n%s, %f, %f, %f, %f, %f, %f, %f, %f, %f, %f, %d, %d, %f\n", "Variables at t=0", variables->xc, variables->xe, variables->n, variables->w, "Parameters", params->am, params->aM, params->bc, params->be, params->g, params->l, params->s, params->d, params->k, params->r, x_factor, w_factor, params->CC);

    for (int i=0 ; i<t ; i++) { 
        fprintf(file, "%f, %f, %f, %f\n", variables[i].xc, variables[i].xe, variables[i].n, variables[i].w);
    } // Warning : frpintf writes strings

    fclose(file);
}

int main(int argc, char const *argv[]) {
/* Runs in two ways. Increments variables and stock them in tab of strucutre
with Euler method for solving differential equations.
Args: type of scenario (str)
      path of file (str) or chosen Carrying Capacity (str)
Returns: a text file containing datas over time.
        uses system to directly run Python files.
*/
;

    int t = 1000;
    struct Struct_variables tab_variables[t] ;
    struct Struct_params parameters ; 
    int size = 14 ;

    // Type of scenario
    const char * condition = argv[1] ;

    double d_optimal = 6.67e-6 ;

    char * eg_f = "eg_f" ;
    char * eq_f = "eq_f" ;
    char * un_f = "un_f" ;
    char * eg_c = "eg_c" ;
    char * eq_c = "eq_c" ;
    char * un_c = "un_c" ;

    // Case from file
    if ((strcmp(condition, eg_f) == 0) || (strcmp(condition, eq_f) == 0) || (strcmp(condition, un_f) == 0)) {
        const char * file_path = argv[2] ;
        char * scenario ;
        int x_factor ;
        int w_factor ;
        if (strcmp(condition, eg_f) == 0) {
            x_factor = 1 ;
            w_factor = 4 ;
            scenario = "eg";
        }
        else if (strcmp(condition, eq_f) == 0) {
            x_factor = 1 ;
            w_factor = 4 ;
            scenario = "eq";
        }
        else {
            x_factor = 1 ;
            w_factor = 4 ;
            scenario = "un";
        }
        readFile(file_path, tab_variables, &parameters, size);
        runAuto(tab_variables, &parameters, t, x_factor, w_factor);
        finalFile("in_C/results_python_file.txt", tab_variables, &parameters, t, x_factor, w_factor) ;
        char runFen2[500] = "python in_Python/fen2.py --fileName in_C/results_python_file.txt --scenario ";
        strcat(runFen2, scenario);
        system(runFen2) ;
    }
    // Case from cursor
    else {
        double CC_c = atof(argv[2]) ;
        char * scenario ;
        int x_factor ;
        int w_factor ;
        if (strcmp(condition, eg_c) == 0) {
            scenario = "eg";
            if (CC_c>=0.7 && CC_c<=1.0) {
                x_factor = 1 ;
                w_factor = 4 ;
            }
            else {
                x_factor = 2 ;
                w_factor = 20 ;
            }
        }
        else if (strcmp(condition, eq_c) == 0) {
            scenario = "eq";
            if (CC_c>=0.7 && CC_c<=1.0) {
                x_factor = 1 ;
                w_factor = 4 ;
            }
            else {
                x_factor = 2 ;
                w_factor = 20 ;
            }
        }
        else {
            scenario = "un";
            x_factor = 2 ;
            w_factor = 40 ;
        }
        valuesDefault(tab_variables, &parameters, scenario, CC_c, d_optimal);
        runAuto(tab_variables, &parameters, t, x_factor, w_factor);
        finalFile("in_C/results_python_cursors.txt", tab_variables, &parameters, t, x_factor, w_factor) ;
        char runFen3[500] = "python in_Python/fen3.py --fileCursors in_C/results_python_cursors.txt --fileBasic in_C/results_python_file.txt --scenario ";
        strcat(runFen3, scenario);
        system(runFen3) ;
    }

    return 0;

}

