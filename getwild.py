import csv

class GetWild:
    csv_file = 'FirstGetWildAndTough.csv'

    @classmethod
    def class_method(cls):
        f = open(cls.csv_file, 'r')

        reader = csv.reader(f)
        header = next(reader)
        wild_ary = []
        for row in reader:
            tmp_arr = row[5].split(":")
            sec = int(tmp_arr[0]) * 60 + int(tmp_arr[1])
            a_wild = GetWild(row[0], row[1], row[3], sec)
            wild_ary.append(a_wild)

        return wild_ary


    def __init__(self, title, artist, file_name, firs_get_wild_seek):
        self.title = title
        self.artist = artist
        self.file_name = file_name
        self.firs_get_wild_seek = firs_get_wild_seek
        self.played = False
        #print  self.title + artist + firs_get_wild_seek + file_name

if __name__ == "__main__":
    a = GetWild.class_method()

    # import pdb;pdb.set_trace()
    # print a
