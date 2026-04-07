class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        idx_word = 0
        idx_abbr = 0
        while idx_word < len(word):
            if abbr[idx_abbr].isalpha():
                if abbr[idx_abbr] != word[idx_word]:
                    return False
                idx_word += 1
                idx_abbr += 1
            else:
                length = ''
                while idx_abbr < len(abbr) and abbr[idx_abbr].isnumeric():
                    length += abbr[idx_abbr]
                    idx_abbr += 1
                if length.startswith('0'):
                    return False
                idx_word += int(length)
                print('asdasd', idx_word)
                if idx_word > len(word):
                    return False
        if idx_abbr < len(abbr):
            return False
        return True