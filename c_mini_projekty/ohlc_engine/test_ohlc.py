import os
import ctypes

class Candle(ctypes.Structure):
    _fields_ = [
        ("open", ctypes.c_double),
        ("high", ctypes.c_double),
        ("low", ctypes.c_double),
        ("close", ctypes.c_double)
    ]

current_dir = os.path.dirname(os.path.abspath(__file__))
lib = ctypes.CDLL(os.path.join(current_dir, 'libohlc.so'))

# Nastavenie tlmočníka
lib.aggregate_ticks.argtypes = [
    ctypes.POINTER(ctypes.c_double), 
    ctypes.c_int                     
]
lib.aggregate_ticks.restype = ctypes.POINTER(Candle)

lib.free_candle_memory.argtypes = [ctypes.POINTER(Candle)]
lib.free_candle_memory.restype = None

if __name__ == "__main__":
    ceny = [20.0, 51.0, -5.0, 26.0, 80.0, -40.0, 40.0]
    pocet = len(ceny)
    
    # Preklad do C poľa
    c_ceny_pole = (ctypes.c_double * pocet)(*ceny)
    
    # Volanie C enginu
    vysledok_ptr = lib.aggregate_ticks(c_ceny_pole, pocet)
    
    if vysledok_ptr:
        print("Sviečka úspešne vygenerovaná z C-Enginu:")
        print(f"Open cena:  {vysledok_ptr.contents.open}") 
        print(f"High cena:  {vysledok_ptr.contents.high}")
        print(f"Low cena:   {vysledok_ptr.contents.low}")
        print(f"Close cena: {vysledok_ptr.contents.close}")
        
        # UPRATANIE PAMÄTE (Memory Management)
        lib.free_candle_memory(vysledok_ptr)
        print("\nPamäť bola bezpečne uvoľnená.")
    else:
        print("Chyba: C-čko vrátilo NULL pointer.")
