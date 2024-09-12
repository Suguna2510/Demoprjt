import sys 

from pylint import lint  

THRESHOLD = 3 

run = lint.Run(["fibo.py"])

score = run.linter.stats["global_note"]  

if score < THRESHOLD: 

    print("Linter failed: Score < threshold value") 

    sys.exit(1) 


sys.exit(0) 
