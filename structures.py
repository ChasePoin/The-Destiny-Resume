# structures created with important hashes used to get information from the API


# hash of every single title currently in the game (records)
title_hashes = ['2889189256','1556658903','1343839969','969142496', '3214425110','2584970263','1384029371','2909250963','540377256','2482004751',
                '3298130972','3464275895','4141971983','1438167672','3588818798','1971228746','2489106733','1228693527','1564001702','3056675381',
                '3097916612','3910736783','1089543274','2126152885','2302993504','3906538939','3646306576','3974717227','865076293','1142693639',
                '3315095100','1382005115','149024466','1156427773','3175660257','3137935313','4083696547','2269203216','3570567217','1722592950',
                '3249408038','4250626982','4176879201','3947410852','1710217127','1284946259','2991743002','2796658869','1087927672','2056461735',
                '2499679097','3169895614','317521250','1185680627','758645239','3766199186','1109459264','966207508','2472740040','1866578144','1561715947']

# hashes that lead to the flawless triumph for each raid (records)
flawless_raid_completion_hashes =  {'380332968': 'Last Wish',
                                    '3560923614': 'Deep Stone Crypt',
                                    '1522774125': 'Garden of Salvation',
                                    '2750088202': 'Vault of Glass',
                                    '4019717242': 'Vow of the Disciple',
                                    '1360511082': "King's Fall",
                                    '397062446': 'Root of Nightmares'}

# hashes that lead to each type of raid, used to get completion info (aggregatve activties)
# for some reason these are int instead of str like everything else
raid_completion_hashes = {910380154: 'Deep Stone Crypt',
                          1042180643: 'Garden of Salvation',
                          3458480158: 'Garden of Salvation',
                          2659723068: 'Garden of Salvation',
                          2122313384: 'Last Wish',
                          3881495763: 'Vault of Glass',
                          3022541210: 'Vault of Glass',
                          1485585878: 'Vault of Glass',
                          1441982566: 'Vow of the Disciple',
                          4217492330: 'Vow of the Disciple',
                          1374392663: "King's Fall",
                          3257594522: "King's Fall",
                          2381413764: 'Root of Nightmares',
                          2918919505: 'Root of Nightmares',
                          4179289725: "Crota's End",
                          1507509200: "Crota's End",
                          1541433876: "Salvation's Edge",
                          4129614942: "Salvation's Edge",
                          4169648179: 'The Pantheon',
                          4169648176: 'The Pantheon',
                          4169648177: 'The Pantheon',
                          4169648182: 'The Pantheon'}

# dungeon completion hashes (METRICS)
dungeon_completion_hashes = {'1339818929': 'Shattered Throne',
                             '1451729471': 'Pit of Heresy',
                             '352659556':  'Prophecy',
                             '451157118':  'Grasp of Avarice',
                             '3862075762': 'Duality',
                             '3702217360': 'Spire of the Watcher',
                             '3846201365': 'Ghosts of the Deep',
                             '3932004679': "Warlord's Ruin"}

# solo flawless triumphs (records)
flawless_dungeon_completion_hashes = {'3205009787': 'Shattered Throne',
                                      '3950599483': 'Pit of Heresy',
                                      '3191784400': 'Prophecy',
                                      '3718971745': 'Grasp of Avarice',
                                      '4126703847': 'Duality',
                                      '4032136335': 'Spire of the Watcher',
                                      '2105117002': 'Ghosts of the Deep',
                                      '238037026': "Warlord's Ruin"}

# element kills metric hashes
element_kills_metric_hashes =  {'1513312460': 'Arc',
                                '2187143539': 'Solar',
                                '2327589890': 'Void',
                                '2889561660': 'Strand',
                                '2464463405': 'Stasis'}

# class nums (api class definitions match 012 to each class)
classes = {0: 'Titan',
           1: 'Hunter',
           2: 'Warlock'}

# same thing for platforms
platforms = {0: 'None',
             1: 'Xbox',
             2: 'Playstation',
             3: 'Steam'}