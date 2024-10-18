# TODO Найдите количество книг, которое можно разместить на дискете
sl_l = 25
l_p = 50
p_b = 100
amount_of_sl_in_one_book = sl_l*l_p*p_b*4
books = 1.44 / (amount_of_sl_in_one_book / 1024**2)
print("Количество книг, помещающихся на дискету:", round(books))
