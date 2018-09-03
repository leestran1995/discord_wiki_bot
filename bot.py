import discord
import requests
from discord.ext import commands

bot = commands.Bot(command_prefix='$', description='A bot that does a thing')
	
@bot.command()
async def ping(ctx):
	latency = bot.latency 
	await ctx.send(latency)
	
@bot.command()
async def echo(ctx, *, content:str):
	await ctx.send(content)
	
@bot.command()
async def count(ctx):
	global counting_num
	counting_num += 1
	await ctx.send(counting_num)
	
@bot.command()
async def wiki_summary(ctx, *, content:str):
	url = 'https://en.wikipedia.org/api/rest_v1/page/summary/'
	resp = requests.get(url + content)
	data = resp.json()
	
	if data['type'] == 'disambiguation':
		await ctx.send("There were multiple results for your search, can you try being more specific?")
	elif resp.status_code == 200:
		await ctx.send(data['extract'])
	else:
		await ctx.send("I'm sorry, I couldn't find a page for {}".format(content))
		
@bot.command()
async def wiki_random(ctx):
	url = 'https://en.wikipedia.org/api/rest_v1/page/random/title'
	resp = requests.get(url)
	data = resp.json()
	title = data['items'][0]['title']
	url = 'https://en.wikipedia.org/api/rest_v1/page/summary/' + title 
	resp = requests.get(url)
	data = resp.json()
	await ctx.send("Here's what I found for: {}".format(data['title']))
	await ctx.send(data['extract'])
	
@bot.command()
async def info(ctx):
	await ctx.send("Here's a list of things I can do!\n\n" \
					"ping: Get your server latency in milliseconds\n\n" \
					"echo: I'll repeat whatever you say\n\n" \
					"count: Let's see how high the server can count!\n\n" \
					"wiki_summary: Follow this command with a page title and I'll give you" \
					"the summary for the article, if I can find it!\n\n" \
					"wiki_random: I'll find a random wikipedia article and give you the summary!")
					
		
		
	
bot.run('NDg1OTM3Njg0MDY2MzM2Nzcz.Dm39Kg.vtwHclLyNoZvIujfhxDKM28b5TI')
