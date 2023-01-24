  # For the test, we gotta check proper embed/files/allowed_mentions/view/reference sending
# Also check for imporper embed/files/allowed_mentions/view/reference sending
# Do for both application commands and normal messageable sending
# Also do for original module and my fork

import discord
from discord import File, Embed, AllowedMentions, MessageReference, PartialMessage
from discord.ui import View, Button
from discord.ext import commands

TOKEN = 'Insert a token to play'

bot = commands.Bot(command_prefix='!')

@bot.command()
async def test_improper_kwarg(ctx):
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
        await ctx.send(embeds=[Embed(), Embed, Embed()])
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
    
    # Improper PartialMessage sending
    try:
        await ctx.send(content='PartialMessage', reference=PartialMessage)
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

@bot.command()
async def test_proper_kwarg(ctx):
    try:
        await ctx.send(embed=Embed())
        await ctx.send(embeds=[Embed(), Embed(), Embed()])
        view = View()
        view.add_item(Button())
        await ctx.send(view=view)
        await ctx.send(file=File('image.png'))
        await ctx.send(files=[File('image.png'), File('image.png')])
        await ctx.send(content='Allowed mentions!! @everyone', allowed_mentions=[AllowedMentions(everyone=True)])
        await ctx.send(content='MessageReference', refernce=MessageReference(message_id=ctx.message.id, channel_id=ctx.channel.id))
        await ctx.send(content='PartialMessage', reference=PartialMessage(channel=ctx.channel, id='what the hellllll oh my goddd'))
    except Exception as e:
        await ctx.send(f'''
            An error occured. This is the error:
            ```
            {repr(e)}
            ```
        ''')






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
    await ctx.respond(embed=Embed())



@bot.slash_command()
async def test_improper_embed_list(ctx):
    # Improper embeds list sending
    try:
        await ctx.respond(embeds=[Embed(), Embed, Embed()])
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
    await ctx.respond(embeds=[Embed(), Embed(), Embed()])



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
    view.add_item(Button())
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
    await ctx.respond(content='Allowed mentions!! @everyone', allowed_mentions=[AllowedMentions(everyone=True)])



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

@bot.slash_command()
async def test_proper_messenge_reference(ctx):
    await ctx.respond(content='MessageReference', refernce=MessageReference(message_id=ctx.message.id, channel_id=ctx.channel.id))



@bot.slash_command()
async def test_improper_partial_message(ctx):
    # Improper PartialMessage sending
    try:
        await ctx.respond(content='PartialMessage', reference=PartialMessage)
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

@bot.slash_command()
async def test_proper_partial_message(ctx):
    await ctx.respond(content='PartialMessage', reference=PartialMessage(channel=ctx.channel, id='what the hellllll oh my goddd'))

    
bot.run(TOKEN)
