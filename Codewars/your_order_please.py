#6 kyu
#Your order, please
#https://www.codewars.com/kata/55c45be3b2079eccff00010f

def order(sentence):
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    words = sentence.split(' ')
    res = []

    for number in numbers:
        for word in words:
            if word.count(number):
                res.append(word)

    return ' '.join(res)


#Test.assert_equals(order("is2 Thi1s T4est 3a"), "Thi1s is2 3a T4est")
# Test.assert_equals(order("4of Fo1r pe6ople g3ood th5e the2"), "Fo1r the2 g3ood 4of th5e pe6ople")
# Test.assert_equals(order(""), "")

print(order("is2 Thi1s T4est 3a"))
print(order("4of Fo1r pe6ople g3ood th5e the2"))
print(order(""))
