// Notre fichier calculs de HANDY

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

struct Struct_vari {
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
    double t ;
} ;

// struct Data {
//     char name ;
//     double value ;
// }

void readfile(char * FileName, struct Struct_params * tableparams, struct Struct_vari * tablevari, int size) {

// Ouvrir le fichier
    FILE * file = fopen(FileName, "r"); // pointer
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

        if (n == 4) tableparams->am ;
        if (n == 5) tableparams->aM ;
        if (n == 6) tableparams->bc ;
        if (n == 7) tableparams->be ;
        if (n == 8) tableparams->g ;
        if (n == 9) tableparams->l ; 
        if (n == 10) tableparams->s ;
        if (n == 11) tableparams->d;
        if (n == 12) tableparams->k ;
        if (n == 13) tableparams->r ;
        if (n == 14) tableparams->t ;

        n = n + 1; // if ok is 1
        
        if (n>size) break ; // ici, size=15
    }
    fclose(file);
}


void euler(struct Struct_vari * vari_i, struct Struct_params * params, struct Struct_vari * vari_i2) {

// possible avec boucle for pour les variables
    // for (int i=0 ; i<10 ; i++) {
    //     double Data[i].name = Data[i].value ;
    // }

    double xc = vari_i->xc ;
    double xe = vari_i->xe ;
    double n = vari_i->n ;
    double w = vari_i->w ;

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
    vari_i2 -> xc = xc ;
    vari_i2 -> xe = xe ;
    vari_i2 -> n = n ;
    vari_i2 -> w = w ;

}

double findMax_xc(struct Struct_vari * vari, int t) {

    double mx = 0 ;

    for (int i = 0; i < t; i++) {
        double val = vari[i].xc ;
        mx = max(mx, val);

    }
    return mx ;
}
// faire les trois autres find max
void run_auto(struct Struct_params * params, struct Struct_vari * vari, int t) {

    for (int i = 0 ; i < t-1 ; i++) {
        euler(&vari[i], &params, &vari[i+1]) ;
    }
    char * xc = "xc" ;
    char * xe = "xe" ;
    char * n = "n" ;
    char * w = "w" ;

    //normalisation
    double mx_XC = findMax(&vari, t, &xc) ; //ajouter variable pour trouver max
    double mx_XE = findMax(&vari, t) ;
    double mx_N = findMax(&vari, t) ;
    double mx_W = findMax(&vari, t) ;

    for (int i = 0 ; i < t ; i++) {
        vari[i].xc = (vari[i].xc / mx_XC) ;
        vari[i].xe = (vari[i].xe / mx_XE) ;
        vari[i].n = (vari[i].n / mx_N) ;
        vari[i].w = (vari[i].w / mx_W) ;
    }
}

void finalfile(char * FileName, struct Struct_params * params, struct Struct_vari * vari, int t) {
//create file containing all datas to send to python (une variable par colonne)

//    ameliorate file name (le mettre en argument)

    FILE *fp;
    fp = fopen(FileName, "w");

    for (int i = 0 ; i < t ; i++) {
        fwrite(&vari[i], sizeof(vari[i]), 1, fp);
    }

    fclose(fp) ;

    // envoyer le file à python pour modélisation --> appeler python file

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


int main(int argc, char const *argv[])
{

    struct Struct_vari vari[1500] ;// = tableau de 1500 structures de types struct_vari
    struct Struct_params params ; //1 seule car les variables ne changent pas
    int t = 1000 ;

    finalfile("data_file_to_python.txt", vari, &params, t);
    return 0;
}
