<h1>WebScraping with Spotify API 🎵</h1>

This repository uses the interaction entre APIS using the package BeautifulSoup to get all the top 100 musics of a specific date, on the site https://www.billboard.com/charts/hot-100 and create a particular playlist on spotify with the same top 100 musics that the user asked for.

So, let's start, I recommend you to check first this links to understand what we will need to this code work and the documentation that we need to check
<ul>
 <li>https://www.youtube.com/watch?v=yAXoOolPvjU&t=1254s -> This youtuber helped me to understand what the default informations we need to get, He uses Node.Js, but if you whatch, you will get the feeling of the Spotify API</li>

 <li>https://developer.spotify.com/documentation/general/guides/ -> This is the documentation of the Spotify API</li>
 <li>https://spotipy.readthedocs.io/en/2.13.0/#spotipy.client.Spotify.current_user -> This make everything easier using the Spotify API<li> 
 <li>https://www.crummy.com/software/BeautifulSoup/bs4/doc/ -> BeautifulSoap Documentation, we use this to get all music names of the website Billboard</li>
</ul>

Executing the code, the first message at the prompt of command ask us to insert a date that the user wants to get the top 100 musics, using the default YYYY-MM-DD, because we will use requests to get the page on Billboard with the exacly date
![image](https://user-images.githubusercontent.com/43189736/151885432-e3d8e142-3d13-4539-a63a-cb145f458579.png)

After that, the browser will start and show a page of the Spotify to authorize the code to get the informations, like ID, Secret Key. Something like this :)

<p align="center">
<img src="https://user-images.githubusercontent.com/43189736/151885934-0082cebf-fe0a-4afd-96a7-4cfdbad28c52.png">
</p>


So, after you click to accept, it will send us to another page, that we configured at the beginning following the tutorials, right? We will copy the URL and paste it on the prompt commando to answer the question of the code

![image](https://user-images.githubusercontent.com/43189736/151886853-d4a2aaf9-ad77-4b74-9013-240b32c0dd1e.png)

A file called token.txt was created and now we have the authentication key to proceed with the informations. After that, we don't need to get the URL again, because we have the Token Key, but pay attention, this token have a time to expire, so if you get an error of authentication. maybe you need to delete the file and set a new one like we created the frist. You can do better on this part of code, maybe try to cut this part and get this Token as it expires, it's a great challenge.

To finish this repository, we can check in our spotify and we will see the playlist of the day that we choosed, the same music at the BillBoard site. 
<p align="center">
<img src="https://user-images.githubusercontent.com/43189736/151887875-1676219c-8d6c-47fb-91fd-12ded09d90d6.png">
</p>
