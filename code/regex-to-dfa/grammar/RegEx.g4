grammar RegEx;

prog : (regex newline)*;

regex : regex '*'      #klnee
  | regex regex	       #concatenation
  | regex '|' regex    #alternation
  | ID         	       #identifier
  | 'λ'	       	       #epsilon
  | '(' regex ')'      #parenthesis
  ;

newline : '\n';

ID: [a-zA-Z0-9];
WS: [\t\r ]->skip;