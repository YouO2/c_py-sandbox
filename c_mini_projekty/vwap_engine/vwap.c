#include <stdio.h>
#include <stdlib.h>

double *calculate_vwap(double *ceny, double *objemy, int pocet){ 
        if (pocet <= 0) {
                return NULL;
        } 
        double *vysledok = malloc(pocet * sizeof(double));
        
        if (vysledok == NULL) {
                return NULL;
        }

        double suma_cena_krat_objem = 0.0;
        double suma_objemov = 0.0;
        
        for  (int i= 0; i < pocet; i++){
                suma_objemov += objemy[i];
                
                if (suma_objemov == 0){
                        free(vysledok);
                        return NULL; 
                }
                
                suma_cena_krat_objem += (ceny[i] * objemy[i]);
                vysledok[i] = (suma_cena_krat_objem / suma_objemov);
        }
        return vysledok;
}

void free_vwap_memory(double *ptr){
        if (ptr != NULL) {
                free(ptr);
        }
}
