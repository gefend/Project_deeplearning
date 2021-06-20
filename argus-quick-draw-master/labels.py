labels = {9: (0, 'apple'), 24: (1, 'bear'), 85: (2, 'crocodile'), 154: (3, 'house'), 173: (4, 'lightning'),
          236: (5, 'rabbit'), 265: (6, 'skull'), 300: (7, 'sword'), 330: (8, 'underwear'), 107: (9, 'eye'),
         63: (10, 'carrot'), 89: (11, 'diamond'), 184: (12, 'mermaid'), 188: (13, 'moon'), 277: (14, 'spider'),
         302: (15, 'table'), 296: (16, 'sun'), 258: (17, 'shark'), 202: (18, 'octopus'), 226: (19, 'pizza')}

def new_label(label):
  item = labels.get(x)
  if item is None:
    return -1, ' '
  return item[0], item[1]
