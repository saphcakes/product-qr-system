import pandas as pd

# Read and display your products.csv
df = pd.read_csv('products.csv')

print("📊 YOUR PRODUCTS.CSV CONTENTS:")
print("=" * 60)
print(df[['product_id', 'product_name', 'image_url']])

print("\n🔍 FULL DETAILS:")
print("=" * 60)
for index, row in df.iterrows():
    print(f"\nProduct {row['product_id']}: {row['product_name']}")
    print(f"Price: {row['price']}")
    print(f"Description: {row['description'][:50]}...")
    print(f"Image URL: {row['image_url']}")
    print("-" * 50)