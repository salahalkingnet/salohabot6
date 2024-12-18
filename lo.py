import telebot
import requests
import re
bot = telebot.TeleBot('8119014141:AAGc0CJwhhnHEPw_tsvwP5HSz1Av-SyZgKE')
@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    url = "https://eslamhacker.com/password.php"
    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 14; RMX3890 Build/UKQ1.230917.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.6778.104 Mobile Safari/537.36",
        'referer': "https://linkjust.com/",
    }
    session = requests.Session()
    cookies = {
        "_ga": "GA1.1.1927675764.1734451753",
        "cf_clearance": "sZeYTKuGM..h9MDKnBUffzAG_2EsYBY3.x.Ze8fuM64-1734458149-1.2.1.1-HIQIH9eq1QcEP2pEBwpeOhjI44dCFkOlNX85gEj6J7HoidP7hY3qZAIuS6_3BY3iv36UJkMCpaJ3OcjMNpCcPCO9W1pLzwhg5m1vJseCEiBp1A_xpbrC516hhTkwHnMC7oPukE9iecSw4lHHdh6CBdxEyP7FfZbj_BJoN.BZpXK_lfUyfJ7fIvGrFCSnv3xwtuN9O7W.ZYZTXFK3lZHZLsGWPIRPRIUBH8DGV8smXif5JLfJ0xHoXF4vLLE709Wa2HKisymcQueCFZ.E7qRsrbJbwG.daKwE7dvYjZ5ou0INnqfda5dY70AEwTZ9lYEeAVL4YNJfibEfsf.1kF1Th5S4qEoTkAhCFXpZZKnOg9eI_NyqEdks7AS0bn0igdq.PNxgpPczQYa5hf1GCDmYNIR71aRbmb22mDXw_0YhJYJFd2xa6X.CRG76NwRcy7nmz8QN1MhcqD2zE4GXdQiuVQWFypwGX5FjVS0TAUP.HrY",
        "Vistteoo": "NDY1MDQ5Mzc3NzAyOTA1NjAy",
        "_ga_0H2KR6N151": "GS1.1.1734515977.6.1.1734516249.0.0.0",
    }
    response = session.get(url, headers=headers, cookies=cookies)
    match = re.search(r'\bEslam\d{4}\b', response.text)
    if match:
        msg = bot.send_message(chat_id, f"""كلمة مرور موقع إسلام الآن هي {match.group()}
        بواسطة الكينج نت صلاح و شكر خاص لأحمد حمدي أندرو نت 😍❤
        الرجاء الأشتراك فضلا وليس امرا بكل من هذه القنوات
        https://t.me/Ashba7_net
        
        https://t.me/IBRAHEMNET01
        
        https://t.me/AndroElNet""")
    else:
        msg = bot.send_message(chat_id, "لم يتم العثور على كلمة المرور")
if __name__ == '__main__':
    bot.polling(none_stop=True)
    print("تم تشغيل البوت بنجاح")