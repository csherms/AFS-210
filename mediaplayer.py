import random
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
    
    
class Deque:
    def __init__(self):
        self.songs = []
        self.popped_list = []
        
    # def clear(self):
    #     return self.songs == []
    
    # 1. Add song
    def add_song(self, title, artist):
        new_song = Song(title, artist)
        self.songs.append(new_song)
        print("New Song Added to Playlist: " + str(new_song))
        
    # 2. Remove song
    # def remove_song(self):
    #     pass
    
    # 3. Play song    
    def play_song(self):
        print("Playing...." + str(self.songs[0]))    
    
    # 4. Skip song
    def skip_song(self):
        self.popped_list.append(self.songs.pop(0))
        cur_song = self.songs[0]
        print("Skipping....") 
        print("Now playing... " + str(cur_song))
    
    # 5. Go back    
    def go_back(self):
        prev_song = self.popped_list[-1]
        print("Replaying.... " + str(prev_song))
        cut_and_return = self.popped_list.pop()
        self.songs.append(cut_and_return)
    
    # 6. Random shuffle
    # def shuffle(self):
    #     for i in range(len(self.songs)-1, 0, -1):
    #         # Generating a random index from 0 to i + 1
    #         r = random.randint(0, i + 1)
    #         # Swap i with the element at random index
    #         self.songs[i], self.songs[r] = self.songs[r], self.songs[i]
    #     print("Shuffling....")
    #     #Cant get it to print values
        
    # 7. Show currently playing song
    # def show_current_song(self):
    #     cur_song = self.songs[0]
    #     print("Currently playing: " + str(cur_song), end=" ")
    
    # 8. Show current playlist order
    def show_playlist(self):
        num_songs = len(self.songs) + len(self.popped_list)
        print("\nNumber or songs in playlist: ", num_songs)
        print("\nSong list:\n")
        for i in self.songs + self.popped_list:
            print(i)
    
     
# Songs will be added to playlist at start    
new_playlist = Deque()
new_playlist.add_song("hey jude", "the beatles")
new_playlist.add_song("dancing nancies", "dave matthews")
new_playlist.add_song("purple hayze", "jimi hendrix")
new_playlist.add_song("what i got", "sublime")


def menu():
    print(20 * "-" , "MENU" , 20 * "-")
    print("1. Add Song to Playlist")
    print("2. Remove song from Playlist")
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
        title = input("Enter song title: ")
        artist = input("Enter artist: ")
        new_playlist.add_song(title, artist)
        # Add song to playlist
    # elif choice == 2:
    #     # Prompt user for Song Title 
    #     # remove song from playlist
    #     new_playlist.remove_song()
    elif choice == 3:
        # Play the playlist from the beginning
        new_playlist.play_song()
        # Display song name that is currently playing        
    elif choice == 4:
        # Skip to the next song on the playlist
        # Display song name that is now playing
        new_playlist.skip_song()                     
    elif choice == 5:
        # Go back to the previous song on the playlist
        # Display song name that is now playing
        new_playlist.go_back()  
    # elif choice == 6:
    #     # Randomly shuffle the playlist and play the first song
    #     # Display song name that is now playing
    #     new_playlist.shuffle()        
    # elif choice == 7:
    #     # Display the song name and artist of the currently playing song
    #     new_playlist.show_current_song()    
    elif choice == 8:
        # Show the current song list order
        new_playlist.show_playlist()
    elif choice == 0:
        print("Goodbye.")
        break

            
