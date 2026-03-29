import pandas as pd

def generate_database():
    print("Generating P.R.I.S.M. product database...")
    
    # A curated list of items to test semantic search and fake review detection.
    # Notice how the descriptions contain context, not just keywords.
    data = [
        {
            "ProductID": 101,
            "ProductName": "boAt Nirvana Ion ANC Earbuds",
            "Description": "True wireless earbuds with active noise cancellation. Features IPX4 water resistance and long battery life, making them ideal for running and gym workouts.",
            "Price": "₹2,299",
            "ReviewText": "Accidentally dropped them in water after a run, but they survived and still sound perfectly fine. ANC is decent for the price.",
            "Is_Fake": 0
        },
        {
            "ProductID": 102,
            "ProductName": "Puma Velocity Nitro Running Shoes (Size 7 UK)",
            "Description": "Lightweight athletic footwear designed for daily running and jogging. Features responsive foam cushioning and breathable mesh.",
            "Price": "₹4,500",
            "ReviewText": "AMAZING SHOES BEST SHOES EVER INVENTED I BOUGHT 10 PAIRS AND MY LIFE IS PERFECT NOW VERY GOOD QUALITY FAST SHIPPING!!!",
            "Is_Fake": 1
        },
        {
            "ProductID": 103,
            "ProductName": "Python for Data Science Handbook",
            "Description": "A comprehensive guide to learning Python programming, focusing on libraries like pandas, scikit-learn, and building machine learning models.",
            "Price": "₹1,850",
            "ReviewText": "Really helpful for my first-year engineering projects. The section on data manipulation is clearly written.",
            "Is_Fake": 0
        },
        {
            "ProductID": 104,
            "ProductName": "Los Pollos Hermanos Apron",
            "Description": "Yellow cooking apron featuring the logo from the famous Albuquerque fried chicken restaurant. Great novelty gift for TV show fans.",
            "Price": "₹899",
            "ReviewText": "PRODUCT IS 100% LEGITIMATE BUY NOW DO NOT HESITATE EXCELLENT SELLER FIVE STARS FIVE STARS FAST DELIVERY",
            "Is_Fake": 1
        },
        {
            "ProductID": 105,
            "ProductName": "Hellfire Club Baseball Tee",
            "Description": "3/4 sleeve raglan t-shirt featuring the Hawkins High School Dungeons & Dragons club logo. Comfortable cotton blend.",
            "Price": "₹750",
            "ReviewText": "Fits true to size. The print quality is solid and hasn't faded after a few washes.",
            "Is_Fake": 0
        },
        {
            "ProductID": 106,
            "ProductName": "Vintage Shelby Company Flat Cap",
            "Description": "Classic 1920s style tweed newsboy hat. Perfect for completing a retro Birmingham industrial look.",
            "Price": "₹1,200",
            "ReviewText": "BEST HAT VERY WOOL MUCH BIRMINGHAM BUY THIS NOW FOR MAXIMUM RESPECT IN THE STREETS VERY GOOD ITEM.",
            "Is_Fake": 1
        },
        {
            "ProductID": 107,
            "ProductName": "Desktop Coffee Mug Warmer",
            "Description": "Electric heating pad for your desk to keep coffee, tea, or hot cocoa warm all day. Auto shut-off safety feature included.",
            "Price": "₹950",
            "ReviewText": "Keeps my drinks at the perfect temperature while I'm coding late into the night. Cord could be a bit longer though.",
            "Is_Fake": 0
        },
        {
            "ProductID": 108,
            "ProductName": "Winden Yellow Raincoat",
            "Description": "Heavy-duty waterproof hooded jacket with a bright yellow finish. Excellent for severe weather and time travel.",
            "Price": "₹2,800",
            "ReviewText": "THIS RAINCOAT CURED MY COLD AND MADE ME INVINCIBLE TO WATER 10/10 WOULD BUY AGAIN HIGHLY RECOMMEND YES.",
            "Is_Fake": 1
        },
        {
            "ProductID": 109,
            "ProductName": "Mechanical Keyboard - Blue Switches",
            "Description": "Tactile and clicky mechanical keyboard with customizable RGB backlighting. Built for heavy typing and programming tasks.",
            "Price": "₹3,499",
            "ReviewText": "The tactile feedback is excellent for long coding sessions, but the blue switches might be too loud if you share a room.",
            "Is_Fake": 0
        },
        {
            "ProductID": 110,
            "ProductName": "Noise-Isolating Studio Headphones",
            "Description": "Over-ear wired headphones offering flat frequency response. Ideal for critical listening, mixing, and producing music.",
            "Price": "₹5,999",
            "ReviewText": "PERFECT SOUND I HEAR THINGS I NEVER HEARD BEFORE BUY THIS BRAND IT IS THE BEST BRAND NO OTHER BRAND COMPARES.",
            "Is_Fake": 1
        }
    ]

    # Convert the list of dictionaries into a pandas DataFrame
    df = pd.DataFrame(data)
    
    # Save it to a CSV file in the same folder
    df.to_csv('products.csv', index=False)
    print("✅ Successfully created 'products.csv' with 10 sample items and reviews!")

if __name__ == "__main__":
    generate_database()