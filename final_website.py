import pandas as pd
import qrcode
import os

# BUSINESS INFORMATION
BUSINESS_INFO = {
    'whatsapp_number': '+2349091138760',
    'phone_number': '+2347050315221', 
    'address': '9, Idiomo Street, Lagos Island',
    'business_name': "Saph's Cakes & More",
    'instagram_handle': 'saphcakes_ndmore',
    'business_hours': {
        'weekdays': 'Monday - Saturday: 8:00 AM - 10:00 PM',
        'sunday': 'Sunday: 10:00 AM - 10:00 PM'
    },
    'delivery_info': 'Free delivery within Lagos Island (Terms and Conditions apply)',
    'payment_methods': 'Cash, Bank Transfer, and Installment Payment Available'
}

def create_final_website():
    """Create the final website using EXACTLY what's in products.csv"""
    
    print("🎯 CREATING FINAL WEBSITE WITH YOUR ACTUAL PRODUCT IMAGES")
    print("=" * 60)
    
    try:
        # Read your products.csv EXACTLY as it is
        df = pd.read_csv('products.csv')
        
        print(f"✅ Loaded {len(df)} products from products.csv")
        print("\n📸 USING YOUR ACTUAL IMAGE LINKS FROM CSV:")
        for index, row in df.iterrows():
            print(f"   {row['product_id']}. {row['product_name']}")
            print(f"      Image: {row['image_url']}")
            
    except Exception as e:
        print(f"❌ Error reading products.csv: {e}")
        return
    
    # Create docs folder
    docs_folder = 'docs'
    os.makedirs(docs_folder, exist_ok=True)
    
    print(f"\n🚀 Generating website files in '{docs_folder}' folder...")
    
    # Create all website files
    create_styles(docs_folder)
    create_index_page(df, docs_folder)
    create_contact_page(docs_folder)
    create_about_page(df, docs_folder)
    
    for index, row in df.iterrows():
        create_product_page(row, docs_folder, df)
    
    create_qr_codes(df, docs_folder)
    
    print(f"\n🎉 FINAL WEBSITE COMPLETE!")
    print(f"📁 Check the '{docs_folder}' folder for your files")
    print(f"🌐 Your live site: https://saphcakes.github.io/product-qr-system/")

def create_product_page(product, folder, all_products):
    """Create product page using ACTUAL image from CSV"""
    
    whatsapp_message = f"Hello! I'd like to order: {product['product_name']} - {product['price']}"
    encoded_message = whatsapp_message.replace(' ', '%20')
    whatsapp_url = f"https://wa.me/{BUSINESS_INFO['whatsapp_number']}?text={encoded_message}"
    
    # Other products for navigation
    other_products = ''
    for idx, other in all_products.iterrows():
        if other['product_id'] != product['product_id']:
            other_products += f'''
            <a href="product-{other['product_id']}.html" class="other-product">
                <img src="{other['image_url']}" alt="{other['product_name']}">
                <span>{other['product_name']}</span>
                <span class="price">{other['price']}</span>
            </a>
            '''
    
    html_content = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{product['product_name']} | {BUSINESS_INFO['business_name']}</title>
        <link rel="stylesheet" href="styles.css">
    </head>
    <body>
        <nav class="main-nav">
            <div class="nav-container">
                <a href="index.html" class="nav-logo">🍰 {BUSINESS_INFO['business_name']}</a>
                <div class="nav-links">
                    <a href="index.html">Home</a>
                    <a href="about.html">About</a>
                    <a href="contact.html">Contact</a>
                </div>
            </div>
        </nav>

        <div class="container">
            <div class="product-card">
                <div class="product-header">
                    <h1>{product['product_name']}</h1>
                    <div class="price">{product['price']}</div>
                </div>
                
                <!-- THIS USES YOUR ACTUAL IMAGE LINK FROM CSV -->
                <img src="{product['image_url']}" alt="{product['product_name']}" class="product-image">
                
                <div class="product-details">
                    <p class="description">{product['description']}</p>
                    
                    <div class="action-buttons">
                        <a href="{whatsapp_url}" class="whatsapp-btn" target="_blank">📱 Order via WhatsApp</a>
                        <a href="tel:{BUSINESS_INFO['phone_number']}" class="call-btn">📞 Call to Order</a>
                    </div>
                    
                    <div class="business-info">
                        <h3>Order Information</h3>
                        <div class="info-grid">
                            <div class="info-item"><strong>Delivery:</strong> {BUSINESS_INFO['delivery_info']}</div>
                            <div class="info-item"><strong>Payment:</strong> {BUSINESS_INFO['payment_methods']}</div>
                            <div class="info-item"><strong>Hours:</strong> {BUSINESS_INFO['business_hours']['weekdays']}</div>
                            <div class="info-item"><strong>Sunday:</strong> {BUSINESS_INFO['business_hours']['sunday']}</div>
                            <div class="info-item"><strong>Address:</strong> {BUSINESS_INFO['address']}</div>
                            <div class="info-item"><strong>Contact:</strong> {BUSINESS_INFO['whatsapp_number']}</div>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="other-products">
                <h2>Other Products</h2>
                <div class="products-scroll">{other_products}</div>
            </div>
        </div>
        
        <footer class="main-footer">
            <div class="footer-content">
                <div class="footer-section">
                    <h3>{BUSINESS_INFO['business_name']}</h3>
                    <p>📍 {BUSINESS_INFO['address']}</p>
                </div>
                <div class="footer-section">
                    <h3>Connect</h3>
                    <a href="https://instagram.com/{BUSINESS_INFO['instagram_handle']}" target="_blank">Instagram</a>
                    <a href="{whatsapp_url}" target="_blank">WhatsApp</a>
                </div>
            </div>
        </footer>
    </body>
    </html>
    '''
    
    filename = f"product-{product['product_id']}.html"
    with open(os.path.join(folder, filename), 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"📄 Created: {filename}")

def create_index_page(df, folder):
    """Create main page with all products"""
    products_html = ''
    for index, row in df.iterrows():
        whatsapp_message = f"Hello! I'm interested in: {row['product_name']} - {row['price']}"
        encoded_message = whatsapp_message.replace(' ', '%20')
        whatsapp_url = f"https://wa.me/{BUSINESS_INFO['whatsapp_number']}?text={encoded_message}"
        
        products_html += f'''
        <div class="product-item">
            <img src="{row['image_url']}" alt="{row['product_name']}" class="product-thumbnail">
            <div class="product-info">
                <h3>{row['product_name']}</h3>
                <div class="price">{row['price']}</div>
                <p class="preview-desc">{row['description'][:80]}...</p>
                <div class="actions">
                    <a href="product-{row['product_id']}.html" class="view-btn">View Details</a>
                    <a href="{whatsapp_url}" class="whatsapp-btn-small" target="_blank">Order Now</a>
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
        <title>{BUSINESS_INFO['business_name']}</title>
        <link rel="stylesheet" href="styles.css">
    </head>
    <body>
        <nav class="main-nav">
            <div class="nav-container">
                <a href="index.html" class="nav-logo">🍰 {BUSINESS_INFO['business_name']}</a>
                <div class="nav-links">
                    <a href="index.html" class="active">Home</a>
                    <a href="about.html">About</a>
                    <a href="contact.html">Contact</a>
                </div>
            </div>
        </nav>

        <div class="container">
            <header class="hero-section">
                <h1>{BUSINESS_INFO['business_name']}</h1>
                <p>Authentic Nigerian Treats Made with Love ❤️</p>
                <p>📍 {BUSINESS_INFO['address']}</p>
                <div class="hero-actions">
                    <a href="#products" class="cta-btn">View Products</a>
                    <a href="https://wa.me/{BUSINESS_INFO['whatsapp_number']}" class="cta-btn-whatsapp" target="_blank">📱 Order via WhatsApp</a>
                </div>
            </header>

            <section id="products" class="products-section">
                <h2>Our Products</h2>
                <div class="products-grid">{products_html}</div>
            </section>
        </div>

        <footer class="main-footer">
            <div class="footer-content">
                <div class="footer-section">
                    <h3>{BUSINESS_INFO['business_name']}</h3>
                    <p>📍 {BUSINESS_INFO['address']}</p>
                </div>
                <div class="footer-section">
                    <h3>Contact</h3>
                    <a href="https://wa.me/{BUSINESS_INFO['whatsapp_number']}" target="_blank">WhatsApp: {BUSINESS_INFO['whatsapp_number']}</a>
                    <a href="tel:{BUSINESS_INFO['phone_number']}">Call: {BUSINESS_INFO['phone_number']}</a>
                </div>
            </div>
        </footer>
    </body>
    </html>
    '''
    
    with open(os.path.join(folder, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("📄 Created: index.html")

def create_contact_page(folder):
    """Create contact page"""
    html_content = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Contact Us | {BUSINESS_INFO['business_name']}</title>
        <link rel="stylesheet" href="styles.css">
    </head>
    <body>
        <nav class="main-nav">
            <div class="nav-container">
                <a href="index.html" class="nav-logo">🍰 {BUSINESS_INFO['business_name']}</a>
                <div class="nav-links">
                    <a href="index.html">Home</a>
                    <a href="about.html">About</a>
                    <a href="contact.html" class="active">Contact</a>
                </div>
            </div>
        </nav>

        <div class="container">
            <div class="page-header">
                <h1>Contact Us</h1>
                <p>Get in touch to place your order</p>
            </div>

            <div class="contact-grid">
                <div class="contact-method">
                    <div class="contact-icon">📱</div>
                    <h3>WhatsApp</h3>
                    <p>{BUSINESS_INFO['whatsapp_number']}</p>
                    <a href="https://wa.me/{BUSINESS_INFO['whatsapp_number']}" class="contact-btn whatsapp" target="_blank">Message Us</a>
                </div>

                <div class="contact-method">
                    <div class="contact-icon">📞</div>
                    <h3>Phone</h3>
                    <p>{BUSINESS_INFO['phone_number']}</p>
                    <a href="tel:{BUSINESS_INFO['phone_number']}" class="contact-btn call">Call Now</a>
                </div>
            </div>
        </div>

        <footer class="main-footer">
            <div class="footer-content">
                <div class="footer-section">
                    <h3>{BUSINESS_INFO['business_name']}</h3>
                    <p>📍 {BUSINESS_INFO['address']}</p>
                </div>
            </div>
        </footer>
    </body>
    </html>
    '''
    
    with open(os.path.join(folder, 'contact.html'), 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("📄 Created: contact.html")

def create_about_page(df, folder):
    """Create about page"""
    html_content = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>About Us | {BUSINESS_INFO['business_name']}</title>
        <link rel="stylesheet" href="styles.css">
    </head>
    <body>
        <nav class="main-nav">
            <div class="nav-container">
                <a href="index.html" class="nav-logo">🍰 {BUSINESS_INFO['business_name']}</a>
                <div class="nav-links">
                    <a href="index.html">Home</a>
                    <a href="about.html" class="active">About</a>
                    <a href="contact.html">Contact</a>
                </div>
            </div>
        </nav>

        <div class="container">
            <div class="page-header">
                <h1>About Us</h1>
                <p>Authentic Nigerian treats made with love</p>
            </div>

            <div class="about-content">
                <h2>Our Story</h2>
                <p>Welcome to {BUSINESS_INFO['business_name']}! We specialize in authentic Nigerian treats that remind you of home.</p>
                
                <h2>Business Information</h2>
                <div class="business-details">
                    <p><strong>📍 Address:</strong> {BUSINESS_INFO['address']}</p>
                    <p><strong>🕒 Hours:</strong> {BUSINESS_INFO['business_hours']['weekdays']}</p>
                    <p><strong>🕒 Sunday:</strong> {BUSINESS_INFO['business_hours']['sunday']}</p>
                    <p><strong>🚚 Delivery:</strong> {BUSINESS_INFO['delivery_info']}</p>
                    <p><strong>💳 Payment:</strong> {BUSINESS_INFO['payment_methods']}</p>
                </div>
            </div>
        </div>

        <footer class="main-footer">
            <div class="footer-content">
                <div class="footer-section">
                    <h3>{BUSINESS_INFO['business_name']}</h3>
                    <p>📍 {BUSINESS_INFO['address']}</p>
                </div>
            </div>
        </footer>
    </body>
    </html>
    '''
    
    with open(os.path.join(folder, 'about.html'), 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("📄 Created: about.html")

def create_qr_codes(df, folder):
    """Generate QR codes"""
    github_username = "saphcakes"
    
    for index, row in df.iterrows():
        product_url = f"https://{github_username}.github.io/product-qr-system/product-{row['product_id']}.html"
        
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(product_url)
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        filename = f"qr-{row['product_id']}.png"
        img.save(os.path.join(folder, filename))
        print(f"🎨 Created QR code: {filename}")

def create_styles(folder):
    """Create CSS styles"""
    css_content = '''
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body { font-family: Arial, sans-serif; background: #f5f5f5; line-height: 1.6; }
    .container { max-width: 1200px; margin: 0 auto; padding: 20px; }
    
    .main-nav { background: white; padding: 1rem; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
    .nav-container { max-width: 1200px; margin: 0 auto; display: flex; justify-content: space-between; align-items: center; }
    .nav-logo { font-size: 1.5rem; font-weight: bold; color: #008751; text-decoration: none; }
    .nav-links { display: flex; gap: 2rem; }
    .nav-links a { text-decoration: none; color: #333; }
    .nav-links a.active { color: #008751; font-weight: bold; }
    
    .hero-section { text-align: center; padding: 3rem 1rem; background: white; margin: 2rem 0; border-radius: 10px; }
    .hero-section h1 { font-size: 2.5rem; color: #008751; margin-bottom: 1rem; }
    .hero-actions { margin-top: 2rem; display: flex; gap: 1rem; justify-content: center; }
    .cta-btn, .cta-btn-whatsapp { padding: 1rem 2rem; border-radius: 5px; text-decoration: none; font-weight: bold; }
    .cta-btn { background: #008751; color: white; }
    .cta-btn-whatsapp { background: #25D366; color: white; }
    
    .products-grid { display: grid; gap: 2rem; margin-top: 2rem; }
    .product-item { background: white; padding: 1.5rem; border-radius: 10px; display: flex; gap: 1.5rem; align-items: center; }
    .product-thumbnail { width: 120px; height: 120px; object-fit: cover; border-radius: 8px; }
    .product-info { flex: 1; }
    .price { font-size: 1.5rem; color: #008751; font-weight: bold; margin: 0.5rem 0; }
    .actions { display: flex; gap: 1rem; margin-top: 1rem; }
    .view-btn, .whatsapp-btn-small { padding: 0.5rem 1rem; border-radius: 5px; text-decoration: none; color: white; }
    .view-btn { background: #008751; }
    .whatsapp-btn-small { background: #25D366; }
    
    .product-card { background: white; padding: 2rem; border-radius: 10px; margin: 2rem 0; }
    .product-header { text-align: center; margin-bottom: 2rem; }
    .product-header h1 { font-size: 2rem; color: #333; }
    .product-image { width: 100%; max-height: 400px; object-fit: cover; border-radius: 10px; margin-bottom: 1.5rem; }
    .action-buttons { display: flex; gap: 1rem; margin: 2rem 0; justify-content: center; }
    .whatsapp-btn, .call-btn { padding: 1rem 2rem; border-radius: 5px; text-decoration: none; color: white; font-weight: bold; }
    .whatsapp-btn { background: #25D366; }
    .call-btn { background: #008751; }
    
    .business-info { background: #f8f9fa; padding: 1.5rem; border-radius: 8px; margin: 1.5rem 0; }
    .info-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1rem; }
    .info-item { background: white; padding: 1rem; border-radius: 5px; }
    
    .other-products { margin: 3rem 0; }
    .products-scroll { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; }
    .other-product { background: white; padding: 1rem; border-radius: 8px; text-decoration: none; color: #333; text-align: center; }
    .other-product img { width: 100px; height: 100px; object-fit: cover; border-radius: 5px; margin-bottom: 0.5rem; }
    
    .page-header { text-align: center; padding: 2rem; background: white; border-radius: 10px; margin-bottom: 2rem; }
    .contact-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem; margin: 2rem 0; }
    .contact-method { background: white; padding: 2rem; border-radius: 10px; text-align: center; }
    .contact-icon { font-size: 3rem; margin-bottom: 1rem; }
    .contact-btn { display: inline-block; padding: 1rem 2rem; border-radius: 5px; text-decoration: none; color: white; margin-top: 1rem; }
    .contact-btn.whatsapp { background: #25D366; }
    .contact-btn.call { background: #008751; }
    
    .about-content { background: white; padding: 2rem; border-radius: 10px; }
    .business-details { background: #f8f9fa; padding: 1.5rem; border-radius: 8px; margin: 1rem 0; }
    
    .main-footer { background: #333; color: white; padding: 2rem 0; margin-top: 3rem; }
    .footer-content { max-width: 1200px; margin: 0 auto; display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 2rem; padding: 0 1rem; }
    .footer-section a { display: block; color: #ccc; text-decoration: none; margin: 0.5rem 0; }
    
    @media (max-width: 768px) {
        .product-item { flex-direction: column; text-align: center; }
        .hero-actions, .action-buttons { flex-direction: column; }
        .nav-container { flex-direction: column; gap: 1rem; }
    }
    '''
    
    with open(os.path.join(folder, 'styles.css'), 'w') as f:
        f.write(css_content)
    print("🎨 Created: styles.css")

if __name__ == "__main__":
    create_final_website()
    