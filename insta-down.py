import instaloader

def download_instagram_photos(username):
    # 인스타로더 객체 생성
    loader = instaloader.Instaloader(
        download_video_thumbnails=False,  # 비디오 썸네일 다운로드 안 함
        download_geotags=False,  # 위치 태그 다운로드 안 함
        save_metadata=False        
    )

    try:
        # 사용자 프로필 객체 가져오기
        profile = instaloader.Profile.from_username(loader.context, username)

        # 프로필 사진 다운로드
        print(f"Downloading profile picture of {username}...")
        loader.download_profilepic(profile)

        # 게시물 다운로드
        print(f"Downloading posts from {username}'s profile...")
        for post in profile.get_posts():
            loader.download_post(post, target=f"{username}_posts")
        
        print("Download completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    print("\ninsta-down v0.3 by Jonghoon\n")
    username = input("인스타그램 아이디를 입력하고 엔터를 치세요: ")
    download_instagram_photos(username)
    
# pyinstaller --onefile --console ./insta-down-0.2.py
