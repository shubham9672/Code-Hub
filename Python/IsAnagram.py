def is_anagram(s: str, t: str) -> bool:
    s = sorted(s)
    t = sorted(t)
    return s == t


if __name__ == "__main__":
    print(is_anagram("tea", "eat"))
    print(is_anagram("teb", "eab"))
