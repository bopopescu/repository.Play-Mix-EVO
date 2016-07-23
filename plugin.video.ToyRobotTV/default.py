# -*- coding: utf-8 -*-

"""
Copyright (C) 2015

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>
"""

import urllib, urllib2, sys, re, os, unicodedata
import xbmc, xbmcgui, xbmcplugin, xbmcaddon

plugin_handle = int(sys.argv[1])

mysettings = xbmcaddon.Addon(id = 'plugin.video.ToyRobotTV')
profile = mysettings.getAddonInfo('profile')
home = mysettings.getAddonInfo('path')
fanart = xbmc.translatePath(os.path.join(home, 'fanart.jpg'))
icon = xbmc.translatePath(os.path.join(home, 'icon.png'))

online_0_xml = mysettings.getSetting('online_0_xml')
online_1_xml = mysettings.getSetting('online_1_xml')
online_2_xml = mysettings.getSetting('online_2_xml')
online_3_xml = mysettings.getSetting('online_3_xml')
online_4_xml = mysettings.getSetting('online_4_xml')
online_5_xml = mysettings.getSetting('online_5_xml')
online_6_xml = mysettings.getSetting('online_6_xml')
online_7_xml = mysettings.getSetting('online_7_xml')
online_8_xml = mysettings.getSetting('online_8_xml')
online_9_xml = mysettings.getSetting('online_9_xml')
online_10_xml = mysettings.getSetting('online_10_xml')
online_11_xml = mysettings.getSetting('online_11_xml')
online_12_xml = mysettings.getSetting('online_12_xml')
online_13_xml = mysettings.getSetting('online_13_xml')
online_14_xml = mysettings.getSetting('online_14_xml')
online_15_xml = mysettings.getSetting('online_15_xml')
online_16_xml = mysettings.getSetting('online_16_xml')
online_17_xml = mysettings.getSetting('online_17_xml')


xml_regex = '<title>(.*?)</title>\s*<link>(.*?)</link>\s*<thumbnail>(.*?)</thumbnail>'
m3u_thumb_regex = 'tvg-logo=[\'"](.*?)[\'"]'
m3u_regex = '#(.+?),(.+)\s*(.+)\s*'

u_tube = 'http://www.youtube.com'

def removeAccents(s):
	return ''.join((c for c in unicodedata.normalize('NFD', s.decode('utf-8')) if unicodedata.category(c) != 'Mn'))
					
def read_file(file):
    try:
        f = open(file, 'r')
        content = f.read()
        f.close()
        return content
    except:
        pass

def make_request(url):
	try:
		req = urllib2.Request(url)
		req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0')
		response = urllib2.urlopen(req)	  
		link = response.read()
		response.close()  
		return link
	except urllib2.URLError, e:
		print 'We failed to open "%s".' % url
		if hasattr(e, 'code'):
			print 'We failed with error code - %s.' % e.code	
		if hasattr(e, 'reason'):
			print 'We failed to reach a server.'
			print 'Reason: ', e.reason
			
def main():
	add_dir('[B]<<<  SEARCH  >>>[/B]', 'searchlink', 99, icon, fanart)
	if len(online_0_xml) > 0:	
		add_dir('[COLOR yellow][B]>> The Flash <<[/B][/COLOR]', u_tube, 0, icon, fanart)	
	if len(online_1_xml) > 0:	
		add_dir('[COLOR yellow][B]>> Legends of Tomorrow <<[/B][/COLOR]', u_tube, 01, icon, fanart)
	if len(online_2_xml) > 0:	
		add_dir('[COLOR yellow][B]>> Shadowhunters <<[/B][/COLOR]', u_tube, 2, icon, fanart)
	if len(online_3_xml) > 0:	
		add_dir('[COLOR yellow][B]>> The X Files Season 10 <<[/B][/COLOR]', u_tube, 3, icon, fanart)
	if len(online_4_xml) > 0:	
		add_dir('[COLOR yellow][B]>> SuperStore  <<[/B][/COLOR]', u_tube, 4, icon, fanart)
	if len(online_5_xml) > 0: 
		add_dir('[COLOR yellow][B]>> The Shannara Chronicles <<[/B][/COLOR]', u_tube, 5, icon, fanart)	
	if len(online_6_xml) > 0: 
		add_dir('[COLOR yellow][B]>> Game of Thrones <<[/B][/COLOR]', u_tube, 6, icon, fanart)
	if len(online_7_xml) > 0: 
		add_dir('[COLOR yellow][B]>> Gravity Falls<<[/B][/COLOR]', u_tube, 7, icon, fanart)
	if len(online_8_xml) > 0: 
		add_dir('[COLOR yellow][B]>> Limitless <<[/B][/COLOR]', u_tube, 8, icon, fanart)
	if len(online_9_xml) > 0: 
		add_dir('[COLOR yellow][B]>> Small Vill <<[/B][/COLOR]', u_tube, 9, icon, fanart)
	if len(online_10_xml) > 0: 
		add_dir('[COLOR yellow][B]>> The Big Bang Theory <<[/B][/COLOR]', u_tube, 10, icon, fanart)
	if len(online_11_xml) > 0: 
		add_dir('[COLOR yellow][B]>> Heroes Reborn <<[/B][/COLOR]', u_tube, 11, icon, fanart)
	if len(online_12_xml) > 0: 
		add_dir('[COLOR yellow][B]>> Proximamente <<[/B][/COLOR]', u_tube, 12, icon, fanart)
	if len(online_13_xml) > 0: 
		add_dir('[COLOR yellow][B]>> Proximamente <<[/B][/COLOR]', u_tube, 13, icon, fanart)
	if len(online_14_xml) > 0: 
		add_dir('[COLOR yellow][B]>> Proximamente <<[/B][/COLOR]', u_tube, 14, icon, fanart)
	if len(online_15_xml) > 0: 
		add_dir('[COLOR yellow][B]>> Proximamente <<[/B][/COLOR]', u_tube, 15, icon, fanart)
	if len(online_16_xml) > 0: 
		add_dir('[COLOR yellow][B]>> Proximamente <<[/B][/COLOR]', u_tube, 16, icon, fanart)
	if len(online_17_xml) > 0: 
		add_dir('[COLOR yellow][B]>> Proximamente <<[/B][/COLOR]', u_tube, 17, icon, fanart)
	if (len(online_0_xml) < 1 and len(online_1_xml) < 1 and len(online_2_xml) < 1 and len(online_3_xml) < 1 and len(online_4_xml) < 1 and len(online_5_xml) 	< 1 and len(online_6_xml) < 1 and len(online_7_xml) < 1 and len(online_8_xml) < 1 and len(online_9_xml) < 1 and len(online_10_xml) < 1 and len	(online_11_xml) < 1 and len(online_12_xml)< 1 and len(online_13_xml) < 1 and len(online_14_xml) < 1 and len(online_15_xml) < 1 and len(online_16_xml) < 	1 and len(online_17_xml) < 1  ):		
		mysettings.openSettings()
		xbmc.executebuiltin("Container.Refresh")		

def search(): 	
	try:
		keyb = xbmc.Keyboard('', 'Enter search text')
		keyb.doModal()
		if (keyb.isConfirmed()):
			searchText = urllib.quote_plus(keyb.getText()).replace('+', ' ')
		
		if len(online_0_xml) > 0:					
			content = make_request(online_0_xml)
			match = re.compile(xml_regex).findall(content)	
			for name, url, thumb in match:
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					xml_playlist(name, url, thumb)	
		if len(online_1_xml) > 0:					
			content = make_request(online_1_xml)
			match = re.compile(xml_regex).findall(content)	
			for name, url, thumb in match:
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					xml_playlist(name, url, thumb)	
		if len(online_2_xml) > 0:					
			content = make_request(online_2_xml)
			match = re.compile(xml_regex).findall(content)	
			for name, url, thumb in match:
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					xml_playlist(name, url, thumb)	
		if len(online_3_xml) > 0:					
			content = make_request(online_3_xml)
			match = re.compile(xml_regex).findall(content)	
			for name, url, thumb in match:
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					xml_playlist(name, url, thumb)	
		if len(online_4_xml) > 0:					
			content = make_request(online_4_xml)
			match = re.compile(xml_regex).findall(content)	
			for name, url, thumb in match:
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					xml_playlist(name, url, thumb)	
		if len(online_5_xml) > 0:					
			content = make_request(online_5_xml)
			match = re.compile(xml_regex).findall(content)	
			for name, url, thumb in match:
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					xml_playlist(name, url, thumb)	
		if len(online_6_xml) > 0:					
			content = make_request(online_6_xml)
			match = re.compile(xml_regex).findall(content)	
			for name, url, thumb in match:
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					xml_playlist(name, url, thumb)	
		if len(online_7_xml) > 0:					
			content = make_request(online_7_xml)
			match = re.compile(xml_regex).findall(content)	
			for name, url, thumb in match:
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					xml_playlist(name, url, thumb)	
		if len(online_8_xml) > 0:					
			content = make_request(online_8_xml)
			match = re.compile(xml_regex).findall(content)	
			for name, url, thumb in match:
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					xml_playlist(name, url, thumb)	
		if len(online_9_xml) > 0:					
			content = make_request(online_9_xml)
			match = re.compile(xml_regex).findall(content)	
			for name, url, thumb in match:
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					xml_playlist(name, url, thumb)	
		if len(online_10_xml) > 0:					
			content = make_request(online_10_xml)
			match = re.compile(xml_regex).findall(content)	
			for name, url, thumb in match:
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					xml_playlist(name, url, thumb)	
		if len(online_11_xml) > 0:					
			content = make_request(online_11_xml)
			match = re.compile(xml_regex).findall(content)	
			for name, url, thumb in match:
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					xml_playlist(name, url, thumb)	
		if len(online_12_xml) > 0:					
			content = make_request(online_12_xml)
			match = re.compile(xml_regex).findall(content)	
			for name, url, thumb in match:
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					xml_playlist(name, url, thumb)	
		if len(online_13_xml) > 0:					
			content = make_request(online_13_xml)
			match = re.compile(xml_regex).findall(content)	
			for name, url, thumb in match:
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					xml_playlist(name, url, thumb)	
		if len(online_14_xml) > 0:					
			content = make_request(online_14_xml)
			match = re.compile(xml_regex).findall(content)	
			for name, url, thumb in match:
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					xml_playlist(name, url, thumb)	
		if len(online_15_xml) > 0:					
			content = make_request(online_15_xml)
			match = re.compile(xml_regex).findall(content)	
			for name, url, thumb in match:
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					xml_playlist(name, url, thumb)	
		if len(online_16_xml) > 0:					
			content = make_request(online_16_xml)
			match = re.compile(xml_regex).findall(content)	
			for name, url, thumb in match:
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					xml_playlist(name, url, thumb)	
		if len(online_17_xml) > 0:					
			content = make_request(online_17_xml)
			match = re.compile(xml_regex).findall(content)	
			for name, url, thumb in match:
				if re.search(searchText, removeAccents(name.replace('Đ', 'D')), re.IGNORECASE):
					xml_playlist(name, url, thumb)	
		
	except:
		pass
		

			
def xml_online_0():			
	content = make_request(online_0_xml)
	match = re.compile(xml_regex).findall(content)
	for name, url, thumb in match:
		try:
			xml_playlist(name, url, thumb)
		except:
			pass
def xml_online_1():			
	content = make_request(online_1_xml)
	match = re.compile(xml_regex).findall(content)
	for name, url, thumb in match:
		try:
			xml_playlist(name, url, thumb)
		except:
			pass
def xml_online_2():			
	content = make_request(online_2_xml)
	match = re.compile(xml_regex).findall(content)
	for name, url, thumb in match:
		try:
			xml_playlist(name, url, thumb)
		except:
			pass
def xml_online_3():			
	content = make_request(online_3_xml)
	match = re.compile(xml_regex).findall(content)
	for name, url, thumb in match:
		try:
			xml_playlist(name, url, thumb)
		except:
			pass
def xml_online_4():			
	content = make_request(online_4_xml)
	match = re.compile(xml_regex).findall(content)
	for name, url, thumb in match:
		try:
			xml_playlist(name, url, thumb)
		except:
			pass
def xml_online_5():			
	content = make_request(online_5_xml)
	match = re.compile(xml_regex).findall(content)
	for name, url, thumb in match:
		try:
			xml_playlist(name, url, thumb)
		except:
			pass

def xml_online_6():			
	content = make_request(online_6_xml)
	match = re.compile(xml_regex).findall(content)
	for name, url, thumb in match:
		try:
			xml_playlist(name, url, thumb)
		except:
			pass
def xml_online_7():			
	content = make_request(online_7_xml)
	match = re.compile(xml_regex).findall(content)
	for name, url, thumb in match:
		try:
			xml_playlist(name, url, thumb)
		except:
			pass
def xml_online_8():			
	content = make_request(online_8_xml)
	match = re.compile(xml_regex).findall(content)
	for name, url, thumb in match:
		try:
			xml_playlist(name, url, thumb)
		except:
			pass
def xml_online_9():			
	content = make_request(online_9_xml)
	match = re.compile(xml_regex).findall(content)
	for name, url, thumb in match:
		try:
			xml_playlist(name, url, thumb)
		except:
			pass
def xml_online_10():			
	content = make_request(online_10_xml)
	match = re.compile(xml_regex).findall(content)
	for name, url, thumb in match:
		try:
			xml_playlist(name, url, thumb)
		except:
			pass
def xml_online_11():			
	content = make_request(online_11_xml)
	match = re.compile(xml_regex).findall(content)
	for name, url, thumb in match:
		try:
			xml_playlist(name, url, thumb)
		except:
			pass
def xml_online_12():			
	content = make_request(online_12_xml)
	match = re.compile(xml_regex).findall(content)
	for name, url, thumb in match:
		try:
			xml_playlist(name, url, thumb)
		except:
			pass
def xml_online_13():			
	content = make_request(online_13_xml)
	match = re.compile(xml_regex).findall(content)
	for name, url, thumb in match:
		try:
			xml_playlist(name, url, thumb)
		except:
			pass
def xml_online_14():			
	content = make_request(online_14_xml)
	match = re.compile(xml_regex).findall(content)
	for name, url, thumb in match:
		try:
			xml_playlist(name, url, thumb)
		except:
			pass
def xml_online_15():			
	content = make_request(online_15_xml)
	match = re.compile(xml_regex).findall(content)
	for name, url, thumb in match:
		try:
			xml_playlist(name, url, thumb)
		except:
			pass

def xml_online_16():			
	content = make_request(online_16_xml)
	match = re.compile(xml_regex).findall(content)
	for name, url, thumb in match:
		try:
			xml_playlist(name, url, thumb)
		except:
			pass
def xml_online_17():			
	content = make_request(online_17_xml)
	match = re.compile(xml_regex).findall(content)
	for name, url, thumb in match:
		try:
			xml_playlist(name, url, thumb)
		except:
			pass
				

					
def xml_playlist(name, url, thumb):
	name = re.sub('\s+', ' ', name).strip()			
	url = url.replace('"', ' ').replace('&amp;', '&').strip()
	if ('youtube.com/user/' in url) or ('youtube.com/channel/' in url) or ('youtube/user/' in url) or ('youtube/channel/' in url):
		if len(thumb) > 0:	
			add_dir(name, url, '', thumb, thumb)			
		else:	
			add_dir(name, url, '', icon, fanart)
	else:
		if 'youtube.com/watch?v=' in url:
			url = 'plugin://plugin.video.youtube/play/?video_id=%s' % (url.split('=')[-1])
		elif 'dailymotion.com/video/' in url:
			url = url.split('/')[-1].split('_')[0]
			url = 'plugin://plugin.video.dailymotion_com/?mode=playVideo&url=%s' % url	
		else:			
			url = url
		if len(thumb) > 0:		
			add_link(name, url, 1, thumb, thumb)			
		else:			
			add_link(name, url, 1, icon, fanart)	
	
def play_video(url):
	media_url = url
	item = xbmcgui.ListItem(name, path = media_url)
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)
	return

def get_params():
	param = []
	paramstring = sys.argv[2]
	if len(paramstring)>= 2:
		params = sys.argv[2]
		cleanedparams = params.replace('?', '')
		if (params[len(params)-1] == '/'):
			params = params[0:len(params)-2]
		pairsofparams = cleanedparams.split('&')
		param = {}
		for i in range(len(pairsofparams)):
			splitparams = {}
			splitparams = pairsofparams[i].split('=')
			if (len(splitparams)) == 2:
				param[splitparams[0]] = splitparams[1]
	return param

def add_dir(name, url, mode, iconimage, fanart):
	u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name) + "&iconimage=" + urllib.quote_plus(iconimage)
	ok = True
	liz = xbmcgui.ListItem(name, iconImage = "DefaultFolder.png", thumbnailImage = iconimage)
	liz.setInfo( type = "Video", infoLabels = { "Title": name } )
	liz.setProperty('fanart_image', fanart)
	if ('youtube.com/user/' in url) or ('youtube.com/channel/' in url) or ('youtube/user/' in url) or ('youtube/channel/' in url):
		u = 'plugin://plugin.video.youtube/%s/%s/' % (url.split( '/' )[-2], url.split( '/' )[-1])
		ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz, isFolder = True)
		return ok		
	ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz, isFolder = True)
	return ok

def add_link(name, url, mode, iconimage, fanart):
	u = sys.argv[0] + "?url=" + urllib.quote_plus(url) + "&mode=" + str(mode) + "&name=" + urllib.quote_plus(name) + "&iconimage=" + urllib.quote_plus(iconimage)	
	liz = xbmcgui.ListItem(name, iconImage = "DefaultVideo.png", thumbnailImage = iconimage)
	liz.setInfo( type = "Video", infoLabels = { "Title": name } )
	liz.setProperty('fanart_image', fanart)
	liz.setProperty('IsPlayable', 'true') 
	ok = xbmcplugin.addDirectoryItem(handle = int(sys.argv[1]), url = u, listitem = liz)  
		
params = get_params()
url = None
name = None
mode = None
iconimage = None

try:
	url = urllib.unquote_plus(params["url"])
except:
	pass
try:
	name = urllib.unquote_plus(params["name"])
except:
	pass
try:
	mode = int(params["mode"])
except:
	pass
try:
	iconimage = urllib.unquote_plus(params["iconimage"])
except:
	pass  

print "Mode: " + str(mode)
print "URL: " + str(url)
print "Name: " + str(name)
print "iconimage: " + str(iconimage)		

if mode == None or url == None or len(url) < 1:
	main()

elif mode == 1:
	play_video(url)
	
elif mode == 0:
	xml_online_0()
elif mode == 01:
	xml_online_1()
elif mode == 2:
	xml_online_2()
elif mode == 3:
	xml_online_3()
elif mode == 4:
	xml_online_4()
elif mode == 5:
	xml_online_5()
elif mode == 6:
	xml_online_6()
elif mode == 7:
	xml_online_7()
elif mode == 8:
	xml_online_8()
elif mode == 9:
	xml_online_9()
elif mode == 10:
	xml_online_10()
elif mode == 11:
	xml_online_11()
elif mode == 12:
	xml_online_12()
elif mode == 13:
	xml_online_13()
elif mode == 14:
	xml_online_14()
elif mode == 15:
	xml_online_15()
elif mode == 16:
	xml_online_16()
elif mode == 17:
	xml_online_17()
	
elif mode == 99:
	search()
	
xbmcplugin.endOfDirectory(plugin_handle)