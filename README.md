## WebScraping with Spotify API 🎵

This repository uses the interaction between APIs and the **BeautifulSoup** package to get the Top 100 songs from a specific date on the [https://www.billboard.com/charts/hot-100](https://www.billboard.com/charts/hot-100) website and create a private Spotify playlist containing those same 100 songs requested by the user.

---

## 🔗 Documentation and References

I recommend checking these links first to understand the necessary code requirements and the documentation you need to consult:

* **Spotify API (Concepts):** [https://www.youtube.com/watch?v=yAXoOolPvjU&t=1254s](https://www.youtube.com/watch?v=yAXoOolPvjU&t=1254s)
    > This YouTuber (uses Node.js) helped me understand the standard information needed to interact with the Spotify API.

* **Spotify API Documentation:** [https://developer.spotify.com/documentation/general/guides/](https://developer.spotify.com/documentation/general/guides/)

* **Spotipy Library (Python):** [https://spotipy.readthedocs.io/en/2.13.0/#spotipy.client.Spotify.current_user](https://spotipy.readthedocs.io/en/2.13.0/#spotipy.client.Spotify.current_user)
    > This makes everything easier when using the Spotify API.

* **BeautifulSoup Documentation:** [https://www.crummy.com/software/BeautifulSoup/bs4/doc/](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
    > Used for **web scraping** to get all the song names from the Billboard website.

---

## 🚀 Execution Flow

1.  **Data Input:** When running the code, the first message in the command prompt will ask the user to enter a date to get the Top 100 songs, using the standard format `YYYY-MM-DD`. The system will use `requests` to fetch the Billboard page for that exact date.

2.  **Spotify Authorization:** Next, the browser will launch and display a Spotify page to authorize the code to obtain necessary information (like ID and Secret Key).

    ![Spotify Authorization Page](https://user-images.githubusercontent.com/43189736/151885934-0082cebf-fe0a-4afd-96a7-4cfdbad28c52.png)

3.  **Token Retrieval:** After clicking 'Accept', the user will be redirected to the configured callback URL. This new URL must be copied and pasted into the command prompt to answer the code's question.

    ![Copy Callback URL](https://user-images.githubusercontent.com/43189736/151886853-d4a2aaf9-ad77-4b74-9013-240b32c0dd1e.png)

4.  **Token File Creation:** A file named `token.txt` is created containing the authentication key. For subsequent runs, this key will be used, bypassing the need to get the URL again.

5.  **Final Result:** To finalize this repository, you can check your Spotify account and see the newly created playlist for the day you chose, containing the same songs from the Billboard website.

    ![Created Spotify Playlist](https://user-images.githubusercontent.com/43189736/151887875-1676219c-8d6c-47fb-91fd-12ded09d90d6.png)
