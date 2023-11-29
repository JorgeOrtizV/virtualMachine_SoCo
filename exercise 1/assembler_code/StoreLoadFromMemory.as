ldc R0 15      
ldc R1 5   
# mem[5] = 15    
str R0 R1    
# 15 
prm R1
# Should print 15
ldr R2 R1
prr R2 
hlt 