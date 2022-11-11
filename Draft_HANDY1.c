#include <stdio.h>

#define MAX 16

int main (void){
    FILE *file;
    int primNum;
    int secNum;
    int listOfNumers[16];
    int numberOfLines = MAX;
    int i = 0;

    file = fopen("file.txt", "rt");

    fscanf(file, "%*f;%*c;%d;%s", &myInt, myString);

    if (file == NULL)
    {
        printf("Error\n");
        return 1;
    }

    fscanf(file, "%d %d\n", &primNum, &secNum);

    printf("\n1st Number: %d",primNum);
    printf("\n2nd Number: %d",secNum);

    printf("List of Numbers");

    for(i=0;i<numberOfLines;i++){
        //Count the number from the second line onwards
    }

    fclose(file);
    return 0;
}  

struct Variables {
    double xc; //commoners population
    double xe; //elites population
    double y; //nature 
    double w; //wealth 
};

struct Parameters {
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
