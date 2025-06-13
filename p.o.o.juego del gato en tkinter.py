import tkinter as tk
from tkinter import messagebox

class Gato:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Juego Gato (Tres en línea)")
        self.turno = "X"
        self.botones = [[None for _ in range(3)] for _ in range(3)]
        self.crear_tablero()

    def crear_tablero(self):
        self.ventana.configure(bg="light purple")
        for fila in range(3):
            for columna in range(3):
                boton = tk.Button(
                    self.ventana, text="", font=('Arial', 40), width=5, height=2,
                    bg="light purple", activebackground="purple",
                    command=lambda f=fila, c=columna: self.jugada(f, c)
                )
                boton.grid(row=fila, column=columna, padx=5, pady=5)
                self.botones[fila][columna] = boton

    def jugada(self, fila, columna):
        boton = self.botones[fila][columna]
        if boton["text"] == "":
            boton["text"] = self.turno
            if self.verificar_ganador():
                messagebox.showinfo("Fin del juego", f"¡El jugador {self.turno} gana!")
                self.reiniciar_juego()
            elif self.esta_empate():
                messagebox.showinfo("Fin del juego", "¡Empate!")
                self.reiniciar_juego()
            else:
                self.turno = "O" if self.turno == "X" else "X"

    def verificar_ganador(self):
        for i in range(3):
            if self.botones[i][0]["text"] == self.botones[i][1]["text"] == self.botones[i][2]["text"] != "":
                return True
            if self.botones[0][i]["text"] == self.botones[1][i]["text"] == self.botones[2][i]["text"] != "":
                return True

        if self.botones[0][0]["text"] == self.botones[1][1]["text"] == self.botones[2][2]["text"] != "":
            return True
        if self.botones[0][2]["text"] == self.botones[1][1]["text"] == self.botones[2][0]["text"] != "":
            return True

        return False

    def esta_empate(self):
        for fila in self.botones:
            for boton in fila:
                if boton["text"] == "":
                    return False
        return True

    def reiniciar_juego(self):
        for fila in self.botones:
            for boton in fila:
                boton["text"] = ""
        self.turno = "X"

    def iniciar(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    juego = Gato()
    juego.iniciar()
