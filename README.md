# Simulación de Sistema Continuo: Masa-Resorte

Este proyecto forma parte de las tareas asignadas para la materia "Simulación de Sistema Continuo". El objetivo es modelar un sistema de masa-resorte utilizando métodos numéricos para resolver ecuaciones diferenciales.

## Preparación del Entorno / Dependencias

Este proyecto requiere las siguientes dependencias:

- [Python >= 3.7](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [ffmpeg](https://ffmpeg.org/download.html) (necesario para generar videos)

Para comprobar si tienes las versiones correctas de Python y pip instaladas, puedes usar los siguientes comandos en tu terminal:

```bash
python --version
pip --version
```
Para verificar la instalación de ffmpeg, puedes utilizar el siguiente comando:

```bash
ffmpeg -version
```


### Instalación de Dependencias del Proyecto:

Todas las dependencias específicas del proyecto están listadas en el archivo `requirements.txt`. Para instalar estas dependencias, navega a la raíz del proyecto en tu terminal y ejecuta el siguiente comando:

```bash
pip install -r requirements.txt
```



## Estructura del Proyecto

El proyecto tiene la siguiente estructura:

- `assets/`: Este directorio contiene todas las imágenes y videos generados por las simulaciones.
- `constants.py`: Este archivo define constantes que son utilizadas en varias partes del proyecto.
- `datos.txt`: Este archivo contiene los datos generados por las simulaciones.
- `euler_mass_spring.py`: Este script implementa el método de Euler para resolver las ecuaciones diferenciales del sistema.
- `experiments.py`: Este script realiza varios experimentos con diferentes parámetros y genera las correspondientes visualizaciones.
- `mass_spring_system.py`: Este script define la clase `MassSpringSystem`, que representa el sistema de masa-resorte.
- `parser.py`: Este script procesa los argumentos de la línea de comandos para configurar la simulación.
- `plotter.py`: Este script genera gráficas a partir de los datos de las simulaciones.
- `run.py`: Este es el script principal que debes ejecutar para realizar una simulación.
- `README.md`: Este archivo proporciona una descripción general y instrucciones para el proyecto.
- `requirements.txt`: Este archivo contiene las dependencias necesarias para ejecutar el proyecto.

## Uso

El script `run.py` permite ejecutar una simulación del sistema masa-resorte con los parámetros proporcionados a través de la línea de comandos. Aquí encontrarás información sobre cómo proporcionar estos parámetros y cómo utilizar el script.

### Parámetros requeridos

- `-mass`: Masa del sistema (en kg).
- `-spring_resistance`: Resistencia del resorte (en N/m).
- `-friction`: Coeficiente de fricción del sistema.
- `-force`: Fuerza aplicada al sistema (en N).

### Parámetros opcionales

- `-dt`: Intervalo de tiempo para la simulación (por defecto es 0.001 s).
- `-t`, `--sim_time`: Tiempo total de simulación (por defecto es 100 s).
- `-x`: Posición inicial del sistema (por defecto es 0 m).
- `-v`: Velocidad inicial del sistema (por defecto es 0 m/s).

Para obtener una descripción detallada de cada parámetro y sus valores predeterminados, puedes ejecutar el siguiente comando para mostrar la ayuda del script:

```bash
python run.py -h
```

## Ejemplos de uso

A continuación, se presentan algunos ejemplos de cómo podrías usar el script `run.py`:

```bash
python run.py -mass 1 -spring_resistance 10 -friction 0.5 -force 10
```


Si deseas cambiar el intervalo de tiempo(paso) a 0.01 s y el tiempo total de simulación a 200 s, mientras mantienes los demás parámetros iguales, el comando sería:

```bash
python run.py -mass 1 -spring_resistance 10 -friction 0.5 -force 10 -dt 0.01 -t 200
```

## Reporte

En el archivo 'report.pdf' encontrarás un análisis detallado de los experimentos más interesantes llevados a cabo durante este proyecto, junto con sus respectivas conclusiones.

