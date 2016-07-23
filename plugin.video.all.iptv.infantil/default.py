import xbmc,xbmcaddon,xbmcgui,xbmcplugin,os,sys,urlparse,re,time,urllib,urllib2,json,random,net,logging
import pyxbmct.addonwindow as pyxbmct
import base64

net = net.Net()
addon_id = 'plugin.video.all.iptv.infantil'
selfAddon = xbmcaddon.Addon(id=addon_id)
skintheme=selfAddon.getSetting('skin')
artpath='/resources/'+skintheme
icon = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'icon.png'))
fanart = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id, 'fanart.jpg'))
button_quit= xbmc.translatePath(os.path.join('special://home/addons/' + addon_id + artpath, 'power.png'))
button_quit_focus= xbmc.translatePath(os.path.join('special://home/addons/' + addon_id + artpath, 'power_focus.png'))
button_focus = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id + artpath, 'button_focus1.png'))
button_no_focus = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id + artpath, 'button_no_focus1.png'))
bg = xbmc.translatePath(os.path.join('special://home/addons/' + addon_id + artpath, 'main-bg2.png'))
logos = os.path.join('logos')
window  = pyxbmct.AddonDialogWindow('')
window.setGeometry(1240, 650, 100, 50)
background=pyxbmct.Image(bg)
window.placeControl(background, -5, 0, 125, 51)

def START():
        if 'Red' in button_quit:text='0xffffffff'
	elif 'Mono' in button_quit:text='0xffffffff'
	else:text='0x000000FF'
	global List
	global Icon
	#create butttons
	List = pyxbmct.List(buttonFocusTexture=button_focus,buttonTexture=button_no_focus,_space=11,_itemTextYOffset=-7,textColor=text)
	Icon=pyxbmct.Image(icon, aspectRatio=4)
	Icon.setImage(icon)
	Quit = pyxbmct.Button(' ',noFocusTexture=button_quit,focusTexture=button_quit_focus)
	#place buttons
	window.placeControl(List, 10, 1, 70, 28)
	window.placeControl(Icon, 75, 2, 40, 25)
	window.placeControl(Quit, 110, 48, 10, 3)
	#capture mouse moves or up down arrows
	window.connectEventList(
	[pyxbmct.ACTION_MOVE_DOWN,
	pyxbmct.ACTION_MOVE_UP,
		pyxbmct.ACTION_MOUSE_MOVE],
	LIST_UPDATE)
	#navigation
	List.controlRight(List)
	#button actions
	window.connect(List, PlayStream)
	window.connect(Quit, window.close)
	GETCHANNELS()

def GETCHANNELS():
	global chname
	global chlogos
	global chicon
	global chstream
	global headers
	chname=[]
	chlogos=[]
	chicon=[]
	chstream=[]
        headers={'User-Agent':'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G920F Build/LMY47X)',
			 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
			 'Accept-Encoding' : 'gzip',
        		 'Connection':'Keep-Alive'}
        page = net.http_GET ('aHR0cHM6Ly9kbC5kcm9wYm94LmNvbS9zL2RlNGtxcjA4czQ0bDJuei9pZCUzRDE0LnBocA=='.decode('base64'),headers).content
        match=re.compile('"channel_title":"(.+?)","channel_url":"(.+?)","channel_thumbnail":"(.+?)"').findall(page)
        match.sort()
        for name,url,thumb in match:
                if not '\u' in name:
                        thumb='http://proyectoluzdigital.info/tvguia/download/tododeportes/Logos/'+thumb
                        chname.append(name)
                        chicon.append(thumb)
                        chstream.append(url)
                        List.addItem(name)
      	window.setFocus(List)


def LIST_UPDATE():
	global playurl
	global iconimage
	global name
	global chstream
	if window.getFocus() == List:
		pos=List.getSelectedPosition()
		iconimage=chicon[pos]
		name=chname[pos]
		Icon.setImage(iconimage)
		playurl=chstream[pos]
		playurl=playurl+'|User-Agent=Mozilla/5.0 (Linux; Android 5.1.1; en-GB; SM-G920F Build/LMY47X.G920FXXS3COK5) MXPlayer/1.7.40'
                       
#####################################################################################
def PlayStream():
        window.close()
        liz=xbmcgui.ListItem(name, iconImage=iconimage,thumbnailImage=iconimage)
        xbmc.Player().play(playurl)
       	
def addLink(name,url,mode,iconimage,fanart,description=''):
		u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&description="+str(description)
		ok=False
		liz=xbmcgui.ListItem(name, iconImage="DefaultFolder.png", thumbnailImage=iconimage)
		liz.setInfo( type="Video", infoLabels={ "Title": name, 'plot': description } )
		liz.setProperty('fanart_image', fanart)
		ok=xbmcplugin.addDirectoryItem(handle=int(sys.argv[0]),url=u,listitem=liz,isFolder=False)
		#import start

START()
window.doModal()
del window
xbmcplugin.endOfDirectory(int(sys.argv[1]))
