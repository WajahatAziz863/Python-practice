#Adding items in a dictionary
solo={
    'anco':2000,
    'flas':1997,
    'part':'classic'
}
solo.update({"intx":"corrupt"})
print(solo)
#Removing items from dictionary
del solo['part']#we can also use solo.pop('part') for removing.
print(solo)