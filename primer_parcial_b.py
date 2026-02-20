class CuentaBancaria : 
    def __init__(self, titular, numero_cuenta, saldo):
        self.titular = titular
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo
        
    def mostrar_info(self):
        print(f"Titular: {self.titular}")
        print(f"Numero de cuenta: {self.numero_cuenta}")
        print(f"Saldo: {self.saldo}")
        
    def depositar(self, monto):
        self.saldo += monto
        print(f"Se ha depositado ${monto}. Saldo actual: ${self.saldo}")
        
    def retirar(self, monto):
        if self.saldo >= monto:
            self.saldo -= monto
            print(f"Se ha retirado ${monto}. Saldo actual: ${self.saldo}")
        else:
            print("Fondos insuficientes.")

cuentas = []
   
def crear_cuenta():
    titular = input("Ingrese el nombre del titular: ")
    numero_cuenta = input("Ingrese el número de cuenta: ")
    saldo_inicial = float(input("Ingrese el saldo inicial: "))
    nueva_cuenta = CuentaBancaria(titular, numero_cuenta, saldo_inicial)
    cuentas.append(nueva_cuenta)
    print("Cuenta creada exitosamente.")

def mostrar_cuentas():
  for cuenta in cuentas:
    cuenta.mostrar_info()
    print("-" * 30)

def realizar_deposito():
  numero_cuenta = input("Ingrese el numero de cuenta: ")
  cuenta = None
  for c in cuentas:
    if c.numero_cuenta == numero_cuenta:
      cuenta = c
      break
  if cuenta is not None:
    monto = float(input("Ingrese el monto a depositar: "))
    cuenta.depositar(monto)
  else:
    print("Cuenta no encontrada.")

def realizar_retiro():
  numero_cuenta = input("Ingrese el numero de cuenta: ")
  cuenta = None
  for c in cuentas:
    if c.numero_cuenta == numero_cuenta:
      cuenta = c
      break
  if cuenta is not None:
    monto = float(input("Ingrese el monto a retirar: "))
    cuenta.retirar(monto)
  else:
    print("Cuenta no encontrada.")

def mostrar_menu():
    print("===== MENU =====")
    print("1. Crear cuenta")
    print("2. Mostrar cuentas")
    print("3. Depositar dinero")
    print("4. Retirar dinero")
    print("5. Salir")

while True:
    mostrar_menu()
    opcion = input("Elige una opcion: ")
    
    if opcion == "1":
        crear_cuenta()
    elif opcion == "2":
        mostrar_cuentas()
    elif opcion == "3":
        realizar_deposito()
    elif opcion == "4":
        realizar_retiro()
    elif opcion == "5":
        print("Hasta luego")
        break
    else:
        print("Opcion no valida. Por favor, elige una opcion del menu.")