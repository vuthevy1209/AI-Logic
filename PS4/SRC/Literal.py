class Literal:
    def __init__(self, symbol = "", negation = False) -> None:
        self.symbol = symbol
        self.negation = negation

    def __repr__(self):
        return '-{}'.format(self.symbol) if self.negation == True else self.symbol

    # compare two literals (==)
    def __eq__(self, literal) -> bool:
        return self.symbol == literal.symbol and self.negation == literal.negation
    
    # compare two literals (<)
    def __lt__(self, literal) -> bool:
        if self.symbol != literal.symbol:
            return self.symbol < literal.symbol
        return self.negation < literal.negation
    
    def __hash__(self):
        result = '-' + self.symbol if self.negation else self.symbol
        return hash(result)

    def negate(self):
        self.negation = 1 - self.negation 
        
    # Check if two literals are opposite
    def isOpposite(self, literal):
        return self.negation != literal.negation and self.symbol == literal.symbol
    
    def parseLiteral(stringLiteral):
        stringLiteral = stringLiteral.strip() 
        if stringLiteral[0] == '-':
            newLiteral = Literal(symbol = stringLiteral[1], negation = True) 
        else:
            newLiteral = Literal(symbol = stringLiteral[0], negation = False) 

        return newLiteral   


