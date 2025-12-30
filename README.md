# Calculadora

Una calculadora gráfica simple desarrollada en Python con interfaz tkinter.

## 📋 Descripción

Esta es una aplicación de calculadora con interfaz gráfica que permite realizar operaciones matemáticas básicas:
- Suma (+)
- Resta (-)
- Multiplicación (*)
- División (/)
- Porcentaje (%)

## 🚀 Características

- Interfaz gráfica intuitiva
- Operaciones matemáticas básicas
- Botón de borrado y limpieza
- Manejo de errores
- Compilación automática a ejecutable de Windows

## 📦 Descargar Ejecutable

Puedes descargar el archivo `.exe` para Windows desde la sección de **Actions** de este repositorio:

1. Ve a la pestaña [Actions](../../actions)
2. Selecciona el workflow "Build Windows Executable"
3. Haz clic en la última ejecución exitosa
4. Descarga el artefacto "Calculadora-Windows" o "Calculadora-Windows-with-README"
5. Extrae el archivo ZIP y ejecuta `Calculadora.exe`

## 🛠️ Ejecución Local

### Requisitos
- Python 3.7 o superior
- tkinter (generalmente incluido con Python)

### Instrucciones

```bash
# Clonar el repositorio
git clone https://github.com/benjamindarrigrandip-gif/calculadora.git
cd calculadora

# Ejecutar la calculadora
python calculadora.py
```

## 🏗️ Compilar a Ejecutable

Para compilar la aplicación a un ejecutable de Windows:

```bash
# Instalar PyInstaller
pip install -r requirements.txt

# Compilar
pyinstaller --onefile --windowed --name Calculadora calculadora.py

# El ejecutable estará en la carpeta dist/
```

## 🤖 GitHub Actions

Este proyecto utiliza GitHub Actions para compilar automáticamente el ejecutable de Windows en cada push. El workflow se encuentra en `.github/workflows/build.yml`.

El ejecutable compilado se sube como artefacto y está disponible para descargar por 90 días.

## 📝 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia que elijas especificar.
