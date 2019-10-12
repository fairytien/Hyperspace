def apple_pen(first_ingredient, second_ingredient):
    l1 = 'I have a pen, I have a apple\\nUh! Apple-Pen!'
    l2 = 'I have a pen, I have a pineapple\\nUh! Pineapple-Pen!'
    l3 = 'I have a pen, I have a pen\\nUh! Long pen!'
    lyrics = [l1, l2, l3]
    for sentence in lyrics:
        if first_ingredient in sentence and second_ingredient in sentence:
            if 0 < sentence.find(first_ingredient) < sentence.find(second_ingredient):
                return(sentence)
