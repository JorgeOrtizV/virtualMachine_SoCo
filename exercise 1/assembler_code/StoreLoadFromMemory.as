ldc R0 1      
ldc R1 5   
# mem[5] = 15    
str R0 R1    
# 15 
prm R1
# R2 should be now 1
ldr R2 R1
hlt 
