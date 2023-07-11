
#################
#Name: Joperezc
#Date: 07/11/23
#File Description: Script for automating
#comment block creation in python files
#################


import sys, os
import re
from prompt_toolkit import completion, prompt



#################
#Comment Block
#Function: grabFile
#Description: Open file and call LookForFunctions
#replace the original file with the new comment block full
#file.
#file Param: file path
#################

def grabFile(file):

    with open(file, "r") as f:
        with open("outfile.py", "w+") as o:
            makeHeader(f, o)
            lookForFunctions(f, o)
            os.replace(o.name, file)
    return

#################
#Comment Block
#Function: makeHeader
#Description: Make an intro comment block
#at top of file
#fileDesc Param: file descriptor
#outFileDesc Param: Temp out file for
#rewriting.
#################

def makeHeader(fileDesc, outFileDesc):
    outFileDesc.write("\n#################\n")
    outFileDesc.write("#Name: \n")
    outFileDesc.write("#Date: \n")
    outFileDesc.write("#File Description: \n")
    outFileDesc.write("#################\n")


#################
#Comment Block
#Function: lookForFunctions
#Description: Look for functions and classes,
#and copy/write lines and comment blocks to temp
#outfile
#fileDesc Param: file descriptor
#outFileDesc Param: Temp out file for
#rewriting.
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
#splitLine Param: file line split with either no
#spaces/tabs preceeding the funciton/class definition
#or spaces/tabs preceeding the function/class definition
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