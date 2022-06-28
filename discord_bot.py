import discord
import os

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.target_message_id = 986739733524787270

    async def on_ready(self):
        print('ready')

    async def on_raw_reaction_add(self, payload):
        if payload.message_id != self.target_message_id:
            return

        guild = client.get_guild(payload.guild_id)

        if payload.emoji.name == '🇻':
            role = discord.utils.get(guild.roles, name='valorant')
            await payload.member.add_roles(role)
        elif payload.emoji.name == '🇵':
            role = discord.utils.get(guild.roles, name='pubg')
            await payload.member.add_roles(role)
        elif payload.emoji.name == '🇼':
            role = discord.utils.get(guild.roles, name='warzone/cod')
            await payload.member.add_roles(role)
        elif payload.emoji.name == '🇲':
            role = discord.utils.get(guild.roles, name='minecraft')
            await payload.member.add_roles(role)
        elif payload.emoji.name == '🇨':
            role = discord.utils.get(guild.roles, name='counter-strike')
            await payload.member.add_roles(role)
        elif payload.emoji.name == '🇷':
            role = discord.utils.get(guild.roles, name='rainbow 6')
            await payload.member.add_roles(role)
        elif payload.emoji.name == 'O':
            role = discord.utils.get(guild.roles, name='phasmophobia')
            await payload.member.add_roles(role)

    async def on_raw_reaction_remove(self, payload):

        if payload.message_id != self.target_message_id:
            return

        guild = client.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)

        if payload.emoji.name == '🇻':
            role = discord.utils.get(guild.roles, name='valorant')
            await member.remove_roles(role)
        elif payload.emoji.name == '🇵':
            role = discord.utils.get(guild.roles, name='pubg')
            await member.remove_roles(role)
        elif payload.emoji.name == '🇼':
            role = discord.utils.get(guild.roles, name='warzone/cod')
            await member.remove_roles(role)
        elif payload.emoji.name == '🇲':
            role = discord.utils.get(guild.roles, name='minecraft')
            await member.remove_roles(role)
        elif payload.emoji.name == '🇨':
            role = discord.utils.get(guild.roles, name='counter-strike')
            await member.remove_roles(role)
        elif payload.emoji.name == '🇷':
            role = discord.utils.get(guild.roles, name='rainbow 6')
            await member.remove_roles(role)
        elif payload.emoji.name == 'O':
            role = discord.utils.get(guild.roles, name='phasmophobia')
            await member.remove_roles(role)



intents = discord.Intents.default()
intents.members = True

token = os.environ.get('DISCORD_TOKEN')
client = MyClient(intents=intents)
client.run(token)