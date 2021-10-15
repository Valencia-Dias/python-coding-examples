def max_charCount(s):
    character_dict={}
    for i in s:
        if i in character_dict:
            character_dict[i]+=1
        else:
            character_dict[i]=1
    values_dict=character_dict.values()
    return max(values_dict)

print(max_charCount("abcdrfkjwrccyhcjbkblkibb"))
