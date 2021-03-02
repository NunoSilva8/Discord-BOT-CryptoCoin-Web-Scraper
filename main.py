import discord
import requests
from bs4 import BeautifulSoup
from os import environ

TOKEN = environ['TOKEN']
client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(msg):
    if (msg.author == client.user):
        return

    if (msg.content == '!bitcoin'):

        page = requests.get(
            'https://coinmarketcap.com/currencies/bitcoin/markets/')
        soup = BeautifulSoup(page.content, 'html.parser')

        page2 = requests.get('https://www.coingecko.com/pt/moedas/bitcoin')
        soup2 = BeautifulSoup(page2.content, 'html.parser')

        current_result_value = soup.find_all(
            'div', class_='priceValue___11gHJ')

        all_results_values = soup2.find_all('span', class_='no-wrap')
        all_results_percentage = soup2.find_all('span', class_='text-green')

        await msg.channel.send('```[BITCOIN]\nValor atual: {} -> {}\nBaixo de 24h: {}\nAlto de 24h: {}\nBaixo de 7 dias: {}\nAlto de 7 dias: {}```'.format(
            current_result_value[0].get_text(), all_results_percentage[0].get_text(), all_results_values[9].get_text(), all_results_values[10].get_text(), all_results_values[11].get_text(), all_results_values[12].get_text()))

    if (msg.content == '!ethereum'):

        page = requests.get(
            'https://coinmarketcap.com/currencies/ethereum/')
        soup = BeautifulSoup(page.content, 'html.parser')

        page2 = requests.get('https://www.coingecko.com/pt/moedas/ethereum')
        soup2 = BeautifulSoup(page2.content, 'html.parser')

        current_result_value = soup.find_all(
            'div', class_='priceValue___11gHJ')

        all_results_values = soup2.find_all('span', class_='no-wrap')
        all_results_percentage = soup2.find_all('span', class_='text-green')

        await msg.channel.send('```[ETHEREUM]\nValor atual: {} -> {}\nBaixo de 24h: {}\nAlto de 24h: {}\nBaixo de 7 dias: {}\nAlto de 7 dias: {}```'.format(
            current_result_value[0].get_text(), all_results_percentage[0].get_text(), all_results_values[8].get_text(), all_results_values[9].get_text(), all_results_values[10].get_text(), all_results_values[11].get_text()))

    if (msg.content == '!binance'):

        page = requests.get(
            'https://coinmarketcap.com/currencies/binance-coin/')
        soup = BeautifulSoup(page.content, 'html.parser')

        page2 = requests.get(
            'https://www.coingecko.com/pt/moedas/binance-coin')
        soup2 = BeautifulSoup(page2.content, 'html.parser')

        current_result_value = soup.find_all(
            'div', class_='priceValue___11gHJ')

        all_results_values = soup2.find_all('span', class_='no-wrap')
        all_results_percentage = soup2.find_all('span', class_='text-green')

        await msg.channel.send('```[BINANCE COIN]\nValor atual: {} -> {}\nBaixo de 24h: {}\nAlto de 24h: {}\nBaixo de 7 dias: {}\nAlto de 7 dias: {}```'.format(
            current_result_value[0].get_text(), all_results_percentage[0].get_text(), all_results_values[9].get_text(), all_results_values[10].get_text(), all_results_values[11].get_text(), all_results_values[12].get_text()))

    if (msg.content == '!litecoin'):

        page = requests.get(
            'https://coinmarketcap.com/currencies/litecoin/')
        soup = BeautifulSoup(page.content, 'html.parser')

        page2 = requests.get('https://www.coingecko.com/pt/moedas/litecoin')
        soup2 = BeautifulSoup(page2.content, 'html.parser')

        current_result_value = soup.find_all(
            'div', class_='priceValue___11gHJ')

        all_results_values = soup2.find_all('span', class_='no-wrap')
        all_results_percentage = soup2.find_all('span', class_='text-green')

        await msg.channel.send('```[LITECOIN]\nValor atual: {} -> {}\nBaixo de 24h: {}\nAlto de 24h: {}\nBaixo de 7 dias: {}\nAlto de 7 dias: {}```'.format(
            current_result_value[0].get_text(), all_results_percentage[0].get_text(), all_results_values[8].get_text(), all_results_values[9].get_text(), all_results_values[10].get_text(), all_results_values[11].get_text()))

    if (msg.content == '!bitcoincash'):

        page = requests.get(
            'https://coinmarketcap.com/currencies/bitcoin-cash/')
        soup = BeautifulSoup(page.content, 'html.parser')

        page2 = requests.get(
            'https://www.coingecko.com/pt/moedas/bitcoin-cash')
        soup2 = BeautifulSoup(page2.content, 'html.parser')

        current_result_value = soup.find_all(
            'div', class_='priceValue___11gHJ')

        all_results_values = soup2.find_all('span', class_='no-wrap')
        all_results_percentage = soup2.find_all('span', class_='text-green')

        await msg.channel.send('```[BITCOIN CASH]\nValor atual: {} -> {}\nBaixo de 24h: {}\nAlto de 24h: {}\nBaixo de 7 dias: {}\nAlto de 7 dias: {}```'.format(
            current_result_value[0].get_text(), all_results_percentage[0].get_text(), all_results_values[8].get_text(), all_results_values[9].get_text(), all_results_values[10].get_text(), all_results_values[11].get_text()))

    if (msg.content == '!monero'):

        page = requests.get(
            'https://coinmarketcap.com/currencies/monero/')
        soup = BeautifulSoup(page.content, 'html.parser')

        page2 = requests.get('https://www.coingecko.com/pt/moedas/monero')
        soup2 = BeautifulSoup(page2.content, 'html.parser')

        current_result_value = soup.find_all(
            'div', class_='priceValue___11gHJ')

        all_results_values = soup2.find_all('span', class_='no-wrap')
        all_results_percentage = soup2.find_all('span', class_='text-green')

        await msg.channel.send('```[MONERO]\nValor atual: {} -> {}\nBaixo de 24h: {}\nAlto de 24h: {}\nBaixo de 7 dias: {}\nAlto de 7 dias: {}```'.format(
            current_result_value[0].get_text(), all_results_percentage[0].get_text(), all_results_values[8].get_text(), all_results_values[9].get_text(), all_results_values[10].get_text(), all_results_values[11].get_text()))

    if (msg.content == '!bitcoinsv'):

        page = requests.get(
            'https://coinmarketcap.com/currencies/bitcoin-sv/')
        soup = BeautifulSoup(page.content, 'html.parser')

        page2 = requests.get('https://www.coingecko.com/pt/moedas/bitcoin-sv')
        soup2 = BeautifulSoup(page2.content, 'html.parser')

        current_result_value = soup.find_all(
            'div', class_='priceValue___11gHJ')

        all_results_values = soup2.find_all('span', class_='no-wrap')
        all_results_percentage = soup2.find_all('span', class_='text-green')

        await msg.channel.send('```[BITCOIN SV]\nValor atual: {} -> {}\nBaixo de 24h: {}\nAlto de 24h: {}\nBaixo de 7 dias: {}\nAlto de 7 dias: {}```'.format(
            current_result_value[0].get_text(), all_results_percentage[0].get_text(), all_results_values[8].get_text(), all_results_values[9].get_text(), all_results_values[10].get_text(), all_results_values[11].get_text()))

    if (msg.content == '!maker'):

        page = requests.get(
            'https://coinmarketcap.com/currencies/maker/')
        soup = BeautifulSoup(page.content, 'html.parser')

        page2 = requests.get('https://www.coingecko.com/pt/moedas/maker')
        soup2 = BeautifulSoup(page2.content, 'html.parser')

        current_result_value = soup.find_all(
            'div', class_='priceValue___11gHJ')

        all_results_values = soup2.find_all('span', class_='no-wrap')
        all_results_percentage = soup2.find_all('span', class_='text-green')

        await msg.channel.send('```[MAKER]\nValor atual: {} -> {}\nBaixo de 24h: {}\nAlto de 24h: {}\nBaixo de 7 dias: {}\nAlto de 7 dias: {}```'.format(
            current_result_value[0].get_text(), all_results_percentage[0].get_text(), all_results_values[10].get_text(), all_results_values[11].get_text(), all_results_values[12].get_text(), all_results_values[13].get_text()))

    if (msg.content == '!dash'):

        page = requests.get(
            'https://coinmarketcap.com/currencies/dash/')
        soup = BeautifulSoup(page.content, 'html.parser')

        page2 = requests.get('https://www.coingecko.com/pt/moedas/dash')
        soup2 = BeautifulSoup(page2.content, 'html.parser')

        current_result_value = soup.find_all(
            'div', class_='priceValue___11gHJ')

        all_results_values = soup2.find_all('span', class_='no-wrap')
        all_results_percentage = soup2.find_all('span', class_='text-green')

        await msg.channel.send('```[DASH]\nValor atual: {} -> {}\nBaixo de 24h: {}\nAlto de 24h: {}\nBaixo de 7 dias: {}\nAlto de 7 dias: {}```'.format(
            current_result_value[0].get_text(), all_results_percentage[0].get_text(), all_results_values[8].get_text(), all_results_values[9].get_text(), all_results_values[10].get_text(), all_results_values[11].get_text()))

    if (msg.content == '!zcash'):

        page = requests.get(
            'https://coinmarketcap.com/currencies/zcash/')
        soup = BeautifulSoup(page.content, 'html.parser')

        page2 = requests.get('https://www.coingecko.com/pt/moedas/zcash')
        soup2 = BeautifulSoup(page2.content, 'html.parser')

        current_result_value = soup.find_all(
            'div', class_='priceValue___11gHJ')

        all_results_values = soup2.find_all('span', class_='no-wrap')
        all_results_percentage = soup2.find_all('span', class_='text-green')

        await msg.channel.send('```[ZCASH]\nValor atual: {} -> {}\nBaixo de 24h: {}\nAlto de 24h: {}\nBaixo de 7 dias: {}\nAlto de 7 dias: {}```'.format(
            current_result_value[0].get_text(), all_results_percentage[0].get_text(), all_results_values[9].get_text(), all_results_values[10].get_text(), all_results_values[11].get_text(), all_results_values[12].get_text()))

    if (msg.content == '!prices'):
        mensagem_final = '```'

        # BITCOIN
        page1 = requests.get(
            'https://coinmarketcap.com/currencies/bitcoin/markets/')
        soup1 = BeautifulSoup(page1.content, 'html.parser')

        page2 = requests.get('https://www.coingecko.com/pt/moedas/bitcoin')
        soup2 = BeautifulSoup(page2.content, 'html.parser')

        current_result_value1 = soup1.find_all(
            'div', class_='priceValue___11gHJ')

        all_results_percentage2 = soup2.find_all('span', class_='text-green')

        mensagem_final = mensagem_final + '[BITCOIN]\nValor atual: {} -> {}\n\n'.format(
            current_result_value1[0].get_text(), all_results_percentage2[0].get_text())

        # ETHEREUM
        page3 = requests.get(
            'https://coinmarketcap.com/currencies/ethereum/')
        soup3 = BeautifulSoup(page3.content, 'html.parser')

        page4 = requests.get('https://www.coingecko.com/pt/moedas/ethereum')
        soup4 = BeautifulSoup(page4.content, 'html.parser')

        current_result_value3 = soup3.find_all(
            'div', class_='priceValue___11gHJ')

        all_results_percentage4 = soup4.find_all('span', class_='text-green')

        mensagem_final = mensagem_final + '[ETHEREUM]\nValor atual: {} -> {}\n\n'.format(
            current_result_value3[0].get_text(), all_results_percentage4[0].get_text())

        # BINANCE
        page5 = requests.get(
            'https://coinmarketcap.com/currencies/binance-coin/')
        soup5 = BeautifulSoup(page5.content, 'html.parser')

        page6 = requests.get(
            'https://www.coingecko.com/pt/moedas/binance-coin')
        soup6 = BeautifulSoup(page6.content, 'html.parser')

        current_result_value5 = soup5.find_all(
            'div', class_='priceValue___11gHJ')

        all_results_percentage6 = soup6.find_all('span', class_='text-green')

        mensagem_final = mensagem_final + '[BINANCE COIN]\nValor atual: {} -> {}\n\n'.format(
            current_result_value5[0].get_text(), all_results_percentage6[0].get_text())

        # LITECOIN
        page7 = requests.get(
            'https://coinmarketcap.com/currencies/litecoin/')
        soup7 = BeautifulSoup(page7.content, 'html.parser')

        page8 = requests.get('https://www.coingecko.com/pt/moedas/litecoin')
        soup8 = BeautifulSoup(page8.content, 'html.parser')

        current_result_value7 = soup7.find_all(
            'div', class_='priceValue___11gHJ')

        all_results_percentage8 = soup8.find_all('span', class_='text-green')

        mensagem_final = mensagem_final + '[LITECOIN]\nValor atual: {} -> {}\n\n'.format(
            current_result_value7[0].get_text(), all_results_percentage8[0].get_text())

        # BITCOIN CASH
        page9 = requests.get(
            'https://coinmarketcap.com/currencies/bitcoin-cash/')
        soup9 = BeautifulSoup(page9.content, 'html.parser')

        page10 = requests.get(
            'https://www.coingecko.com/pt/moedas/bitcoin-cash')
        soup10 = BeautifulSoup(page10.content, 'html.parser')

        current_result_value9 = soup9.find_all(
            'div', class_='priceValue___11gHJ')

        all_results_percentage10 = soup10.find_all('span', class_='text-green')

        mensagem_final = mensagem_final + '[BITCOIN CASH]\nValor atual: {} -> {}\n\n'.format(
            current_result_value9[0].get_text(), all_results_percentage10[0].get_text())

        # MONERO
        page11 = requests.get(
            'https://coinmarketcap.com/currencies/monero/')
        soup11 = BeautifulSoup(page11.content, 'html.parser')

        page12 = requests.get('https://www.coingecko.com/pt/moedas/monero')
        soup12 = BeautifulSoup(page12.content, 'html.parser')

        current_result_value11 = soup11.find_all(
            'div', class_='priceValue___11gHJ')

        all_results_percentage12 = soup12.find_all('span', class_='text-green')

        mensagem_final = mensagem_final + '[MONERO]\nValor atual: {} -> {}\n\n'.format(
            current_result_value11[0].get_text(), all_results_percentage12[0].get_text())

        # BITCOIN SV
        page13 = requests.get(
            'https://coinmarketcap.com/currencies/bitcoin-sv/')
        soup13 = BeautifulSoup(page13.content, 'html.parser')

        page14 = requests.get('https://www.coingecko.com/pt/moedas/bitcoin-sv')
        soup14 = BeautifulSoup(page14.content, 'html.parser')

        current_result_value13 = soup13.find_all(
            'div', class_='priceValue___11gHJ')

        all_results_percentage14 = soup14.find_all('span', class_='text-green')

        mensagem_final = mensagem_final + '[BITCOIN SV]\nValor atual: {} -> {}\n\n'.format(
            current_result_value13[0].get_text(), all_results_percentage14[0].get_text())

        # MAKER
        page15 = requests.get(
            'https://coinmarketcap.com/currencies/maker/')
        soup15 = BeautifulSoup(page15.content, 'html.parser')

        page16 = requests.get('https://www.coingecko.com/pt/moedas/maker')
        soup16 = BeautifulSoup(page16.content, 'html.parser')

        current_result_value15 = soup15.find_all(
            'div', class_='priceValue___11gHJ')

        all_results_percentage16 = soup16.find_all('span', class_='text-green')

        mensagem_final = mensagem_final + '[MAKER]\nValor atual: {} -> {}\n\n'.format(
            current_result_value15[0].get_text(), all_results_percentage16[0].get_text())

        # DASH
        page17 = requests.get(
            'https://coinmarketcap.com/currencies/dash/')
        soup17 = BeautifulSoup(page17.content, 'html.parser')

        page18 = requests.get('https://www.coingecko.com/pt/moedas/dash')
        soup18 = BeautifulSoup(page18.content, 'html.parser')

        current_result_value17 = soup17.find_all(
            'div', class_='priceValue___11gHJ')

        all_results_percentage18 = soup18.find_all('span', class_='text-green')

        mensagem_final = mensagem_final + '[DASH]\nValor atual: {} -> {}\n\n'.format(
            current_result_value17[0].get_text(), all_results_percentage18[0].get_text())

        # ZCASH
        page19 = requests.get(
            'https://coinmarketcap.com/currencies/zcash/')
        soup19 = BeautifulSoup(page19.content, 'html.parser')

        page20 = requests.get('https://www.coingecko.com/pt/moedas/zcash')
        soup20 = BeautifulSoup(page20.content, 'html.parser')

        current_result_value19 = soup19.find_all(
            'div', class_='priceValue___11gHJ')

        all_results_percentage20 = soup20.find_all('span', class_='text-green')

        mensagem_final = mensagem_final + '[ZCASH]\nValor atual: {} -> {}\n\n'.format(
            current_result_value19[0].get_text(), all_results_percentage20[0].get_text())

        mensagem_final = mensagem_final + '```'
        await msg.channel.send(mensagem_final)

    if (msg.content == '!juvenal'):
        await msg.channel.send('O Juvenal é lindo!')

    if (msg.content == '!diego'):
        await msg.channel.send('Então, estás-te a passar?')

    if (msg.content == '!lopes'):
        await msg.channel.send('Gostas de ler?')

    if (msg.content == '!espama'):
        await msg.channel.send('Olá, eu gosto de abanar a cabeça quando não estou a ouvir música nenhuma nos meus headphones!')

    if (msg.content == '!toribio'):
        await msg.channel.send('NI||NJ||A')

client.run(TOKEN)
