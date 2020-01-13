def graduates (students):
    dict_hasil = {}

    for dict_students in students:
      lst = []
      for bio in students:
        if bio['class'] == dict_students['class']:
          if bio['score'] > 75:
            dict_copy = bio.copy()
            del dict_copy['class']
            lst.append(dict_copy)
      dict_hasil[dict_students['class']]=lst
    
    return dict_hasil

print(graduates([]))

print(graduates([
 {
   'name': 'Dimitri',
   'score': 90,
   'class': 'foxes'
 },
 {
   'name': 'Alexei',
   'score': 85,
   'class': 'wolves'
 },
 {
   'name': 'Sergei',
   'score': 74,
   'class': 'foxes'
 },
 {
   'name': 'Anastasia',
   'score': 78,
   'class': 'wolves'
 }
]))

print(graduates([
 {
   'name': 'Alexander',
   'score': 100,
   'class': 'foxes'
 },
 {
   'name': 'Alisa',
   'score': 76,
   'class': 'wolves'
 },
 {
   'name': 'Vladimir',
   'score': 92,
   'class': 'foxes'
 },
 {
   'name': 'Albert',
   'score': 71,
   'class': 'wolves'
 },
 {
   'name': 'Viktor',
   'score': 80,
   'class': 'tigers'
 }
]))
