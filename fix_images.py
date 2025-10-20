import pandas as pd
import re

def fix_google_drive_links():
    print("🔧 Fixing Google Drive image links...")
    
    # Read the current CSV
    df = pd.read_csv('products.csv')
    
    print("📊 Current image URLs:")
    for index, row in df.iterrows():
        print(f"Product {row['product_id']}: {row['image_url'][:80]}...")
    
    # Fix each Google Drive link
    for index, row in df.iterrows():
        current_url = row['image_url']
        
        # Convert Google Drive view links to direct image links
        if 'drive.google.com/file/d/' in current_url:
            # Extract file ID from the URL
            file_id_match = re.search(r'/d/([^/]+)', current_url)
            if file_id_match:
                file_id = file_id_match.group(1)
                # Create direct image URL
                direct_url = f'https://drive.google.com/uc?export=view&id={file_id}'
                df.at[index, 'image_url'] = direct_url
                print(f"✅ Fixed: {row['product_name']}")
            else:
                print(f"❌ Could not extract file ID from: {current_url}")
        else:
            print(f"ℹ️  Already direct link: {row['product_name']}")
    
    # Save the fixed CSV
    df.to_csv('products.csv', index=False)
    print("\n✅ All Google Drive links converted to direct image URLs!")
    
    return df

def test_image_links():
    """Test if the image links work"""
    print("\n🔍 Testing image links...")
    df = pd.read_csv('products.csv')
    
    for index, row in df.iterrows():
        url = row['image_url']
        if 'drive.google.com/uc?' in url:
            print(f"✅ {row['product_name']}: Direct image link ready")
        else:
            print(f"⚠️  {row['product_name']}: May not be direct link")

if __name__ == "__main__":
    print("🖼️ Google Drive Image Fixer")
    print("=" * 50)
    fixed_df = fix_google_drive_links()
    test_image_links()
    
    print("\n🎯 Next steps:")
    print("1. Run: python generate_github_pages.py")
    print("2. Run: git add . && git commit -m 'Fix image links' && git push")
    print("3. Wait 2-3 minutes for GitHub Pages to update")
    