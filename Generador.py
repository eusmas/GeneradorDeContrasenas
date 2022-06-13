import random

def generar_contrasena():
    mayusculas=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","r","s","t","u","v","w","x","y","z"]
    minusculas=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    simbolos=["#","$","%","&","("]
    numeros=["1","2","3","4","5","6","7","8","9","0"]

    caracteres= mayusculas + minusculas + simbolos + numeros

    contrasena=[]

    for i in range(15):
        caracter_random=random.choice(caracteres)   #Escoge de forma aleatorio un pos de la lista random
        contrasena.append(caracter_random)          #agrega a la contaseña el caracter random anterior
    contrasena="".join(contrasena)                  #convierte la lista (contrasena) en string
    return contrasena



def run():
    contrasena=generar_contrasena()
    print("Tu nueva contrasena es: " + contrasena)




if __name__=="__main__":
    run()