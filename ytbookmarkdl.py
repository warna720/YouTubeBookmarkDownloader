#! /usr/bin/env python3
#-*- coding: utf-8 -*-

import sys, os, re, shlex
from pytube import YouTube


def lynx_dump (src):
    return os.popen("lynx -dump -width 999 --listonly " + src).read()

def filter_links(txt):
    #\d+.\W+?(.+)
    return re.findall('\d+.\W+?(.+)', txt)

def dl_video(link):
    print("Downloading [" + link + "]")

    try:
        yt = YouTube(link)
        yt.filter('mp4')[-1].download('./')
        print("Done [" + link + "] (" + yt.filename + ")")
        return yt.filename
    except:
        print("Could not download: " + link)
        print(sys.exc_info()[0])
        return False

def mp4_to_mp3(filename):
    print("Converting [" + filename + "] mp4 -> mp3")

    escaped_filename = shlex.quote(filename)
    os.system("ffmpeg -i " + escaped_filename + ".mp4 -b:a 256k -vn " + escaped_filename + ".mp3")

    print("Done converting [" + filename + "]")

def delete_mp4(filename):
    os.system("rm " + shlex.quote(filename) + ".mp4")

def main(src):
    references = lynx_dump(src)
    links = filter_links(references)

    print("Found [" + str(len(links)) + "] links")

    print("Starting download")
    for link in links:
        title = dl_video(link)
        if title:
            mp4_to_mp3(title)
            delete_mp4(title)

    print("Execution finished")

if __name__ == "__main__":
    main(sys.argv[1])
    print(sys.argv[1])
    