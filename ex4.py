def assoc(_d, key, value):
    from copy import deepcopy
    d = deepcopy(_d)
    d[key] = value
    return d

def set_canada_as_country(band):
    return assoc(band, 'country', "Canada")

def strip_punctuation_from_name(band):
    return assoc(band, 'name', band['name'].replace('.', ''))

def capitalize_names(band):
    return assoc(band, 'name', band['name'].title())

def pipeline_each(values, fns):
  # Para cada funcao de FNS, usar em map,
  # aplicando em cada campo do dicionario a fn(i)
  # 
  # a = resultado da fn(i-1); x = fn(i)
  return reduce(lambda a, x: map(x, a), fns, values)


bands = [{'name': 'sunset rubdown', 'country': 'UK', 'active': False},
         {'name': 'women', 'country': 'Germany', 'active': False},
         {'name': 'a silver mt. zion', 'country': 'Spain', 'active': True}]


print pipeline_each(bands, [set_canada_as_country,
                  strip_punctuation_from_name,
                  capitalize_names])