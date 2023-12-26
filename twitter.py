import feedparser
import asyncio
import discord
from datetime import datetime, timedelta

async def verificar_twitter_periodico(bot, Variables):    
    await bot.wait_until_ready()
    # Analizar el feed RSS
    while not bot.is_closed():
        USER_TWITTER = Variables[1]
        ultimo_tweet = Variables[0]
        ROLE = Variables[2]
        canal_id = Variables[3]
        fecha_ayer = datetime.now() - timedelta(days=1)
        feed_url = f"https://nitter.poast.org/{USER_TWITTER}/rss"
        feed = feedparser.parse(feed_url)
        canal = bot.get_channel(canal_id)
        tweets = []
        messages = []
        role = discord.utils.get(canal.guild.roles, name=ROLE)

        if len(ultimo_tweet) == 0:
            primer_item = feed.entries[0]
            url_primer_item = primer_item.link[:-2].replace("nitter.poast.org", "fxtwitter.com")
            Variables[0] = url_primer_item
            ultimo_tweet = Variables[0]
            mensaje = f"{role.mention} {USER_TWITTER} just tweeted here:\n{ultimo_tweet}"
            await canal.send(mensaje)
        else:
            for i in range(0,5):
                primer_item = feed.entries[i]
                url_primer_item = primer_item.link[:-2].replace("nitter.poast.org", "fxtwitter.com")
                fecha_str = primer_item.published
                fecha_str = fecha_str.rsplit(' ', 1)[0]  # Eliminar la parte 'GMT' al final
                fecha_tweet = datetime.strptime(fecha_str, '%a, %d %b %Y %H:%M:%S')

                # Verificar si el primer tweet es diferente al último
                if url_primer_item != ultimo_tweet and fecha_tweet > fecha_ayer:
                    # Publicar el mensaje en el canal especificado
                    tweets.append(url_primer_item)
                    mensaje = f"{role.mention} {USER_TWITTER} just tweeted here:\n{url_primer_item}"
                    messages.append(mensaje)
                    if i==4:
                        Variables[0] = tweets[0]
                        ultimo_tweet = Variables[0]
                elif i!=0 and url_primer_item == ultimo_tweet:
                    # Actualizar la variable del último tweet
                    Variables[0] = tweets[0]
                    ultimo_tweet = Variables[0]
                    break
                elif i==0 and url_primer_item == ultimo_tweet:
                    break
                else:
                    break    
                
            if len(messages) > 0:
                for msg in messages[::-1]:
                    await canal.send(msg)
                    await asyncio.sleep(10)
        await asyncio.sleep(30)


async def mensaje_de_prueba(ctx, bot, Variables):    
    ultimo_tweet = Variables[0]
    USER_TWITTER = Variables[1]
    ROLE = Variables[2]
    canal = ctx.channel
    await bot.wait_until_ready()
    # Analizar el feed RSS
    role = discord.utils.get(canal.guild.roles, name=ROLE)
    mensaje = f"{role.mention} {USER_TWITTER} just tweeted here:\n{ultimo_tweet}"
    await canal.send(mensaje)