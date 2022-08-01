uInput = input('Enter string to check for not bad: ')

#compare indexes of not and bad if both are found and if they are in correct order than replace string with good from where bad started

notIndex = uInput.find('not')
badIndex = uInput.find('bad')


if((notIndex > 0) and (badIndex > notIndex)):
    range_list = [(notIndex, len(uInput))]
    res = ''.join(chr for idx, chr in enumerate(uInput, 1) if not any(strt_idx <= idx <= end_idx  #erases everything from not forward
         for strt_idx, end_idx in range_list)) 
         
         
    newString = str(res)
    repString = "good"

    finalString = newString + " " +  repString
    print(finalString)  
else:
    print(uInput)
    

