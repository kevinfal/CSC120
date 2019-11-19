

def construct_dict(filename):
    file = open(filename)
    d = dict()
    for line in file:
        line = line.strip()
        line = line.split()
        d[line[0]] = line[1:]
    file.close()
    return d

def transfer(words,diction):
    file = open("my_dict.txt",'w')
    words = words.split()
    for word in words:
        word = word.upper()
        file.write(word +"  " +' '.join(diction[word])+"\n")

    file.close()



def main():
    filename = "PronunciationDictionary.txt"
    dic = construct_dict(filename)
    words = input("Words: ")
    transfer(words,dic)


if __name__ == "__main__":
    main()