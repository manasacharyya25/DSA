class Solution:
    @staticmethod
    def calculateTime(keyboard: str, word: str) -> int:
        keyboard_pos = [0 for i in range(26)]

        for i in range(26):
            keyboard_pos[ord(keyboard[i])-97] = i

        prev_pos = 0
        curr_pos = 0
        cost = 0

        for i in range(len(word)):
            curr_pos = keyboard_pos[ord(word[i])-97]
            cost += abs(curr_pos-prev_pos)
            prev_pos = curr_pos

        return cost


if __name__ == '__main__':
    Solution.calculateTime("abcdefghijklmnopqrstuvwxyz", "cba")
