import ctypes
import os

# Ceste ku kniznici
current_dir = os.path.dirname(os.path.abspath(__file__))
lib = ctypes.CDLL(os.path.join(current_dir, 'libsma.so'))

# 2. Nastavenie "tlmočníka" (Typing)
# aké typy premenných C-čková funkcia čaká
lib.calculate_sma.argtypes = [
    ctypes.POINTER(ctypes.c_double), # Pointer na pole historických cien
    ctypes.c_int,                    # Počet cien
    ctypes.c_int                     # Veľkosť okna
]
lib.free_sma_memory.argtypes = [ctypes.POINTER(ctypes.c_double)]
lib.free_sma_memory.restype = None

#  čo funkcia vráti 
lib.calculate_sma.restype = ctypes.POINTER(ctypes.c_double)


if __name__ == "__main__":
    # 3. Dáta 
    ceny = [10.0, 11.0, 12.0, 13.0, 14.0]
    pocet = len(ceny)
    okno = 3
    
    print(f"Vstupné ceny: {ceny}")
    
    # 4. Preklad Python Listu na surové C pole
    # Vytvoríme typ poľa a hneď doňho "rozbalíme" ceny 
    c_ceny_pole = (ctypes.c_double * pocet)(*ceny)
    
    # 5. Volanie C funkcie.
    vysledok_ptr = lib.calculate_sma(c_ceny_pole, pocet, okno)
    
    if vysledok_ptr:
        pocet_vysledkov = pocet - okno + 1
        print("\nVypočítané kĺzavé priemery:")
        
        # 6. Čítanie hodnôt z Heapu 
        for i in range(pocet_vysledkov):
            print(f"SMA[{i}]: {vysledok_ptr[i]}")
	
	lib.free_sma_memory(vysledok_ptr)
        print("Pamäť v C-čku bola úspešne uvoľnená!")            
    else:
        print("C-čko vrátilo NULL pointer - niekde nastala chyba v parametroch.")
