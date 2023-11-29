ldc R0 @array # Beginning address of the array
ldc R2 1  # Value to add to the array
ldc R1 6  # Length of the array
# Write values to the array
loop:
str R2 R0
inc R2
inc R0
dec R1
bne R1 @loop

# Proof the values 0 to 4 are in the array
ldc R0 @array
ldc R1 6
loop1:
prm R0
inc R0
dec R1
bne R1 @loop1

# Swap in place
ldc R0 @array
ldc R1 6
ldc R2 3 # Stop of iteration. This has to be added manually since division is not supported
ldc R3 0 # Upper limit
loop2:
# Addition to get upper limit
dec R1
add R3 R0
add R3 R1
# 15 + 5 = 20
# 16 + 3 = 19
# 17 + 1 = 18
swp R0 R3
ldc R3 0
dec R1
inc R0 
dec R2
bne R2 @loop2

# Prove that the swap was actually made
ldc R0 @array
ldc R1 6
loop3:
prm R0
inc R0
dec R1
bne R1 @loop3

hlt
.data
array: 6