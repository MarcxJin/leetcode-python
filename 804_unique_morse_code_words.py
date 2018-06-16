class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        morse_d = {}
        for i in range(26):
            morse_d[chr(i+97)] = morse[i]
        retset = set()
        for word in words:
            curr_morse = ""
            for char in word:
                curr_morse += morse_d[char]
            retset.add(curr_morse)
        return len(retset)