import pandas as pd
import qrcode
import os

def setup_github_pages():
    """Complete setup for GitHub Pages"""
    
    try:
        # Read products
        df = pd.read_csv('products.csv')
        print(f"✅ Loaded {len(df)} products from CSV")
        
        # Verify we have all required columns
        required_columns = ['product_id', 'product_name', 'price', 'description', 'instagram_handle', 'image_url']
        missing_columns = [col for col in required_columns if col not in df.columns]
        
        if missing_columns:
            print(f"❌ Missing columns: {missing_columns}")
            print("💡 Your CSV should have these exact columns:")
            for col in required_columns:
                print(f"   - {col}")
            return
        
        print("✅ All required columns present!")
        
    except FileNotFoundError:
        print("❌ Error: products.csv file not found!")
        return
    except Exception as e:
        print(f"❌ Error reading CSV: {e}")
        return
    
    # Create docs folder
    docs_folder = 'docs'
    os.makedirs(docs_folder, exist_ok=True)
    
    print("🚀 Setting up GitHub Pages...")
    
    # Create files
    create_styles_file(docs_folder)
    
    for index, row in df.iterrows():
        create_product_page(row, docs_folder)
    
    create_index_page(df, docs_folder)
    create_qr_codes(df, docs_folder)
    
    print(f"\n🎉 SUCCESS! GitHub Pages setup complete!")
    print(f"📁 All files created in '{docs_folder}' folder")

def create_product_page(product, folder):
    """Create individual product HTML page"""
    
    # Extract Instagram username
    instagram_info = str(product['instagram_handle']).strip()
    username = instagram_info.lstrip('@')  # Remove @ if present
    
    html_content = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{product['product_name']} - {product['price']} | Saph's Cakes & More</title>
        <link rel="stylesheet" href="styles.css">
    </head>
    <body>
        <div class="container">
            <div class="product-card">
                <div class="product-header">
                    <h1>{product['product_name']}</h1>
                    <div class="price">{product['price']}</div>
                </div>
                
                <img src="{product['image_url']}" alt="{product['product_name']}" class="product-image">
                
                <div class="product-details">
                    <p class="description">{product['description']}</p>
                    
                    <div class="brand-section">
                        <div class="brand-info">
                            <h3>🍰 Saph's Cakes & More</h3>
                            <p>Delicious treats made with love ❤️</p>
                        </div>
                        
                        <div class="instagram-section">
                            <a href="https://instagram.com/{username}" class="instagram-btn" target="_blank">
                                📷 Follow @{username} on Instagram
                            </a>
                            <p class="instagram-tag">See more products and place orders</p>
                        </div>
                    </div>
                    
                    <div class="navigation">
                        <a href="index.html" class="back-btn">← View All Products</a>
                    </div>
                </div>
            </div>
        </div>
    </body>
    </html>
    '''
    
    filename = f"product-{product['product_id']}.html"
    with open(os.path.join(folder, filename), 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"📄 Created: {filename}")

def create_index_page(df, folder):
    """Create main products listing page"""
    
    first_instagram = str(df.iloc[0]['instagram_handle']).strip()
    username = first_instagram.lstrip('@')
    
    products_html = ''
    for index, row in df.iterrows():
        products_html += f'''
        <div class="product-item">
            <img src="{row['image_url']}" alt="{row['product_name']}" class="product-thumbnail">
            <div class="product-info">
                <h3>{row['product_name']}</h3>
                <div class="price">{row['price']}</div>
                <p class="preview-desc">{row['description'][:80]}...</p>
                <div class="actions">
                    <a href="product-{row['product_id']}.html" class="view-btn">View Details</a>
                    <a href="qr-{row['product_id']}.png" download class="qr-btn">Download QR</a>
                </div>
            </div>
        </div>
        '''
    
    html_content = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Saph's Cakes & More - Products</title>
        <link rel="stylesheet" href="styles.css">
    </head>
    <body>
        <div class="container">
            <header>
                <div class="brand-header">
                    <h1>🍰 Saph's Cakes & More</h1>
                    <p class="tagline">Delicious treats made with love ❤️</p>
                    <p class="instagram-link">Follow us on Instagram: 
                        <a href="https://instagram.com/{username}" target="_blank" class="instagram-handle">@{username}</a>
                    </p>
                </div>
            </header>
            
            <div class="products-intro">
                <h2>Our Products</h2>
                <p>Scan QR codes or click to view product details. Perfect for sharing with customers!</p>
            </div>
            
            <div class="products-grid">
                {products_html}
            </div>
            
            <footer>
                <div class="footer-content">
                    <p>📍 Share these QR codes with customers for easy product information</p>
                    <p>📱 Scan with any smartphone camera to view product details</p>
                    <p>🎯 Perfect for packaging, menus, and social media</p>
                </div>
            </footer>
        </div>
    </body>
    </html>
    '''
    
    with open(os.path.join(folder, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("📄 Created: index.html")

def create_qr_codes(df, folder):
    """Generate QR codes"""
    
    github_username = input("Enter your GitHub username: ").strip()
    
    for index, row in df.iterrows():
        product_url = f"https://{github_username}.github.io/product-qr-system/product-{row['product_id']}.html"
        
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(product_url)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        filename = f"qr-{row['product_id']}.png"
        img.save(os.path.join(folder, filename))
        print(f"🎨 Created QR code: {filename}")

def create_styles_file(folder):
    """Create CSS file with Saph's Cakes & More branding"""
    css_content = '''
    * { 
        margin: 0; 
        padding: 0; 
        box-sizing: border-box; 
    }
    
    body { 
        font-family: 'Arial', sans-serif; 
        background: linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%);
        min-height: 100vh; 
        padding: 20px; 
        line-height: 1.6;
        color: #333;
    }
    
    .container { 
        max-width: 1200px; 
        margin: 0 auto; 
    }
    
    /* Header Styles */
    header {
        text-align: center;
        background: white;
        padding: 40px 30px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        margin-bottom: 40px;
    }
    
    .brand-header h1 {
        font-size: 3em;
        margin-bottom: 10px;
        color: #e91e63;
        background: linear-gradient(45deg, #e91e63, #ff5722);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .tagline {
        font-size: 1.3em;
        color: #666;
        margin-bottom: 15px;
        font-style: italic;
    }
    
    .instagram-link {
        font-size: 1.2em;
    }
    
    .instagram-handle {
        color: #e91e63;
        font-weight: bold;
        text-decoration: none;
        font-size: 1.3em;
    }
    
    .instagram-handle:hover {
        text-decoration: underline;
    }
    
    /* Products Intro */
    .products-intro {
        text-align: center;
        margin-bottom: 40px;
        color: white;
    }
    
    .products-intro h2 {
        font-size: 2.5em;
        margin-bottom: 15px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .products-intro p {
        font-size: 1.2em;
        max-width: 600px;
        margin: 0 auto;
    }
    
    /* Product Card Styles */
    .product-card { 
        background: white; 
        max-width: 500px; 
        margin: 20px auto; 
        border-radius: 20px; 
        padding: 30px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.1);
    }
    
    .product-header { 
        text-align: center; 
        margin-bottom: 25px; 
        border-bottom: 2px solid #f0f0f0;
        padding-bottom: 20px;
    }
    
    .product-header h1 { 
        color: #333; 
        margin-bottom: 15px;
        font-size: 2em;
    }
    
    .price { 
        font-size: 2.5em; 
        color: #e91e63; 
        font-weight: bold; 
    }
    
    .product-image { 
        width: 100%; 
        height: 350px; 
        object-fit: cover; 
        border-radius: 15px; 
        margin-bottom: 25px;
        border: 3px solid #f8f9fa;
    }
    
    .description { 
        color: #666; 
        line-height: 1.7; 
        margin-bottom: 30px;
        font-size: 1.1em;
        text-align: center;
    }
    
    /* Brand Section */
    .brand-section {
        background: #f8f9fa;
        padding: 25px;
        border-radius: 15px;
        margin: 25px 0;
        text-align: center;
    }
    
    .brand-info h3 {
        color: #e91e63;
        margin-bottom: 10px;
        font-size: 1.4em;
    }
    
    .instagram-section { 
        text-align: center; 
        margin-top: 20px;
    }
    
    .instagram-btn {
        background: linear-gradient(45deg, #405DE6, #5851DB, #833AB4, #C13584, #E1306C, #FD1D1D);
        color: white; 
        padding: 15px 30px; 
        border-radius: 25px;
        text-decoration: none; 
        font-weight: bold; 
        display: inline-block;
        transition: transform 0.3s ease;
        font-size: 1.1em;
    }
    
    .instagram-btn:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(224, 58, 132, 0.4);
    }
    
    .instagram-tag {
        color: #666;
        margin-top: 10px;
        font-size: 0.9em;
    }
    
    .back-btn { 
        color: #e91e63; 
        text-decoration: none; 
        font-weight: bold;
        display: inline-block; 
        margin-top: 20px;
        padding: 12px 25px;
        border: 2px solid #e91e63;
        border-radius: 8px;
        transition: all 0.3s ease;
        font-size: 1.1em;
    }
    
    .back-btn:hover {
        background: #e91e63;
        color: white;
        transform: translateY(-2px);
    }
    
    /* Index Page Styles */
    .products-grid { 
        display: grid; 
        gap: 30px; 
        max-width: 900px; 
        margin: 0 auto; 
    }
    
    .product-item {
        background: white; 
        padding: 25px; 
        border-radius: 20px;
        display: flex; 
        gap: 25px; 
        align-items: center;
        box-shadow: 0 8px 25px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
        border: 1px solid #f0f0f0;
    }
    
    .product-item:hover {
        transform: translateY(-8px);
        box-shadow: 0 15px 35px rgba(0,0,0,0.15);
    }
    
    .product-thumbnail { 
        width: 140px; 
        height: 140px; 
        object-fit: cover; 
        border-radius: 12px;
        border: 3px solid #f8f9fa;
    }
    
    .product-info { 
        flex: 1; 
    }
    
    .product-info h3 { 
        color: #333; 
        margin-bottom: 10px;
        font-size: 1.5em;
    }
    
    .preview-desc {
        color: #666;
        margin: 12px 0;
        line-height: 1.5;
    }
    
    .actions { 
        margin-top: 18px; 
        display: flex; 
        gap: 12px; 
    }
    
    .view-btn, .qr-btn {
        padding: 12px 20px; 
        border-radius: 10px; 
        text-decoration: none;
        font-size: 1em; 
        color: white;
        transition: all 0.3s ease;
        font-weight: bold;
    }
    
    .view-btn { 
        background: #e91e63; 
    }
    
    .view-btn:hover {
        background: #c2185b;
        transform: translateY(-2px);
    }
    
    .qr-btn { 
        background: #4caf50; 
    }
    
    .qr-btn:hover {
        background: #45a049;
        transform: translateY(-2px);
    }
    
    /* Footer */
    footer {
        text-align: center;
        color: white;
        margin-top: 60px;
        padding: 30px;
        background: rgba(255,255,255,0.1);
        border-radius: 15px;
        backdrop-filter: blur(10px);
    }
    
    .footer-content p {
        margin: 8px 0;
        font-size: 1.1em;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.3);
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .product-item {
            flex-direction: column;
            text-align: center;
            padding: 20px;
        }
        
        .product-thumbnail {
            width: 180px;
            height: 180px;
        }
        
        .actions {
            justify-content: center;
        }
        
        .brand-header h1 {
            font-size: 2.2em;
        }
        
        .products-intro h2 {
            font-size: 2em;
        }
        
        .product-card {
            margin: 10px;
            padding: 20px;
        }
    }
    '''
    
    with open(os.path.join(folder, 'styles.css'), 'w') as f:
        f.write(css_content)
    print("🎨 Created: styles.css")

if __name__ == "__main__":
    print("🍰 Saph's Cakes & More - QR Code System")
    print("=" * 50)
    setup_github_pages()
    