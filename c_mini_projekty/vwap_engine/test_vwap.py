import os
import ctypes

current_dir = os.path.dirname(os.path.abspath(__file__))
lib = ctypes.CDLL(os.path.join(current_dir, 'libvwap.so'))


lib.calculate_vwap.argtypes= [
	ctypes.POINTER(ctypes.c_double),
	ctypes.POINTER(ctypes.c_double),
	ctypes.c_int
]
lib.calculate_vwap.restype = ctypes.POINTER(ctypes.c_double)

lib.free_vwap_memory.argtypes = [ ctypes.POINTER(ctypes.c_double)
]
lib.free_vwap_memory.restype = None


if __name__=='__main__':
	ceny=[51.0,87.4,93.0,12.0,71.0]
	objemy=[100,547,2810,666,123]
	pocet=len(ceny)
	
	c_ceny_pole= (ctypes.c_double * pocet)(*ceny)
	c_objemy_pole= (ctypes.c_double * pocet)(*objemy)
	vysledok_ptr= lib.calculate_vwap( c_ceny_pole, c_objemy_pole, pocet)
	if vysledok_ptr:
		for i in range(pocet):
            		print(f"Tick {i+1} | Cena: {ceny[i]:.1f} | Objem: {objemy[i]} | VWAP: {vysledok_ptr[i]:.2f}")
		lib.free_vwap_memory(vysledok_ptr)
		print("\nPamäť bola bezpečne uvoľnená.")
	else:
		print("Chyba: C-čko vrátilo NULL pointer.")
	
