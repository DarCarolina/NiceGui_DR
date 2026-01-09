from nicegui import ui
#Funciones

#Estructura de la interfaz de usuario
with ui.card().classes('w-full max-w-md mx-auto mt-10 p-6'):
    ui.label('Hola, Mundo!').classes('fontserif')

ui.run()