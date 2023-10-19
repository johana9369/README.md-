import readchar
key = readchar.readkey()  
from readchar import readkey,key 
input_str = ""
while True:
    k = readkey() 
    print("Tecla presionada. Saliendo del bucle.", k)
    (input_str) += k
    if k == key.UP: 
     break   