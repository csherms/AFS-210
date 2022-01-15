from deque_class import MyDeque
class Song:
    def __init__(self,title,artist):
        self.title = title
        self.artist = artist

    def getTitle(self):
        return self.title

    def getArtist(self):
        return self.artist
        
    def __str__(self):
        return self.title + " by " + self.artist 

    def __eq__(self, other):
        return ((self.title, self.artist) == (other.title, other.artist))
        
    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))
        
    def __gt__(self, other):
        return ((self.title, self.artist) < (other.title, other.artist))
    
     
class MyMediaPlayer():
    def __init__(self):
        self.playlist = MyDeque()

    def add_song(self, song):
        self.playlist.appendLeft(song)
        
    def remove_song(self, title):#2 still broken
        self.playlist.remove(title)
        
    def skip(self):
        self.playlist.rotate(1)
        self.play()
        
    def reverse(self):
        self.playlist.rotate(-1)
        self.play()
        
    def play(self):
        cur_song = self.playlist.peek_left()
        print(cur_song.getTitle())
        
    def song_info(self):
        print(self.playlist.get_data())
        
    def show_playlist(self):
        return self.playlist.show_all()
        
    def shuffle_songs(self):
        self.playlist.shuffle_all_songs()
        print(self.play())
        
        
        
player = MyMediaPlayer()
player.add_song(Song("Johnny B. Goode", "Chuck Berry"))
player.add_song(Song("Nancy Mulligan", "Ed Sheeran"))
player.add_song(Song("Wish You Were Here", "Pink Floyd"))
player.add_song(Song("So Thankful", "Nahko"))
player.add_song(Song("Enemy", "Imagine Dragons"))
player.add_song(Song("Drug", "Marcus Eaton"))
player.add_song(Song("Still", "Dr. Dre"))
player.add_song(Song("Spancil Hill", "The High Kings"))


        
        

def menu():
    print(20 * "-" , "MENU" , 20 * "-")
    print("1. Add Song to Playlist")
    print("2. Remove song from Playlist") #2 still broken
    print("3. Play")
    print("4. Skip")
    print("5. Go Back")
    print("6. Shuffle")
    print("7. Show Currently Playing Song")
    print("8. Show Current Playlist Order")
    print("0. Exit")
    print(47 * "-")


while True:
    menu()
    choice = int(input())

    if choice == 1:
        # Add code to prompt user for Song Title and Artist Name
        # Add song to playlist
        title = input("Enter song title: ")
        artist = input("Enter artist: ")
        player.add_song(Song(title, artist))
    elif choice == 2:
        # Prompt user for Song Title 
        # remove song from playlist
        title = input("Enter song title: ")
        player.remove_song(title)
    elif choice == 3:
        # Play the playlist from the beginning
        # Display song name that is currently playing
        print("Playing....") 
        player.play()       
    elif choice == 4:
        # Skip to the next song on the playlist
        # Display song name that is now playing    
        player.skip()                 
    elif choice == 5:
        # Go back to the previous song on the playlist
        # Display song name that is now playing 
        player.reverse()
    elif choice == 6:
        # Randomly shuffle the playlist and play the first song
        # Display song name that is now playing
        print("Shuffling.... Now Playing: ") 
        player.shuffle_songs()       
    elif choice == 7:
        # Display the song name and artist of the currently playing song
        player.song_info()   
    elif choice == 8:
        # Show the current song list order
        print("\nSong list:\n")
        player.show_playlist()
    elif choice == 0:
        print("Goodbye.")
        break

            
