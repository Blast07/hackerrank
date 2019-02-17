def wordCount(words):
    word_dict = {}
    for word in words:
        if word_dict.get(word):
            word_dict[word]+=1
        else:
            word_dict[word]=1
    return word_dict

def checkMagazine(magazine, note):
    magazine_dict = wordCount(magazine)
    note_dict = wordCount(note)
    for word in note_dict:
        if magazine_dict.get(word):
            if magazine_dict[word]<note_dict[word]:
                print("No")
                break
        else:
            print("No")
            break
    else:
        print("Yes")


checkMagazine("two times three is not four".split(),"two times two is not four".split())
