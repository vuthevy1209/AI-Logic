from KB import KB

class FileIO:
    @staticmethod
    def readInputFile(fileName):
        with open(fileName, 'r') as file:
            lines = file.readlines()
            alphaClause = lines[0].strip()
            cnfClauses = []
            for line in lines[1:]:
                cnfClauses.append(line.strip())
            
            file.close()
            return KB(alphaClause, cnfClauses)
        
    @staticmethod
    def writeOutputFile(fileName, result, derivedClauses):
        with open(fileName, 'w') as file:
            for clauses in derivedClauses:
                file.write('{}\n'.format(len(clauses)))
                for clause in clauses:
                    file.write('{}\n'.format(clause))
            if result == True:
                file.write('YES')
            else:
                file.write('NO')
            file.close()