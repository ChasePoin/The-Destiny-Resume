import grabbers

# hash translator; very rough, gets the job done but is rigid for now... will work on this later. #

def translateHashes(user: grabbers.AccountStats, hash: str | list | dict, typeOfData: str, is_title: bool):
    # translates hashes to actual meaning using endpoint
    # titles are annoying and are the ONLY thing with a separate path... hence the bool
    api_endpoint_url = f"https://www.bungie.net/Platform/Destiny2/Manifest/{typeOfData}/"

    if isinstance(hash, list):
        decoded_array = []
        if is_title == True:
        # check out of for loop bc unnecessary to loop through if is_title == false
        # titles are special circumstance and must have a condition checked due to where they are in json
            for element in hash:
                response = user.session.get(f"{api_endpoint_url}/{element}", headers=grabbers.HEADERS)
                response = response.json()
                decoded_array.append(response['Response']['titleInfo']['titlesByGender']['Male'])
        else:
        # non-title lists
            for element in hash:
                response = user.session.get(f"{api_endpoint_url}/{element}", headers=grabbers.HEADERS)
                response = response.json()
                decoded_array.append(response['Response']['displayProperties']['name'])
                
        return decoded_array
    
    elif isinstance(hash, dict):
    # decoding a dict
    # separated for future proofing
        decoded_dict = {}
        for key in hash:
            # should work for basically any dictionary passed in if any are added in future
            response = user.session.get(f"{api_endpoint_url}/{key}", headers=grabbers.HEADERS)
            response = response.json()
            decoded_dict[response['Response']['displayProperties']['name']] = hash[key]

        return decoded_dict
    
    # one hash at a time
    else:
        response = user.session.get(f"{api_endpoint_url}/{hash}", headers=grabbers.HEADERS)
        response = response.json()
        # once again title is special... WHY
        if is_title == True:
            return response['Response']['titleInfo']['titlesByGender']['Male']
        else:
            return response['Response']['displayProperties']['name']