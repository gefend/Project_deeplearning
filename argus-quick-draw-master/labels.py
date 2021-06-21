labels = {9: (0, 'apple'), 24: (1, 'bear'), 85: (2, 'crocodile'), 154: (3, 'house'), 173: (4, 'lightning'),
          236: (5, 'rabbit'), 265: (6, 'skull'), 300: (7, 'sword'), 330: (8, 'underwear'), 107: (9, 'eye'),
         63: (10, 'carrot'), 89: (11, 'diamond'), 184: (12, 'mermaid'), 188: (13, 'moon'), 277: (14, 'spider'),
         302: (15, 'table'), 296: (16, 'sun'), 258: (17, 'shark'), 202: (18, 'octopus'), 226: (19, 'pizza'),
          4:(20,'ambulance'),30:(21,'bicycle'),51:(22,'cactus'),56:(23,'camera'),92:(24,'dog'),107:(25,'eye'),
          118:(26,'flamingo'),130:(27,'giraffe'),144:(28,'helmet'),161:(29,'key'),175:(30,'lion'),187:(31,'monkey'),
          198:(32,'necklace'),203:(33,'onion'),209:(34,'panda'),240:(35,'rainbow'),272:(36,'snowflake'),305:(37:'telephone'),
         337:(38:'whale'),344:(39,'zebra')}

def new_label(label):
  item = labels.get(x)
  if item is None:
    return -1, ' '
  return item[0], item[1]
