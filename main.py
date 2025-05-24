import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from cryptoUtils import caesarBruteForce

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

# Command that convert a utf8 string to hexadecimal
@bot.tree.command(name="tohex", description="Convert a utf8 string to hexadecimal")
async def to_hex(interaction: discord.Interaction, text: str):
    hex_string = text.encode("utf-8").hex()
    await interaction.response.send_message(f"Hexadecimal: {hex_string}")

# Command that convert a hexadecimal string to utf8
@bot.tree.command(name="fromhex", description="Convert a hexadecimal string to utf8")
async def from_hex(interaction: discord.Interaction, hex_string: str):
    try:
        utf8_string = bytes.fromhex(hex_string).decode("utf-8")
        await interaction.response.send_message(f"UTF-8 String: {utf8_string}")
    except ValueError:
        await interaction.response.send_message("Invalid hexadecimal string.", ephemeral=True)

# Command who decrypt a caesar cipher
@bot.tree.command(name="caesar", description="Decrypt a caesar cipher")
async def caesar(interaction: discord.Interaction, text: str):
    decrypted_texts = caesarBruteForce(text)[1:]
    embed = discord.Embed(title="Caesar Cipher Decryption", description="Decrypted texts for all shifts:")
    for i, decrypted_text in enumerate(decrypted_texts):
        embed.add_field(name=f"Shift {i+1}", value=decrypted_text, inline=True)
    await interaction.response.send_message(embed=embed)

# Run the bot with your token
bot.run(TOKEN)

