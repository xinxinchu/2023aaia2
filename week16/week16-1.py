#import collections �ק�e
from collections import collections #�ק��
words = ["bella", "label", "ruller"]
for i in range(3):
  counter = collections.Counter(words[i])
  print(word[i], counter)
#ans = collections.Counter(word[0])&collections.Counter(word[1])&collections.Counter(word[2])
ans = Counter(word[0]) & Counter(word[0]) & Counter(word[0])
print(ans)
