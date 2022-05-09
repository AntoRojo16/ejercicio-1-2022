from Email import Email
from ManejadorEmail import Manejador
def mostrarMensaje(nom, email):
    print("Estimado " +nom+" enviaremos sus mensajes a "+ email.metodoRetornaEmail())
def crearCuentaNueva(nuevoEmail):
    correo=input("Ingrese una nueva direccion de correo electronico")
    nuevoEmail.crearCuenta(correo)

def prueba ():
    print("1- Ingresar el nombre de una persona y de su cuenta de correo, el identificador de cuenta,\n dominio y tipo de dominio  y luego imprima un mensaje")
    nombre=str(input("Ingrese su nombre "))
    id=input("Ingresar ID de correo")
    dominio=input("Ingrese dominio de la cuenta")
    tipo=input("Ingrese el tipo de dominio")
    contr=input("Ingrese la contraseña")
    otroEmail=Email()
    otroEmail.inicalizar(id,dominio,tipo,contr)
    mostrarMensaje(nombre,otroEmail)
    print("2- Modificar la contraseña del item anterior")
    otroEmail.modificarContraseña()
    print("3- Crear un objeto de clase Email, a partir de una dirección de correo")
    nuevoEmail=Email()
    crearCuentaNueva(nuevoEmail)
    print("Se creo la cuenta")
    print("4- Leer de un archivo separado por comas 10 direcciones de e-mail")
    unaLista=Manejador()
    unaLista.listarLibros()
    unaLista.mostrar()
    print("Ingresar un identificador de cuenta e indicar si está repetido o no")
    iden=input("ingrese indentidicador de email")
    unaLista.buscarIdentificador(iden)
if __name__ == '__main__':
    prueba()
