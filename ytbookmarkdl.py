#! /usr/bin/env python3
#-*- coding: utf-8 -*-

import sys, os, re, shlex, threading, math
from pytube import YouTube


def lynx_dump (src):
    return os.popen("lynx -dump -width 999 --listonly " + src).read()

def filter_links(txt):
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

def list_to_sublists(l, n):
    return [l[i:i+n] for i in range(0, len(l), n)]

def thread_worker(links):
    for link in links:
        title = dl_video(link)
        if title:
            mp4_to_mp3(title)
            delete_mp4(title)

def main(src, amount_threads):
    amount_threads = int(amount_threads)

    references = lynx_dump(src)
    links = filter_links(references)

    print("Found [" + str(len(links)) + "] links")

    amount_subsets = math.ceil(len(links)/amount_threads)
    links = list_to_sublists(links, amount_subsets)

    print("Starting download")

    for sublist in links:
        t = threading.Thread(target=thread_worker, args = (sublist,))
        t.start()

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
    print(sys.argv[1])
