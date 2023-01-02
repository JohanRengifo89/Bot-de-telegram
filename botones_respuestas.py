from config import *
import telebot
from telebot.types import ReplyKeyboardMarkup
from telebot.types import ForceReply
#inicio Bot
#La Variable de Telegram Token hace referencia al Token que ubica nuestro BOT en las BD de Telegram
bot = telebot.TeleBot(TELEGRAM_TOKEN)
#Variable global
usuarios = {}

#/start
@bot.message_handler(commands=['start', 'ayuda', 'help'])
def cmd_start(message):
    #Comandos disponibles
    bot.send_message(message.chat.id, " Este Bot se encuentra en estado de Desarrollo.\nPuede presentar fallas en su Funcionamiento. Aun no es recomendable su uso.")
    bot.send_message(message.chat.id, "Hola, soy Karen tu Asistente Virtual.\n Para proceder a ayudarte, Porfavor dime ¿Quien eres?. \n A continuación Completa la información Solicitada")
    bot.send_message(message.chat.id, " Usa el Comando /iniciar para completar la información")

@bot.message_handler(commands=['iniciar'])
def cmd_init(message):
    #Comando Nombre
    markup = ForceReply()
    msg = bot.send_message(message.chat.id, "¿Como te llamas? \n Digita Tu Nombre completo", reply_markup=markup)
    bot.register_next_step_handler(msg, preguntar_cur) # En su cambio cambiamos el "preguntar_cur" a "preguntar_edad" ° Para omitir estos dos pasos q eran actualiados do eliminados

def preguntar_cur(message):
    #Cur usuario
    usuarios[message.chat.id] = {}
    usuarios[message.chat.id]["cur"] = message.text
    markup = ForceReply()
    msg = bot.send_message(message.chat.id, "Ingrese su CUR de Usuario", reply_markup=markup)
    msg = bot.send_message(message.chat.id, "Recuerda que tu CUR de usuario te la brinda nuestra plataforma y es un cadena de palabras similar a este:\n Col-Ppy-LADH-SdCtl-Stdt-000001 ")
    bot.register_next_step_handler(msg, preguntar_ruc)

def preguntar_ruc(message):
    #Ruc usuario
    usuarios[message.chat.id] = {}
    usuarios[message.chat.id]["ruc"] = message.text
    markup = ForceReply()
    msg = bot.send_message(message.chat.id, "Ingrese su RUC de Usuario", reply_markup=markup)
    msg = bot.send_message(message.chat.id, "Recuerda que la Cur de usuario te la Brinda nuestra plataforma y es una cadena de palabras similar a esta:\n user-ladh-sdctl-ppy-00001-roluser")
    bot.register_next_step_handler(msg, preguntar_edad)

def preguntar_edad(message):
    #edad usuario
    usuarios[message.chat.id] = {}
    usuarios[message.chat.id]["nombre"] = message.text
    markup = ForceReply()
    msg = bot.send_message(message.chat.id, "Ingrese su Edad.", reply_markup=markup)
    bot.register_next_step_handler(msg, preguntar_sexo)
    
def preguntar_sexo(message):
    if not message.text.isdigit():
        markup = ForceReply()
        msg = bot.send_message(message.chat.id, 'Error: Indique en Numeros enteros su edad Correspondiente')
        bot.register_next_step_handler(msg, preguntar_sexo)
    else:
        usuarios[message.chat.id]["edad"] = message.text
        markup = ReplyKeyboardMarkup(
            one_time_keyboard=True,
            input_field_placeholder="Escoja su Sexo",
            resize_keyboard=True
            )
        markup.add("Masculino", "Femenino", "Otro", "Prefiero No decirlo")
        msg = bot.send_message(message.chat.id, '¿Cual es tu sexo?', reply_markup=markup)
        bot.register_next_step_handler(msg, select_error)

# En Producción en el cambio de estos dos pasos presentamos error de no reconocimiento de la respuesta UNIFIED ANSWER

def select_error(message):
    if message.text != "Masculino" and message.text != "Femenino" and message.text != "Otro" and message.text != "Prefierlo No decirlo":
        msg = bot.send_message(message.chat_id, 'ERROR: Sexo no valido.\n Seleccione una Opción')
        bot.register_next_step_handler(msg, preguntar_sexo)
    else:
        usuarios[message.chat.id]["select_error"] = message.text
        markup = ReplyKeyboardMarkup(
            one_time_keyboard=True,
            input_field_placeholder="Escoja el error presentado",
            resize_keyboard=True
            )
        markup.add("error_707", "error_801", "error_808", "error_907", "error_908", "errorr_909", "error_107", "error_089", "error_404", "error_500")
        msg = bot.send_message(message.chat.id, '¿Que error presentas dentro de la platafora?', reply_markup=markup)
        bot.register_next_step_handler(msg, commands_error)
#El paso anterior Muestra en Pantalla Los Botones de Errores
# Dependiendo del Id del Boton Muestra la Respuesta Correspondiente

#Respuestas a Comandos de Error ############
#Para determinar en la sentencia el procedimiento correspondiente. Solicitar el Manual de Usuario
def commands_error(message):
    if message.text != "error_707":
        msg = bot.send_message(message.chat.id, "Este es un error de Servicio no encontrado")
    elif message.text != "error_801":
        msg = bot.send_message(message.chat.id, "Erro 801")
    elif message.text != "error_808":
        msg = bot.send_message(message.chat.id, "Error 808")
    elif message.text != "error_907":
        msg = bot.send_message(message.chat,id, "Error 907")
    elif message.text != "error_908":
        msg = bot.send_message(message.chat,id, "Error 908")
    elif message.text != "error_909":
        msg = bot.send_message(message.chat,id, "Error 909")
    elif message.text != "error_107":
        msg = bot.send_message(message.chat,id, "Error 107")
    elif message.text != "error_089":
        msg = bot.send_message(message.chat,id, "Error 089")
    elif message.text != "error_404":
        msg = bot.send_message(message.chat,id, "Error 404")
    elif message.text != "error_500":
        msg = bot.send_message(message.chat,id, "Error 500")
    else:
        msg = bot.send_message(message.chat.id, "No presentas errores.\n Te Invito a seguir disfrutando de la aplicacón")
########Fin a Comando Error ################

# En el footer es necesario saber la satisfación del usuario
# Crear Encuenta Breve de Satisfacción

####### Inicio Footer ##############

def commands_finbot(message):
    msg = bot.send_message(message.chat.id, "Espero Haber Resuelto tu Problema.")

####### Fin Footer #################

#MAIN ####################
if __name__ == '__main__':
    print("Iniciando Bot de soporte...")
    bot.infinity_polling()
