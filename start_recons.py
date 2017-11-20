#!/usr/bin/python

import sys, os, time, threading

domains = ["lyst.com",
"bimeanalytics.com",
"toytalk.com",
"goodhire.com",
"identity.com",
"glasswire.com",
"keybase.io",
"quora.com",
"nextcloud.com",
"boards.greenhouse.io",
"trello.com",
"trello.services",
"badoo.com",
"pinion.gg",
"unikrn.com",
"spotify.com",
"mapbox.com",
"semrush.com",
"ok.ru",
"booztx.com",
"irccloud.com",
"irccloud-cdn.com",
"udemy.com",
"legalrobot.com",
"harvestapp.com",
"forecastapp.com",
"spectacles.com",
"bitstrips.com",
"bitmoji.com",
"scan.me"]

def run(d):
	os.system("/home/rjp/Documents/Tools/start_recon.sh "+d)

for domain in domains:
	if domain is not "":
		thr = threading.Thread(target=run, args=(domain,))
		thr.start()
		time.sleep(500)


