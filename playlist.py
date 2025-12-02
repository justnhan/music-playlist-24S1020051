songs=[
    {'Title':'Người đừng lặng im','artist':'soobin','duration':200},
    {'Title':'Yêu 5','artist':'Rhymastic','duration':300},
    {'Title':'Thất tình','artist':'Trịnh Đình Quang','duration':400}
    ]

def main():
    while True: 
        print("\n--- MUSIC PLAYLIST MANAGER ---") 
        print("1. Thêm bài hát") 
        print("2. Xem danh sách phát") 
        print("3. Tìm bài hát theo ca sĩ") 
        print("4. Thoát") 
         
        choice = input("Chọn chức năng: ") 
         
        if choice == '1': 
            add_song() 
        elif choice == '2': 
            view_playlist() 
        elif choice == '3': 
            search_by_artist() 
        elif choice == '4': 
            print("Kết thúc chương trình.") 
            break 
        else: 
            print("Lựa chọn không hợp lệ.") 

def add_song():
    print ("Vui lòng nhập tên bài hát:")
    title = input()
    print("Nhập nghệ sĩ:")
    artist = input()
    print("Nhập thời lượng:")
    duration = int(input())
    songs.append({
        "Title": title,
        "artist": artist,
        "duration": duration
    })
    print("Đã thêm bài hát vào playlist.")


def view_playlist():
    for i in range (len(songs)):
        print ("1.",songs[i]["Title"],"- Nghệ sĩ -",songs[i]["artist"],"(",songs[i]["duration"],"s)")


    

if __name__ == "__main__": 
    main() 

