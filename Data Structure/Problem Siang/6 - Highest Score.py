def highestScore(students):
    dict_hasil = {}
    
    for dict_students in students:
      kamus = {}
      maks = 0
      for bio in students:
        if bio['class'] == dict_students['class']:
          if bio['score'] > maks:
            maks = bio['score']
            dict_copy = bio.copy()
            del dict_copy['class']
            kamus['name'] = bio['name']
            kamus['score'] = maks
      dict_hasil[dict_students['class']]=kamus
    
    return dict_hasil

print(highestScore([]))

print(highestScore([
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
   'score': 100,
   'class': 'foxes'
 },
 {
   'name': 'Anastasia',
   'score': 78,
   'class': 'wolves'
 }]))

print(highestScore([
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
 }]))

