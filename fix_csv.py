import pandas as pd

# Read your current CSV file
try:
    df = pd.read_csv('products.csv')
    print("Current columns in your CSV:")
    print(df.columns.tolist())
    
    # Check what columns you have
    if 'instagram_handle' not in df.columns:
        print("\n❌ Missing 'instagram_handle' column!")
        
        # Add the missing column
        df['instagram_handle'] = '@sisters_business'  # Default value
        
        # Save the fixed CSV
        df.to_csv('products.csv', index=False)
        print("✅ Added 'instagram_handle' column to your CSV")
        print("📝 Please edit the CSV to add actual Instagram handles/URLs")
    
    print("\n✅ Your CSV is now ready!")
    
except Exception as e:
    print(f"Error: {e}")
    print("\n💡 Creating a new template CSV for you...")
    
    # Create a template CSV
    template_data = {
        'product_id': [101, 102],
        'product_name': ['Product One', 'Product Two'],
        'price': ['$9.99', '$12.99'],
        'description': ['Description one', 'Description two'],
        'instagram_handle': ['@sisters_business', '@sisters_business'],
        'image_url': ['https://example.com/image1.jpg', 'https://example.com/image2.jpg']
    }
    
    template_df = pd.DataFrame(template_data)
    template_df.to_csv('products.csv', index=False)
    print("✅ Created 'products.csv' template")
    print("📝 Please edit it with your actual product data")
    