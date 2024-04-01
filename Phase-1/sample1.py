# write a program aone single subject mark check if the marks are >35 cheated marks==35 pass if marks are <35 fail
mark =int(input("Enter the marks"))
if mark>35:
    print('cheated')
elif mark==35:
    print('pass')
else:
    print('fail')