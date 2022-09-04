from responseM import responseD
import random
import time
def response(message, responses):
    if message in responses:
        return "Bot:" + random.choice(responses[message])
    else:
        return " Sorry i cant help you with that would you like to check online"
rep = str(input()).lower()
print("User:{}".format(rep))
time.sleep(1.2)
print((response(rep, responseD)))
