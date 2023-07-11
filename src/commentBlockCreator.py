



import sys, os
import re
from prompt_toolkit import completion, prompt



#################
#Comment Block
#Function: grabFile
#Description: Open file and call LookForFunctions
#replace the original file with the new comment block full
#file.
#################

def grabFile(file):

    with open(file, "r") as f:
        with open("outfile.py", "w+") as o:
            lineNumLis = lookForFunctions(f, o)
            os.replace(o.name, file)
    return



#################
#Comment Block
#Function: lookForFunctions
#Description: Look for functions and classes,
#and copy/write lines and comment blocks to temp
#outfile
#################

def lookForFunctions(fileDesc, outFileDesc):
    content = fileDesc.readlines()
    params = ""
    
    for line in content:
        if "def " in line or "class " in line or "if __name" in line:
            splitLine = re.split("d", line)
            try:
                params = re.search('\(([^)]+)', line).group(1)
            except:
                pass
            
            indent = indentCalc(splitLine)
                
            outFileDesc.write(f"\n{indent}#################\n")
            if len(params.split(", ")) > 2 and params != None:
                outFileDesc.write(f"{indent}#Comment Block\n")
                if("def" in line):
                    lineSplit = line.split("(")[0].split(" ")
                    outFileDesc.write(indent + f"#Function: {lineSplit[len(lineSplit) - 1]}\n")
                elif("class" in line):
                    lineSplit = line.split("(")[0].split(" ")[1].split(":")[0]
                    outFileDesc.write(f"{indent}#Class: {lineSplit}\n")
                outFileDesc.write(f"{indent}#Description: \n")
                for i in params.split(", "):
                    if i != "self":
                        outFileDesc.write(f"{indent}#{i} Param: \n")

            else:
                outFileDesc.write(f"{indent}#Comment Block\n")
                if("def" in line):
                    lineSplit = line.split("(")[0].split(" ")
                    outFileDesc.write(f"{indent}#Function: {lineSplit[len(lineSplit) - 1]}\n")
                elif("class" in line):
                    lineSplit = line.split("(")[0].split(" ")[1].split(":")[0]
                    outFileDesc.write(f"{indent}#Class: {lineSplit}\n")
                outFileDesc.write(f"{indent}#Description: \n")
            
            outFileDesc.write(indent + "#################\n\n")
            
        outFileDesc.write(line)



#################
#Comment Block
#Function: indentCalc
#Description: Calculate the indentation of the 
#comment block based on the amount of \t or spaces
#in the split lines
#################

def indentCalc(splitLine):
    defIndent = 0
    if(len(splitLine) > 1 or "\t" in splitLine[0]):
        if(len(splitLine) == 1):
            for i in splitLine[0]:
                if i == "\t":
                    defIndent = defIndent + 1
        else:
            if("\t" in splitLine[0]):
                for i in splitLine[0]:
                    defIndent = defIndent + 1
            else:
                defIndent = int(len(splitLine[0]) / 4)
            
        indent = ""
        for i in range(defIndent):
            indent = indent + "\t"
        return indent
    else:
        return ""




#################
#Comment Block
#Description: Runs main when program called
#with prompt_toolkit allowing for tab completion
#################

if __name__ == "__main__":
    ret = prompt("File Path: ", completer = completion.PathCompleter())
    grabFile(ret)