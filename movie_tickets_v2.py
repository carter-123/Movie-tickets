""" Movie theatre ticketing system - v1
Get category and number of tickets required
Created by Carter Wilson
"""


# Component 1 - Welcome screen and set up variables
def sell_ticket():
    print("********** FanFare Movies - ticketing system **********\n")

    adult_tickets = 0
    student_tickets = 0
    child_tickets = 0
    gift_vouchers = 0
    tickets_sold = 0
    total_sales = 0

    # Component 2 - Get category and number of tickets required

    ticket_wanted = "Y"
    while ticket_wanted == "Y":
        ticket_type = input("What kind of ticket do you want? \n"
                            "\t'A' for Adult, or\n"
                            "\t'S' for Student, or\n"
                            "\t'C' for Child, or\n"
                            "\t'G' for Gift Voucher\n"
                            ">> ").upper()
        num_tickets = int(input(f"How many {ticket_type} tickets do you want? "
                                f""))
        print(f"\nYou have ordered {num_tickets} {ticket_type} ticket(s)!")
        ticket_wanted = input("Do you want to sell another ticket? (Y/N): "
                              "").upper()


# Main routine
sell_ticket()
