amount_due = 50

# Keep asking for coins until 50 cents or more is paid
while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    coin = int(input("Insert Coin: "))

    # Only accept valid coin values
    if coin in [25, 10, 5]:
        amount_due -= coin

# Calculate change (turns negative remaining amount into positive change)
change_owed = abs(amount_due)
print(f"Change Owed: {change_owed}")
