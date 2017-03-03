from slackbot.bot import respond_to
from slackbot.bot import listen_to
import quantities as q
import re

def F_to_C(temp_F):
    return (temp_F - 32.0)*(5.0/9.0)

def C_to_F(temp_C):
    return temp_C*(9.0/5.0) + 32.0

def C_to_K(temp_C):
    return temp_C+273.15

def F_to_K(temp_F):
    return C_to_K(F_to_C(temp_F))

@respond_to('(.*)F', re.IGNORECASE)
def temptoC(message, incoming_message):
    print "Responding to", incoming_message
    try:
        temp_f = float(incoming_message.split()[-1].lower().replace("f",""))
    except:
        return
    temp_c = F_to_C(temp_f)
    message.reply("That is {:.2f} C!".format(temp_c))

@respond_to('(.*)C', re.IGNORECASE)
def temptoF(message, incoming_message):
    print "Responding to", incoming_message
    try:
        temp_c = float(incoming_message.split()[-1].lower().replace("c",""))
    except:
        return
    temp_f = C_to_F(temp_c)
    message.reply("That is {:.2f} F!".format(temp_f))
