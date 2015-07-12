#!/usr/bin/env python

import argparse

def parse_url(url):
    protocol, url = url.split("://",1)
    apikey, url = url.split("@",1)
    
    return {"url":protocol+"://"+url, "apikey": apikey.lower()}

def CLI():
    #usage: galaxyfs  [api-key@][galaxy-url]  mountpoint

    parser = argparse.ArgumentParser(description="Mount Galaxy Datasets for direct read access using FUSE.")
    parser.add_argument("url",help="http[s]://api-key@localhost:8080/galaxy-url/")
    parser.add_argument("mountpoint",help="mountpoint (/mnt/galaxy)")
    parser.add_argument("-l", "--logfile", default=None,help="Log-file")
    parser.add_argument("-f", "--foreground", default=False,help="Directory under which to mount the Galaxy Datasets.")
    
    args = parser.parse_args()
    url = parse_url(args.url)
    args.url = url['url']
    args.apikey = url['apikey']
    
    return args
