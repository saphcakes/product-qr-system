import pandas as pd

def show_current_images():
    """Show what images you currently have and what you need to replace"""
    df = pd.read_csv('products.csv')
    
    print("🖼️ CURRENT IMAGE LINKS (These are generic food images):")
    print("=" * 60)
    
    for index, row in df.iterrows():
        print(f"\n{row['product_id']}. {row['product_name']}")
        print(f"   Current: {row['image_url']}")
        print(f"   Should be: YOUR ACTUAL {row['product_name']} PHOTO")
    
    print("\n📝 INSTRUCTIONS:")
    print("1. Take photos of each product")
    print("2. Upload to https://imgbb.com")
    print("3. Copy the 'Direct Link' for each")
    print("4. Replace the Unsplash links in products.csv")
    print("5. Run the website generator again")

show_current_images()