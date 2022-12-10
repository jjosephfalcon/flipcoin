
# Write a function flipCoin() that returns either "heads" or "tails" randomly to represent heads or tails. Using the function, flip the coin 1000 times and tally up the number of heads and the number of tails. Finally, let's print out the percentage of heads and the percentage of tails we got.


import random 



def flipCoin():
  coin_flips = ['heads', 'tails']

  return random.choice(coin_flips)



heads_count = 0
tails_count = 0

for i in range(0, 1000):
  coin = flipCoin()

  if coin == 'heads':
    heads_count += 1
  elif coin == 'tails':
    tails_count += 1


heads_percentage = (heads_count / 1000) * 100
tails_percentage = (tails_count / 1000) * 100


print(str(heads_percentage) + "% of your flips were heads.")
print(str(tails_percentage) + "% of your flips were tails.")


