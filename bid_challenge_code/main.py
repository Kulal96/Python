import os
bidder_dict={}
game_on=True


def bid_price():
    #print(bidder_dict)
    max=0
    for key in bidder_dict:
        if bidder_dict[key] > max:
            max=bidder_dict[key]
            winner_name=key
    print(f'The winner is {winner_name} with a bid of ${max} ')


while game_on:
    bidder_name=input("What is your name ?")
    bidder_price=int(input("What is the bid price ?"))
    #os.system('cls')
    bidder_dict[bidder_name]=bidder_price
    choice=input("Is there any biders who wants to bid. Type yes or no: ?")
    if choice=='yes':
        game_on=True
    else:
        bid_price()
        game_on=False


