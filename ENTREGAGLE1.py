class CajeroAutomatico:
    def __init__(self):
        self.saldo = 0
        self.billetes = [200, 100, 50, 20, 10, 5, 1]  # Denominaciones de billetes en soles

    def consultar_saldo(self):
        print(f"Saldo actual: ${self.saldo:.2f}")

    def depositar_dinero(self, monto):
        if monto > 0:
            self.saldo += monto
            print(f"Has depositado S/{monto:.2f}.")
        else:
            print("El monto a depositar debe ser mayor que cero.")

    def retirar_dinero(self, monto):
        if monto > 0:
            if monto <= self.saldo:
                self.saldo -= monto
                self._entregar_billetes(monto)
            else:
                print("Fondos insuficientes.")
        else:
            print("El monto a retirar debe ser mayor que cero.")

    def _entregar_billetes(self, monto):
        print(f"Retirando ${monto:.2f}:")
        for billete in self.billetes:
            if monto >= billete:
                cantidad = monto // billete
                monto -= cantidad * billete
                print(f"{cantidad} billete(s) de ${billete}")
        if monto > 0:
            print("No se pudo entregar la cantidad exacta con los billetes disponibles.")

def procesar_monto(entrada):
    if entrada.startswith('$'):
        try:
            monto = float(entrada[1:].replace(',', ''))
            return monto
        except ValueError:
            print("Formato de monto inválido. Asegúrate de ingresar un número válido después del símbolo '$'.")
            return None
    else:
        print("Debes ingresar el monto con el símbolo '$'.")
        return None

def main():
    cajero = CajeroAutomatico()

    while True:
        print("\n--- Cajero Automático ---")
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Salir")

        opcion = input("Selecciona una opción (1-4): ")

        if opcion == '1':
            cajero.consultar_saldo()
        elif opcion == '2':
            entrada = input("Introduce el monto a depositar en soles (ej. $1000): ")
            monto = procesar_monto(entrada)
            if monto is not None:
                cajero.depositar_dinero(monto)
        elif opcion == '3':
            entrada = input("Introduce el monto a retirar en soles (ej. 4500): ")
            monto = procesar_monto(entrada)
            if monto is not None:
                cajero.retirar_dinero(monto)
        elif opcion == '4':
            print("Gracias por usar el cajero automático. ¡Adiós!")
            break
        else:
            print("Opción no válida. Por favor, elige una opción entre 1 y 4.")

if __name__ == "__main__":
    main()
