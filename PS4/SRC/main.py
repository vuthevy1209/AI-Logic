import os
import glob
from KB import KB
from FileIO import FileIO

def main():

    currentDir = os.path.dirname(os.path.abspath(__file__))
    inputDir = os.path.join(currentDir, 'input')
    outputDir = os.path.join(currentDir, 'output')
    
    if not os.path.exists(inputDir):
        print(f"Input directory '{inputDir}' does not exist.")
        return
    
    os.makedirs(outputDir, exist_ok=True)
    
    inputFiles = glob.glob(os.path.join(inputDir, '*.txt'))
    
    if not inputFiles:
        print(f"No input files found in directory '{inputDir}'.")
        return
    
    for inputFile in inputFiles:
        outputFile = os.path.join(outputDir, os.path.basename(inputFile))
        
        kb = FileIO.readInputFile(inputFile)
        result, derivedClauses = kb.PL_Resolution()
        FileIO.writeOutputFile(outputFile, result, derivedClauses)

if __name__ == '__main__':
    main()