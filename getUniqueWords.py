import os

#Get the texto from the document
def openTXT(documentName):
    try:
        # Intentamos abrir el archivo en modo lectura
        with open(documentName, 'r') as text:
            return text.readlines()  # Leer las líneas del archivo
    except FileNotFoundError:
        # Si el archivo no existe, lo creamos
        with open(documentName, 'w') as text:
            # Si el archivo se crea, podemos escribir algo inicial si es necesario
            print(f"El archivo '{documentName}' no existía, ha sido creado.")
            return []  # Retornamos una lista vacía ya que no hay contenido
    except Exception as e:
        # Capturamos otros posibles errores
        print(f"Error al abrir o crear el archivo: {e}")
        return []

            
#Get the unique words
def getUniqueWords(text):
    uniqueWords = []

    for i in text:
        if len(i.split()) > 1:
            word = i.split()[1]
            if word not in uniqueWords:
                uniqueWords.append(word)

    return uniqueWords

#Print the words of the document
def printWords(list):
    for i in enumerate(list, 1):
        print(f"{i[0]}. {i[1].title()}")

#Write the words in the document
def writeDocument(documentName, list):
    try:
        # Abrimos el archivo en modo de adición ('a'), lo que asegura que no se sobrescriban las líneas existentes
        with open(documentName, 'w') as document:
            for i in enumerate(list,1):
                document.write(f"{i[0]}. {i[1].title()}\n")
        print("Writting completed")
    except Exception as e:
        print("There was an error.")

#Open the document to visualize it
def open_document(DocumentName):
    try:
        # Para sistemas Windows
        os.startfile(DocumentName)  # Abre el archivo con la aplicación predeterminada
    except Exception as e:
        print(f"Error al intentar abrir el archivo: {e}")


def writeNewWords(DocumentToCopyFrom, DocumentToWriteIn):
    old_document = openTXT(DocumentToWriteIn)
    new_document = openTXT(DocumentToCopyFrom)
    new_words = getUniqueWords(new_document)
    old_Words = getUniqueWords(old_document)
    for i in new_words:
        if i not in old_Words:
            old_Words.append(i)
    writeDocument(DocumentToWriteIn, old_Words)
    open_document(DocumentToWriteIn)
    
   

writeNewWords("(Working)_LabTech_200_Verbs_Enumerated.txt", "English_Verbs.txt")
    

        

    
