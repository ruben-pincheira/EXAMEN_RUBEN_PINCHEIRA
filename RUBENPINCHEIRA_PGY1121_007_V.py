import datetime

class Departamento:
    def __init__(self, numero, piso, tipo, precio):
        self.numero = numero
        self.piso = piso
        self.tipo = tipo
        self.precio = precio
        self.vendido = False
        self.comprador = None

class CasaFeliz:
    def __init__(self):
        self.departamentos = []
        self.piso = 10
        self.depa = 4
        self.tipos = {"A": "3.800 UF", "B": "3.000 UF", "C": "2.800 UF", "D": "3.500 UF"}
        self.matriz_departamentos = [["" for _ in range(self.depa + 1)] for _ in range(self.piso + 1)]

        for p in range(1, self.piso + 1):
            for d in range(1, self.depa + 1):
                tipo = ""
                if d == 1:
                    tipo = "A"
                elif d == 2:
                    tipo = "B"
                elif d == 3:
                    tipo = "C"
                elif d == 4:
                    tipo = "D"
                precio = self.tipos[tipo]
                self.departamentos.append(Departamento(d, p, tipo, precio))
                self.matriz_departamentos[p][d] = tipo

        self.compradores = []
        self.ganancias_totales = 0

    def mostrar_menu(self):
        print("Hola Bienvenido a la Inmobiliaria Casa Feliz")
        print("A continuación te dejaremos un menú para que elijas tu departamento")
        #menu
        print("---- MENÚ ----")
        print("1. Comprar departamento")
        print("2. Mostrar departamentos disponibles")
        print("3. Ver listado de compradores")
        print("4. Mostrar ganancias totales")
        print("5. Salir")

    def comprar_departamento(self):
        piso = int(input("Ingrese el número de piso del 1 al 10: "))
        if not 1 <= piso <= 10:
            print("El número de piso ingresado no es válido.")
            return
        
        tipo = input("Ingrese el tipo de departamento (SOLO LETRAS MAYUSCULAS) (A, B, C, D): ")
        departamento = self.buscar_departamento_disponible(piso, tipo)
        
        if departamento is not None:
            if departamento.vendido:
                print("El departamento seleccionado no está disponible.")
                return

            nombre = input("Ingrese su nombre: ")
            apellido = input("Ingrese su apellido: ")
            telefono = input("Ingrese su número de teléfono: ")
            run = input("Ingrese su RUN (sin guiones ni puntos): ")
            if self.validar_run(run):
                departamento.vendido = True
                departamento.comprador = (nombre, apellido, telefono, run)
                self.compradores.append((nombre, apellido, telefono, run, piso, tipo))
                self.ganancias_totales += float(departamento.precio[:-3])
                print("¡Felicitaciones! Departamento comprado con éxito.")
            else:
                print("El RUN ingresado no es válido.")
        else:
            print("Lo sentimos, el departamento que ha escogido ya ha sido comprado. Por favor, intente con otro.")

    def mostrar_departamentos_disponibles(self):
        print("---- DEPARTAMENTOS DISPONIBLES ----")
        print("( Piso | Tipo )")
        for piso in range(1, self.piso + 1):
            row = f"(  {piso}  |"
            for departamento in self.departamentos:
                if departamento.piso == piso and not departamento.vendido:
                    row += f" {departamento.tipo} |"
            row += " )"
            print(row)

    def ver_listado_compradores(self):
        print("---- LISTADO DE COMPRADORES ----")
        compradores_ordenados = sorted(self.compradores, key=lambda x: x[0])
        for comprador in compradores_ordenados:
            nombre, apellido, telefono, run, piso, tipo = comprador
            print(f"Nombre: {nombre} - Apellido: {apellido} - Teléfono: {telefono} - RUN: {run} - Departamento: {tipo}{piso}")

    def mostrar_ganancias_totales(self):
        print(f"Ganancias totales: ${self.ganancias_totales} UF")

    def buscar_departamento_disponible(self, piso, tipo):
        for departamento in self.departamentos:
            if departamento.piso == piso and departamento.tipo == tipo:
                return departamento
        return None

    def validar_run(self, run):
        run = run.replace(".", "").replace("-", "")
        if len(run) != 9 or not run[:-1].isdigit() or (run[-1].lower() != "k" and not run[-1].isdigit()):
            return False
        return True

    def ejecutar(self):
        while True:
            self.mostrar_menu()
            opcion = input("Selecciona una opción: ")
            if opcion == "1":
                self.comprar_departamento()
            elif opcion == "2":
                self.mostrar_departamentos_disponibles()
            elif opcion == "3":
                self.ver_listado_compradores()
            elif opcion == "4":
                self.mostrar_ganancias_totales()
            elif opcion == "5":
                nombre = input("Ingrese su nombre: ")
                apellido = input("Ingrese su apellido: ")
                fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d")
                print(f"¡Muchas gracias por comprar en Inmobiliaria Casa Feliz! Esperamos que disfrute su nueva casa. ¡Hasta luego, {nombre} {apellido}! Fecha de salida: {fecha_actual}")
                break
            else:
                print("Opción inválida. Por favor, ingrese solo números del 1 al 5. Intente nuevamente.")

# Ejemplo de uso
casa_feliz = CasaFeliz()
casa_feliz.ejecutar()
