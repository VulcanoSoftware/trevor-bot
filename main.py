import discord
from discord import app_commands
import asyncio

TOKEN = "TOKEN" 

class MyBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def on_ready(self):
        print(f"Ingelogd als {self.user}")
        try:
            synced = await self.tree.sync()
            print(f"Synced {len(synced)} commands.")
        except Exception as e:
            print(f"Fout bij synchroniseren: {e}")

bot = MyBot()

@bot.tree.command(name="musictip", description="Get music suggestions to use with VulcanoMusic")
async def music(interaction: discord.Interaction):
    # Create the embed to send
    embed = discord.Embed(
        title="Music Links",
        description="Here are your direct and indirect music links:\n\n",
        color=discord.Color.blue()
    )
    
    # Direct YouTube Link
    embed.add_field(name="Direct YouTube Link", value="/play query: https://www.youtube.com/watch?v=YCCDQfYMo0s", inline=False)
    
    # Indirect YouTube Link
    embed.add_field(name="Indirect YouTube Link", value="/play query: https://vulcanolinks.pages.dev/rickroll", inline=False)
    
    # Direct Spotify Link
    embed.add_field(name="Direct Spotify Link", value="/play query: https://open.spotify.com/track/1J03Vp93ybKIxfzYI4YJtL?si=c3bfefc811eb4cba", inline=False)
    
    # Indirect Spotify Link
    embed.add_field(name="Indirect Spotify Link", value="/play query: https://links.vulcanocraft.is-a.dev/megaspot", inline=False)
    
    # Direct Audio Link
    embed.add_field(name="Direct Audio Link", value="/play query: https://drive.google.com/uc?export=download&id=1dB5Pe6PvsZcKPRaHeivOwwHx2O9faaDp", inline=False)
    
    # Indirect Audio Link
    embed.add_field(name="Indirect Audio Link", value="/play query: https://vulcanolinks.pages.dev/tom", inline=False)
    
    # Direct SoundCloud Link
    embed.add_field(name="Direct SoundCloud Link", value="/play query: https://soundcloud.com/justaddictive/rick-astley-never-gonna-give-you-up-sterbinszky-disco-remix-1?utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing", inline=False)
    
    # Indirect SoundCloud Link
    embed.add_field(name="Indirect SoundCloud Link", value="/play query: https://links.vulcanocraft.is-a.dev/marioc", inline=False)
    
    # Send the embed
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="active-dev-badge", description="Claim your Active Developer Badge")
async def active_dev_badge(interaction: discord.Interaction):
    embed = discord.Embed(
        title="🤖 Command Ran Successfully",
        description="You have successfully executed the command to get the **Active Developer Badge**!\n\n"
                    "After Discord processes the execution of the command, **you** will be able to claim the badge "
                    "by pressing the button below. Please note that Discord may take up to **24 hours** to process your eligibility.\n\n"
                    f"_You've first ran this command **{interaction.created_at.strftime('%B %d, %Y %I:%M %p')}**_",
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url=interaction.user.display_avatar.url)
    view = discord.ui.View()
    button = discord.ui.Button(label="Check Status", url="https://discord.com/developers/active-developer", style=discord.ButtonStyle.primary)
    view.add_item(button)
    await interaction.response.send_message(embed=embed, view=view, ephemeral=True)

@bot.tree.command(name="cj", description="What does CJ say?")
async def cj_command(interaction: discord.Interaction):
    await interaction.response.send_message("ah shit, here we go again")

@bot.tree.command(name="insults", description="If you want me to insult you, just say it.")
async def insults(interaction: discord.Interaction):
    messages = [
        "You look like you struggle with simple tasks.\n=====================================================================",
        "Did you lose a very big bet?\n=====================================================================", 
        "Why hasn't someone sensible shot you yet? 🔫\n=====================================================================", 
        "Oh, you really suck. 🍆\n=====================================================================", 
        "Idiot!\n=====================================================================",
        "Fool!\n=====================================================================",
        "Moron!\n=====================================================================",
        "You're a waste of space on this Earth! 🌍\n=====================================================================",
        "I've trodden shits with more brains! 🧠\n=====================================================================",
        "You make me want to emigrate. ✈️\n=====================================================================",
        "You make me want a lobotomy!\n=====================================================================",
        "You're a total moron.\n=====================================================================",
        "You dumbass.\n=====================================================================",
        "Brainless fool!\n=====================================================================",
        "Why, oh why do you exist?\n=====================================================================",
        "Why, oh why weren't you drowned at birth?\n=====================================================================",
        "Listen, nobody likes you.\n=====================================================================",
        "Listen, even your parents can't stand you!\n=====================================================================",
        "Argh, you give me hives.\n=====================================================================",
        "You are utterly ridiculous.\n====================================================================="
    ]
    embed = discord.Embed(title="Insulting ...", description="Thinking of insults ...", color=discord.Color.red())
    await interaction.response.send_message(embed=embed)
    for msg in messages:
        await interaction.channel.send(msg)
    new_embed = discord.Embed(title="Insulted", description="You have been insulted.", color=discord.Color.red())
    new_embed.set_image(url="https://i.giphy.com/media/kNnuXduMMcnReOdlb1/giphy.gif")
    await interaction.edit_original_response(embed=new_embed)

@bot.tree.command(name="angry", description="Wanna make me angry huh?")
async def angry(interaction: discord.Interaction):
    messages = [
        "YOU CHUMP!\n=====================================================================",
        "IDIOT!\n=====================================================================",
        "YOU MORON!\n=====================================================================",
        "HOW ARE YOU ALLOWED TO WALK THE STREETS, MORON?!\n=====================================================================",
        "You asshole!\n=====================================================================",
        "You puddle of vomit!\n=====================================================================",
        "YOU ARE AN ASSHOLE!\n=====================================================================",
        "YOU PILE OF SICK!\n=====================================================================",
        "YOU ARE SUCH AN ASS!\n=====================================================================",
        "TURD!\n=====================================================================",
        "YOU ARE AN IDIOT!\n=====================================================================",
        "You depressing afterthought!\n=====================================================================",
        "You hideous mistake!\n=====================================================================",
        "TWAT!\n=====================================================================",
        "YOU FOOL!\n====================================================================="
    ]
    
    embed = discord.Embed(title="Trevor is angry! 😡", description="Brace yourself...", color=discord.Color.red())
    await interaction.response.send_message(embed=embed)

    for msg in messages:
        await interaction.channel.send(msg)

    gif_embed = discord.Embed(title="asshole! 🤬", description="That was intense...", color=discord.Color.red())
    gif_embed.set_image(url="https://i.giphy.com/media/kNnuXduMMcnReOdlb1/giphy.gif")
    await interaction.channel.send(embed=gif_embed)
    
@bot.tree.command(name="overweight", description="I am going to say things about your big fat mother!")
async def angry(interaction: discord.Interaction):
    messages = [
        "You're a big hunk of love aren't you? A massive, blubbery ball of hot, sexy, CHUBBY LUST! Hey come back here! I was enjoying that thought!\n=====================================================================",
        "Hey, pork chop! How's it going? I said: 'How's it going, pork chop?!' Well that's not very friendly, is it?!\n=====================================================================",
        "Have you ever tried exercising, pork chop? And I don't mean just your arm. Oh there you go! See?! That's not so bad!\n=====================================================================",
        "What's your problem, fatso? I said: 'What's your problem, fatso?!' Oh, come on, where's your sense of humour? DID YA EAT IT?\n=====================================================================",
        "You are large, my friend. I mean, large. Like a big thing! And you've got a shit line in repartee too!\n=====================================================================",
        "Do, uhhh, chubby chasers seek you out? I mean, I can see it being FUN having a BOUNCY, BOUNCY, BOUNCY. Hey, it's not my thing! I think it's revolting!\n=====================================================================",
        "Listen, I think you should give up the comfort eating. I mean, somebody probably loves you! Although I don't know why!\n=====================================================================",
        "My God, you're massive! I mean, you're the size of a house! And you run real funny, too!\n=====================================================================",
        "Food is a drug, and, you're an addict. I mean, for some it's junk, but for you, it's CHEESECAKE! But you all rehab just the same!\n=====================================================================",
        "You're pretty big there, my friend. But, I'm sure someone loves ya! Actually, they probably don't!\n=====================================================================",
        "You're MASSIVE! I mean... You're ffffffffffffat! You'll need more than just jogging!\n=====================================================================",
        "Look at you. You're... Vast. I mean, you're really FUCKING BIG! You should do more of that running! It might help!\n=====================================================================",
        "So... You're a big one, aren't ya? I said: you're pretty big! And boy do you wobble when you move!\n=====================================================================",
        "You're a big ol' thing, aren't ya? Hey, now don't get defensive on me, porkchop! It's not my fault! I didn't eat all that food!\n====================================================================="
    ]
    
    embed = discord.Embed(title="Looking at your mom ... 🥓", description="She is in the mc donalds again 🙄", color=discord.Color.red())
    await interaction.response.send_message(embed=embed)

    for msg in messages:
        await interaction.channel.send(msg)

    gif_embed = discord.Embed(title="Me at de mc donalds", description="i want to order a fat mac menu please 👿", color=discord.Color.red())
    gif_embed.set_image(url="https://iili.io/d6pDnta.gif")
    await interaction.channel.send(embed=gif_embed)

bot.run(TOKEN)
