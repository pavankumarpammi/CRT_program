# for i in range(1,6):
#     for j in range(1,i+1):
#         # if(i+j <=6):                            
#         print(i,end='')
    
#     print()
# for i in range(5,1,-1):
#     for j in range(1,5-i+1):
#         print(i,end='')
#     print()
# # for i in range(1,6): 
# #     for j in range(1,6):
# #         if(i==1 or j==5 or j==1 or i==5):                            
# #             print('*',end='')
# #         else:
# #             print(" ",end="")
# #     print()
# #     *
# #    **
# #   ***
# #  ****
# # *****
r,c=4,7
for i in range(1,r+1):
    #space
    for s in range(1,r-i+1):
        print(" ",end="")
    #pattern
    for p in range(1,2*i):
        print("*",end="")
    #space
    # for s in range(2,2*i):

    print()

