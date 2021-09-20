from pythonisms.linked_list_iterator import*


def test_string():

    food = LinkedList()
    food.insert("apple")
    food.insert("banana")


    actual = (food.__str__())
    expected = "[ banana ] -> [ apple ] -> None" 

    assert actual == expected



def test_of_range():

    number_range = range(1,50+1)

    num = LinkedList(number_range)

    actual = len(num)
    excepted = 50

    assert actual == excepted












