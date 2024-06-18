def single_root_words(*args):
    same_words = []
    other_words = [*args]
    root_word = str(other_words[0])           #здесь можно вводить любое слово из списка
    for word in other_words:
        def_word = word.lower()               #вводим отдельную переменную, в которой символы только нижнего регистра
        def_root_word = root_word.lower()     #вводим отдельную переменную, в которой символы только нижнего регистра
        if word == root_word:                 #исключаем одинаковые слова
            continue
        #elif def_word in def_root_word:      #как вариант использования оператора in
        elif def_word.count(def_root_word):   #сравниваем переменные с нижним регистром
            same_words.append(word)           #но вводим при это изначальное слово с сохранением регистра
        #elif def_root_word in def_word:      #как вариант использования оператора in
        elif def_root_word.count(def_word):
            same_words.append(word)
    result1 = same_words
    result2 = same_words
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)