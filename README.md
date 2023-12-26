
# Discord-Bot-for-Twitter

  

Este bot monitorea feeds de Twitter específicos y notifica a su servidor cada vez que se publica un nuevo tweet. (Por el momento sólo para una cuenta de Twitter)

  

El proyecto utiliza un archivo `.env` para gestionar las variables de entorno. Se entrega un .txt que simula el .env para que sea más sencillo la inicialización de variables.
A continuación, se explica cómo llenar los datos necesarios:

  

### Crear el archivo .env

  

1. Crea un archivo llamado `.env` en la raíz del proyecto.

  

### Configuración de Variables de Entorno

  

A continuación se detallan las variables de entorno necesarias y cómo llenarlas:

  

#### `WHITELIST`

  

La variable `WHITELIST` es una lista de ID de usuario permitidos separados por comas. Puedes obtener estos IDs desde Discord.
Ejemplo:
WHITELIST=1234567890,9876543210

  

#### `TWITTER_CHANNEL`

TWITTER_CHANNEL es el ID del canal de Discord donde el bot publicará las actualizaciones de Twitter.
Ejemplo:
TWITTER_CHANNEL=123456789012345678

  

#### `BOT_TOKEN`
BOT_TOKEN es el token de tu bot de Discord. Puedes obtener esto al crear un bot en el Portal de Desarrolladores de Discord.
Ejemplo: 
BOT_TOKEN="AKJSDASKASJDKAJSD_DWDNKASD_Asd"

  

#### `ULTIMO_TWEET`

ULTIMO_TWEET es el url (con fx al inicio) del último tweet procesado por el bot. Puedes dejarlo en blanco.
Ejemplo: 
ULTIMO_TWEET="https://fxtwitter.com/elonmusk/status/1737488430202851389"

  

#### `ROLE`

ROLE es el nombre del rol de Discord utilizado para las menciones en las actualizaciones de Twitter.
EJEMPLO: 
ROLE="Admin"

  

Guarda el archivo .env después de ingresar estos valores.