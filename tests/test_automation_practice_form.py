from model.pages import practice_form


def test_filling_and_submitting_form():
    practice_form.open_practice_form()

    # WHEN
    practice_form.type_first_name('Harry')
    practice_form.type_last_name('Potter')
    practice_form.type_email('hp@test.com')
    practice_form.select_gender('Male')
    practice_form.type_phone('0123456789')

    practice_form.select_birthday(6, 1980, 31)

    practice_form.type_subject('Arts')
    practice_form.select_hobby('Sports')

    practice_form.add_file()

    practice_form.type_address('Hogwarts')

    practice_form.select_state('Haryana')
    practice_form.select_city('Karnal')

    practice_form.submit_form()

    # THEN
    practice_form.should_be_data_in_form(
        'Harry Potter',
        'hp@test.com',
        'Male',
        '0123456789',
        '31 July,1980',
        'Arts',
        'Sports',
        'Pytest_logo.svg.png',
        'Hogwarts',
        'Haryana Karnal'
    )