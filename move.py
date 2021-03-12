import requests,json

import urllib.parse


dest_folder = "/HD3_8T/music_unlike"

getsid_url = "http://myds.com:5555/webapi/auth.cgi?api=SYNO.API.Auth&version=3&method=login&account=admin&passwd=123456&session=AudioStation&format=sid"

res = requests.get(getsid_url)
sid=json.loads(res.text).get('data').get('sid')

print('sid:{}'.format(sid))
playlist_url = 'http://myds.com:5555/webapi/AudioStation/playlist.cgi?limit=1000&method=getinfo&library=shared&api=SYNO.AudioStation.Playlist&id=playlist_personal_smart%2Frat1&additional=songs_song_tag%2Csongs_song_audio%2Csongs_song_rating%2Csharing_info&version=3&offset=0&sort_by=&sort_direction=ASC&_sid='+sid

py_result = requests.get(playlist_url)

playlist_json = json.loads(py_result.text)
resultcode = playlist_json.get('success')

songspaths = []
if resultcode :
    songs = playlist_json.get('data').get('playlists')[0].get('additional').get('songs')
    # print(songs)
    
    for index in range(len(songs)):
        son = songs[index]
        son_path = son['path']
        songspaths.append(son_path)
    songspathlen = len(songspaths)
    print('songs path len:{}'.format(songspathlen))
    if songspathlen != 0:
        # songspaths = songspaths.replace("'","\"")
        # python 列表转字符串,再单引号转双引号
        songspathstr = str(songspaths).replace("'","\"").replace(r"\n","")
        print(songspathstr)

        #encode param
        values={}
        values['path']=songspathstr
        values['dest_folder_path']="\"{}\"".format(dest_folder)
        data=urllib.parse.urlencode(values)
        
        move_url = 'http://myds.com:5555/webapi/entry.cgi?{}&overwrite=true&remove_src=true&accurate_progress=true&api=SYNO.FileStation.CopyMove&method=start&version=3&_sid={}'.format(data,sid)
        print(move_url)
        mv_result = requests.get(move_url)
        print(mv_result.text)