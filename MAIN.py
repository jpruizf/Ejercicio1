from claseemail import email

if __name__ == '__main__':
    idcuenta = input("Ingrese nombre de cuenta(ejemplo@):")
    dom = input("Ingrese dominio(gmail.outlook.yahoo):")
    tipodom = input("Ingrese tipo de dominio(org,com,ar):")
    password = input("Ingrese una contraseña:")
    nuevo = email(idcuenta,dom,tipodom,password)
    print(nuevo.crearcuenta("juanpablo@gmail.com"))
    print(nuevo.crearcuenta("juanpablogmail.com"))
    print(nuevo.crearcuenta("@gmail.com"))
    print(nuevo.crearcuenta("@"))
    print(nuevo.crearcuenta("juanpablo@"))
    print(nuevo.crearcuenta("juanpablo@gmail"))
    print(nuevo.crearcuenta("gmail.com"))
    nuevacontrasenia = input("Ingrese contraseña")
    nuevo.cambiarcontrasenia(nuevacontrasenia)