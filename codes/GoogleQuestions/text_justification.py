# Leetcode 68

def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
    curr_line = []
    curr_word = ""
    i = 0
    ans = []
    width = 0

    while i < len(words):
        curr_word = words[i]
        if (width + len(curr_word)) <= maxWidth:
            width += len(curr_word) + 1
            curr_line.append(curr_word)
            i += 1
        else:
            # justifying the curr_line

            spaces = maxWidth - width + len(curr_line)
            added = 0
            j = 0

            while added < spaces:
                if j >= len(curr_line) - 1:
                    j = 0

                curr_line[j] += " "
                added += 1
                j += 1

            """
            spaces = (maxWidth - width + len(curr_line)) / (len(curr_line)-1)
            curr_line[0] += " " * math.ceil(spaces)
            for j in range(1, len(curr_line)-1):
                curr_line[j] += " " * math.floor(spaces)  
            """
            ans.append("".join(curr_line))

            curr_line = []
            width = 0

    # justifying the last line
    for i in range(len(curr_line) - 1):
        curr_line[i] += " "
    spaces_left = maxWidth - width + 1
    curr_line[-1] += " " * spaces_left
    ans.append("".join(curr_line))
    return ans