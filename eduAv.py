###############################################################################

##################### eduAv Prototype Class Functionality #####################

###############################################################################

class eduAv():
    """
    Data structure for an eduAV, for use in the personaliation process
    """
    def __init__(self):
        self.hair_choices = ["BLONDE", "BROWN", "BLACK"] # "RED"
        self.hair_style_choices = ["SHORT", "LONG"] # "BALD", "MEDIUM", "CURLY"
        self.eyes_choices = ["BLUE", "BROWN", "GREEN"]
        self.nose_choices = ["SMALL", "MEDIUM", "LARGE"]
        self.mouth_choices = ["SMILE", "GRIN", "SMIRK"]
        self.skin_tone_choices = ["SKIN1", "SKIN2", "SKIN3", "SKIN4", "SKIN5"] # ["#FFCCAA", "#D38D5F", "#AA4400", "#2B1100"]
        self.uniform_choices = ["BUTTONUP", "TSHIRT", "JUMPER", "SKIRT", "DRESS"]
        # self.uniform_colour_choices = ["#D50000", "#AA00FF", "#03A9F4", "#76FF03", "#FF6D00"]
        self.activity_pose_choices = ["SOCIALPOSE1", "SOCIALPOSE2", "AIRGUITAR"]

        self.hair = ""
        self.eyes = ""
        self.nose = ""
        self.mouth = ""
        self.skin_tone = ""
        self.uniform = ""
        # self.uniform_colour = ""
        self.activity_pose = ""
        self.user_name = ""

    def set_hair(self, hair):
        if hair in self.hair_choices:
            self.hair = hair
            return True
        else:
            print("Not a valid hair colour, please try your selection again:")
            return False

    def get_hair(self):
        return self.hair

    def set_hair_style(self, hair_style):
        if hair_style in self.hair_style_choices:
            self.hair_style = hair_style
            return True
        else:
            print("Not a valid hair style, please try your selection again:")
            return False

    def get_hair_style(self):
        return self.hair_style

    def set_eyes(self, eyes):
        if eyes in self.eyes_choices:
            self.eyes = eyes
            return True
        else:
            print("Not a valid eye, please try your selection again:")
            return False

    def get_eyes(self):
        return self.eyes

    def set_nose(self, nose):
        if nose in self.nose_choices:
            self.nose = nose
            return True
        else:
            print("Not a valid nose, please try your selection again:")
            return False

    def get_nose(self):
        return self.nose

    def set_mouth(self, mouth):
        if mouth in self.mouth_choices:
            self.mouth = mouth
            return True
        else:
            print("Not a valid mouth, please try your selection again:")
            return False

    def get_mouth(self):
        return self.mouth

    def set_skin_tone(self, skin_tone):
        if skin_tone in self.skin_tone_choices:
            self.skin_tone = skin_tone
            return True
        else:
            print("Not a valid skin tone, please try your selection again:")
            return False

    def get_skin_tone(self):
        return self.skin_tone

    def set_uniform(self, uniform):
        if uniform in self.uniform_choices:
            self.uniform = uniform
            return True
        else:
            print("Not a valid uniform, please try your selection again:")
            return False

    def get_uniform(self):
        return self.hair

    def set_activity_pose(self, activity_pose):
        if activity_pose in self.activity_pose_choices:
            self.activity_pose = activity_pose
            return True
        else:
            print("Not a valid activity pose, please try your selection again:")
            return False

    def get_activity_pose(self):
        return self.activity_pose

    def set_user_name(self, user_name):
        self.user_name = user_name
        
    def get_user_name(self):
        return self.user_name

    def get_eduAv(self):
        return self.user_name, self.skin_tone, self.eyes, self.nose, self.mouth, self.hair, self.activity_pose



def main():
    print ("Welome to the 'eduAv' creator, your first step in creating your very own personalised educational avatar!")

    while True:
        confirmation = input('Please input "Yes" to proceed: ')
        if confirmation == "Yes":
            break
        else:
            print("Your input wasn't quite correct, please try again")

    user_eduAv = eduAv()

    user_name = input("\nLets start with your name: ")
    user_eduAv.set_user_name(user_name)

    print("\nHello", user_name, "; Please type your selections exactly as you see them written")

    while True:
        print ("\nHere are your available skin tones:", "SKIN1", "SKIN2", "SKIN3", "SKIN4")
        skin_tone = input("What is your skin tone choice?: ")
        bool_test = user_eduAv.set_skin_tone(skin_tone)
        if bool_test:
            break

    while True:
        print ("\nHere are your available eyes:", "BLUE", "BROWN", "GREEN")
        eyes = input("What is your eye choice?: ")
        bool_test = user_eduAv.set_eyes(eyes)
        if bool_test:
            break

    while True:
        print ("\nHere are your available noses:", "SMALL", "MEDIUM", "LARGE")
        nose = input("What is your nose choice?: ")
        bool_test = user_eduAv.set_nose(nose)
        if bool_test:
            break

    while True:
        print ("\nHere are your available mouths:", "SMILE", "GRIN", "SMIRK")
        mouth = input("What is your mouth choice?: ")
        bool_test = user_eduAv.set_mouth(mouth)
        if bool_test:
            break

    while True:
        print ("\nHere are your available hair colours:", "BLONDE", "BROWN", "BLACK")
        hair = input("What is your hair choice?: ")
        bool_test = user_eduAv.set_hair(hair)
        if bool_test:
            break

    while True:
        print ("\nHere are your available hair styles:", "SHORT", "LONG")
        hair_style = input("What is your hair choice?: ")
        bool_test = user_eduAv.set_hair_style(hair_style)
        if bool_test:
            break

    while True:
        print ("\nHere are your available uniforms:", "BUTTONUP", "TSHIRT", "JUMPER", "SKIRT", "DRESS")
        uniform = input("What is your uniform choice?: ")
        bool_test = user_eduAv.set_uniform(uniform)
        if bool_test:
            break

    while True:
        print ("\nHere are your available activity poses:", "SOCIALPOSE1", "SOCIALPOSE2", "AIRGUITAR")
        activity_pose = input("What is your activity pose choice?: ")
        bool_test = user_eduAv.set_activity_pose(activity_pose)
        if bool_test:
            break

    print("\nThank you for designing your very own personalised eduAv!")
    print("\nYour Personalised eduAv:\n", user_eduAv.get_eduAv())

if __name__ == "__main__":
    main()