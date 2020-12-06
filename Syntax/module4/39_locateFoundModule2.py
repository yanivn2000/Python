#slide 25
#half way solution
import sys
print(sys.path)
sys.path.append("not_searched")
print(sys.path)
import foundModule

foundModule.found()