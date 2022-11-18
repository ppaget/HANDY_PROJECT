
// parse en remplissant struct paramètres avec conditions initiales--> PEPS params[1500]
// struct contenant variables --> PEPS vari[1500]
// tableau de struct qui se remplit avec variables --> MAHLIA
// fichier contenant variables --> MAHLIA
// python lit ces fichiers et plot tout --> Mahlia
// méthode runge kutta pour équa diff --> comparer les 2 méthodes pour précision

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

struct Struct_params {
    double xc ;
    double xe ;
    double n ;
    double w ;
} ;

struct Struct_vari {
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

void readfile(char * nomFichier, struct Struct_params * params, struct Struct_vari * vari, int size) {

    FILE * file = fopen(nomFichier, "r");
    if (file == NULL) return -1;
    int size = len(file);
    fclose(file);

    for (int i=0 ; i<size ; i++){
        char *tab1 = strchr(file, '\t');
        char *tab2 = strchr(tab1 + 1, '\t'); 
    }
}

void lireLigne() {

}

void euler(struct Struct_params * params_i, struct Struct_vari * vari, struct Struct_params * params_i2) {

// possible avec boucle for ?

    double xc = params_i->xc ;
    double xe = params_i->xe ;
    double n = params_i->n ;
    double w = params_i->w ;

    double am = vari->am ;
    double aM = vari->aM ;
    double bc = vari->bc ;
    double be = vari->be ;
    double g = vari->g ;
    double l = vari->l ;
    double s = vari->s ;
    double d = vari->d ;
    double k = vari->k ;
    double r = vari->r ;

    double wth = (r * xc) + (k * r * xe) ; //dépend du temps
    double cc ;
    double ce ;
    double ac ;
    double ae ;


    if (wth != 0) {
        double cc = min(1, w/wth) * s * xc ;
        double ce = min(1, w/wth) * k * s * xe ;
    }
    else {
        double cc = s * xc ;
        double ce = k * s * xe ;
    }
    if (s * xc != 0) {
        double ac = am + (max(0, 1 - (cc / (s * xc))) * (aM - am)) ;
    }
    else {
        double ac = am ;
    } 
    if (s * xe != 0) {
        double ae = am + (max(0, 1 - (ce / (s * xe))) * (aM - am)) ;
    }
    else {
        double ae = am ;
    }

    double dxc = (bc * xc) - (ac * xc) ;
    double dxe = (be * xe) - (ae * xe) ;
    double dn = (g * n * (l - n)) - (d * xc * n) ;
    double dw = (d * xc * n) - cc - ce ;

    double xc = xc + dxc ;
    if (xc < 0) xc = 0 ;
    double xe = xe + dxe ;
    if (xe < 0) xe = 0 ;
    double n = n + dn ;
    if (n < 0) n = 0 ;
    double w = w + dw ;
    if (w < 0) w = 0 ;

    //ajout des valeurs à ma strucutre n°i+1
    params_i2 -> xc = xc ;
    params_i2 -> xe = xe ;
    params_i2 -> n = n ;
    params_i2 -> w = w ;

}

double findMax(struct Struct_params * params, int t) {
    double mx = 0 ;
    for (int i = 0; i < t; i++) {
        double val = params[i].xc ;
        mx = max(mx, val);
    }
    return mx ;
}

void run_auto(struct Struct_params * params, struct Struct_vari * vari, int t) {

    for (int i = 0 ; i < t-1 ; i++) {
        update(&params[i], &vari, &params[i+1]) ;
    }

    //normalisation
    double mx_XC = findMax(&params, t) ; //ajouter variable pour trouver max
    double mx_XE = findMax(&params, t) ;
    double mx_N = findMax(&params, t) ;
    double mx_W = findMax(&params, t) ;

    for (int i = 0 ; i < t ; i++) {
        params[i].xc = (params[i].xc / mx_XC) ;
        params[i].xe = (params[i].xe / mx_XE) ;
        params[i].n = (params[i].n / mx_N) ;
        params[i].w = (params[i].w / mx_W) ;

    }
}

void finalfile(struct Struct_params * params, struct Struct_vari * vari, int t) {
//create file containing all datas

//    ameliorate file name

    FILE *fp;
    fp = fopen("file_name", "w");

    for (int i = 0 ; i < t ; i++) {
        fwrite(&params[i], sizeof(params[i]), 1, fp);
    }

    fclose(fp) ;

    // envoyer le file à python pour modélisation --> appeler python file

}

void runge_kutta4(struct Struct_params * params, struct Struct_vari * vari, int t) {

    double h ;
    double k1_xc ;
    double k2_xc ;
    double k3_xc ;
    double k4_xc ;

    for (int i = 0 ; i < t ; i++) {

        // double xc = params[i].xc ;
        // double xe = params[i].xe ;
        // double n = params[i].n ;
        // double w = params[i].w ;

        k1_xc = f_xc(i, params[i].xc) ;
        k2_xc = f_xc(i + h/2, params[i].xc + h/2*k1_xc) ;
        k3_xc = f_xc(i + h/2, params[i].xc + h/2*k2_xc) ;
        k4_xc = f_xc(i + h, params[i].xc + h*k3_xc) ;

        params[i].xc = params[i].xc + h/6 * (k1_xc + 2*k2_xc + 2*k3_xc + k4_xc) ;
    }
}

double f_xc(t,xc) {

    double wth = (r * xc) + (k * r * xe) ;
    xc * (bc - (am + max(0,1-min(1,w/wth))(aM-am))) ;
}


int main(int argc, char const *argv[])
{
    struct Struct_params params[1500] ;//= tableau de 1500 structures de types struct_params
    struct Struct_vari vari ; //1 seule car les variables ne changent pas

    return 0;
}
