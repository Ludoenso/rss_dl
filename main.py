#!/bin/python3

import requests
import xml.etree.ElementTree as ET
import os.path
import filecmp

MFP_URL = "http://musicforprogramming.net/rss.php"

MFP_XML = ""

DIR_PATH = "/media/Multimedia/Music/MusicForProgramming/"

tab_song_url = []

tab_song_title = []

def get_url2xml(url):

    return ET.fromstring(requests.get(url).text)

def download_url(url):

    return requests.get(url,stream=True)


# Append the url of the song into the tab_song
# dictionnary
def load_song_url(xml):

    for i in xml:

        for j in i:

            if j.tag == "item":

                for k in j :

                    if k.tag == "comments":

                        tab_song_url.append(k.text)

# Append the title of the song into the tab_song
# dictionnary
def load_song_name(xml):

    for i in xml:

        for j in i:

            if j.tag == "item":

                for k in j :

                    if k.tag == "title":

                        tab_song_title.append(k.text)


# If the name of the song is not in the directory download it.
def download_songs():

    for i in range(0,len(tab_song_url)):

        ## Download the song and store it into the variable
        song_file = download_url(tab_song_url[i])

        if not os.path.isfile(DIR_PATH + tab_song_title[i]):

            with open(DIR_PATH + "{}".format(tab_song_title[i]),"wb") as file :

                for chunk in song_file.iter_content(chunk_size = 1024):

                    file.write(chunk)
def __main__():

    MFP_XML = get_url2xml(MFP_URL)

    load_song_url(MFP_XML)

    load_song_name(MFP_XML)

    download_songs()


if __name__ :

    __main__()
