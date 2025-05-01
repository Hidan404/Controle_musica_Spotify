from dados import DadosApi
import spotipy
from spotipy.oauth2 import SpotifyOAuth

class Requisicao():
    def __init__(self):
        self.dados = DadosApi()
        self.sp =  spotipy.Spotify(auth_manager=SpotifyOAuth(
            client_id= self.dados.CLIENTE_ID,
            client_secret= self.dados.CLIENTE_SECRET,
            redirect_uri= self.dados.url,
            scope= self.dados.ESCOPO
        ))


    def mostrar_status(self):
        atual = self.sp.current_playback()
        if atual and atual["is_playing"]:
            musica = atual["item"]
            print(f"\n🎵 Tocando agora: {musica['name']} - {musica['artists'][0]['name']}")
            print(f"Álbum: {musica['album']['name']}")
        else:
            print("\nNenhuma música está tocando.")

    def pausar(self):
        self.sp.pause_playback()
        print("⏸ Pausado.")

    def continuar(self):
        self.sp.start_playback()
        print("▶ Continuando...")

    def proxima(self):
        self.sp.next_track()
        print("⏭ Próxima música.")

    def anterior(self):
        self.sp.previous_track()
        print("⏮ Música anterior.")

    def buscar_musica(self):
        nome = input("🔍 Digite o nome da música: ")
        resultado = self.sp.search(q=nome, type="track", limit=1)
        if resultado["tracks"]["items"]:
            uri = resultado["tracks"]["items"][0]["uri"]
            self.sp.start_playback(uris=[uri])
            print(f"🎧 Tocando: {resultado['tracks']['items'][0]['name']}")
        else:
            print("❌ Música não encontrada.")    
