def check_input(element):
    return isinstance(element, str)


def get_substring(s):
    seen = set()
    left = 0
    max_len = 0
    max_sub = ""

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])

        if right - left + 1 > max_len:
            max_len = right - left + 1
            max_sub = s[left:right + 1]

    return max_sub


def main(data):
    longest_str = ""
    longest_index = -1

    for i, item in enumerate(data):
        if check_input(item):
            if len(item) > len(longest_str):
                longest_str = item
                longest_index = i

    if longest_index == -1:
        print("-1, ''")
        return

    substring = get_substring(longest_str)
    print(f"{longest_index}, '{substring}'")
