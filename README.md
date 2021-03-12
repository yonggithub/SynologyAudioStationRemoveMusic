# Synology AudioStation RemoveMusic
Remove Music For Synology AudioStation 
在使用audio station过程中，发现没有删除音乐的功能。
如果发现某些音乐不喜欢，如何删除他？ 这是这个项目产生的原因。
这个项目可以帮助大家删除audio staion 中不喜欢的音乐。

关键思路：  
1. 获取sid  
    GET  
    http://***yoursyno.com:yourport***/webapi/auth.cgi?api=SYNO.API.Auth&version=3&method=login&account=***admin***&passwd=***123***&session=AudioStation&format=sid  
    参数说明:   
    1)***yoursyno.com:yourport***: 你群辉登陆的host和port   
    2)***admin***: 你群辉登陆的账号   
    3)***123***: 你群辉登陆的密码   
    ![image](https://user-images.githubusercontent.com/25076827/110906907-9f180400-8347-11eb-887d-4415a9d79a80.png)
    
2. 通过sid调用Synology的playlist播放列表。   
    GET   
    http://***yoursyno.com:yourport***/webapi/AudioStation/playlist.cgi?limit=1000&method=getinfo&library=shared&api=SYNO.AudioStation.Playlist&id=playlist_personal_smart%2F***rat1***&additional=songs_song_tag%2Csongs_song_audio%2Csongs_song_rating%2Csharing_info&version=3&offset=0&sort_by=&sort_direction=ASC&_sid=***ZVRFERJOFE3WcC7LW9761***   
    
    参数说明:   
    1)***yoursyno.com:yourport***: 你的群辉登陆的host和port   
    2) ***rat1***: 需要提前创建***rat1***智播放列表   
       移除评级是1星的歌曲   
       ![image](https://user-images.githubusercontent.com/25076827/110907558-8b20d200-8348-11eb-8062-82be73eb903b.png)   
    3)***ZVRFERJOFE3WcC7LW9761***: sid,见第一步的返回结果   
    ![image](https://user-images.githubusercontent.com/25076827/110907821-ec48a580-8348-11eb-8416-380303d16c68.png)   

    
    
3. 通过sid 调用   
SYNO.FileStation.CopyMove接口，把不喜欢的音乐移除。   
    GET   
    http://***yoursyno.com:yourport***/webapi/entry.cgi?path=***%5B%22%2FMUSIC%2F%E8%BF%AA%E4%B8%BD%E7%83%AD%E5%B7%B4_%E6%AF%9B%E4%B8%8D%E6%98%93-%E6%B5%B4%E7%81%AB%E6%88%90%E8%AF%97-%E3%80%8A%E7%83%88%E7%81%AB%E5%A6%82%E6%AD%8C%E3%80%8B%E7%94%B5%E8%A7%86%E5%89%A7%E7%89%87%E5%B0%BE%E6%9B%B2.mp3%22%5D***&dest_folder_path=***%22%2FMUSIC%2Ftest%22***&overwrite=true&remove_src=true&accurate_progress=true&api=SYNO.FileStation.CopyMove&method=start&version=3&_sid=***ZVRFERJOFE3WcC7LW9761***   
    参数说明:   
    1)***%5B%22%2FMUSIC%2F%E8%BF%AA%E4%B8%BD%E7%83%AD%E5%B7%B4_%E6%AF%9B%E4%B8%8D%E6%98%93-%E6%B5%B4%E7%81%AB%E6%88%90%E8%AF%97-%E3%80%8A%E7%83%88%E7%81%AB%E5%A6%82%E6%AD%8C%E3%80%8B%E7%94%B5%E8%A7%86%E5%89%A7%E7%89%87%E5%B0%BE%E6%9B%B2.mp3%22%5D***: 这是html格式的歌曲路径路径,即:["/music/test/Blue Stahli - Antisleep Vol. 01 - Shotgun Senorita.mp3"] ,音乐路径在上一步【2.通过sid调用Synology的playlist播放列表】可以得到.   
    2)***yoursyno.com:yourport***: 略   
    3)***%22%2FMUSIC%2Ftest%22***: 要移动的地路径   
    4)***ZVRFERJOFE3WcC7LW9761***: sid,请看第一步，获取sid的返回结果   
    ![image](https://user-images.githubusercontent.com/25076827/110908853-5d3c8d00-834a-11eb-80b0-d00283b1a2d0.png)   

    需要关于群辉的更多支持请发邮件到:876222665@qq.com (秒回,有偿回答,5元一次)
