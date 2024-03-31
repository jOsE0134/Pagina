from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('pagina.html')


@app.route('/submit', methods=['POST'])
def submit():
    from flask import send_file

    @app.route('/descargar')
    def descargar():
        return send_file('datos.xlsx', as_attachment=True)

    from openpyxl import Workbook

    @app.route('/submit', methods=['POST'])
    def submit():
        if request.method == 'POST':
            nombre = request.form['nombre']
            documento = request.form['documento']
            telefono = request.form['telefono']
            horario_contacto = request.form['horario_contacto']

            # Guardar los datos en un archivo Excel
            workbook = Workbook()
            sheet = workbook.active

            # Agregar encabezados
            sheet.append(['Nombre', 'Documento', 'Teléfono', 'Horario de contacto'])

            # Agregar los datos del formulario
            sheet.append([nombre, documento, telefono, horario_contacto])

            # Guardar el archivo
            workbook.save('datos.xlsx')

            # Redirigir a una página de agradecimiento o mostrar un mensaje de confirmación
            return 'Gracias por enviar tus datos y se han guardado en un archivo Excel.'

    if request.method == 'POST':
        nombre = request.form['nombre']
        documento = request.form['documento']
        telefono = request.form['telefono']
        horario_contacto = request.form['horario_contacto']

        # Aquí puedes procesar los datos como desees, como guardarlos en una base de datos o enviarlos por correo electrónico.
        # Por ahora, simplemente los imprimiremos en la consola.
        print(
            f'Nombre: {nombre}, Documento: {documento}, Teléfono: {telefono}, Horario de contacto: {horario_contacto}')

        # Puedes redirigir a una página de agradecimiento o mostrar un mensaje de confirmación.
        return 'Gracias por enviar tus datos.'


if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')
