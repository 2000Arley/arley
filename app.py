

from flask import Flask, request, render_template, send_file
import pandas as pd
from datetime import datetime, timedelta
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from flask import Flask, request, render_template, send_file
import pandas as pd
from datetime import datetime, timedelta
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas



import os
import qrcode
from io import BytesIO
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.utils import ImageReader

from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime
import os


from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os
from datetime import datetime
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.lib.enums import TA_JUSTIFY
import os


from flask import Flask, render_template, request, send_file
import pandas as pd
from datetime import datetime, timedelta
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
from flask import Flask, render_template, request, send_file
from datetime import datetime, timedelta



#unica parte modificable para ingresar una nueva persona a la base de datos #

app = Flask(__name__)

# Diccionario de usuarios con números de celular en formato internacional
Diccionario = {
    "nombre": ["yenifer rendon", "alix rincon", "Carlos Sánchez", "Ana Gómez", "Luis Ramírez", "Laura Torres"],
    "cedula": [1000992177, 40417761, 10000003, 10000004, 10000005, 10000006],
    "numero_celular": ["+573103396961", "+573134864352", "+573134864354", "+573134864353", "+573134864354", "+573134864356"],
    "afiliado": [230, 450, 550, 600, 700, 800],
    "fecha_emision": [
        datetime(2023, 2, 1),
        datetime(2023, 3, 1),
        datetime(2023, 4, 1),
        datetime(2023, 5, 1),
        datetime(2023, 6, 1),
        datetime(2023, 7, 1),
    ],
    "parcela": ["Parcela La Rinconada", "Parcela La Rinconada", "La Nueva", "El Amanecer", "La Laguna", "La Última"],
}

# Convertir el diccionario a DataFrame
df = pd.DataFrame(Diccionario)


df = pd.DataFrame(Diccionario)

print(df)








def generar_pdf(nombre, cedula, fecha_emision, fecha_vencimiento, parcela):
    buffer = BytesIO()
    p = canvas.Canvas(buffer, pagesize=letter)

    # Rutas de los logos
    logo1_path = "C:/Users/Usuario/OneDrive/Desktop/mi proyecto/logo.gif"
    logo2_path = "C:/Users/Usuario/OneDrive/Desktop/mi proyecto/logo_2.gif"
    #logo3_path = "C:/Users/Usuario/OneDrive/Desktop/mi proyecto/logo_3.gif"


    # Verificar y dibujar logos
    if os.path.exists(logo1_path):  # vertical 
        p.drawImage(logo1_path, 25, 685, width=107, height=77)

    if os.path.exists(logo2_path):
        p.drawImage(logo2_path, 490, 680, width=90, height=60)
 
    #if os.path.exists(logo3_path):  #           listo       listo
        #p.drawImage(logo3_path,    490, 120, width=97, height=-100)

    # Función para texto centrado
    def escribir_centrado_simple(canvas, texto, y, fuente="Helvetica-Bold", tamano=12):
        canvas.setFont(fuente, tamano)
        canvas.drawCentredString(letter[0] / 2, y, texto)

    # Encabezado
    encabezado = [
        "REPUBLICA DE COLOMBIA",
        "DEPARTAMENTO DEL META",
        "MUNICIPIO DE PUERTO GAITAN META",
        "JUNTA DE ACCIÓN COMUNAL VEREDA SANTA HELENA",
        "PERSONERÍA JURÍDICA No. 2886 DE 1985 - 01 - 04",
    ]
    y_pos = 730
    for linea in encabezado:
        escribir_centrado_simple(p, linea, y_pos)
        y_pos -= 15

    # Estilos de párrafo
    styles = getSampleStyleSheet()
    estilo_justificado = ParagraphStyle(
        name="Justify",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=11,
        leading=15,
        alignment=TA_JUSTIFY,
    )
    estilo_justificado_pie = ParagraphStyle(
        name="JustificadoPie",
        fontName="Helvetica",
        fontSize=11,
        leading=15,
        alignment=TA_JUSTIFY,
    )

    texto_largo = (
    "El suscrito presidente de la JAC vereda Santa Helena, zona rural del municipio "
    "de Puerto Gaitán, Meta; fundamentado en la ley 1851 del 2012, que modifica el artículo 91 "
    "de la ley 136 de 1994, el cual en su artículo 91. <b>FUNCIONES:</b> Los alcaldes ejercerán ... "
    "y además de estas, en el literal F – Numeral 6, con relación a la prosperidad integral de "
    "su región: expedir la <b>CONSTANCIA DE AFILIACIÓN</b> para acreditar la residencia a aquellas "
    "personas que residen en territorio del área de influencia de los proyectos de explotación "
    "petrolera y minera en general, y que aspiren a acceder a labores como mano de obra calificada "
    "y no calificada, los alcaldes expedirán dichos certificados con base en los <b>REGISTROS ELECTORALES</b> "
    "O DEL <b>SISBEN</b>, así como en los <b>REGISTROS DE AFILIADOS</b> DE LAS <b>JUNTAS DE ACCIÓN COMUNAL</b>."
)
    parrafo = Paragraph(texto_largo, estilo_justificado)
    parrafo.wrapOn(p, 470, 300)
    parrafo.drawOn(p, 80, 500)

    # Certificación
    y = 450
    p.setFont("Helvetica-Bold", 11)
    p.drawString(250, y, "CERTIFICA QUE:")

    
# Configurar el estilo del párrafo para justificar
    estilos = getSampleStyleSheet()
    estilo_justificado = estilos["Normal"]
    estilo_justificado.alignment = 4  # 4 = Justificado

# Crear el texto con formato
    certificacion = (
    f"El (la) señor (a) <b>{nombre}</b>, identificado (a) con cédula de ciudadanía No. <b>{cedula}</b>, "
    f"expedida en Puerto Gaitán Meta, se encuentra afiliado (a) la JUNTA DE ACCION COMUNAL "
    f"DE LA VEREDA DE SANTA HELENA, desde el día <b>{fecha_emision}</b> en la parcela <b>{parcela}</b>."
)

# Crear el párrafo con estilo justificado
    certificado_1 = Paragraph(certificacion, estilo_justificado)
    certificado_1.wrapOn(p, 470, 300)  # Ajustar tamaño del contenedor
    certificado_1.drawOn(p, 80, y - 75)  # Dibujar en el lienzo 


    # Pie de certificación
    texto_pie_certificacion = (
        "La presente constancia de afiliación se expide a solicitud verbal del interesado (a) "f"el día {datetime.now().strftime('%d de %B del %Y')}, en Vereda Santa Helena (puerto gaitan-meta), <B>CON DESTINO ALCALDIA MUNICIPAL</b> "
    )

    parrafo_pie = Paragraph(texto_pie_certificacion, estilo_justificado_pie)
    parrafo_pie.wrapOn(p, 470, 300)
    parrafo_pie.drawOn(p, 80, y -130)


    # Texto de vigencia
    texto_vigencia = (
        "La presente constancia tendrá una vigencia de tres (03) meses a partir de la fecha de emisión."
    )

    y -= 110  # Ajustar la posición vertical
    parrafo_vigencia = Paragraph(texto_vigencia, estilo_justificado_pie)
    parrafo_vigencia.wrapOn(p, 470, 300)
    parrafo_vigencia.drawOn(p, 80, y -70)

    # Firmas
    firmas = [
        ["Cordialmente:", "_____________", "DAMARIS HERNANDEZ", "PRESIDENTA DE LA JAC", "C.C. No. 1073693052", "Cel. 3122550516"],
        ["Cordialmente:", "_____________", "DAMARIS HERNANDEZ", "PRESIDENTA DE LA JAC", "C.C. No. 1073693052", "Cel. 3122550516"],
    ]
    x_pos = [80, 390]
    for i, firma in enumerate(firmas):
        y_firma = 190
        for linea in firma:
            p.drawString(x_pos[i], y_firma, linea)
            y_firma -= 15



    # GENERAR EL CÓDIGO QR
    qr_data = f"Nombre: {nombre}\nCédula: {cedula}\nFecha de emisión: {fecha_emision}\nFecha de vencimiento: {fecha_vencimiento}\nParcela: {parcela}"
    qr = qrcode.make(qr_data)

    # Guardar el QR en memoria
    qr_buffer = BytesIO()
    qr.save(qr_buffer, format="PNG")
    qr_buffer.seek(0)

    # Agregar QR al PDF
    qr_image = ImageReader(qr_buffer)
    p.drawImage(qr_image, 240, 50, width=100, height=100)  # Posición (x, y) y tamaño

    # Finalizar el PDF
    p.showPage()
    p.save()
    buffer.seek(0)
    return buffer




import re

import os
from datetime import datetime
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
import re

from datetime import datetime
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException
import re

# Credenciales de Twilio
import os
from dotenv import load_dotenv
from twilio.rest import Client




dotenv_path = r"C:\Users\Usuario\OneDrive\Desktop\mi proyecto\.env"
load_dotenv(dotenv_path)


account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_phone = os.getenv("TWILIO_PHONE")

client = Client(account_sid, auth_token)



import threading
import pandas as pd
from datetime import datetime



def enviar_mensaje(nombre, nueva_fecha_emision, nueva_fecha_vencimiento):
    # Buscar el número de celular en el DataFrame
    fila_usuario = df[df['nombre'] == nombre]
    
    if fila_usuario.empty:
        print(f"No se encontró número de teléfono para {nombre}.")
        return
    
    numero_destino = fila_usuario['numero_celular'].values[0]  # Extrae el número de celular

    try:
        message = client.messages.create(
            body=f"¡Hola {nombre}! 🎉 Bienvenido/a. Nos alegra que formes parte de nuestra comunidad. "
                 f"Tu carta de residencia fue emitida el {nueva_fecha_emision}. Si necesitas ayuda, estamos aquí para ti. "
                 f"¡Disfruta tu estancia! {nueva_fecha_vencimiento} 😊",
            from_=twilio_phone,
            to=f'whatsapp:{numero_destino}'
        )
        print(f"Mensaje de bienvenida enviado a {numero_destino}: {message.sid}")
    except Exception as e:
        print(f"Error al enviar el mensaje a {numero_destino}: {e}")





print(f"TWILIO_ACCOUNT_SID: {account_sid}")
print(f"TWILIO_AUTH_TOKEN: {auth_token}")
print(f"TWILIO_PHONE: {twilio_phone}")







import time

from datetime import datetime
import time
from twilio.rest import Client

dotenv_path = r"C:\Users\Usuario\OneDrive\Desktop\mi proyecto\.env"
load_dotenv(dotenv_path)


account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_phone = os.getenv("TWILIO_PHONE")

client = Client(account_sid, auth_token)



client = Client(account_sid, auth_token)


def enviar_mensaje_vencido(nombre, nueva_fecha_emision, nueva_fecha_vencimiento):
    # Buscar el número de celular en el DataFrame
    fila_usuario = df[df['nombre'] == nombre]

    if fila_usuario.empty:
        print(f"❌ No se encontró número de teléfono para {nombre}.")
        return

    numero_destino = fila_usuario['numero_celular'].values[0]  # Extrae el número de celular

    fecha_vencimiento_dt = datetime.strptime(nueva_fecha_vencimiento, '%Y-%m-%d %H:%M:%S')

    print(f"📅 Fecha actual: {datetime.now()}")
    print(f"📅 Fecha de vencimiento: {fecha_vencimiento_dt}")

    # Esperar hasta que la fecha de vencimiento haya pasado
    while datetime.now() < fecha_vencimiento_dt:
        print("⌛ Esperando que venza la carta...")
        time.sleep(30)  # Esperar 30 segundos antes de volver a verificar

    try:
        message = client.messages.create(
            body=f"¡Hola {nombre}! ⚠️ Tu carta de residencia ha vencido. "
                 f"Fue emitida el {nueva_fecha_emision} y su fecha de vencimiento era el {nueva_fecha_vencimiento}. "
                 "Por favor, contacta con nosotros para renovarla. ¡Estamos aquí para ayudarte! 🙌",
            from_=twilio_phone,
            to=f'whatsapp:{numero_destino}'
        )
        print(f"✅ Mensaje de vencimiento enviado a {numero_destino}: {message.sid}")
    except Exception as e:
        print(f"❌ Error al enviar el mensaje a {numero_destino}: {str(e)}")






@app.route('/')
def index():
    return render_template('index.html')  # Ahora apunta a 'index_2.html'

@app.route('/buscador')
def buscador():
    return render_template('busqueda.html')  # Ahora apunta a 'index.html'


from datetime import datetime, timedelta
import pandas as pd
import threading
from flask import render_template, request, send_file

@app.route('/buscar', methods=['POST'])
def buscar():
    try:
        cedula = request.form['cedula']

        # Verificar si la cédula es un número válido
        try:
            cedula = int(cedula)
        except ValueError:
            return render_template('busqueda.html', error="Por favor, ingresa un número de cédula válido.")

        # Buscar la cédula en el DataFrame
        if cedula in df['cedula'].values:
            # Extraer los datos del usuario
            nombre = df.loc[df['cedula'] == cedula, 'nombre'].values[0]
            fecha_emision = df.loc[df['cedula'] == cedula, 'fecha_emision'].values[0]
            parcela = df.loc[df['cedula'] == cedula, 'parcela'].values[0]

            # Verificar si la fecha de emisión es válida
            if pd.isna(fecha_emision) or fecha_emision == "":
                return render_template('busqueda.html', error="Error: La fecha de emisión está vacía o no es válida.")

            # Convertir la fecha de emisión a datetime correctamente
            fecha_emision = pd.to_datetime(fecha_emision).to_pydatetime()
            fecha_vencimiento = fecha_emision + timedelta(minutes=2)

            # 🔍 Depuración: Imprimir fechas en consola
            print(f"Fecha emisión: {fecha_emision}, Fecha vencimiento: {fecha_vencimiento}, Fecha actual: {datetime.now()}")

            # Verificar si la carta está vencida
            if datetime.now() > fecha_vencimiento:
                # Generar una nueva carta con la fecha actual
                nueva_fecha_emision = datetime.now()
                nueva_fecha_vencimiento = nueva_fecha_emision + timedelta(minutes=2)

                # Actualizar la fecha en el DataFrame
                df.loc[df['cedula'] == cedula, 'fecha_emision'] = nueva_fecha_emision

                # Guardar cambios en CSV (si aplica)
                try:
                    df.to_csv("datos.csv", index=False)
                    print("✅ Datos actualizados en CSV")
                except Exception as e:
                    print(f"❌ Error guardando en CSV: {str(e)}")

                try:
                    # Generar el PDF con las nuevas fechas
                    pdf_buffer = generar_pdf(
                        nombre, cedula,
                        nueva_fecha_emision.strftime('%Y-%m-%d %H:%M:%S'),
                        nueva_fecha_vencimiento.strftime('%Y-%m-%d %H:%M:%S'),
                        parcela
                    )

                    if pdf_buffer is None:
                        return render_template('busqueda.html', error="Error: El PDF no se generó correctamente.")

                except Exception as e:
                    print(f"❌ Error generando el PDF: {str(e)}")
                    return render_template('busqueda.html', error=f"Error generando el PDF: {str(e)}")

                # Guardar el registro solo después de generar el PDF
                try:
                    with open(registro_path, 'a') as archivo:
                        registro = f"{cedula},{nombre},{nueva_fecha_emision.strftime('%Y-%m-%d %H:%M:%S')},{parcela}\n"
                        archivo.write(registro)
                    print(f"Registro guardado: {registro.strip()}")
                except Exception as e:
                    print(f"❌ Error guardando el registro: {str(e)}")
                    return render_template('busqueda.html', error=f"Error guardando el registro: {str(e)}")

                # Enviar mensajes sin bloquear la ejecución
                threading.Thread(target=enviar_mensaje, args=(nombre, nueva_fecha_emision.strftime('%Y-%m-%d %H:%M:%S'), nueva_fecha_vencimiento.strftime('%Y-%m-%d %H:%M:%S'))).start()
                threading.Thread(target=enviar_mensaje_vencido, args=(nombre, nueva_fecha_emision.strftime('%Y-%m-%d %H:%M:%S'), nueva_fecha_vencimiento.strftime('%Y-%m-%d %H:%M:%S'))).start()

                # Descargar el PDF
                return send_file(pdf_buffer, as_attachment=True, download_name='carta_residencia.pdf', mimetype='application/pdf')

            else:
                return render_template('carta_vigente.html', fecha_vencimiento=fecha_vencimiento.strftime('%Y-%m-%d %H:%M:%S'))

        else:
            return render_template('busqueda.html', error="La cédula ingresada no está registrada.")

    except Exception as e:
        print(f"❌ Error inesperado: {str(e)}")
        return render_template('busqueda.html', error=f"Error inesperado: {str(e)}")


registro_path = 'registro_emisiones.txt'
import os
registro_path = os.path.join(os.path.dirname(__file__), 'registro_emisiones.txt')

@app.route('/historial')
def historial():
    registros = []
    try:
        # Leer el archivo de registros
        with open(registro_path, 'r') as archivo:
            for linea in archivo:
                registros.append(linea.strip().split(','))
    except Exception as e:
        registros = []
        print(f"Error al leer el archivo de registros: {e}")

    return render_template('historial.html', registros=registros)







@app.route('/agregar', methods=['POST'])
def agregar():
    try:
        nombre = request.form['nombre']
        cedula = int(request.form['cedula'])
        parcela = request.form['parcela']
        fecha_emision = datetime.now()
        fecha_vencimiento = (fecha_emision + timedelta(days=180)).strftime('%d/%m/%Y %H:%M:%S')
        
        # Agregar la nueva entrada al DataFrame
        global df
        nuevo_registro = pd.DataFrame({'nombre': [nombre], 'cedula': [cedula], 'fecha_emision': [fecha_emision], 'parcela': [parcela]})
        df = pd.concat([df, nuevo_registro], ignore_index=True)
        
        fecha_emision_formateada = fecha_emision.strftime('%d/%m/%Y %H:%M:%S')
        
        return f"Usuario {nombre} con cédula {cedula} agregado correctamente el {fecha_emision_formateada} con vencimiento el {fecha_vencimiento}."
    except Exception as e:
        return f"Ocurrió un error: {e}"

if __name__ == '__main__':
    app.run(debug=True, port=5000)







