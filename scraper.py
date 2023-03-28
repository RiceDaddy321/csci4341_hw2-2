from bs4 import BeautifulSoup
import requests
import time
from datetime import date
import mysql.connector
from mysql.connector import Error
import random
import smtplib
from email.mime.text import MIMEText

url = 'https://www.metal-archives.com/lists/black'

# Define POST request parameters.
print("Requesting...")

page = requests.post(url)

# Check for 200(ok) HTTP status code.
if (page.status_code == 200):

    # Parse HTML page content using BeautifulSoup.
    soup = BeautifulSoup(page.content, 'html.parser')