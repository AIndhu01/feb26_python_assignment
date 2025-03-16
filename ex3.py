#ipl match tickets booking
def RCBvsCSK():
    print("the entry fee for this match is 20k per person")
    customer = input("Do you want to book the tickets:")
    if customer == "yes":
        one_person=20000
        name=input("enter your name:")
        age=int(input("enter your age:"))
        n=int(input("enter the number of persons:"))
        total_amt=one_person*n
        gst_rate=float(input("enter the GST rate (in %):"))
        gst_amt=(total_amt*gst_rate)/100
        final_amt=(total_amt+gst_amt)
        print("the final total amt is:",final_amt)
        if final_amt>100000:
            offer_amt=10000
            Total_amt=final_amt-offer_amt
            print(f"Hello {name}.To book your tickets for RCBvsCSK match you have to pay {Total_amt}.")
            print("Thank you for booking.")
        else:
            print(f"Hello {name}.To book your tickets for RCBvsCSK match you have to pay {final_amt}.")
            print("Thank you for booking.")
    else:
        print("Thank you.")
def MIvsGT():
    print("the entry fee for this match is 12k per person")
    customer = input("Do you want to book the tickets:")
    if customer == "yes":
        one_person=12000
        name=input("enter your name:")
        age=int(input("enter your age:"))
        n=int(input("enter the number of persons:"))
        total_amt=one_person*n
        gst_rate=float(input("enter the GST rate (in %):"))
        gst_amt=(total_amt*gst_rate)/100
        final_amt=(total_amt+gst_amt)
        print("the final total amt is:",final_amt)
        if final_amt>100000:
            offer_amt=10000
            Total_amt=final_amt-offer_amt
            print(f"Hello {name}.To book your tickets for MIvsGT match you have to pay {Total_amt}.")
            print("Thank you for booking.")
        else:
            print(f"Hello {name}.To book your tickets for MIvsGT match you have to pay {final_amt}.")
            print("Thank you for booking.")
    else:
        print("Thank you.")
def MIvsCSK():
    print("the entry fee for this match is 15k per person")
    customer = input("Do you want to book the tickets:")
    if customer == "yes":
        one_person=15000
        name=input("enter your name:")
        age=int(input("enter your age:"))
        n=int(input("enter the number of persons:"))
        total_amt=one_person*n
        gst_rate=float(input("enter the GST rate (in %):"))
        gst_amt=(total_amt*gst_rate)/100
        final_amt=(total_amt+gst_amt)
        print("the final total amt is:",final_amt)
        if final_amt>100000:
            offer_amt=10000
            Total_amt=final_amt-offer_amt
            print(f"Hello {name}.To book your tickets for MIvsCSK match you have to pay {Total_amt}.")
            print("Thank you for booking.")
        else:
            print(f"Hello {name}.To book your tickets for MIvsCSK match you have to pay {final_amt}.")
            print("Thank you for booking.")
    else:
        print("Thank you.")
def RCBvsMI():
    print("the entry fee for this match is 10k per person")
    customer = input("Do you want to book the tickets:")
    if customer == "yes":
        one_person=10000
        name=input("enter your name:")
        age=int(input("enter your age:"))
        n=int(input("enter the number of persons:"))
        total_amt=one_person*n
        gst_rate=float(input("enter the GST rate (in %):"))
        gst_amt=(total_amt*gst_rate)/100
        final_amt=(total_amt+gst_amt)
        print("the final total amt is:",final_amt)
        if final_amt>100000:
            offer_amt=10000
            Total_amt=final_amt-offer_amt
            print(f"Hello {name}.To book your tickets for RCBvsMI match you have to pay {Total_amt}.")
            print("Thank you for booking.")
        else:
            print(f"Hello {name}.To book your tickets for RCBvsMI match you have to pay {final_amt}.")
            print("Thank you for booking.")
    else:
        print("Thank you.")
def RCBvsKKR():
    print("the entry fee for this match is 18k per person")
    customer = input("Do you want to book the tickets:")
    if customer == "yes":
        one_person=18000
        name=input("enter your name:")
        age=int(input("enter your age:"))
        n=int(input("enter the number of persons:"))
        total_amt=one_person*n
        gst_rate=float(input("enter the GST rate (in %):"))
        gst_amt=(total_amt*gst_rate)/100
        final_amt=(total_amt+gst_amt)
        print("the final total amt is:",final_amt)
        if final_amt>100000:
            offer_amt=10000
            Total_amt=final_amt-offer_amt
            print(f"Hello {name}.To book your tickets for RCBvsKKR match you have to pay {Total_amt}.")
            print("Thank you for booking.")
        else:
            print(f"Hello {name}.To book your tickets for RCBvsKKR match you have to pay {final_amt}.")
            print("Thank you for booking.")
    else:
        print("Thank you.")
def main():
    print("WELCOME TO BOOKING CENTER")
    print("1.RCBvsCSK\n 2.MIvsGT\n 3.MIvsCSK\n 4.RCBvsMI\n 5.RCBvsKKR")
    choice=int(input("enter your choice:"))
    if choice==1:
        RCBvsCSK()
    elif choice==2:
        MIvsGT()
    elif choice==3:
        MIvsCSK()
    elif choice==4:
        RCBvsMI()
    elif choice==5:
        RCBvsKKR()
    else:
        print("invalid choice")
main()