class Solution(object):
     def backspaceCompare(self, S, T):
        def build_string(string):
            result = []
            for char in string:
                if char != '#':
                    result.append(char)
                elif result:
                    result.pop()
            return "".join(result)

        s_processed = build_string(S)
        t_processed = build_string(T)

        return s_processed == t_processed