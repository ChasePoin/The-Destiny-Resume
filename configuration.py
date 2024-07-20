import grabbers
import translator
import structures

class UserSetup():
    def __init__(self):
        self.user = grabbers.AccountStats()
    def raidSetup(self):
        # grabs all raid related information
        self.user.grabRaidInfo()
        self.user.grabRaidLowmans()
        self.user.grabFlawlessRaids()
    def dungeonSetup(self):
        # grabs all dungeon related information
        self.user.grabDungeonInfo()
        self.user.grabSoloFlawlessDungeons()
    def generalSetup(self):
        # grabs all general character information (emblem, weapons, titles)
        self.user.grabAndStore()
        self.user.grabCharacterInfo()
        self.user.grabTenFavoriteWeapons()
        self.user.grabGlimmerShardsDust()
        self.user.grabAcquiredTitles()
        self.user.favoriteElement()
    def translation(self):
        # translates any needed hashes to understandable stuff
        self.user.titleStatus = translator.translateHashes(self.user, self.user.titleStatus, 'DestinyRecordDefinition', True)
        self.user.most_used_exotic_dict = translator.translateHashes(self.user, self.user.most_used_exotic_dict, 'DestinyInventoryItemDefinition', False)
        self.user.seasons_played = translator.translateHashes(self.user,self.user.seasons_played, 'DestinySeasonDefinition', False)
        self.user.main_emblem = translator.translateHashes(self.user,self.user.main_emblem, 'DestinyInventoryItemDefinition', False)
        self.user.main_title = translator.translateHashes(self.user,self.user.main_title, 'DestinyRecordDefinition', True)
        self.user.main = structures.classes[self.user.main]
        self.user.platform = structures.platforms[self.user.platform]
    def fullUserSetup(self):
        # calls all setups (change this if you want to only get information from a certain part)
        self.generalSetup()
        self.raidSetup()
        self.dungeonSetup()
        self.translation()
    
    
# class due to the fact that I may add more descriptors later, like more precise ones that only use raid or dungeon or general
class UserDescriptors():
    def __init__(self, user: grabbers.AccountStats):
        self.user = user
    def create_user_desc(self) -> str:
        str_to_pass_gemai = ("Pull all knowledge you have about the game 'Destiny 2,' including everything about the stats, activities, characters, and players. " 
                              "Write a professional resume for a player of 'Destiny 2' include all of the following stats: " 
                              f"Name: {self.user.bungie_name}, Destiny Membership ID: {self.user.destiny_membership_id}. "
                              f"They started playing destiny 2 on {self.user.date_of_new_light}. They play on {self.user.platform}."
                              f"They are a {self.user.favorite_element} {self.user.main}. "
                              f"The title the mainly use is {self.user.main_title} and the emblem they mainly use is {self.user.main_emblem}. "
                              f"Their total playtime is {self.user.totalPlaytime / 60} hours and have played in the following seasons: {str(self.user.seasons_played)}. "
                              f"They have {self.user.glimmer} Glimmer and {self.user.bright_dust} Bright Dust. "
                              f"Their top 10 exotic weapons with the number following the weapon being the kills of the weapon are: {str(self.user.most_used_exotic_dict)}. "
                              f"They have the following titles/seals: {str(self.user.titleStatus)} "
                              f"Their active triumph score is {self.user.active_triumph_score} and their total triumph score is {self.user.total_triumph_score}. "
                              f"Here is a list of their raid clears, with the number after each raid corresponding to the amount of clears that raid has: {str(self.user.raidClears)} "
                              f"They have flawlessly done the following raids: {str(self.user.flawlessRaidClears)}. "
                              f"They have lowmanned the following raids, ron means root of nightmares, with the number preceeding the raid list the amount of people they cleared it with, for example 3 is trio, 2 is duo, 1 is solo: {str(self.user.total_lowmans)}. "
                              f"These are their dungeon completions with the number following the dungeon being the number of clears they have of the dungeon: {str(self.user.dungeon_completions)}. "
                              f"They have solo flawlessed the following dungeons: {str(self.user.SoloFlawlessDungeonClears)}. "
                              "Give them a rating from 1-10 and describe what kind of guardian they are based off of these stats in 600 words.")
        return str_to_pass_gemai
