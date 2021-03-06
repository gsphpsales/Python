import nltk

#nltk.download()

base = [('eu sou admirada por muitos','alegria'),
        ('me sinto completamente amado','alegria'),
        ('amar e maravilhoso','alegria'),
        ('estou me sentindo muito animado novamente','alegria'),
        ('eu estou muito bem hoje','alegria'),
        ('que belo dia para dirigir um carro novo','alegria'),
        ('o dia está muito bonito','alegria'),
        ('estou contente com o resultado do teste que fiz no dia de ontem','alegria'),
        ('o amor e lindo','alegria'),
        ('nossa amizade e amor vai durar para sempre', 'alegria'),
        ('estou amedrontado', 'medo'),
        ('ele esta me ameacando a dias', 'medo'),
        ('isso me deixa apavorada', 'medo'),
        ('este lugar e apavorante', 'medo'),
        ('se perdermos outro jogo seremos eliminados e isso me deixa com pavor', 'medo'),
        ('tome cuidado com o lobisomem', 'medo'),
        ('se eles descobrirem estamos encrencados', 'medo'),
        ('estou tremendo de medo', 'medo'),
        ('eu tenho muito medo dele', 'medo'),
        ('estou com medo do resultado dos meus testes', 'medo')]

#print(base[0])


stopwordsnltk = nltk.corpus.stopwords.words('portuguese')
#print(stopwordsnltk)

def removestopwords(texto):
    frases = []
    for (palavras, emocao) in texto:
        semstop = [p for p in palavras.split() if p not in stopwordsnltk]
        frases.append((semstop, emocao))
    return frases

print(removestopwords(base))

#with radical
def aplicastemmer(texto):
    stemmer = nltk.stem.RSLPStemmer()
    frasessstemming = []
    for (palavras, emocao) in texto:
        comstemming = [str(stemmer.stem(p)) for p in palavras.split() if p not in stopwordsnltk]
        frasessstemming.append((comstemming, emocao))
    return frasessstemming
frasescomstemming = aplicastemmer(base)
print(frasescomstemming)

#words without emotion - emocao
def buscapalavras(frases):
    todaspalavras = []
    for (palavras, emocao) in frases:
        todaspalavras.extend(palavras)
    return todaspalavras
palavras = buscapalavras(frasescomstemming)
print(palavras)

def buscafrequencia(palavras):
    palavras = nltk.FreqDist(palavras)
    return palavras

frequencia = buscafrequencia(palavras)
print(frequencia.most_common(50))

def buscapalavrasunicas(frequencia):
    freq = frequencia.keys()
    return freq

palavrasunicas = buscapalavrasunicas(frequencia)
print(palavrasunicas)

#passing words to be checked in the database. word radical

def extratorpalavras(documento):
    doc = set(documento)
    caracteristicas = {}
    for palavras in palavrasunicas:
        caracteristicas['%s' % palavras] = (palavras in doc)
    return caracteristicas

caracteristicasfrase = extratorpalavras(['am', 'nov', 'dia'])
print(caracteristicasfrase)

#test base full

basecompleta = nltk.classify.apply_features(extratorpalavras, frasescomstemming)
print(basecompleta)