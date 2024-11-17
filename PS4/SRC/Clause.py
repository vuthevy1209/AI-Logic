from Literal import Literal

class Clause:
    def __init__(self):
        self.clause = [] 
    
    def __repr__(self):
        if self.clause:
            return ' OR '.join(map(str, self.clause))
        else:
            return '{}'
    
    # Compare two clauses (==)
    def __eq__(self, other):
        return set(self.clause) == set(other.clause)
    
    # Compare two clauses (<)
    def __lt__(self, other):
        if len(self.clause) != len(other.clause):
            return len(self.clause) < len(other.clause)

        for i in range(len(self.literals)):
            if self.clause[i] != other.clause[i]:
                return self.clause[i] < other.clause[i]
        
        return False
    
    def __hash__(self) -> int:
        return hash(tuple(self.clause)) 
    
    def isEmpty(self):
        return len(self.clause) == 0
    
    # Check if clause is meaningless
    def isMeaningless(self):
        for literal in self.clause:
            if literal.negation:
                if Literal(symbol = literal.symbol, negation = False) in self.clause:
                    return True
            else:
                if Literal(symbol = literal.symbol, negation = True) in self.clause:
                    return True
    
    # Add literal into clause
    def addLiteral(self, literal):
        self.clause.append(literal)
    
    # Remove duplicate and sort literals
    def cleanClause(self):
        self.clause = sorted(set(self.clause))
    
    # Clone clause with exception
    def cloneClauseNot(self, literal):
        newClause = Clause()
        for l in self.clause:
            if l != literal:
                newClause.addLiteral(l)
                
        return newClause
    
    # Parse clause
    @staticmethod
    def parseClause(stringClause):
        newClause = Clause()
        stringLiterals = stringClause.strip().split('OR')
        for stringLiteral in stringLiterals:
            newClause.addLiteral(Literal.parseLiteral(stringLiteral))
            
        newClause.cleanClause()
        return newClause
    
    # Merge clauses
    @staticmethod
    def mergeClauses(clause1, clause2):
        newClause = Clause()
        newClause.clause = clause1.clause + clause2.clause
        newClause.cleanClause()
        
        return newClause
    
    # Negate clause
    def negate(self):
        for literal in self.clause:
            literal.negate()
    
    # Resolve clauses
    @staticmethod
    def PL_Resolve(clause1, clause2) :
        isEmpty = False
        resolvents = set()

        for literal1 in clause1.clause:
            for literal2 in clause2.clause:
                if literal1.isOpposite(literal2):
                    newClause = Clause.mergeClauses(clause1.cloneClauseNot(literal1), clause2.cloneClauseNot(literal2))
                    if newClause.isMeaningless(): 
                        continue
                    if newClause.isEmpty():
                        isEmpty = True
                        
                    resolvents.add(newClause)

        return resolvents, isEmpty
