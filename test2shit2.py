import glob
from collections import Counter
import re
import gc
import timeit
import tkinter.messagebox as dialog
from tkinter.filedialog import askdirectory


class Parse():
    def runMe(self):
        start = timeit.default_timer()
        dialog.showinfo('Instructions', 'In the next step select the folder where the positive reviews are')
        path = askdirectory()
        paths = str(path)
        print(paths)
        path1 = paths.replace('C:', '')
        print(path1)
        files = glob.glob((path1+'/*.txt'))
        dialog.showinfo('Instructions', 'In the next step select the folder where the negative reviews are')
        path2 = askdirectory()
        paths2 = str(path2)
        path2 = paths2.replace('C:', '')
        nfiles = glob.glob((path2+'/*.txt'))

        trainarray = []
        list2 = []
        list3 = []


        for review in files:
            try:
                with open(review, encoding="utf8") as fi:
                    list2.append(filter(None, re.split("[,}\@\£\$\€¨\*^< \" \ -!{?:/>=.)(0-9]+",
                                                            fi.read().lower())))
                    # list2 = [x for x in trainarray if x != ['']]
                    fi.close()
            except (IOError, OSError):
                print("Error: Double check the folderpath for negative reviews")


        for review in nfiles:
            try:
                with open(review, encoding="utf8") as fi:
                    list3.append(filter(None, re.split("[,}\@\£\$\€¨\*^< \" \ -!{?:/>=.)(0-9]+",
                                                            fi.read().lower())))
                    # list3 = [x for x in trainarray if x != ['']]
                    fi.close()
            except (IOError, OSError):
                print("Error: Double check the folderpath for negative reviews")


        def frequency(para):
            # for underliste in para:
            tot_review = sum(para, Counter())



            return tot_review


        tot_reviews = frequency(list2)
        tot_reviews3 = frequency(list3)


        def iterates(filename, file):
            try:
                with open(filename, 'w', encoding="utf8") as f:
                    print(file, file=f)
            except (IOError, OSError):
                print("Something went wrong when writing to file")


        iterates('positive_train.txt', tot_reviews)
        iterates('negative_train.txt', tot_reviews3)
        stop = timeit.default_timer()

        stop1 = ((stop - start) / 60)
        print("Your request took this many minutes to complete: {:.0f}".format(stop1))




