#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

struct GpsPoint {
    double latitude ;
    double longitude ;
    double altitude ;
} ;

struct Coord {
    double x ;
    double y ; 
    double z ;
} ;

void afficher(struct GpsPoint * point) { //-> (* et &) sinon . (sans * ni & mais creer une copie)
    printf("Latitude : %0.4f °\nLongitude : %0.4f °\nAltitude : %0.0f m\n", point->latitude, point->longitude, point->altitude);
} ;

int lireLigne(char * ligne, struct GpsPoint * point) {

    char * virg_1 = strchr(ligne, ',') ;
    char * virg_2 = strchr(virg_1 + 1, ',') ; 

    double gps[3] ; //pour stocker les chiffres
    double nbr_1 = atof(ligne) ;
    double nbr_2 = atof(virg_1 + 1) ;
    double nbr_3 = atof(virg_2 + 1) ;

    char zero = '0' ;

    if (nbr_1 != 0) gps[0] = nbr_1 ; //si c'est un chiffre
    else if (*ligne == zero) gps[0] = nbr_1 ; 
    else return 0 ;

    if (nbr_2 != 0) gps[1] = nbr_2 ; 
    else if (*(virg_1 + 1) == zero) gps[1] = nbr_2  ;
    else return 0 ;

    if (nbr_3 != 0) gps[2] = nbr_3 ; 
    else if (*(virg_2 + 1) == zero) gps[2] = nbr_3 ;
    else return 0 ;

//    struct GpsPoint point_checked = {gps[0], gps[1], gps[2]} ;
    // afficher(&point_checked) ;

    point->latitude = gps[0] ;
    point->longitude = gps [1];
    point->altitude = gps[2];
    return 1 ;

}

int lireFichier(char * nomFichier, struct GpsPoint * tableauARemplir, int longueur) {
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
    return n;  // nombre de lignes ok pour coordonnées
}

void afficher_points(struct GpsPoint * gps_struct) {
    // recuperer gps_struct = tableau de struct de 0 à 9
    for (int i=0 ; i<10 ; i++) {
        printf("Point n°%d\nLatitude : %0.0f °\nLongitude : %0.0f °\nAltitude : %0.0f m\n",i, gps_struct[i].latitude, gps_struct[i].longitude, gps_struct[i].altitude) ;
    }
}

void diff_alt(struct GpsPoint * gps_struct, int n) { //n = longueur tableau = nbr_points
    double diff = gps_struct[n-1].altitude - gps_struct[0].altitude ;
    printf("Différence altitude:%f", diff) ;
}

void montee(struct GpsPoint * gps_struct, int n) {
    int montee = 0 ;
    for (int i=0 ; i<n ; i++) {
        int diff_alt = gps_struct[i+1].altitude - gps_struct[i].altitude ;
        if (diff_alt > 0) montee += diff_alt ;
    }
    printf("Montée totale : %d\n", montee) ;
}

void conversion_xyz(struct GpsPoint * gps_struct, struct Coord * coord_struct, int n) {
    int r = 6378100 ;
    for (int i=0 ; i<n ; i++) {
        double lat_rad = gps_struct[i].latitude * M_PI / 180 ;
        double long_rad = gps_struct[i].longitude * M_PI / 180 ;
        double x_c = (r+gps_struct[i].altitude)*cos(lat_rad)*cos(long_rad) ;
        double y_c = (r+gps_struct[i].altitude)*cos(lat_rad)*sin(long_rad) ;
        double z_c = (r+gps_struct[i].altitude)*sin(lat_rad) ;



        //struct Coord * coords = coord_struct + i ;
        coord_struct[i].x = x_c ;
        (*(coord_struct + i)).y = y_c ;
        (coord_struct + i)->z = z_c ;
    }  //coord stockées dans tableau de structures
}

void distance_tot(struct Coord * coord_struct, int n) {
    double distance_tot = 0 ;
    for (int i=0 ; i<n ; i++) {
        double norme = sqrt(pow(coord_struct[i+1].x-coord_struct[i].x, 2)+pow(coord_struct[i+1].y-coord_struct[i].y, 2)+ pow(coord_struct[i+1].z-coord_struct[i].z, 2)) ;
        distance_tot += norme ;
    }
    printf("Distance totale : %0.4f km\n", distance_tot/pow(10,3)) ;
}

void pente_max(struct GpsPoint * gps_struct, struct Coord * coord_struct, int n) {
    double pente_max = 0 ;
    double alt = 0 ;
    double dist = 0 ;
    for (int i=0 ; i<n ; i++) {
        double diff_alt = fabs(gps_struct[i+1].altitude - gps_struct[i].altitude) ;
        alt = diff_alt ;
        double norme = sqrt(pow(coord_struct[i+1].x-coord_struct[i].x, 2)+pow(coord_struct[i+1].y-coord_struct[i].y, 2)+ pow(coord_struct[i+1].z-coord_struct[i].z, 2)) ;
        dist = norme ;
        if (alt/dist > pente_max) pente_max = alt/dist ;
    }
    printf("Pente max : %0.0f pourcent\n", pente_max*100) ;
}

int main(int argc, char * argv[]) {

    //struct GpsPoint point = {45.97639, 7.65833, 4478};
    // afficher(&point) ;

    // struct GpsPoint point ;
    // printf("%d\n", lireLigne("46.878787,6.8776,1117.0", &point)) ;

    struct GpsPoint gps_structs[1000];
    int nbPoints = lireFichier("creux-du-van.csv", gps_structs, 1000);
    // montee(gps_structs, nbPoints) ;
    struct Coord coord_structs[1000] ;
    conversion_xyz(gps_structs, coord_structs, nbPoints) ;
    //distance_tot(coord_structs, nbPoints) ;
    //pente_max(gps_structs, coord_structs, nbPoints) ;

    return 0 ;

}