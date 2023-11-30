class Solution:
    def interpret(self, command: str) -> str:
        interpretation = []
        i = 0
        while i < len(command):
            if command[i] == 'G':
                interpretation.append('G')
                i += 1
            elif command[i] == '(' and command[i+1] == ')':
                interpretation.append('o')
                i += 2
            elif command[i] == '(' and command[i+1] == 'a':
                interpretation.append('al')
                i += 4
        return ''.join(interpretation)

