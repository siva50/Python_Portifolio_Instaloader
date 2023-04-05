import instaloader
siva=instaloader.Instaloader()
name=input("enter your id:")
siva.download_profile(name,profile_pic_only=True)
name=instaloader.Profile.from_username(siva.context,"sivaramakrishnagundu")
print(name.biography)