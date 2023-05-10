
import turtle

# Configuración de la ventana
turtle.setup(width=800, height=600)
window = turtle.Screen()
window.bgcolor("white")

# Creación de la tortuga para dibujar
tortuga = turtle.Turtle()
tortuga.shape("turtle")
tortuga.speed(2)

# Configuración de los colores
colores = ["blue", "gray", "white"]

# Dibujar el logo
tortuga.penup()
tortuga.goto(-100, 0)
tortuga.pendown()

for i in range(2):
    tortuga.color(colores[i % 3])
    tortuga.pensize(5)
    tortuga.forward(200)
    tortuga.right(90)
    tortuga.forward(100)
    tortuga.right(90)

# Escribir el texto del logo
tortuga.penup()
tortuga.goto(-80, -40)
tortuga.pendown()
tortuga.color(colores[2])
tortuga.write("E'GRUP", align="left", font=("Arial", 24, "bold"))
tortuga.penup()
tortuga.goto(-40, -80)
tortuga.pendown()
tortuga.write("Consultoría e", align="left", font=("Arial", 18))
tortuga.penup()
tortuga.goto(-30, -110)
tortuga.pendown()
tortuga.write("Ingeniería Ltda.", align="left", font=("Arial", 18))

# Finalizar el dibujo
turtle.done()
