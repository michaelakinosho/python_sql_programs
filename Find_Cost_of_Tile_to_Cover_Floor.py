#My signature and contact details
#Written by: Michael Akinosho
#Email: michaelakinosho@moaadvisory.com
#Let's figure out the cost of tiling a floor given its width, length and cost of one square tile

def input_num():
    flr_width = 0
    flr_length = 0
    cost_per_tile = 0

    try:
        print("\n")
        flr_width = float(input("Enter a positive number as the floor's width in feet\nFor example enter 2.34 NOT 2.34 feet: "))
        while flr_width < 0:
            print("\n")
            print("Please try again and enter a positive number as the floor's width in feet.")
            flr_width = float(input("Enter a positive number as the floor's width in feet\nFor example enter 2.34 NOT 2.34 feet: "))

        print("\n")
        flr_length = float(input("Enter a positive number as the floor's length in feet\nFor example enter 4.32 NOT 4.32 feet: "))
        while flr_length < 0:
            print("\n")
            print("Please try again and enter a positive number as the floor's length in feet.")
            flr_length = float(input("Enter a positive number as the floor's length in feet\nFor example enter 4.32 NOT 4.32 feet: "))

        print("\n")
        cost_per_tile = float(input("Enter a positive number as cost per tile in square feet\nFor example enter 2.50 NOT $2.50/sq ft: "))
        while cost_per_tile < 0:
            print("\n")
            print("Please try again and enter a positive number for the cost per tile.")
            cost_per_tile = float(input("Enter a positive number as cost per tile in square feet\nFor example enter 2.50 NOT $2.50/sq ft: "))

        flr_area = round(flr_width*flr_length,2)
        flr_tile_cost = round(flr_area*cost_per_tile,2)
        print("A floor area of: {} square feet, will cost: ${} to tile.".format(flr_area, flr_tile_cost))

    except ValueError:
        print("Oops an incorrect value was entered!!")
        print("Values entered for width: {}, for length: {} and cost per tile: {}.".format(flr_width,flr_length,cost_per_tile))
        input_num()

    finally:
        print("Thank you!!")

input_num()
