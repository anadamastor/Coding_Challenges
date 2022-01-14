# https://leetcode.com/problems/find-the-town-judge/

# 
# 
# 
# 
# 
# 

def findJudge(n, trust):

  counter = {}

  #iterate through trusts

  for single_trust in trust:
    counter.setdefault(single_trust[1], 0)
    counter[single_trust[1]] += 1
    #add each trusted person to hash

  print(n, counter.values())

  if n in counter.values():
    return list(counter.keys())[0]
  else:
    return -1
    # if trusted people == n that;s the judge otherwise nowone
        

n = 3
trust = [[1,3],[2,3],[3,1]]

print(findJudge(n, trust))





    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        counter = {}
        
        if len(trust) == 1:
            return trust[0][1]

        for single_trust in trust:
            counter.setdefault(single_trust[1], 0)
            counter[single_trust[1]] += 1
        
        if len(trust) in counter.values():
            return list(counter.keys())[0]
        else:
            return -1