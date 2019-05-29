#!/usr/bin/python3
import time
import discord
import RPi.GPIO as gpio
in1 = 24
in2 = 23
in3 = 17
in4 = 27
en = 25
bn = 22
def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(in1, gpio.OUT)
    gpio.setup(in2, gpio.OUT)
    gpio.setup(in3, gpio.OUT)
    gpio.setup(in4, gpio.OUT)
    gpio.setup(en, gpio.OUT)
    gpio.setup(bn, gpio.OUT)
    print("OK1")
client = discord.Client()
@client.event
async def on_ready():
    print('{0.user}'.format(client))
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('#f'):
        await message.channel.send('party on dudes!')
        init()
        p=gpio.PWM(en,.1)
        p.start(25)
        b=gpio.PWM(bn,.1)
        b.start(22)
        gpio.output(in1, gpio.HIGH)
        gpio.output(in2, gpio.LOW)
        gpio.output(in3, gpio.LOW)
        gpio.output(in4, gpio.HIGH)
        time.sleep(3)
        gpio.cleanup()
    if message.content.startswith('#tl'):
        await message.channel.send('party on dudes!')
        init()
        p=gpio.PWM(en,.1)
        p.start(25)
        b=gpio.PWM(bn,.1)
        b.start(22)
        gpio.output(in1, gpio.HIGH)
        gpio.output(in2, gpio.LOW)
        gpio.output(in3, gpio.HIGH)
        gpio.output(in4, gpio.LOW)
        time.sleep(3)
        gpio.cleanup()
    if message.content.startswith('#tr'):
        await message.channel.send('party on dudes!')
        init()
        p=gpio.PWM(en,.1)
        p.start(25)
        b=gpio.PWM(bn,.1)
        b.start(22)
        gpio.output(in1, gpio.LOW)
        gpio.output(in2, gpio.HIGH)
        gpio.output(in3, gpio.LOW)
        gpio.output(in4, gpio.HIGH)
        time.sleep(3)
        gpio.cleanup()
    if message.content.startswith('!'):
        time.sleep(2)
        await message.channel.send(message.content[1:])
    if message.content.startswith('hello'):
        time.sleep(2)
        await message.channel.send('hi '+str(message.author)[:-5])
    if message.content.startswith('be excellent'):
        await message.channel.send('party on dudes!')
    if message.content.startswith('Be excellent'):
        await message.channel.send('party on dudes!')
    elif message.content.startswith('stop'):
        await message.channel.send('grugger')
print("OK2")
client.run('NTcwNjIzOTk2MTY1NjE5NzEz.XMB75w._2AD2nfVicR1bTcxfrM4JieHAkM')
