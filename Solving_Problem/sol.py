def palindrome(word):
    result = []
    str_set = word
    re_str_set = str_set[::-1]
    if str_set == re_str_set :
        return True
    else :
        return False

print(palindrome('nana'))