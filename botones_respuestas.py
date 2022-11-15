from config import *
import telebot #api Telegram
from telebot.types import ReplyKeyboardMarkup #Botones
from telebot.types import ForceReply
#inicio Bot
bot = telebot.TeleBot(TELEGRAM_TOKEN)
#Variable global
usuarios = {}

#/start
@bot.message_handler(commands=['start', 'ayuda', 'help'])
def cmd_start(message):
    #Comandos disponibles
    bot.send_message(message.chat.id, "Hola, soy Katen tu Asistente Virtual.\n Para proceder a ayudarte, Porfavor dime ¿Quien eres?. \n  Acontinuación Completa la información Solicitada")
    bot.send_message(message.chat.id, " Usa el Comando /iniciemos para completar la información")

@bot.message_handler(commands=['iniciemos'])
def cmd_start(message):
    #Comando Nombre
    markup = ForceReply()
    msg = bot.send_message(message.chat.id, "¿Como te llamas? \n Digita Tu Nombre completo", reply_markup=markup)
    bot.register_next_step_handler(msg, preguntar_cur)
    
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
        usuarios[message.chat.id]["edad"] = int(message.text)
        markup = ReplyKeyboardMarkup(
            one_time_keyboard=True,
            input_field_placeholder="Escoja su Sexo",
            resize_keyboard=True
            )
        markup.add("Masculino", "Femenino", "Otro", "Prefiero No decirlo")
        msg = bot.send_message(message.chat.id, '¿Cual es tu sexo?', reply_markup=markup)
        bot.register_next_step_handler(msg, select_error)

def select_error(message):
    if message-text != "Masculino" and message.text != "Femenino" and message.text != "Otro" and message.text != "Prefierlo No decirlo":
        msg = bot.send_message(message.chat_id, 'ERROR: Sexo no valido.\n Seleccione una Opción')
        bot.register_next_step_handler(msg, preguntar_sexo)
    else:
        usuarios[message.chat.id]["select_error"] = int(message.text)
        markup = ReplyKeyboardMarkup(
            one_time_keyboard=True,
            input_field_placeholder="Escoja el error presentado",
            resize_keyboard=True
            )
        markup.add("Error 707", "Error 801", "Error 808", "Error 907", "Error 908", "Error 909", "Error 107", "Error 089", "Error 404", "Error 500" "Error 707")
        msg = bot.send_message(message.chat.id, '¿Que error presenta?', reply_markup=markup)
        bot.register_next_step_handler(msg, error)





#MAIN ####################
if __name__ == '__main__':
    print("Iniciando Bot de soporte...")
    bot.infinity_polling()