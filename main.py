from nicegui import ui
#Funciones
def sumar():
    try:
        n1 = float(num1.value)
        n2 = float(num2.value)
        res = n1 + n2
        resultado.set_text(f'Resultado: {res}')
    except ValueError:
        resultado.set_text('Error: Por favor ingrese números válidos.')

def restar():
    try:
        n1 = float(num1.value)
        n2 = float(num2.value)
        res = n1 - n2
        resultado.set_text(f'Resultado: {res}')
    except ValueError:
        resultado.set_text('Error: Por favor ingrese números válidos.')

def multiplicar():
    try:
        n1 = float(num1.value)
        n2 = float(num2.value)
        res = n1 * n2
        resultado.set_text(f'Resultado: {res}')
    except ValueError:
        resultado.set_text('Error: Por favor ingrese números válidos.')


def dividir():
    try:
        n1 = float(num1.value)
        n2 = float(num2.value)
        if n2 == 0:
            resultado.set_text('Error: División por cero no permitida.')
        else:
            res = n1 / n2
            resultado.set_text(f'Resultado: {res}')
    except ValueError:
        resultado.set_text('Error: Por favor ingrese números válidos.')


#Estructura de la interfaz de usuario
with ui.card().classes('w-full max-w-md mx-auto mt-10 p-6'):
    ui.label('Calculadora').classes('fontserif w-full text-center')
    num1 = ui.input('Número 1').classes('w-full mb-4')
    num2 = ui.input('Número 2').classes('w-full mb-4')
    bt_sumar = ui.button('Sumar').classes('w-full mb-4').on('click', sumar)
    bt_restar = ui.button('Restar').classes('w-full mb-4').on('click', restar)
    bt_multiplicar = ui.button('Multiplicar').classes('w-full mb-4').on('click', multiplicar)
    bt_dividir = ui.button('Dividir').classes('w-full mb-4').on('click', dividir)
    resultado = ui.label('Resultado: ').classes('fontserif w-full text-center')


ui.run()