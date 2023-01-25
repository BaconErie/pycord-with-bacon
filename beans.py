# This tests Object Checking for Messageable.send and Webhook.send for the Pycord library
# PR #1889 

import discord
from discord import File, Embed, AllowedMentions, MessageReference, PartialMessage
from discord.ui import View, Button
from discord.ext import commands

TOKEN = ''
intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(intents=intents, command_prefix='$')

@bot.command(name='improper')
async def test_improper(ctx):
    print('yo yo yo improper ')
    # Improper embed sending
    try:
        await ctx.send(embed=Embed)
    except Exception as e:
        if str(e) == 'Embeds being sent must be discord.Embed objects, not classes. Have you forgotten parentheses?':
            await ctx.send(
                f'''PASS: Embed object checking passed! Here is output:
                ```
                {str(e)}
                ```'''
            )
        else:
            await ctx.send(
                f'''FAIL: Embed object checking failed! Here is output:
                ```
                {str(e)}
                ```'''
            )
    
    # Improper embeds list sending
    try:
        await ctx.send(embeds=[Embed(description='Improper embeds list'), Embed, Embed(description='Improper embeds list')])
    except Exception as e:
        if str(e) == 'Embeds being sent must be discord.Embed objects, not classes. Have you forgotten parentheses?':
            await ctx.send(
                f'''PASS: Embeds list object checking passed! Here is output:
                ```
                {str(e)}
                ```'''
            )
        else:
            await ctx.send(
                f'''FAIL: Embeds list object checking failed! Here is output:
                ```
                {str(e)}
                ```'''
            )
    
    # Improper view sending
    try:
        await ctx.send(view=View)
    except Exception as e:
        if str(e) == 'The view you passed, View, should be an object, not a class. Have you forgotten parentheses?':
            await ctx.send(
                f'''PASS: View object checking passed! Here is output:
                ```
                {str(e)}
                ```'''
            )
        else:
            await ctx.send(
                f'''FAIL: View object checking failed! Here is output:
                ```
                {str(e)}
                ```'''
            )
    

    # Improper file sending
    try:
        await ctx.send(file=File)
    except Exception as e:
        if str(e) == 'Files being sent should be discord.File objects, not classes. Have you forgotten parentheses?':
            await ctx.send(
                f'''PASS: File object checking passed! Here is output:
                ```
                {str(e)}
                ```'''
            )
        else:
            await ctx.send(
                f'''FAIL: File object checking failed! Here is output:
                ```
                {str(e)}
                ```'''
            )

    # Improper files list sending
    try:
        await ctx.send(files=[File('image.png'), File, File('image.png')])
    except Exception as e:
        if str(e) == 'Files being sent should be discord.File objects, not classes. Have you forgotten parentheses?':
            await ctx.send(
                f'''PASS: Files list object checking passed! Here is output:
                ```
                {str(e)}
                ```'''
            )
        else:
            await ctx.send(
                f'''FAIL: Files list object checking failed! Here is output:
                ```
                {str(e)}
                ```'''
            )
    
    # Improper AllowedMentions sending
    try:
        await ctx.send(content='Hi @everyone', allowed_mentions=AllowedMentions)
    except Exception as e:
        if str(e) == 'The argument you passed into allowed_mentions must be an object, not a class. Have you forgotten parentheses?':
            await ctx.send(
                f'''PASS: AllowedMentions list object checking passed! Here is output:
                ```
                {str(e)}
                ```'''
            )
        else:
            await ctx.send(
                f'''FAIL: AllowedMentions list object checking failed! Here is output:
                ```
                {str(e)}
                ```'''
            )
    
    # Improper MessageReference sending
    try:
        await ctx.send(content='MessageReference', reference=MessageReference)
    except Exception as e:
        if str(e) == 'The argument you passed into reference must be an object, not a class. Have you forgotten parentheses?':
            await ctx.send(
                f'''PASS: MessageReference object checking passed! Here is output:
                ```
                {str(e)}
                ```'''
            )
        else:
            await ctx.send(
                f'''FAIL: MessageReference list object checking failed! Here is output:
                ```
                {str(e)}
                ```'''
            )

    await ctx.send('DONE!')

@bot.command(name='proper')
async def proper(ctx):
    print('yo yo yo proper')
    try:
        await ctx.send(embed=Embed(description='proper embeds'))
        await ctx.send(embeds=[Embed(description='proper embeds list'), Embed(description='proper embeds list'), Embed(description='proper embeds list')])
        view = View()
        view.add_item(Button(label='proper view'))
        await ctx.send(view=view)
        await ctx.send(file=File('image.png'))
        await ctx.send(content='Allowed mentions!! @everyone', allowed_mentions=AllowedMentions(everyone=True))
        await ctx.send(content='MessageReference', reference=MessageReference(message_id=ctx.message.id, channel_id=ctx.channel.id))
    except Exception as e:
        await ctx.send(f'''
            An error occured. This is the error:
            ```
            {repr(e)}
            ```
        ''')

        raise e

    await ctx.send('DONE!') 





@bot.slash_command()
async def test_improper_embed(ctx):
    try:
        await ctx.respond(embed=Embed)
    except Exception as e:
        if str(e) == 'Embeds being sent must be discord.Embed objects, not classes. Have you forgotten parentheses?':
            await ctx.channel.send(
                f'''PASS: Embed object checking passed! Here is output:
                ```
                {str(e)}
                ```'''
            )
        else:
            await ctx.channel.send(
                f'''FAIL: Embed object checking failed! Here is output:
                ```
                {str(e)}
                ```'''
            )

@bot.slash_command()
async def test_proper_embed(ctx):
    await ctx.respond(embed=Embed(description='Proper embed'))



@bot.slash_command()
async def test_improper_embed_list(ctx):
    # Improper embeds list sending
    try:
        await ctx.respond(embeds=[Embed(description='Improper embed list'), Embed, Embed(description='Improper embed list')])
    except Exception as e:
        if str(e) == 'Embeds being sent must be discord.Embed objects, not classes. Have you forgotten parentheses?':
            await ctx.channel.send(
                f'''PASS: Embeds list object checking passed! Here is output:
                ```
                {str(e)}
                ```'''
            )
        else:
            await ctx.channel.send(
                f'''FAIL: Embeds list object checking failed! Here is output:
                ```
                {str(e)}
                ```'''
            )

@bot.slash_command()
async def test_proper_embed_list(ctx):
    await ctx.respond(embeds=[Embed(description='Proper'), Embed(description='embed'), Embed(description='list')])



@bot.slash_command()
async def test_improper_view(ctx):
    # Improper view sending
    try:
        await ctx.respond(view=View)
    except Exception as e:
        if str(e) == 'The view you passed, View, should be an object, not a class. Have you forgotten parentheses?':
            await ctx.channel.send(
                f'''PASS: View object checking passed! Here is output:
                ```
                {str(e)}
                ```'''
            )
        else:
            await ctx.channel.send(
                f'''FAIL: View object checking failed! Here is output:
                ```
                {str(e)}
                ```'''
            )

@bot.slash_command()
async def test_proper_view(ctx):
    view = View()
    view.add_item(Button(label='Proper view'))
    await ctx.respond(view=view)



@bot.slash_command()
async def test_improper_file(ctx):
    # Improper file sending
    try:
        await ctx.respond(file=File)
    except Exception as e:
        if str(e) == 'Files being sent should be discord.File objects, not classes. Have you forgotten parentheses?':
            await ctx.channel.send(
                f'''PASS: File object checking passed! Here is output:
                ```
                {str(e)}
                ```'''
            )
        else:
            await ctx.channel.send(
                f'''FAIL: File object checking failed! Here is output:
                ```
                {str(e)}
                ```'''
            )

@bot.slash_command()
async def test_proper_file(ctx):
    await ctx.respond(file=File('image.png'))



@bot.slash_command()
async def test_improper_file_list(ctx):
    # Improper files list sending
    try:
        await ctx.respond(files=[File('image.png'), File, File('image.png')])
    except Exception as e:
        if str(e) == 'Files being sent should be discord.File objects, not classes. Have you forgotten parentheses?':
            await ctx.channel.send(
                f'''PASS: Files list object checking passed! Here is output:
                ```
                {str(e)}
                ```'''
            )
        else:
            await ctx.channel.send(
                f'''FAIL: Files list object checking failed! Here is output:
                ```
                {str(e)}
                ```'''
            )

@bot.slash_command()
async def test_proper_file_list(ctx):
    await ctx.respond(files=[File('image.png'), File('image.png')])



@bot.slash_command()
async def test_improper_allowed_message(ctx):
    # Improper AllowedMentions sending
    try:
        await ctx.respond(content='Hi @everyone', allowed_mentions=AllowedMentions)
    except Exception as e:
        if str(e) == 'The argument you passed into allowed_mentions must be an object, not a class. Have you forgotten parentheses?':
            await ctx.channel.send(
                f'''PASS: AllowedMentions list object checking passed! Here is output:
                ```
                {str(e)}
                ```'''
            )
        else:
            await ctx.channel.send(
                f'''FAIL: AllowedMentions list object checking failed! Here is output:
                ```
                {str(e)}
                ```'''
            )

@bot.slash_command()
async def test_proper_allowed_message(ctx):
    await ctx.respond(content='Allowed mentions!! @everyone', allowed_mentions=AllowedMentions(everyone=True))



@bot.slash_command()
async def test_improper_message_reference(ctx):
    # Improper MessageReference sending
    try:
        await ctx.respond(content='MessageReference', reference=MessageReference)
    except Exception as e:
        if str(e) == 'The argument you passed into reference must be an object, not a class. Have you forgotten parentheses?':
            await ctx.channel.send(
                f'''PASS: MessageReference object checking passed! Here is output:
                ```
                {str(e)}
                ```'''
            )
        else:
            await ctx.channel.send(
                f'''FAIL: MessageReference list object checking failed! Here is output:
                ```
                {str(e)}
                ```'''
            )

bot.run(TOKEN)
