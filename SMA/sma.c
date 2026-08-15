#include <stdio.h>
#include <stdlib.h>

double *calculate_sma(double *hist_ceny, int pocet, int vel_okna) {
        if (pocet < vel_okna || vel_okna <= 0) {
                return NULL;
        }
        
        int pocet_vysledkov = pocet - vel_okna + 1;
        double *pole_vys = malloc(pocet_vysledkov * sizeof(double));
        
        if (pole_vys == NULL) {
                return NULL;
        }
        
        for (int i = 0; i < pocet_vysledkov; i++) {
                double suma = 0.0;
                for (int j = 0; j < vel_okna; j++) {
                        suma += hist_ceny[i + j];
                }
                pole_vys[i] = suma / vel_okna; 
        }

        return pole_vys;
}
void free_sma_memory(double *ptr) {
    if (ptr != NULL) {
        free(ptr);
    }
}
