class Gato:
    def __init__(self):
        self.tablero = [[" " for _ in range(3)] for _ in range(3)]
        self.turno = "X"

    def mostrar_tablero(self):
        print("\n")
        for fila in self.tablero:
            print(" | ".join(fila))
            print("-" * 9)

    def realizar_jugada(self, fila, columna):
        if self.tablero[fila][columna] == " ":
            self.tablero[fila][columna] = self.turno
            return True
        else:
            print("Casilla ocupada. Intenta otra vez.")
            return False

    def verificar_ganador(self):
       
        for i in range(3):
            if self.tablero[i][0] == self.tablero[i][1] == self.tablero[i][2] != " ":
                return True
            if self.tablero[0][i] == self.tablero[1][i] == self.tablero[2][i] != " ":
                return True

        
        if self.tablero[0][0] == self.tablero[1][1] == self.tablero[2][2] != " ":
            return True
        if self.tablero[0][2] == self.tablero[1][1] == self.tablero[2][0] != " ":
            return True

        return False

    def es_empate(self):
        for fila in self.tablero:
            if " " in fila:
                return False
        return True

    def cambiar_turno(self):
        self.turno = "O" if self.turno == "X" else "X"

    def jugar(self):
        print("¡Bienvenido al juego Gato!")
        while True:
            self.mostrar_tablero()
            print(f"Turno de {self.turno}")
            try:
                fila = int(input("Fila (0-2): "))
                columna = int(input("Columna (0-2): "))
                if fila not in range(3) or columna not in range(3):
                    print("Coordenadas fuera de rango. Intenta de nuevo.")
                    continue
            except ValueError:
                print("Entrada inválida. Usa números del 0 al 2.")
                continue

            if self.realizar_jugada(fila, columna):
                if self.verificar_ganador():
                    self.mostrar_tablero()
                    print(f"¡El jugador {self.turno} gana!")
                    break
                elif self.es_empate():
                    self.mostrar_tablero()
                    print("¡Empate!")
                    break
                else:
                    self.cambiar_turno()



if __name__ == "__main__":
    juego = Gato()
    juego.jugar()
 