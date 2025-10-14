from typing import *
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        def newWordFunction(w:str,wordList:set):
            # wL=list(w)
            new_words=[]
            for i in range(len(w)):
                wL=list(w)
                original_w=wL[i]
                for j in range(ord('a'),ord('z')+1):
                    # old=wL[i]
                    new=chr(j)
                    if new==original_w:
                        continue
                    wL[i]=new
                    new_word=''.join(wL)
                    if new_word in wordList:
                        new_words.append(new_word)
            
            return new_words



        if endWord not in wordList:
            return 0
        
        q=deque([])
        wordList=set(wordList)
        q.append((beginWord,1))  #(word, level)
        if beginWord in wordList:
            wordList.remove(beginWord)

        while q:
            w,l=q.popleft() #word,level
            new_words:list=newWordFunction(w,wordList)

            # if new_word == endWord:
            #     return l+1
            # elif new_word in wordList:
            #     q.append((new_word,l+1))
            #     wordList.remove(new_word)
            for newWord in new_words:
                if newWord==endWord:
                    return l+1
                if newWord in wordList:
                    q.append((newWord,l+1))
                    wordList.remove(newWord)
        return 0        



obj=Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
ans=obj.ladderLength(beginWord,endWord,wordList)
print(ans)

beginWord ="hot"
endWord ="dog"
wordList =["hot","dog","dot"]
ans=obj.ladderLength(beginWord,endWord,wordList)
print(ans)

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
ans=obj.ladderLength(beginWord,endWord,wordList)
print(ans)

beginWord = "a"
endWord = "c"
wordList = ["a","b","c"]
ans=obj.ladderLength(beginWord,endWord,wordList)
print(ans)

beginWord = "hot"
endWord = "dog"
wordList = ["hot","dog"]
ans=obj.ladderLength(beginWord,endWord,wordList)
print(ans)