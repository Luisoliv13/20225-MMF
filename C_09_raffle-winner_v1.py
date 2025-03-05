import pandas
import random

# lists to hold ticket details
all_names = ["A", "B", "C", "D", "E"]
all_ticket_costs = [7.50, 7.50, 10.50, 10.50, 6.50]
all_surcharges = [0, 0, 0.53, 0.53, 0]

mini_movie_dict = {
    'Name': all_names,
    'Ticket Price': all_ticket_costs,
    'Surcharge': all_surcharges
}

# create dataframe / table from dictionary
mini_movie_frame = pandas.DataFrame(mini_movie_dict)

# Calculate the total payable & profit for each ticket
mini_movie_frame['Total'] = mini_movie_frame['Ticket Price'] + mini_movie_frame['Surcharge']
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# Work out total paid and total profit...
total_paid = mini_movie_frame['Total'].sum()
total_profit = mini_movie_frame['Profit'].sum()

# print(mini_movie_frame)
print(mini_movie_frame.to_string(index=False))

# choose random winner...
winner = random.choice(all_names)

# find index of winner (ie: position in list)
winner_index = all_names.index(winner)
print("winner", winner, "list position", winner_index)

# retrieve ticket price and surcharge
winner_ticket_price = all_ticket_costs[winner_index]
winner_surcharge = all_surcharges[winner_index]

# find total won
total_won = winner_ticket_price + winner_surcharge

# winner announcement
print(f"The lucky winner is {winner}.  Their ticket worth ${total_won:.2f} is free!")
