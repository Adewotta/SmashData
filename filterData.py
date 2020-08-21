import copy
import csv
resultsDict = {'Bayonetta': [0, 0], 'Bowser Jr.': [0, 0], 'Bowser': [0, 0], 'Captain Falcon': [0, 0], 'Cloud': [0, 0], 'Corrin': [0, 0], 'Daisy': [0, 0], 'Dark Pit': [0, 0], 'Diddy Kong': [0, 0], 'Donkey Kong': [0, 0], 'Dr. Mario': [0, 0], 'Duck Hunt': [0, 0], 'Falco': [0, 0], 'Fox': [0, 0], 'Ganondorf': [0, 0], 'Greninja': [0, 0], 'Ice Climbers': [0, 0], 'Ike': [0, 0], 'Inkling': [0, 0], 'Jigglypuff': [0, 0], 'King Dedede': [0, 0], 'Kirby': [0, 0], 'Link': [0, 0], 'Little Mac': [0, 0], 'Lucario': [0, 0], 'Lucas': [0, 0], 'Lucina': [0, 0], 'Luigi': [0, 0], 'Mario': [0, 0], 'Marth': [0, 0], 'Mega Man': [0, 0], 'Meta Knight': [0, 0], 'Mewtwo': [0, 0], 'Mii Brawler': [0, 0], 'Ness': [0, 0], 'Olimar': [0, 0], 'Pac-Man': [0, 0], 'Palutena': [0, 0], 'Peach': [0, 0], 'Pichu': [0, 0], 'Pikachu': [0, 0], 'Pit': [0, 0], 'Pokemon Trainer': [0, 0], 'Ridley': [0, 0], 'R.O.B.': [0, 0], 'Robin': [0, 0], 'Rosalina': [0, 0], 'Roy': [0, 0], 'Ryu': [0, 0], 'Samus': [0, 0], 'Sheik': [0, 0], 'Shulk': [0, 0], 'Snake': [0, 0], 'Sonic': [0, 0], 'Toon Link': [0, 0], 'Villager': [0, 0], 'Wario': [0, 0], 'Wii Fit Trainer': [0, 0], 'Wolf': [0, 0], 'Yoshi': [0, 0], 'Young Link': [0, 0], 'Zelda': [0, 0], 'Zero Suit Samus': [0, 0], 'Mr. Game & Watch': [0, 0], 'Incineroar': [0, 0], 'King K. Rool': [0, 0], 'Dark Samus': [0, 0], 'Chrom': [0, 0], 'Ken': [0, 0], 'Simon Belmont': [0, 0], 'Richter': [0, 0], 'Isabelle': [0, 0], 'Mii Swordfighter': [0, 0], 'Mii Gunner': [0, 0], 'Piranha Plant': [0, 0], 'Joker': [0, 0], 'Hero': [0, 0], 'Banjo-Kazooie': [0, 0], 'Terry': [0, 0], 'Byleth': [0, 0], 'Random Character': [0, 0], 'Min Min': [0, 0]}
characterDict = {}
for characterKeys in resultsDict:
    characterDict[characterKeys] = copy.deepcopy(resultsDict)
with open('Sets.tsv', newline='') as setsTsv:
    setsReader = csv.reader(setsTsv, delimiter='\t')
    with open('dataSheet.tsv',"w", newline='') as dataTsv:
        dataWriter = csv.writer(dataTsv, delimiter='\t')
        for row in setsReader:
            participants = int(row[1])
            losingPlacement = int(row[2])
            winningPlacement = int(row[3])
            losingCharacter = row[4]
            winningCharacter = row[5]
            worstPlacing = participants//4
            if participants >= 50 and losingPlacement <= worstPlacing and winningPlacement <= worstPlacing :
                characterDict[winningCharacter][losingCharacter][0]+=1
                characterDict[losingCharacter][winningCharacter][1] += 1
        header = [" ","LOST"]
        for characters in characterDict:
            header.append(characters)
        dataWriter.writerow(header)
        dataWriter.writerow(["WON"])
        for outerCharacterKeys in characterDict:
            characterList = [outerCharacterKeys," "]
            for innerCharacterKeys in characterDict[outerCharacterKeys]:
                characterList.append(characterDict[outerCharacterKeys][innerCharacterKeys])
            dataWriter.writerow(characterList)