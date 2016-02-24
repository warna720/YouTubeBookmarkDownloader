# YouTubeBookmarkDownloader
Downloads and converts from YouTube with links from any HTML-file. It's multithreaded btw.

Command-line usage:

    python3 ytbookmarkdl.py <html-source> <amount_of_threads>

Example:
        
    Download from a html-file
    python3 ytbookmarkdl.py bookmarks_2_24_16.html 8
    
    Download from a web-resource
    python3 ytbookmarkdl.py https://www.youtube.com/watch?v=JFMv0tEJfbM 8


TODO:

    Better argument handling

Dependencies:

    lynx
    pytube
    ffmpeg
