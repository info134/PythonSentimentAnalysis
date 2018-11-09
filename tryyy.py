import json
import re
import math

class Calculate():

    def naive_bayes(self, inputs):
        text15 = ""
        oke = (1, 1)
        with open("positive_train.txt", "rb") as f:
            text = f.read().decode("ascii", "ignore")
        with open("negative_train.txt", "rb") as f:
            negtext = f.read().decode("ascii", "ignore")
        name = ""


        def cleanUpPos():
            text1 = text.replace("-", "")
            text0 = text1.replace("`", "")
            text2 = re.sub("\'", "\"", text0)
            text3 = re.sub("\[", "", text2)
            text4 = re.sub('[\\\\/;)*?<>|]', '', text3)
            text5 = text4.replace("{", "")
            text66 = text5.replace("}", "")
            text6 = re.sub("\]", "", text66)
            text8 = re.sub('\"\"', '"', text6)
            text7 = re.sub(r'(?<=\w)"(?=\w)', "'", text8)
            text9 = text7.replace("\\", "")
            text10 = text9.replace("₤", "")
            text11 = text10.replace("Counter(", "")
            text12 = re.sub(r'(?<=\")"', "", text11)
            text13 = text12.replace(' ": ', ' "empty_string": ')
            text14 = re.sub(r'\b"\b', "'", text13)
            text15 = "{" + text14 + "}"
            # print(text15[595033:595035])
            text16 = (text15)
            return text16

        def cleanUpNeg():
            text1 = negtext.replace("-", "")
            text0 = text1.replace("`", "")
            text2 = re.sub("\'", "\"", text0)
            text3 = re.sub("\[", "", text2)
            text4 = re.sub('[\\\\/;)*?<>|]', '', text3)
            text5 = text4.replace("{", "")
            text66 = text5.replace("}", "")
            text6 = re.sub("\]", "", text66)
            text8 = re.sub('\"\"', '"', text6)
            text7 = re.sub(r'(?<=\w)"(?=\w)', "'", text8)
            text9 = text7.replace("\\", "")
            text10 = text9.replace("₤", "")
            text11 = text10.replace("Counter(", "")
            text12 = re.sub(r'(?<=\")"', "", text11)
            text13 = text12.replace(' ": ', ' "empty_string": ')
            text14 = re.sub(r'\b"\b', "'", text13)
            text15 = "{" + text14 + "}"
            # print(text15[595033:595035])
            text16 = (text15)
            return text16

        searchFor = inputs

        searchForM = searchFor.split(" ")
        dicttxt = json.loads(cleanUpNeg())
        dicttxt2 = json.loads(cleanUpPos())




        def prob(pos, neg, sannsyn_pos, sannsyn_neg, x):
            lengthn = len(dicttxt)
            lengthp = len(dicttxt2)
            leng = lengthn+ lengthp
            # print (leng)
            pap = math.log(lengthp, leng)
            # print (pap)
            pan = math.log(lengthn, leng)
            # print(pan)
            sannsyn_pos *= (pap * pos) / lengthp
            # print (sannsyn_pos)
            sannsyn_neg *= (pan * neg) / lengthn
            positive = "maybe"
            if sannsyn_pos < sannsyn_neg:
                print("\nThe new word is: ", x, "\nAt this point the sentence is probably negative")
                print("Positive output: {:.50f}".format(sannsyn_pos), " Entries: ", pos,
                      "\nNegative output: {:.50f}".format(sannsyn_neg), " Entries: ", neg, "\n\n")
                positive = "f"
                return sannsyn_neg, sannsyn_pos, positive
            elif sannsyn_neg == sannsyn_pos:
                print("\nThe probabilities are too close to determine the sentiment")
                print("Positive output: {:.50f}".format(sannsyn_pos), " Entries: ", pos,
                      "\nNegative output: {:.50f}".format(sannsyn_neg), " Entries: ", neg, "\n\n")
                positive="e"
                return sannsyn_neg, sannsyn_pos, positive
            else:
                print("\nThe new word is: ", x, "\nAt this point the sentence is probably positive")
                print("Positive output: {:.50f}".format(sannsyn_pos), " Entries: ", pos,
                  "\nNegative output: {:.50f}".format(sannsyn_neg), " Entries: ", neg, "\n\n")
                positive = "t"
                return sannsyn_neg, sannsyn_pos, positive


        okes = (())
        for x in searchForM:
            try:
                pos = dicttxt2[x]
                neg = dicttxt[x]
                sum = pos + neg
                oke = prob(pos, neg, oke[0], oke[1], x)
                okes = oke[2]
            except KeyError:
                pass
        okes2 = ','.join(str(v) for v in okes)
        return okes2
