from textblob import TextBlob

a = input("Enter a text:")
print("Original text: " + str(a))

b = TextBlob(a)

print("Correct text: "+ str(b.correct()))