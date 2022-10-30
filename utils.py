import sqlite3


def get_value_from_db(sql):
    with sqlite3.connect("netflix.db") as connection:
        connection.row_factory = sqlite3.Row
        result = connection.execute(sql).fetchall()
        return result


def search_by_tite(title):
    sql = f'''SELECT title, country , release_year , listed_in as genre , description  FROM netflix
           WHERE title = {title}
           order by date_added desc
           LIMIT 1'''
    result = get_value_from_db(sql)
    for item in result:
        return dict(item)


def search_by_release_year(year_from, year_to):
    sql = f'''SELECT title, release_year FROM netflix
            WHERE release_year BETWEEN {year_from} and {year_to}
            LIMIT 100'''
    result = get_value_from_db(sql)
    return dict(result)


def search_by_rating(rating):
    rating_dict = {
        'children': ("G"),
        'family': ("G", "PG", "PG-13"),
        'adult': ("R", "NC-17")
    }
    sql = f'''SELECT title, rating, description FROM netflix
            WHERE rating in {rating_dict.get(rating)}
            LIMIT 100'''
    result = get_value_from_db(sql)
    tmp = []
    for elem in result:
        tmp.append(dict(elem))
    return tmp


def search_by_genre(genre):
    sql = f'''SELECT title,description FROM netflix
            WHERE listed_in LIKE '%{genre.title()}%'
            LIMIT 10'''
    result = get_value_from_db(sql)
    tmp = []
    for elem in result:
        tmp.append(dict(elem))
    return tmp


def step5(name1, name2):
    sql = f'''SELECT * from netflix
            WHERE "cast" like "%{name1}%" and "cast" like "%{name2}%"'''
    result = get_value_from_db(sql)
    tmp = []
    names_dict = {}
    for elem in result:
        names = set(dict(elem).get("cast").split(", "))-set([name1, name2])
        for name in names:
            names_dict[name.strip()] = names_dict.get(name, 0)+1
    for key,value in names_dict.items():
        if value > 2:
            tmp.append(key)
    return tmp


def step6(typ, release_year, genre):
    sql = f'''SELECT * from netflix
        WHERE "type" = '{typ}' AND 
        release_year = {release_year} AND 
        listed_in like '%{genre}%'
'''
    result = get_value_from_db(sql)
    tmp =[]
    for elem in result:
        tmp.append(dict(elem))
    return tmp


# print(step6('TV Show', 2020, 'Dramas'))
# for item in result:
#    print(dict(item))
