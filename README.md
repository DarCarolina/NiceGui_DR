# NiceGui_DR
## main.py
        Indicador: Funcionalidad principal
        Este programa crea una calculadora básica con interfaz gráfica usando NiceGUI, que permite realizar las operaciones de:

        Suma

        Resta

        Multiplicación

        División

        El resultado se muestra directamente en pantalla y el sistema controla errores de ingreso.
    Librería utilizada

    Indicador: Tecnología empleada

    from nicegui import ui


    Se importa NiceGUI, una librería de Python que permite crear interfaces gráficas web de forma sencilla.

    Indicador: Datos de entrada
    El programa recibe:

    Número 1 (num1): ingresado por el usuario en un campo de texto.

    Número 2 (num2): ingresado por el usuario en otro campo de texto.

    Ambos valores se convierten a tipo float para realizar cálculos matemáticos.

    Procesos (Funciones)

    Indicador: Procesamiento de datos

    🔹 Función sumar()

    Convierte los valores ingresados a números.

    Suma ambos números.

    Muestra el resultado.

    Si hay un error de ingreso, muestra un mensaje de error.

    🔹 Función restar()

    Convierte los valores ingresados a números.

    Resta el segundo número al primero.

    Muestra el resultado.

    Controla errores de entrada.

    🔹 Función multiplicar()

    Convierte los valores ingresados a números.

    Multiplica ambos valores.

    Muestra el resultado.

    Controla errores de entrada.

    🔹 Función dividir()

    Convierte los valores ingresados a números.

    Verifica si el divisor es cero.

    Si es cero, muestra un mensaje de error.

    Si no, realiza la división y muestra el resultado.

    Controla errores de entrada.

    Manejo de errores

    Indicador: Validación
    El programa utiliza try-except para:

    Evitar errores si el usuario escribe letras u otros caracteres.

    Mostrar mensajes claros como:

    “Por favor ingrese números válidos”

    “División por cero no permitida”

    arjeta principal
    with ui.card()


    Centra la calculadora.

    Define tamaño, margen y espaciado.

    🏷️ Etiqueta de título
    ui.label('Calculadora')


    Muestra el título de la aplicación.

    🔢 Campos de texto
    num1 = ui.input('Número 1')
    num2 = ui.input('Número 2')


    Permiten ingresar los números.

    🔘 Botones
    ui.button('Sumar')
    ui.button('Restar')
    ui.button('Multiplicar')
    ui.button('Dividir')


    Cada botón ejecuta una función distinta al hacer clic.

    📢 Resultado
    resultado = ui.label('Resultado:')


    Muestra el resultado de la operación o un mensaje de error.

    7. Salidas del sistema

    Indicador: Resultados
    El programa muestra:

    El resultado numérico de la operación.

    Mensajes de error, si los datos no son válidos.

    8. Ejecución del programa

    Indicador: Puesta en marcha

    ui.run()


    Inicia la aplicación.

    Abre la interfaz en el navegador.

    ✅ Resumen general

    Indicador: Síntesis
    Este programa es una calculadora web interactiva, con:

    Interfaz gráfica amigable

    Operaciones matemáticas básicas

    Validación de errores

    Uso eficiente de NiceGUI