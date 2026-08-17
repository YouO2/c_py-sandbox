#include <stdio.h>
#include <stdlib.h>

typedef struct {
	double open;
	double high;
	double low;
	double close;
} Candle; 

Candle *aggregate_ticks( double *ceny, int pocet) {
	if ( pocet <= 0){
		return NULL;
	}
	Candle *vysledok =malloc(sizeof(Candle));
	if (vysledok == NULL){
		return NULL;
	}
	vysledok->open = ceny[0];
	vysledok->close = ceny[pocet - 1 ];
	vysledok->high = ceny[0];
	vysledok->low = ceny[0];
	for (int i =0; i< pocet; i++){
		if (ceny[i] > vysledok-> high){
			vysledok->high = ceny[i];
		}
		if (ceny[i] < vysledok->low){
			vysledok->low = ceny[i];
		}
	}
	return vysledok;
}

void free_candle_memory(Candle *ptr) {
    if (ptr != NULL) {
        free(ptr);
    }
}
