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


#Estructura de la interfaz de usuario en un contendedor tipo tarjeta
with ui.card().classes('w-full max-w-md mx-auto mt-10 p-6'):
    ui.label('Calculadora').classes('fontserif w-full text-center')
    with ui.column().classes('w-full'):
        num1 = ui.input('Número 1').classes('w-full mb-4')
        num2 = ui.input('Número 2').classes('w-full mb-4')
    with ui.row().classes('w-full mt-4 gap-2'): 
        bt_sumar = ui.button('Sumar').classes('bg-blue-500 text-white flex-1').on('click', sumar)
        bt_restar = ui.button('Restar').classes('bg-green-500 text-white flex-1').on('click', restar)
    with ui.row().classes('w-full mt-4 gap-2'):
        bt_multiplicar = ui.button('Multiplicar').classes('bg-yellow-500 text-white flex-1').on('click', multiplicar)
        bt_dividir = ui.button('Dividir').classes('bg-purple-500 text-white flex-1').on('click', dividir)
    resultado = ui.label('Resultado: ').classes('fontserif w-full text-center')


ui.run()