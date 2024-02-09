print(' ---- Anagrama? ----')
def esAnagrama(palabra_uno, palabra_dos):
    palabra_tres = palabra_uno[::-1]
    print(f"Las palabras {palabra_uno} y {palabra_dos} son anagramas ((({palabra_dos == palabra_tres})))")
print('\n')

esAnagrama("amor", "roca") #amor