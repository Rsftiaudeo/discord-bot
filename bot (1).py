import discord
import asyncio
import psutil
import datetime
from datetime import datetime
from discord.ext import commands
bot = commands.Bot(command_prefix= '!')

#client 是我們與 Discord 連結的橋樑
client = discord.Client()
#調用 event 函式庫
@client.event
#當機器人完成啟動時
async def on_ready():
	print(f'目前登入身份：{client.user}')
	game = discord.Game('!help')
	await client.change_presence(status=discord.Status.online, activity=game)
	embed=discord.Embed(title=f":robot:機器人啟動了",timestamp=datetime.utcnow(), color=0x00ff04)
	embed.add_field(name="機器人恢復工作", value=f"現在可以正常使用指令了", inline=False)
	await client.get_channel(983318821916004382).send(content=None, embed=embed)    



#調用 event 函式庫
@client.event
#當有訊息時
async def on_message(message):
    #排除自己的訊息，避免陷入無限循環          

#防止髒髒的話 下面
	if message.content == '幹你娘':
		baduser = {message.author.nick}
		if message.guild.name == '可樂瓶工作室':
			embed=discord.Embed(title=f"一則訊息遭到刪除",timestamp=datetime.utcnow(), color=0xff0000)
			embed.add_field(name="原因", value=f"此伺服器不允許此類的訊息", inline=False)
			await message.channel.send(embed=embed)
			await message.delete()            
#防止髒髒的話 上面

#sleep
	if message.content == "!sleep":
		if message.channel.id == 983317929305190450:	
			await message.channel.send("done!")
			embed=discord.Embed(title=f":robot:機器人暫時關機了",timestamp=datetime.utcnow(), color=0xff0000)
			embed.add_field(name="關機原因", value=f"機器人進行維護", inline=False)
			await client.get_channel(983318821916004382).send(content=None, embed=embed)
			exit()

	newsmessagefrom = 981360025341661214
	if message.channel.id == newsmessagefrom:
		newsmessage = message.content
		embed=discord.Embed(title=f"📢機器人更新",timestamp=datetime.utcnow(), color=0x00ff04)
		embed.add_field(name="更新內容", value=f"{newsmessage}", inline=False)
		embed.set_footer(text=f'發布者: {message.author}')
		await client.get_channel(980769680383959060).send(content=None, embed=embed)      

	if message.content == '!ads':
		await message.channel.send('芒果俱樂部 https://discord.gg/nARYdDsagv ')             
        
	if message.content == '!invite':
		await message.channel.send('https://discord.com/api/oauth2/authorize?client_id=981820750652649472&permissions=8&scope=bot')    
    
	if message.content == "!bot-info":
		servers = len(client.guilds)
		embed=discord.Embed(title=f":crown: 本機器人的資訊",timestamp=datetime.utcnow(), color=0xffc5ab)
		embed.add_field(name="機器人id", value=f"{client.user}", inline=True)
		embed.add_field(name="群組數", value=f"{servers}個", inline=False)
		embed.add_field(name="CPU占用", value=f'{psutil.cpu_percent()}%', inline=True)
		embed.add_field(name="記憶體占用", value=f'{psutil.virtual_memory().percent}%', inline=True)           
		await message.channel.send(embed=embed)
	if message.content == '!help':
		embed=discord.Embed(title=":printer: 幫助頁面", description="版本:1.0", color=0x00cc29)
		embed.add_field(name="!help", value="幫助頁面", inline=True)
		embed.add_field(name="!ads", value="廣告內容", inline=True)
		embed.add_field(name="!invite", value="邀請本機器人", inline=True)
		embed.add_field(name="!status", value="獲取機器人狀態", inline=True)
		embed.add_field(name="!poll", value="了解如和使用投票功能", inline=True)
		embed.add_field(name="!server-info", value="獲得該伺服器的資訊", inline=True)
		embed.add_field(name="!user-info", value="獲取使用者資訊", inline=True)
		embed.set_footer(text="本機器人由 可樂瓶工作室負責維護以及編寫")
		await message.channel.send(content=None, embed=embed)

	if message.content == '!status':    
		embed=discord.Embed(title=":chart_with_upwards_trend: 機器人狀態", description="版本:1.0",timestamp=datetime.utcnow(), color=0x31a300)
		embed.add_field(name="連線品質", value=":white_check_mark: 非常穩定！！！！", inline=True)
		await message.channel.send(content=None, embed=embed)        
    
	if message.content.startswith('!poll'):
      #分割訊息成兩份
		tmp = message.content.split(" ",1)
      #如果分割後串列長度只有1
		if len(tmp) < 2:
			await message.channel.send("用法 !poll [投票內容]")
		else:
			embed=discord.Embed(title=":police_officer: 投票", description=f"題目:{tmp[1]}\n\n是=👍\n\n否=👎",timestamp=datetime.utcnow(), color=0x00ff2a)
			embed.set_footer(text=f"發起者: {message.author}")
			poll = await message.channel.send(embed=embed)
			await poll.add_reaction("👍")
			await poll.add_reaction("👎")            
			print(f'{message.author.display_name} 在 {message.guild.name} 創建了一個提問 題目:{tmp[1]}')
			channel = client.get_channel(980771355433762816)
			#await channel.send(f'後臺發送: {message.author} 在 {message.guild.name} 創建了一個提問 題目:{tmp[1]} ')
            


	if message.content == '!server-info':
		embed=discord.Embed(title=":man_teacher: 此伺服器的資訊",timestamp=datetime.utcnow(), color=0x00ff88)
		embed.set_thumbnail(url=f'{message.guild.icon_url}')
		embed.add_field(name=f"伺服器名稱", value=f"{message.guild.name}", inline=True)
		embed.add_field(name=f"伺服器人數", value=f"{message.guild.member_count}人", inline=True)
		embed.add_field(name=f"擁有者", value=f"<@{message.guild.owner_id}>", inline=True)
		embed.add_field(name=f"創建時間", value=f"{message.guild.created_at}", inline=True)
		await message.channel.send(embed=embed)
            
	if message.content == '!user-info':
		embed=discord.Embed(title=f":vertical_traffic_light: {message.author}的資料",timestamp=datetime.utcnow(), color=0xffc5ab)
		embed.add_field(name="名稱：", value=f"{message.author}", inline=False)
		embed.add_field(name="暱稱：", value=f"{message.author.nick}", inline=False)
		embed.add_field(name="Discord id：", value=f"{message.author.id}", inline=False)
		embed.add_field(name="帳號創建時間：", value=f"{message.author.created_at}", inline=False)
		embed.set_thumbnail(url=f'{message.author.avatar_url}')
		await message.channel.send(embed=embed)


        #這邊設定機器人的狀態
    #discord.Status.<狀態>，可以是online（上線）,offline（下線）,idle（閒置）,dnd（請勿打擾）,invisible（隱身）
status_w = discord.Status.dnd

    #這邊設定機器當前的狀態文字
    #type可以是playing（遊玩中）、streaming（直撥中）、listening（聆聽中）、watching（觀看中）、custom（自定義）


client.run('OTgxODIwNzUwNjUyNjQ5NDcy.Gdpe16.qumx6LccPopXS96G3sG2oYLMYf3fvH23OMchpE') #TOKEN 在剛剛 Discord Developer 那邊「BOT」頁面裡面
