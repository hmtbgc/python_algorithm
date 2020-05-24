# Rabin-Karp algorithm

class RabinKarp:

    def __init__(self):
        self.alpha_num = 256
        self.mod_num = 101
    
    def compute_hashcode(self, string):
        hashcode = 0
        temp_alpha_num = self.alpha_num % self.mod_num
        for c in string[:-1]:
            hashcode = (hashcode + ord(c)) * temp_alpha_num % self.mod_num
        hashcode = (hashcode + ord(string[-1])) % self.mod_num
        return hashcode

    def single_string_search(self, string, pattern):
        m = len(pattern)
        n = len(string)
        pattern_hashcode = self.compute_hashcode(pattern)
        previous_hashcode = self.compute_hashcode(string[:m])
        ans = []
        for i in range(n-m+1):
            if (i == 0):
                temp_hashcode = previous_hashcode
            else:
                temp_hashcode = ((previous_hashcode+self.mod_num - ord(string[i-1])*pow(self.alpha_num, m-1, self.mod_num))\
                                * self.alpha_num + ord(string[i+m-1])) % self.mod_num
            if (pattern_hashcode == temp_hashcode):
                if (pattern == string[i:i+m]):
                    ans.append(i)
            previous_hashcode = temp_hashcode
        if (not ans):
            return "not found"
        else:
            return ans     
