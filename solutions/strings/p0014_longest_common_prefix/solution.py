class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        minString = len(strs[0])
        index = 0
        counter = 0
        for i in range(len(strs)):
            if minString >= len(strs[i]):
                minString = len(strs[i])
                index = i
    
        minString = strs[index]
        strs.pop(index)
        strsLength = len(strs)
        minStringLength = len(minString)
        output = ""
        for i in range(1,minStringLength + 1):
            for j in range(strsLength):
                if minString[0:i] == strs[j][0:i]:
                    counter = counter + 1
                else:
                    break
            if counter >= strsLength:
                output = minString[0:i]
            counter = 0

        if strsLength <= 0:
            output =  minString
        return output
