
class email:
    
    __idcuenta = str
    __dominio = str
    __tipodominio = str
    __password = str

    def __init__(self, idcuenta , dom , tipodom , password):
        self.__idcuenta = idcuenta
        self.__dominio = dom
        self.__tipodominio = tipodom
        self.__password = password
    def returnemail(self):
        return self.__idcuenta +'@'+self.__dominio+'.'+self.__tipodominio # type: ignore
    
    def getdominio(self):
        return self.__dominio
    
    def cambiarcontrasenia(self, password):
        if self.__password == password:
            print("Son iguales")
        else:

            self.__password = password
            print("Cambio exitoso!")
    def crearcuenta(self,correo):
        if correo.find('@') != -1:
            aux1 = email.__idcuenta.split('@') 
            auxidcuenta = aux1[0]
            if correo.find('.') != -1:
                aux = email.__dominio.split ('.')
                auxdominio = correo
                auxtipodominio = correo
                self.__idcuenta = auxidcuenta
                self.__dominio = auxdominio
                self.__tipodominio = auxidcuenta
                self.__init__(aux1,aux,auxdominio,auxtipodominio)
                print("Cuenta de correo crearda con exito!")
            else: print("Error :/ Falta el punto en el dominio")
        else: print("Error :/ Falta @ en el correo")