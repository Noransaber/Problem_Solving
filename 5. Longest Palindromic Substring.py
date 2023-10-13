# Given a string s, return the longest palindromic


def checkLongestPal(s):
    pal = ""
    for i in range(len(s)):
        for j in range(-1, len(s)):
            if s[j] == s[i]:
                pal += s[j]
    return pal
                
  
print(checkLongestPal("babad"))              
            