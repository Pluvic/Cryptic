import discord
import os
from dotenv import load_dotenv
from discord.ext import commands

# Load environment variables from .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
if not TOKEN:
    raise ValueError("No DISCORD_TOKEN found in environment variables")

# Create a bot instance
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

# Event triggered when bot is ready
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(f"Failed to sync commands: {e}")

# Define a slash command
@bot.tree.command(name="hello", description="Prints a hello world message")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message("Hello, world!")

# Run the bot with your token
bot.run(TOKEN)

