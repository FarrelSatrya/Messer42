import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        print('Message from {0.author}: {0.content}'.format(message))

    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = 'Greetings {0.mention}, to {1.name}!'.format(member, guild)
            await guild.system_channel.send(to_send)\
    
    async def on_member_remove(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            to_send = 'Goodbye {0.mention}, may you find peace in the waking world.'.format(member)
            await guild.system_channel.send(to_send)\

client = MyClient()
client.run('OTk5NzI1NTI5MjQwNDM2NzU2.GWh2hz.uc7vNd4I4g3hM_9kcA-FXLHTM4Yuth5b-Tsgzk')