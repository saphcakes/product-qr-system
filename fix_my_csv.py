import pandas as pd
import re

def fix_csv_file():
    # Read your current CSV
    df = pd.read_csv('products.csv')
    
    print("🔧 Fixing your CSV file...")
    
    # Remove duplicate columns and keep only what we need
    fixed_data = []
    
    for index, row in df.iterrows():
        # Convert Google Drive links to direct image links
        image_url = str(row['image_url']).strip('" ')
        if 'drive.google.com/file/d/' in image_url:
            # Extract file ID and convert to direct link
            file_id = image_url.split('/d/')[1].split('/')[0]
            direct_image_url = f'https://drive.google.com/uc?export=view&id={file_id}'
        else:
            direct_image_url = image_url
        
        # Use the correct Instagram handle
        instagram_handle = "@saphcakes_ndmore"  # Updated handle
        
        # Clean description and other fields
        description = str(row['description']).strip('" ')
        manufacturer = str(row['manufacturer']).strip('" ')
        
        # Create fixed product entry
        fixed_product = {
            'product_id': row['product_id'],
            'product_name': str(row['product_name']).strip(),
            'price': str(row['price']).replace('#', '₦'),  # Replace # with ₦
            'description': f"{description}",
            'instagram_handle': instagram_handle,
            'image_url': direct_image_url
        }
        
        fixed_data.append(fixed_product)
    
    # Create new DataFrame
    fixed_df = pd.DataFrame(fixed_data)
    
    # Save fixed CSV
    fixed_df.to_csv('products_fixed.csv', index=False)
    
    print("✅ Fixed CSV created: 'products_fixed.csv'")
    print("\n📊 Fixed data preview:")
    print(fixed_df[['product_id', 'product_name', 'price']])
    
    return fixed_df

def test_fixed_csv():
    """Test if the fixed CSV works with our main script"""
    try:
        df = pd.read_csv('products_fixed.csv')
        required_columns = ['product_id', 'product_name', 'price', 'description', 'instagram_handle', 'image_url']
        
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            print(f"❌ Still missing: {missing_columns}")
            return False
        
        print("✅ Fixed CSV has all required columns!")
        print(f"📦 Products: {len(df)}")
        return True
        
    except Exception as e:
        print(f"❌ Error testing CSV: {e}")
        return False

# Run the fix
if __name__ == "__main__":
    print("🛠️ CSV Fixing Tool")
    print("=" * 40)
    
    fixed_df = fix_csv_file()
    
    if test_fixed_csv():
        print("\n🎉 CSV is now fixed and ready!")
        print("💡 Next: Rename 'products_fixed.csv' to 'products.csv'")
    else:
        print("\n❌ CSV still has issues, please check manually")
        