class Solution:
    def reverseVowels(self, s):
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        characters = list(s)
        i = 0
        j = len(s) - 1

        while i < j:
            while i < j and characters[i] not in vowels:
                i+=1
            while i < j and characters[j] not in vowels:
                j -=1
            characters[i], characters[j] = characters[j], characters[i]
            i+=1
            j -=1
        return ''.join(characters)

    # def reverseVowels(self, s):
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        vowels_list = []
        for i, char in enumerate(s):
            if char in vowels:
                vowels_list.append((i, char))
        vowels_list.reverse()
        vowel_index = 0
        new_string = ''
        for i, char in enumerate(s):
            if char in vowels:
                index, character = vowels_list[vowel_index]
                vowel_index +=1
                new_string += character
            else:
                new_string += char
        return new_string

# s = "leetcode"
s = 'aAbo'
solution = Solution()
solution.reverseVowels(s)
