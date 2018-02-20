import discord
import asyncio
import random
import re
import sys

token = sys.argv[1] #Will figure out somewhere convenient to keep the token eventually.

client = discord.Client()

@client.event
@asyncio.coroutine 
def on_message(message):
    if message.author == client.user: #bot can't trigger itself
        return
    
    if message.content.startswith('!bye'):
        msg = 'Goodbye!'
        yield from client.send_message(message.channel, msg.format(message))

    if message.content.startswith('!roll'):
        try:
            numDice = re.split('[\sd]',message.content)[1]
            valDice = re.split('[\sd]',message.content)[2]
            #Yes, this also takes !roll 3 4.
        except:
            msg = 'Try \'!roll XdY\'.'
        else:
            rolls = []
            total = 0
            for r in range(int(numDice)):
                rolls.append(str(random.randint(1, int(valDice))))
                total+=int(rolls[r])
                
            #It looks nice like this okay
            msg = '```'
            msg += ', '.join(rolls)
            msg += '\nTotal: ' + str(total)
            msg += '```'
        yield from client.send_message(message.channel, msg.format(message))

        
client.run(token)
