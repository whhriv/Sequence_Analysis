

#FASTA format converter - convert to string
def FASTAConverter(FASTAstring):
    #check for FASTA headers, pull and assign title
    if FASTAstring[0] == ">":
        finalIndex = FASTAstring.index('\n')
        title = FASTAstring[:finalIndex]
        sequence = FASTAstring[finalIndex+1:]
        sequence = sequence.replace("\n", "")
        sequence = sequence.replace("\r", "")
        return [title, sequence]
    else:
        FASTAstring = FASTAstring.replace("\n", "")
        FASTAstring = FASTAstring.replace("\r", "")
        return ["untitled", FASTAstring]
    
#Find compliment DNA base pair string
def sequenceCompliment(sequenceDNA):
    complimentDNA = []
    sequenceDNA = sequenceDNA.lower()
    for i in sequenceDNA:
        if i == "t":
            complimentDNA.append("a")
        elif i == "a":
            complimentDNA.append("t")
        elif i == "c":
            complimentDNA.append("g")
        elif i == "g":
            complimentDNA.append("c")
    complimentDNA = ''.join(complimentDNA)
    return complimentDNA
        

#Validate that string is compatible DNA sequence
def isSequenceValid(sequenceDNA):
    if sequenceDNA != "":
            sequenceDNA = set(list(sequenceDNA.lower()))
            a = True
            for i in sequenceDNA:
                if not (i in ['a', 'c', 't', 'g']):
                    a = False
            return a
    else:
        print("this is not a valid DNA sequence")
        return False

#finding ATGC composition of sequence
def composition(sequenceDNA):
    composition = {}
    for i in sequenceDNA.lower():
        composition[i] = composition.get(i, 0) + 1
    return composition

#translate DNA to RNA
def DNA_to_RNA(sequenceDNA):
    sequenceRNA = []
    sequenceDNA = sequenceDNA.lower()
    for i in sequenceDNA:
        if i == "t":
            sequenceRNA.append("a")
        elif i == "a":
            sequenceRNA.append("u")
        elif i == "c":
            sequenceRNA.append("g")
        elif i == "g":
            sequenceRNA.append("c")
    sequenceRNA = ''.join(sequenceRNA)
    return sequenceRNA

# GC content calculator -See composition function - 
def percentGC(sequenceDNA):
    compositionDNA = composition(sequenceDNA)
    percentGC = 100 * (compositionDNA["g"] + compositionDNA["c"]) / (len(sequenceDNA))
    return percentGC

#Translation function - RNA->Protein ||Need to convert to RNA before use||
def translation(sequenceRNA):
    AAlibrary = {
    'uuu': 'F', 'ucu': 'S', 'uau': 'Y', 'ugu': 'C',
    'uuc': 'F', 'ucc': 'S', 'uac': 'Y', 'ugc': 'C',
    'uua': 'L', 'uca': 'S', 'uaa': '*', 'uga': '*',
    'uug': 'L', 'ucg': 'S', 'uag': '*', 'ugg': 'W',
    'cuu': 'L', 'ccu': 'P', 'cau': 'H', 'cgu': 'R',
    'cuc': 'L', 'ccc': 'P', 'cac': 'H', 'cgc': 'R',
    'cua': 'L', 'cca': 'P', 'caa': 'Q', 'cga': 'R',
    'cug': 'L', 'ccg': 'P', 'cag': 'Q', 'cgg': 'R',
    'auu': 'I', 'acu': 'T', 'aau': 'N', 'agu': 'S',
    'auc': 'I', 'acc': 'T', 'aac': 'N', 'agc': 'S',
    'aua': 'I', 'aca': 'T', 'aaa': 'K', 'aga': 'R',
    'aug': 'M', 'acg': 'T', 'aag': 'K', 'agg': 'R',
    'guu': 'V', 'gcu': 'A', 'gau': 'D', 'ggu': 'G',
    'guc': 'V', 'gcc': 'A', 'gac': 'D', 'ggc': 'G',
    'gua': 'V', 'gca': 'A', 'gaa': 'E', 'gga': 'G',
    'gug': 'V', 'gcg': 'A', 'gag': 'E', 'ggg': 'G',
    }
    proteinSequence = []
    for i in range(0,3):

        sequenceCodon = [ sequenceRNA[j:j+3] for j in range(i, len(sequenceRNA), 3) ]
        sequenceProtein = [ AAlibrary[i] for i in sequenceCodon if i in AAlibrary ]
        proteinSequence.append(sequenceProtein)

    return proteinSequence

def tempPCR(sequenceADN):
    GC = percentGC(sequenceADN)
    Tm = 67.5 + (0.34*GC)-(395/len(sequenceADN))
    return Tm