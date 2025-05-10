import fitz  # PyMuPDF
import pandas as pd
import os
import zipfile

#=========================================================#
#                   Rutas de entrada                      #
#=========================================================#
pdf_base = r"C:\Users\ian00\YUNXIAYU-1.pdf"
excel_path = r"C:\Users\ian00\CursoManipulaciónAlimentos-8Abril.xlsx"

#=========================================================#
#                   Cargar nombres                        #
#=========================================================#
df = pd.read_excel(excel_path)
nombres = df.iloc[:, 0].dropna().tolist()

#=========================================================#
#                   Crear carpeta de salida               #
#=========================================================#
script_dir = os.getcwd()
output_folder = os.path.join(script_dir, "certificados_generados")
os.makedirs(output_folder, exist_ok=True)

#=========================================================#
#                  Procesar cada nombre                   #
#=========================================================#
for nombre in nombres:
    doc = fitz.open(pdf_base)

    for page in doc:
        # Añadir texto directamente en la coordenada del nombre
        page.insert_text((158.20, 260.21), f"Nombre y Apellido: {nombre}", fontsize=12, color=(0, 0, 0))

    output_path = os.path.join(output_folder, f"Certificado_{nombre.replace(' ', '_')}.pdf")
    print(f"Guardado: {output_path}")
    doc.save(output_path)
    doc.close()

#=========================================================#
#                   Crear ZIP                             #
#=========================================================#
zip_name = os.path.join(script_dir, "Certificados_Manipulador_Alimentos.zip")
with zipfile.ZipFile(zip_name, 'w') as zipf:
    files = os.listdir(output_folder)
    print(f"Archivos encontrados para comprimir: {files}")
    for file in files:
        file_path = os.path.join(output_folder, file)
        if os.path.isfile(file_path):
            zipf.write(file_path, arcname=file)
print(f" Certificados comprimidos en: {zip_name}")
