import util
import checkIndex

RCNF = {
    "K" : [
        ["K2K1"],
        ["K2O"],
        ["K2K3"],
        ["K2Ket"],
        ["K2Pel"]
    ],
    "K1" : [["OKet"]],
    "K2" : [["SP"]],
    "K3" : [["OPel"]],

    "S" : [
        ["PropNoun"],
        ["NPAdj"],
        ["NPNoun"],
        ["NumNP"],
        ["NPPropnoun"],
        ["AdjNP"],
        ["NounNP"],
        ["Hari"],
        ["kemerdekaan"],
        ["tanggal"],
        ["Agustus"],
        ["17"],
    ],
    "O" : [
        ["PropNoun"],
        ["NPAdj"],
        ["NPNoun"],
        ["NumNP"],
        ["NPPropnoun"],
        ["AdjNP"],
        ["NounNP"],
        ["17"],
    ],
    "Pel" : [
        ["PropNoun"],
        ["NPAdj"],
        ["NPNoun"],
        ["NumNP"],
        ["NPPropnoun"],
        ["AdjNP"],
        ["NounNP"],
        ["PrepNP"],
        ["17"],
    ],
    "Ket" : ["PrepNP"],
    "NP" : [
        ["NPAdj"],
        ["NPNoun"],
        ["NumNP"],
        ["NPPropnoun"],
        ["AdjNP"],
        ["NPPronoun"],
        ["NounNP"],
        ["Indonesia"],
        ["17"],
    ],
    "PP" : [["PrepNP"]],
    "P" : [["dilaksanakan"]],
    "VP" : [["dilaksanakan"]],
    "Noun" : [
        ["Hari"],
        ["kemerdekaan"],
        ["tanggal"],
        ["Agustus"],
    ],
    "PropNoun" : [["Indonesia"]],
    "Verb" : [["dilaksanakan"]],
    "Prep" : [["pada"]],
    "Num" : [["17"]]
}

def check(word) :
    rows = len(word)
    table = util.makeTable(word, rows)

    for i in range(0, rows, 1): 
        for j in range(0, rows - i, 1) : 
            ### exctract dictionary kiri & kanan
            if i == 0 : table = checkIndex.firstIndex(RCNF, table[i][j], table, i, j)
            if i > 0 : table = checkIndex.otherIndex(i - 1, j, RCNF, table, i, j)

    util.printTable(table, rows)

    if "K" in (table[rows-1][0][0].split()) : return True
    else : return False