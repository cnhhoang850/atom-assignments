# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.11.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# + [markdown] colab_type="text" id="view-in-github"
# <a href="https://colab.research.google.com/github/anhdanggit/atom-assignments/blob/main/assignment_2/ATOM_Home_Assignment_2.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# + [markdown] id="WNjHxu0-0Urk"
# ## 0. Initial Set-up

# + [markdown] id="ky3QJTULRGhG"
# 1. Clone this Github repo về máy: https://github.com/anhdanggit/atom-assignments
# 2. Mở file `env_variable_test.json`. Thay đổi & Đổi tên thành `env_variable.json`: 
#   - `"SENDER_EMAIL"`: Email của bạn
#   - `"PWD_EMAIL"`: App Password tương ứng với Email trên (Hướng Dẫn: [link](https://support.google.com/accounts/answer/185833?p=InvalidSecondFactor&visit_id=637562139468610337-3856071038&rd=1))
#   - `"WEATHER_API_KEY"`: API Key của account của bạn trên [Open Weather Map](https://support.google.com/accounts/answer/185833?p=InvalidSecondFactor&visit_id=637562139468610337-3856071038&rd=1)
# 3. Upload lên Files hoặc Google Drive, nếu bạn sử dụng Google Colab.
#
# **!!!! NOTICE !!!!** File json sau khi cho các thông tin thực của bạn, KHÔNG đưa lên Github hay để public. Tips: Để tên `env_variable.json` trong file `.gitignore` để Git tự động ignore không publish file này.

# + [markdown] id="mQHvoBrV2wAS"
# ### 0.1. Environment Variables

# + [markdown] id="wsarlH3fTc0_"
# Đặt `!` phía trước 1 cell để bắt đầu viết lệnh [Shell Commands](https://docs.cs.cf.ac.uk/notes/linux-shell-commands/) (đây là các lệnh giao tiếp với OS - Hệ điều hành đang dùng bên dưới để chạy Colab Notebook)

# + colab={"base_uri": "https://localhost:8080/"} id="I2nTgPRQ1MjI" outputId="54be56d9-0817-4158-8369-0678f4576d26"
# !ls #để liệt kể các files đang có trong cùng "folder" với file notebook

# + colab={"base_uri": "https://localhost:8080/"} id="3EPceevo0yWp" outputId="61fed2a0-6081-41be-ba05-a9a211c04764"
# !python3 env_variables.json #để chạy một file python (bên ngoài notebook)

# + id="j3Fv0NUdXyd1"
import json
with open('env_variables.json', 'r') as j:
    json_data = json.load(j)
    print(json_data)

# + [markdown] id="ZWYv-VjeZpK2"
# ### Concept: JSON File
# * JSON là một dạng đa ta phổ biến, có dạng key-value. Nghĩa là những giá trị bên trong có thể "gọi" bằng các key, tương tự cấu trúc của Dictionary (Week 2)
# * Reference: [JSON Data in Python](https://www.datacamp.com/community/tutorials/json-data-python?utm_source=adwords_ppc&utm_campaignid=1455363063&utm_adgroupid=65083631748&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=278443377095&utm_targetid=aud-522010995285:dsa-429603003980&utm_loc_interest_ms=&utm_loc_physical_ms=1028581&gclid=Cj0KCQjws-OEBhCkARIsAPhOkIYshv7eHMZhcLYnRmnCVdoXMbchc_nxeSYbyoGnSlauIGaJWudvBf8aAql6EALw_wcB)

# + [markdown] id="TPqTOA8DbGgq"
# ### TODO #1
# 1. Thử un-comment bằng cách để dấu nháy chuột ở dòng print(json_data) và nhấn `Ctrl+/`. Sau đó, chạy lại.
# 2. Cấu trúc của `json_data` tương tự `dictionary`: thử gọi biến `SENDER_EMAIL` trong file json và `print`
# => Task này sẽ giúp bạn tìm hiểu thêm về cấu trúc của 1 file JSON.

# + [markdown] id="1SU_ozhPU2B1"
# ### Concept: Environment Variables
# * [Environment Variables](https://medium.com/chingu/an-introduction-to-environment-variables-and-how-to-use-them-f602f66d15fa#:~:text=An%20environment%20variable%20is%20a,at%20a%20point%20in%20time.) là các biến (variable) được set bên ngoài program
# * Lý do: Có một số value có tính nhạy cảm (password), việc để trong code (và đưa lên Git) sẽ không bảo mật các thông tin này
#
# Trong đoạn code dưới, ta giữ các thông tin nhạy cảm khỏi code bằng việc lưu giữ trong một file json, và gọi các giá trị `SENDER_MAIL`, `PWD_EMAIL`, `API_KEY` lưu vào Environmental Variables.

# + colab={"base_uri": "https://localhost:8080/"} id="4vlqLayL2IDd" outputId="86786eac-de8f-41b3-9ea4-e9d366db64a0"
import os
os.environ['SENDER_EMAIL'] = json_data['SENDER_EMAIL'] ## INPUT: Your Email
os.environ['PWD_EMAIL'] = json_data['PWD_EMAIL'] ## INPUT: Your App Password
os.environ['WEATHER_API_KEY'] = json_data['WEATHER_API_KEY'] ## INPUT: OpenWeather API Key
print('DONE! Get Env. Variable')

# + colab={"base_uri": "https://localhost:8080/"} id="pnWQlWHMZja7" outputId="af9cb1b9-1d07-4c67-862e-12aa4624ba61"
print(os.environ['SENDER_EMAIL'])
print(os)

# + [markdown] id="fnJtI0S12eh-"
# ### 0.2. Import Modules
#
#
# *   [Modules](https://docs.python.org/3/tutorial/modules.html): là một file gồm các definitions & statements trong python. Nói nôm ra, modules là một gói chứa nhiều functions. 
# *   Dấu `.` chỉ sự "thuộc về": a.b.c nghĩa là c nằm trong b, b nằm trong a. Ví dụ: `json.load()` nghĩa là function `load()` trong module `json()`
# *   Load một module bằng `import` 
# *   Install một module vào máy bằng: `!pip install`. Có dấu `!`, nghĩa là **Shell Commands**
#
# Dưới đây ta import tất cả các module cần sử dụng cho Assignment, một practice tốt là gom hết các modules và install trên đầu notebook/file code.
#
#

# + id="pbOfgkfU3XYz"
# !pip install beautifulsoup4

# + id="C0dJywJtOtEK"
import email, smtplib, ssl # to automate email
import email as mail

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import requests, json # to pull API, and work with json
import datetime as dt # to work with date, time
from bs4 import BeautifulSoup # to work with web scrapping (HTML)
import pandas as pd # to work with tables (DataFrames) data
from IPython.core.display import HTML # to display HTML in the notebook

# + [markdown] id="KkJiWpgkgNyB"
# ## 1. Email Bot
# Đoạn code sau để gửi email:
# - Từ: `SENDER_EMAIL`
# - Đến: `RECEIVER_MAIL`
# - Với subject và body gồm 3 phần: Phần nội dung được viết bằng HTML, nếu chưa quen thuộc bạn có thể dùng công cụ xong để convert từ style của MS Word sang HTML: https://wordtohtml.net/

# + colab={"base_uri": "https://localhost:8080/"} id="9unEmluARSpH" outputId="bad054b2-da52-4132-ea4c-d93a79eaa6d5"
subject = "Test Email" #INPUT1: Subject of the Email
receiver_email = input("Your email: ") #INPUT2: email address to receive the email
sender_email = os.environ['SENDER_EMAIL']
password = os.environ['PWD_EMAIL'] 

# (1) Create the email head (sender, receiver, and subject)
email = MIMEMultipart()
email["From"] = sender_email
email["To"] = receiver_email 
email["Subject"] = subject

# (2) Create Body part
# We use html, you can convert word to html: https://wordtohtml.net/
html1 = """
    <html>
    <h1><strong>Hello World</strong></h1>
    <body>
    <p>Hi!<br>
       How are you?<br>
       Here is the <a href="https://docs.python.org/3.4/library/email-examples.html">link</a> you wanted.
    </p>
    </body>
    </html>
    """
html2 = """
<html>
Email sent at <b>{}</b><br>
</html>
""".format(dt.datetime.now().isoformat())

text3 = '--- End ----'

# Combine parts
part1 = MIMEText(html1, 'html')
part2 = MIMEText(html2, 'html')
part3 = MIMEText(text3, 'plain')

email.attach(part1)
email.attach(part2)
email.attach(part3)

# (3) Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_email, password) #login with mail_id and password
text = email.as_string()
session.sendmail(sender_email, receiver_email, text)
session.quit()

print('DONE! Mail Sent'.format(sender_email, receiver_email))


# + [markdown] id="LKXSTGhMiyGa"
# ### TODO #2
# 1.   Từ Email Bot Code viết function `send_email`:
#   - **inputs**: subject, receiver_email, part1, part2, part3
#   - **output**: thực hiện việc gửi email và in ra kết quả
# 2.   Kết hợp Loops (For ... in) với function để gửi cùng nội dung email đến 1 list user: `email_list = ['abc@gmail.com', 'xyz@gmail.com']` (thay đổi email bằng các email thật của bạn để test)

# + id="2YV6peDOmNkA"
def send_email(receiver_email, subject, parts):
    email = MIMEMultipart() 
    email["To"] = receiver_email
    email["Subject"] = subject 
    
    [email.attach(MIMEText(i)) for i in parts] 
    text = email.as_string()
    
    session = smtplib.SMTP('smtp.gmail.com', 587) 
    session.starttls() 
    session.login(sender_email, password) 
    text = email.as_string()
    session.sendmail(sender_email, receiver_email, text)
    session.quit()
    print('DONE! Mail Sent'.format(sender_email, receiver_email))


# + id="4ydkiKUqmhMw"
email_list = ['cnhhoang850@gmail.com', 'ipadsucker246@gmail.com']
for i in email_list:
  send_email(i, 'Ads', ['Buy X products', "Because it's good", "That's all!"])


# + [markdown] id="RM7HKTGIh9IC"
# ## Call API

# + [markdown] id="z22CtbW8mvqh"
# ### Concept: API
# * **API** ([Application Programming Interface](https://en.wikipedia.org/wiki/API)): Là cách thức và phương tiện để 2 applications nói chuyện với nhau. Ở đây là giữa Python program trên Colab của bạn và các Web application khác. 
# * Đây là concept nền tảng trong việc Automation
# * API nhận input là JSON file (có khi không nhận) và trả lại output là JSON file => Request/Call API
# * Đây là một cách phổ biến đế gửi và nhận data
#
# Đoạn code bên dưới: 
# * Lấy input là `API_KEY`, country, ta request **API** của Open Weather
# * Được trả lại file kết quả dưới dạng `JSON`
# * Trích xuất 1 vài thông tin, và lưu ra file text

# + colab={"base_uri": "https://localhost:8080/"} id="3ZzdPfFbiCZa" outputId="e545d025-5a9c-444a-8255-c489e81d6bf6"
# base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
# City Name 
CITY = "London"
# API key 
API_KEY = os.environ['WEATHER_API_KEY']
# upadting the URL
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
# HTTP request
response = requests.get(URL)
# checking the status code of the request
if response.status_code == 200:
   # getting data in the json format
   data = response.json()
   # getting the main dict block
   main = data['main']
   # getting temperature
   temperature = main['temp']
   # getting the humidity
   humidity = main['humidity']
   # getting the pressure
   pressure = main['pressure']
   # weather report
   report = data['weather']
   f = open('weather.txt','w') ## write to text file
   print(f"{CITY:-^30}", file=f)
   print(f"Temperature: {temperature}", file=f)
   print(f"Humidity: {humidity}", file=f)
   print(f"Pressure: {pressure}", file=f)
   print(f"Weather Report: {report[0]['description']}", file=f)
   f.close()
   print("DONE! Output in weather.txt file")
else:
   # showing the error message
   print("Error in the HTTP request")
   print(response)

# + colab={"base_uri": "https://localhost:8080/"} id="aOTClQTCn7wh" outputId="c8a74544-6073-4d72-9c4c-9254fd99d3c2"
# !ls

# + colab={"base_uri": "https://localhost:8080/"} id="I_4mwiKRpVzJ" outputId="a354c204-8110-4186-ae37-9cbd72210e9f"
print(open("weather.txt", "r").read())

# + colab={"base_uri": "https://localhost:8080/"} id="kqwsvfxolao7" outputId="0a860e33-6993-4b70-e513-93d63ec075a0"
# Khám phá file JSON
data

# + colab={"base_uri": "https://localhost:8080/", "height": 35} id="9m9ccXB6nOyN" outputId="2bd4169e-ea31-4b5e-b4a4-dfe02aaddd47"
data['name']

# + colab={"base_uri": "https://localhost:8080/"} id="-hfJui94nQ8i" outputId="c5e67e49-ad39-4310-f170-a5ee32fe5b3a"
data['coord']['lat']

# + [markdown] id="jbmpcldqGhuk"
# ### TODO #3
# 1. Trên file json kết quả:
#   - Lấy thông tin trạng thái thời tiết (weather) chính (main) ở London
#   - Lấy lat & lon (kinh độ và vĩ độ của London)
# 2. Viết function `get_weather_data` 
#   - inputs: city
#   - outputs: đoạn text thông tin thời tiết
# 3. Dùng function `send_email` in **TODO #1**, thay phần 3 trong nội dùng email bằng thông tin thời tiết của London gửi cho 1 địa chỉ email của bạn

# + id="p9tm-FzIoof1"
# YOUR CODE
print(data['main'], data['coord'])


# + id="onTj-Et3o2PO"
def get_weather_data(city):
  url = BASE_URL + "q=" + city + "&appid=" + API_KEY
  res = requests.get(url)
  
  if res.status_code == 200: 
   data = response.json()
   # getting the main dict block
   main = data['main']
   # getting temperature
   temperature = main['temp']
   # getting the humidity
   humidity = main['humidity']
   # getting the pressure
   pressure = main['pressure']
   
   result = ""
   result += (f"{city:.^30}") + '\n'
   result += (f"Temperature: {temperature}") + '\n'
   result += (f"Humidity: {humidity}") + '\n'
   result += (f"Pressure: {pressure}") + '\n'
   result += (f"Weather Report: {report[0]['description']}") + '\n'
   print(result)
   return result
  else: 
   print(res)

info = get_weather_data('Ho Chi Minh')
        

# + id="BxVhcoDuo78n"
info = get_weather_data('London')
tosend = info.split('\n')

send_email('cnhhoang850@gmail.com', "Today's weather", tosend)


# + [markdown] id="qdAc1M91tLRV"
# ## Web Scrapping

# + [markdown] id="9lJY0KlSrLIy"
# ### Concept: Web Scrapping
# * Web Scrapping là hoạt động lấy data từ các website. Nội dung của các website được trình bày bằng HTML
# * Để hiểu cấu trúc của HTML: Có thể vào `Chrome => More Tools => Developer Tools`
# * Cấu trúc và cách lấy giá trị của HTML cũng tương tự như JSON và Dictionary.
# * BeautifulSoup là một modules cho phép ta trích xuất thông tin từ HTML dễ dàng hơn
#
# **Reference**
# https://www.freecodecamp.org/news/scraping-wikipedia-articles-with-python/

# + colab={"base_uri": "https://localhost:8080/"} id="Bnp36lyEtxS0" outputId="ef826dab-a7d0-4bdf-ee2e-30008d2de06d"
response = requests.get(
	url="https://en.wikipedia.org/wiki/COVID-19",
  )
print("API Status Code: "+ str(response.status_code))
soup = BeautifulSoup(response.content, 'html.parser')

title = soup.find(id="firstHeading")
print(title.string)

# + colab={"base_uri": "https://localhost:8080/"} id="lY8xzPlJt5U3" outputId="ee020655-1162-4859-9520-25dedbf476e1"
response.content ## Explore contents

# + id="jvjNUghruM3j"
# Get all the links
p = soup.find(id="bodyContent").find_all("p")
print(p)

# + colab={"base_uri": "https://localhost:8080/", "height": 67} id="Hecg5C84vkzJ" outputId="6c25c4ce-f871-4284-b75b-b2ffd9ebcfd0"
from IPython.core.display import HTML
HTML(str(p[3]))

# +
#TODO 4
k = p[3].getText()

send_email('cnhhoang850@gmail.com', 'Covid', ['Hey', 'This is a COVID notice', k ])

# + [markdown] id="d7YEfY3qqq10"
# ### TODO #4
# 1. Dùng function `send_email` in Excercise 1.1, thay phần 3 trong nội dùng email bằng thông tin COVID-19 từ Wikipedia gửi cho 1 địa chỉ email của bạn

# + [markdown] id="kxfS-b_T2W0a"
# ## CSV

# + [markdown] id="3ssJNK-0rUo4"
# ### Concept CSV
# * CSV là dạng data có các cột được ngăn cách bằng dấu phẩy ([Comma-separated value](https://en.wikipedia.org/wiki/Comma-separated_values#:~:text=A%20comma%2Dseparated%20values%20(CSV,more%20fields%2C%20separated%20by%20commas.))
# * Đây là dạng data (bảng) cực kỳ phổ biến trong Data Analytics & Data Science
# * Có thể đọc, ghi, và xử lý bằng `pandas`

# + id="36c89M5BymVw"
csv = """email,contents,city
abc@gmail.com,News,Hanoi
xyz@gmail.com,Weather,London
"""
f = open('email_list.csv','w') ## write to text file
f.write(csv)
f.close()

# + colab={"base_uri": "https://localhost:8080/"} id="-yNfErkP20Pt" outputId="aaf39923-3fe0-4b9a-c98d-909bc6cd8d52"
# !ls

# + id="9BNju19j3B5d"
import pandas as pd
email_list = pd.read_csv('email_list.csv')

# + colab={"base_uri": "https://localhost:8080/", "height": 111} id="AsOSx3hT3Ih2" outputId="d88c855a-5a75-4be0-876b-939cad2e77f6"
email_list


# + [markdown] id="lDxNcYmxq3zr"
# ### TODO #5
# * Add các địa chỉ email có ý nghĩa, và thêm dòng vào file csv (lưu ý không có dấu cách)
# * Dùng code để gửi email cho một list từ csv:
#   - Nếu email có contents = 'News' => Gửi thông tin COVID19
#   - Nếu email có contents = 'Weather' => Gửi thông tin thời tiết theo thành phố trong cột city (lưu ý check các city được hỗ trợ trong API)
#
# **Hints:**
# * Sử dụng loops for ... in 
# * Sử dụng function `send_email`, `get_weather_data`

# + colab={"base_uri": "https://localhost:8080/"} id="EQ9nMwc93KS8" outputId="03570269-1b07-41f7-f98b-0a8ec0b411bd"
for i in list(range(2)):
  print('Email #{}'.format(i))
  if email_list['contents'][i] == 'News':
    print('COVID To: {}'.format(email_list['email'][i]))
    response = requests.get(
	url="https://en.wikipedia.org/wiki/COVID-19",
    )
    print("API Status Code: "+ str(response.status_code))
    soup = BeautifulSoup(response.content, 'html.parser')
    toSend = soup.findAll('p')[3].getText() + ''
    send_email(email_list['email'][i], email_list['contents'][i], [toSend])

  elif email_list['contents'][i] == 'Weather':
    print('Weather To: {}'.format(email_list['email'][i]))
    weather = get_weather_data('London')
    weatherSend = info.split('\n')
    print('sth')
    send_email(email_list['email'][i], email_list['contents'][i], weatherSend)
  else:
    print('Invalid Contents')
print('DONE!')
# -




