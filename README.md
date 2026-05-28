# Raspberry Moon Web

Interfaz web local para revisar la fase lunar desde una Raspberry Pi.

El proyecto levanta un pequeno servidor Flask en la Raspberry Pi y permite abrir una pagina interna desde cualquier computadora, celular o tablet conectada a la misma red. No requiere pantalla fisica conectada a la Raspberry.

## Caracteristicas

- Interfaz web responsive para escritorio y movil.
- Calculo local de fase lunar, iluminacion, edad lunar, distancia aproximada y proxima luna llena.
- API JSON disponible en `/api/moon`.
- Diseno visual inspirado en una pantalla astronomica.
- Archivo `index.html` comentado con marcas `### EDITABLE` para personalizar textos, colores y medidas.
- Script `install_service.sh` para arrancar automaticamente al reiniciar la Raspberry Pi.

## Vista General

La pagina principal muestra:

- Fase lunar actual.
- Porcentaje de iluminacion.
- Edad de la luna en dias.
- Fecha estimada de la proxima luna llena.
- Cuenta regresiva aproximada hasta la proxima luna llena.
- Distancia aproximada Tierra-Luna en kilometros.

## Requisitos

- Raspberry Pi con Raspberry Pi OS o Linux compatible.
- Python 3.
- Acceso a la red local.
- Navegador web en otro dispositivo de la misma red.

## Instalacion

Clona o copia este proyecto en tu Raspberry Pi:

```bash
cd /home/pi
git clone https://github.com/TU-USUARIO/raspberry-moon-web.git
cd raspberry-moon-web
```

Si copiaste la carpeta por `scp`, entra directamente a ella:

```bash
cd /home/pi/raspberry_moon_web
```

Crea el entorno virtual e instala dependencias:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Ejecutar Manualmente

```bash
python app.py
```

Luego abre desde otro dispositivo en la misma red:

```text
http://IP-DE-TU-RASPBERRY:5000
```

Para ver la IP de la Raspberry:

```bash
hostname -I
```

## API

La API de datos esta disponible en:

```text
http://IP-DE-TU-RASPBERRY:5000/api/moon
```

Ejemplo de respuesta:

```json
{
  "phaseName": "WAXING CRESCENT",
  "phaseIndex": 1,
  "age": 4.23,
  "illumination": 0.18,
  "illuminationPercent": 18,
  "nextFullDate": "Jun 1, 2026",
  "daysToFull": 10,
  "hoursToFull": 5,
  "distance": 389421,
  "date": "05/28/2026"
}
```

## Arranque Automatico

Para que la interfaz se inicie sola al reiniciar la Raspberry Pi:

```bash
chmod +x install_service.sh
./install_service.sh
```

Verifica el estado:

```bash
sudo systemctl status moon-web
```

Ver logs en tiempo real:

```bash
journalctl -u moon-web -f
```

Reiniciar el servicio:

```bash
sudo systemctl restart moon-web
```

Detener el servicio:

```bash
sudo systemctl stop moon-web
```

Desactivar el arranque automatico:

```bash
sudo systemctl disable moon-web
```

## Personalizacion

Edita este archivo:

```text
templates/index.html
```

Dentro encontraras comentarios `### EDITABLE` para ubicar rapidamente:

- Titulo de la pagina.
- Colores principales.
- Textos visibles.
- Tamano de la luna.
- Posicion de crateres.
- Formato de numeros.
- Frecuencia de actualizacion.

Despues de editar, reinicia el servicio:

```bash
sudo systemctl restart moon-web
```

## Estructura Del Proyecto

```text
raspberry_moon_web/
+-- app.py
+-- install_service.sh
+-- requirements.txt
+-- templates/
|   +-- index.html
+-- README.md
```

## Subir A GitHub

Desde la carpeta del proyecto:

```bash
git init
git add .
git commit -m "Initial Raspberry Moon Web project"
git branch -M main
git remote add origin https://github.com/TU-USUARIO/raspberry-moon-web.git
git push -u origin main
```

Cambia `TU-USUARIO` y el nombre del repositorio por los tuyos.

## Descripcion Corta Para GitHub

```text
Interfaz web local para consultar la fase lunar desde una Raspberry Pi.
```

## Topics Sugeridos

```text
raspberry-pi flask moon lunar-phase astronomy python local-web-server
```

## Licencia

MIT. Puedes usar, modificar y compartir este proyecto libremente.
