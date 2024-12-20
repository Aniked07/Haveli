'''copyright @aniked
ig = aniked_heikham
github = aniked07'''




import discord
from discord.ext import commands
import asyncio
from gtts import gTTS
from discord import FFmpegPCMAudio
import os


TOKEN = 'bot token'


intents = discord.Intents.default()
intents.voice_states = True  
intents.guilds = True


bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_voice_state_update(member, before, after):

    if after.channel and (not before.channel or before.channel != after.channel):
        try:

            if member.guild.voice_client:
                await member.guild.voice_client.disconnect()

 
            vc = await after.channel.connect()

            await asyncio.sleep(2)

        
            message = f"Welcome to Haveli's voice Chat , Enjoy your stay,ji!"
            tts = gTTS(text=message, lang='hi', slow=True)  
            tts_file = "welcome.mp3"
            tts.save(tts_file)

            
            vc.play(FFmpegPCMAudio(tts_file), after=lambda e: print("Finished playing audio."))
            while vc.is_playing():
                await asyncio.sleep(1)

            
            await vc.disconnect()
            os.remove(tts_file)

        except Exception as e:
            print(f"Error: {e}")

bot.run(TOKEN)




















'''import discord
from discord.ext import commands
from gtts import gTTS
from discord import FFmpegPCMAudio
import os
import asyncio

# Replace this with your actual bot token
TOKEN = 'MTMxOTE0NzcwNDkwNjk0MDUwNw.G2CXh3.ovucNJGxVJdxGDShMWoGyLabCqI8YoiOIgXf9g'

# Intents
intents = discord.Intents.default()
intents.voice_states = True  # To track voice state changes
intents.guilds = True

# Bot Setup
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_voice_state_update(member, before, after):
    # Trigger only when a user joins a new voice channel
    if not before.channel and after.channel:
        try:
            # Connect to the voice channel
            vc = await after.channel.connect()

            # Generate TTS welcome message
            welcome_message = f"Welcome to Haveli, Boss!"
            tts = gTTS(text=welcome_message, lang='en')
            tts_file = "welcome.mp3"
            tts.save(tts_file)

            # Play the welcome message
            audio = FFmpegPCMAudio(tts_file)
            vc.play(audio, after=lambda e: print("Finished playing audio."))

            # Wait for the audio to finish
            while vc.is_playing():
                await asyncio.sleep(1)

            # Disconnect and clean up
            await vc.disconnect()
            os.remove(tts_file)

        except Exception as e:
            print(f"Error: {e}")

bot.run(TOKEN)'''

