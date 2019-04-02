class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        
        # The first check that we can make is to check if the end word is even in the word list
        if endWord not in endList:
            return 0
        
        # How can we compare two words and check if there was only a one letter difference?
        
        # Brute force solution will be O (n^2)
        
        # TODO: For every word in the word list for check for every letter in that word if the counter gets decremeneted to 1 meaning that is a valid transformation
        word_set = set(wordList)
        counter = 0
        
        while counter < len(word_set):
            
        
        # Remove from set making amount of words shorter than check through elements in that set by repeating step 1
        
        # TODO: Need a constant check if you are one transformation away from the end word
        
        