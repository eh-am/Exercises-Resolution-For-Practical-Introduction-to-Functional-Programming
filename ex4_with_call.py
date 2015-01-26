def assoc(_d, key, value):
    from copy import deepcopy
    d = deepcopy(_d)
    d[key] = value
    return d

def call(fn, key):
  def apply_fn(record):
    return assoc(record, key, fn(record.get(key)))
  return apply_fn

def pipeline_each(values, fns):
  return reduce(lambda a, x: map(x, a), fns, values)

bands = [{'name': 'sunset rubdown', 'country': 'UK', 'active': False},
         {'name': 'women', 'country': 'Germany', 'active': False},
         {'name': 'a silver mt. zion', 'country': 'Spain', 'active': True}]

print pipeline_each(bands,
                    [call(lambda x: 'Canada', 'country'),
                     call(lambda x: x.replace(',', ''), 'name'),
                     call(lambda x: x.title(), 'name')
                    ])