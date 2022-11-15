
class PatternSearch:

    def __init__(self, pattern, file_in, file_out):
        self.pattern = pattern
        self.occurrency = []
        self.file_out = file_out
        self.good_sf_count = 0
        self.bad_char_count = 0

        file = open(file_in, 'r')
        self.text = file.read()

    def generateBadCharShift(self):
        skipList = {}
        for i in range(0, len(self.pattern) - 1):
            skipList[self.pattern[i]] = i + 1
        return skipList

    def boyer_moore_search(self):
        badShift = self.generateBadCharShift()
        i = 0
        while i < len(self.text) - len(self.pattern) + 1:
            j = len(self.pattern)
            while j > 0 and self.pattern[j - 1] == self.text[i + j - 1]:
                j -= 1
            if j > 0:
                arr = self.pattern[j::]
                diggit = self.findMatch(self.pattern[j - 1], j, arr)
                if self.text[i + j - 1] in badShift:
                    letter = abs(j - badShift[self.text[i + j - 1]])
                else:
                    letter = len(self.pattern[:j])
                if diggit > letter:
                    self.good_sf_count +=1
                elif diggit < letter:
                    self.bad_char_count +=1
                i += max(diggit, letter)

            else:
                self.occurrency.append(i)
                i += 1
        return -1

    def findMatch(self, bad_w, index, sub_p):
        if sub_p == "":
            return 1
        new_index = 0
        new_pat = self.pattern[:index]
        all_matches = self.findAllMatch(sub_p, new_pat, [], new_pat)

        if len(all_matches) > 0:
            while len(all_matches) > 0:
                match_index = all_matches[-1]
                if new_pat[match_index - 1] != bad_w or match_index - 1 == -1:
                    new_index = len(new_pat) - match_index
                    break
                else:
                    all_matches.pop()
            if len(all_matches) == 0 and new_index == 0:
                new_index = len(new_pat) + 1
        else:
            new_index = self.findMatch(sub_p[0], index + 1, sub_p[1::])
        return new_index

    def findAllMatch(self, sub_p, new_p, sub, sub_arr):
        if sub_p in new_p:
            sub.append(new_p.index(sub_p[0]) + len(sub_arr) - len(new_p))
            new_p = new_p[new_p.index(sub_p[-1]) + 1::]
            self.findAllMatch(sub_p, new_p, sub, sub_arr)
        return sub

    def write_to_file(self):
        file = open(self.file_out, 'w+')
        try:
            for i in self.occurrency:
                file.write("Pattern mathed at index {} to {}".format(i, i + len(self.pattern)))
                file.write(". With good suffix {} and bad character {} counts".format(self.good_sf_count,
                                                                                          self.bad_char_count))
                file.write("\n")
        finally:
            file.close()



