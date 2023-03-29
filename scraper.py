from bs4 import BeautifulSoup
import requests
import time
from datetime import date
import mysql.connector
from mysql.connector import Error
import random
import smtplib
from email.mime.text import MIMEText

# get the band names from the downloaded table
bands = []
with open("bandsTable.html") as f:
    # read in file and store into a buffer
    data = f.read().replace('\n', '')

    # make our parser
    soup = BeautifulSoup(data, 'html.parser')

    # get all of the sortings
    tmp = soup.find_all('td', class_="sorting_1")

    # now only get the text
    for band in tmp:
        band_text = band.a.get('href')
        bands.append(band_text)

output_path = "metal_dataset"
# Define POST request parameters.
print("Requesting...")
hdr = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'}
##PUT FOR HERE
for i, band in enumerate(bands):
    try:
        i += 1500
        url = band
        page = requests.get(url, headers=hdr)
        # Check for 200(ok) HTTP status code.
        if (page.status_code == 200):

            # Parse HTML page content using BeautifulSoup.
            soup = BeautifulSoup(page.content, 'html.parser')

            # look for the band_name_img div
            container = soup.find(id="logo", class_="image", href=True)

            if container is None:
                print("Failed to get image for {}: \n{}".format(band, url))
                continue

            # extract the href
            img_url = container['href']

            # download the img
            img_name = "{}/{}.jpg".format(output_path, str(i))
            with open(img_name, 'wb') as handler:
                response = requests.get(img_url, stream=True)

                if not response.ok:
                    print(response)

                for block in response.iter_content(1024):
                    if not block:
                        break

                    handler.write(block)

            # second option
            # import urllib.request
            #
            # imgURL = "http://site.meishij.net/r/58/25/3568808/a3568808_142682562777944.jpg"
            #
            # urllib.request.urlretrieve(imgURL, "D:/abc/image/local-filename.jpg")

            print("{} written to {}. Downloaded from {}".format(band, img_name, img_url))
        else:
            print("Failed to get image for {}: \n{}".format(band, url))
    except Error:
        continue
print("Finished downloading images")
