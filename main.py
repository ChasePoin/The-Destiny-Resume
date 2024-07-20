import configuration
import gai

# REQUIRES ENVIRONMENTAL VARIABLES: GOOGLE_API_KEY, BUNGIE_CLIENT_SECRET, BUNGIE_TOKEN, BUNGIE_CLIENT_ID
#### LOWMAN DATA PROVIDED BY LOWMAN-CENTRAL.COM ####
##


def main():
    # sets up AI
    model = gai.configureAI()
    # sets up user (gets user stats, translates them)
    user_setup = configuration.UserSetup()
    user_setup.fullUserSetup()
    # creates the description for the AI
    userDescriptor = configuration.UserDescriptors(user_setup.user)
    description = userDescriptor.create_user_desc()
    # sends the description to gemini
    response = gai.sendPrompt(model, description)
    # write to resume text file
    f = open("resume.txt", "x", encoding="utf-8")
    f.write(response.text)

if __name__ == "__main__":
    main()


# to do: make api endpoint generator function so that grabbers is less ugly...