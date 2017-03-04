from slackbot.bot import respond_to
from slackbot.bot import listen_to
import quantities as q
import re


degC_relativ_cte = 32.0*5.0/9.0


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
    print("Responding to", incoming_message)
    try:
        temp_in = float(incoming_message.split()[-1].lower().replace("f",""))
    except:
        return
    temp = temp_in * q.degF
    temp.units = q.degC
    temp -= degC_relativ_cte * q.degC
    message.reply("{} °F corresponds to {:.2f} °C!".format(incoming_message, float(temp.magnitude)))

@respond_to('(.*)C', re.IGNORECASE)
def temptoF(message, incoming_message):
    print("Responding to", incoming_message)
    try:
        temp_in = float(incoming_message.split()[-1].lower().replace("c",""))
    except:
        return
    temp = temp_in * q.degC + degC_relativ_cte * q.degC
    temp.units = q.degF
    message.reply("{} °C corresponds to {:.2f} °F!".format(incoming_message, float(temp.magnitude)))
