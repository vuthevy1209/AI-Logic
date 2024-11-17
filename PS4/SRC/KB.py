from Clause import Clause
from itertools import combinations

class KB:
    def __init__(self, alphaClause=None, cnfClauses=None):
        self.KB = [] 
        if alphaClause and cnfClauses:
            alphaClause = alphaClause.strip()
            alphaLiterals = alphaClause.split('OR')
            for literal in alphaLiterals:
                clause = Clause.parseClause(literal)
                clause.negate()
                self.KB.append(clause)

            for clauseString in cnfClauses:
                clause = Clause.parseClause(clauseString)
                clause.cleanClause()
                self.KB.append(clause)


    def PL_Resolution(self):
        currentClauses = set(self.KB) 
        derivedClauses = [] 
        hasContradiction = False 

        while True:
            newClauses = set()  
            
            for (clauseA, clauseB) in combinations(currentClauses, 2):
                resolvents, isEmpty = Clause.PL_Resolve(clauseA, clauseB)
                newClauses.update(resolvents)
                
                if isEmpty:
                    hasContradiction = True

            newUniqueClauses = newClauses.difference(currentClauses)
            derivedClauses.append(newUniqueClauses)
            currentClauses.update(newClauses)

            if hasContradiction: 
                return True, derivedClauses
            if not newUniqueClauses: 
                return False, derivedClauses
