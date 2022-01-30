import instaloader
ig = instaloader.Instaloader()
dp = input("enter your name ")
ig.download_profile(dp, profile_pic_only=True)
