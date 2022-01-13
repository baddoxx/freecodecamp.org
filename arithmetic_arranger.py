import re

def arithmetic_arranger( problems, ans=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    maxlen=[]
    if ans==True:
        answers=[]
        nrows=4
    else:
        answers=[ '' ]*len(problems)
        nrows=3
    rows=[ [] for _ in range( nrows ) ]

    for p in problems:
        operand1, op, operand2 = p.split()
        if op not in ('+','-'):
            return "Error: Operator must be '+' or '-'."
        if ( bool(re.match('^\d+$', operand1)) == False ) or ( bool(re.match('^\d+$', operand2)) == False) :
            return "Error: Numbers must only contain digits."
        if len( operand1 ) > 4 or len( operand2 ) > 4:
            return "Error: Numbers cannot be more than four digits."   

        maxlen=2+max(len(operand1),len(operand2))
        rows[0].append(operand1.rjust(maxlen))
        rows[1].append( op+' '+( operand2 ).rjust( maxlen -2) )
        rows[2].append(  '-'*maxlen )

        if ans==True:
            if op=='+':
                rows[3].append( str( int(operand1) + int(operand2) ).rjust(maxlen) )
            else:
                rows[3].append( str( int(operand1) - int(operand2) ).rjust(maxlen) )

    for row in rows:
        rowstr=''
        for col in row:
            rowstr += col
            rowstr+='    '
        print( rowstr )

