# DISCORD NITRO GEN #
import string, random
from time import sleep

def id_generator(size=16, chars=string.ascii_lowercase + string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

for user in range(0, 15):
    code = id_generator()
    print(" [-] | DISCORD GEN | https://discord.gift/" + code)
    sleep(0.4)
