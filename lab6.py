####################################################################################
# Name: Robert Miller
# Pledge: "I pledge my honor that I have abided by the Stevens Honor System."
####################################################################################
# Lab 6: Recursion 2
# Demonstrate recursion as an algorithm design technique for the problem of 
# computing the (length of the) longest common subsequence of two given strings
#####################################################################################

##############################################################################
# Example: The longest common subsequence of "helllowo_rld" and "!helloabcworld!"
# is "helloworld", and it has a length of 10.
#
# Therefore LLCS("helllowo_rld", "!helloabcworld!") returns 10, and
# LCS("helllowo_rld", "!helloabcworld!") returns "helloworld"
##############################################################################
def LLCS(S1, S2):
#intake is 2 strings that will return the length of the longest subsequence
    if len(S1) >= 1 and len(S2) >= 1:
        if S1[0] == S2[0]:
            return 1 + LLCS(S1[1:],S2[1:])
        else:
            return 0 + max(LLCS(S1[0:],S2[1:]),LLCS(S1[1:],S2[0:]))
        #the max function allows both paths to be checked, which is how I am going to word that ok?
    else:
        return 0
    #0 is returned when the length is ending
    '''
    Return the length of the longest common subsequence (LLCS) of strings S1 and S2
    '''

##############################################################################
# Instead of returning the length of the longest common substring, this task
# asks you to return the string itself.
##############################################################################
# Tip: You may find it helpful to copy your solution to LLCS and edit it
# to solve this problem
##############################################################################

def LCS(S1, S2):
    if len(S1) >= 1 and len(S2) >= 1:
        if S1[0] == S2[0]:
            return S1[0] + LCS(S1[1:],S2[1:])
        else:
            t1 = LCS(S1[0:],S2[1:])
            t2 = LCS(S1[1:],S2[0:])
            if len(t1) > len(t2):
                return '' + t1
            else:
                return '' + t2
        #the max function allows both paths to be checked, which is how I am going to word that ok?
    else:
        return ''
    '''return the longest common subsequence (LCS) between strings S1 and S2'''
