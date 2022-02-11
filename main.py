from instafollower import InstaFollower

# Chrome Driver Path
chrome_driver_path = "CHROME_DRIVER_PATH"

# Instagram Credentials
insta_username = "YOUR_USERNAME"
insta_password = "YOUR_PASS"

# Instagram profile to get followers from
reference_account = "INSTAGRAM_PROFILE_REFERENCE"

# QUANTITY of profiles to follow
how_many_follows = 5

# Creating the Driver
insta_bot = InstaFollower(chrome_driver_path, insta_username, insta_password)

# Logging in to Instagram
insta_bot.login()

# Finding profiles not followed in reference account
insta_bot.find_followers(reference_account)

# Follow a number of profiles
insta_bot.follow(how_many_follows)
