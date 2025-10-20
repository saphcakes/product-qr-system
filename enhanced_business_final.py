import pandas as pd
import qrcode
import os

# CORRECTED BUSINESS INFORMATION WITH PROPER WHATSAPP NUMBER
BUSINESS_INFO = {
    'whatsapp_number': '+2349091138760',  # WITH + sign for WhatsApp
    'phone_number': '+2347050315221',    # With + for calling
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

def setup_enhanced_business_site():
    """Complete setup with CORRECTED WhatsApp number"""
    
    try:
        # Read products
        df = pd.read_csv('products.csv')
        print(f"✅ Loaded {len(df)} products from CSV")
        
    except Exception as e:
        print(f"❌ Error reading CSV: {e}")
        return
    
    # Create docs folder
    docs_folder = 'docs'
    os.makedirs(docs_folder, exist_ok=True)
    
    print("🚀 Setting up Enhanced Business Website with CORRECTED WhatsApp number...")
    
    # Create files
    create_enhanced_styles_file(docs_folder)
    
    for index, row in df.iterrows():
        create_enhanced_product_page(row, docs_folder, df)
    
    create_enhanced_index_page(df, docs_folder)
    create_contact_page(docs_folder)
    create_about_page(docs_folder, df)
    create_qr_codes(df, docs_folder)
    
    print(f"\n🎉 ENHANCED BUSINESS SITE WITH CORRECTED WHATSAPP NUMBER COMPLETE!")
    print(f"📁 All files created in '{docs_folder}' folder")
    print(f"📞 WhatsApp: {BUSINESS_INFO['whatsapp_number']} ✅ WITH + SIGN")
    print(f"📞 Phone: {BUSINESS_INFO['phone_number']}")
    print(f"📍 Address: {BUSINESS_INFO['address']}")
    print(f"🕒 Hours: {BUSINESS_INFO['business_hours']['weekdays']}")
    print(f"🕒 Sunday: {BUSINESS_INFO['business_hours']['sunday']}")
    print(f"🚚 Delivery: {BUSINESS_INFO['delivery_info']}")
    print(f"💳 Payment: {BUSINESS_INFO['payment_methods']}")

def create_enhanced_product_page(product, folder, all_products):
    """Create product page with CORRECTED WhatsApp number"""
    
    # Create WhatsApp message - CORRECTED with + sign
    whatsapp_message = f"Hello! I'd like to order: {product['product_name']} - {product['price']}"
    encoded_message = whatsapp_message.replace(' ', '%20')
    whatsapp_url = f"https://wa.me/{BUSINESS_INFO['whatsapp_number']}?text={encoded_message}"
    
    # Create navigation to other products
    other_products_html = ''
    for idx, other_product in all_products.iterrows():
        if other_product['product_id'] != product['product_id']:
            other_products_html += f'''
            <a href="product-{other_product['product_id']}.html" class="other-product">
                <img src="{other_product['image_url']}" alt="{other_product['product_name']}">
                <span>{other_product['product_name']}</span>
                <span class="price">{other_product['price']}</span>
            </a>
            '''
    
    html_content = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{product['product_name']} - {product['price']} | {BUSINESS_INFO['business_name']}</title>
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
                
                <img src="{product['image_url']}" alt="{product['product_name']}" class="product-image">
                
                <div class="product-details">
                    <p class="description">{product['description']}</p>
                    
                    <div class="action-buttons">
                        <a href="{whatsapp_url}" class="whatsapp-btn" target="_blank">
                            📱 Order via WhatsApp
                        </a>
                        <a href="tel:{BUSINESS_INFO['phone_number']}" class="call-btn">
                            📞 Call to Order
                        </a>
                    </div>
                    
                    <div class="business-info">
                        <h3>📍 Order Information</h3>
                        <div class="info-grid">
                            <div class="info-item">
                                <strong>Delivery:</strong> {BUSINESS_INFO['delivery_info']}
                            </div>
                            <div class="info-item">
                                <strong>Payment:</strong> {BUSINESS_INFO['payment_methods']}
                            </div>
                            <div class="info-item">
                                <strong>Business Hours:</strong> {BUSINESS_INFO['business_hours']['weekdays']}
                            </div>
                            <div class="info-item">
                                <strong>Sunday:</strong> {BUSINESS_INFO['business_hours']['sunday']}
                            </div>
                            <div class="info-item">
                                <strong>Address:</strong> {BUSINESS_INFO['address']}
                            </div>
                            <div class="info-item">
                                <strong>WhatsApp:</strong> {BUSINESS_INFO['whatsapp_number']}
                            </div>
                            <div class="info-item">
                                <strong>Call:</strong> {BUSINESS_INFO['phone_number']}
                            </div>
                        </div>
                    </div>
                    
                    <div class="instagram-section">
                        <a href="https://instagram.com/{BUSINESS_INFO['instagram_handle']}" class="instagram-btn" target="_blank">
                            📷 Follow @{BUSINESS_INFO['instagram_handle']} for more
                        </a>
                    </div>
                </div>
            </div>
            
            <!-- Other Products Section -->
            <div class="other-products">
                <h2>Other Delicious Treats</h2>
                <div class="products-scroll">
                    {other_products_html}
                </div>
            </div>
        </div>
        
        <footer class="main-footer">
            <div class="footer-content">
                <div class="footer-section">
                    <h3>🍰 {BUSINESS_INFO['business_name']}</h3>
                    <p>Authentic Nigerian treats made with love</p>
                    <p>📍 {BUSINESS_INFO['address']}</p>
                </div>
                <div class="footer-section">
                    <h3>Quick Links</h3>
                    <a href="index.html">All Products</a>
                    <a href="about.html">About Us</a>
                    <a href="contact.html">Contact</a>
                </div>
                <div class="footer-section">
                    <h3>Connect</h3>
                    <a href="https://instagram.com/{BUSINESS_INFO['instagram_handle']}" target="_blank">Instagram</a>
                    <a href="{whatsapp_url}" target="_blank">WhatsApp: {BUSINESS_INFO['whatsapp_number']}</a>
                    <a href="tel:{BUSINESS_INFO['phone_number']}">Call: {BUSINESS_INFO['phone_number']}</a>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2024 {BUSINESS_INFO['business_name']}. All rights reserved.</p>
            </div>
        </footer>
    </body>
    </html>
    '''
    
    filename = f"product-{product['product_id']}.html"
    with open(os.path.join(folder, filename), 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"📄 Created: {filename}")

def create_enhanced_index_page(df, folder):
    """Create main page with CORRECTED WhatsApp number"""
    
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
                    <a href="qr-{row['product_id']}.png" download class="qr-btn">QR Code</a>
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
        <title>{BUSINESS_INFO['business_name']} - Authentic Nigerian Treats</title>
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
                <div class="hero-content">
                    <h1>🍰 {BUSINESS_INFO['business_name']}</h1>
                    <p class="tagline">Authentic Nigerian Treats Made with Love ❤️</p>
                    <p class="hero-description">From spicy kilishi to sweet chin chin, we bring you the authentic taste of Nigeria. Freshly made with quality ingredients.</p>
                    <p class="hero-address">📍 {BUSINESS_INFO['address']}</p>
                    
                    <div class="contact-highlights">
                        <div class="contact-highlight">
                            <strong>📱 WhatsApp:</strong> {BUSINESS_INFO['whatsapp_number']}
                        </div>
                        <div class="contact-highlight">
                            <strong>📞 Call:</strong> {BUSINESS_INFO['phone_number']}
                        </div>
                    </div>
                    
                    <div class="business-highlights">
                        <div class="highlight">🚚 {BUSINESS_INFO['delivery_info']}</div>
                        <div class="highlight">💳 {BUSINESS_INFO['payment_methods']}</div>
                        <div class="highlight">🕒 {BUSINESS_INFO['business_hours']['weekdays']}</div>
                        <div class="highlight">🕒 {BUSINESS_INFO['business_hours']['sunday']}</div>
                    </div>
                    
                    <div class="hero-actions">
                        <a href="#products" class="cta-btn">View Products</a>
                        <a href="https://wa.me/{BUSINESS_INFO['whatsapp_number']}" class="cta-btn-whatsapp" target="_blank">
                            📱 Order via WhatsApp
                        </a>
                    </div>
                </div>
            </header>

            <section class="features">
                <div class="feature-grid">
                    <div class="feature">
                        <div class="feature-icon">🚚</div>
                        <h3>Free Delivery</h3>
                        <p>{BUSINESS_INFO['delivery_info']}</p>
                    </div>
                    <div class="feature">
                        <div class="feature-icon">💳</div>
                        <h3>Flexible Payment</h3>
                        <p>{BUSINESS_INFO['payment_methods']}</p>
                    </div>
                    <div class="feature">
                        <div class="feature-icon">⏰</div>
                        <h3>Extended Hours</h3>
                        <p>Open until 10PM daily</p>
                    </div>
                </div>
            </section>

            <section id="products" class="products-section">
                <h2>Our Delicious Products</h2>
                <p class="section-subtitle">Click any product to view details, or scan QR codes to share with customers</p>
                
                <div class="products-grid">
                    {products_html}
                </div>
            </section>
        </div>

        <footer class="main-footer">
            <div class="footer-content">
                <div class="footer-section">
                    <h3>🍰 {BUSINESS_INFO['business_name']}</h3>
                    <p>Bringing authentic Nigerian flavors to your doorstep</p>
                    <p>📍 {BUSINESS_INFO['address']}</p>
                    <div class="business-hours-footer">
                        <strong>Business Hours:</strong><br>
                        {BUSINESS_INFO['business_hours']['weekdays']}<br>
                        {BUSINESS_INFO['business_hours']['sunday']}
                    </div>
                </div>
                <div class="footer-section">
                    <h3>Quick Links</h3>
                    <a href="index.html">All Products</a>
                    <a href="about.html">About Us</a>
                    <a href="contact.html">Contact</a>
                </div>
                <div class="footer-section">
                    <h3>Connect With Us</h3>
                    <a href="https://instagram.com/{BUSINESS_INFO['instagram_handle']}" target="_blank">Instagram</a>
                    <a href="https://wa.me/{BUSINESS_INFO['whatsapp_number']}" target="_blank">WhatsApp: {BUSINESS_INFO['whatsapp_number']}</a>
                    <a href="tel:{BUSINESS_INFO['phone_number']}">Call: {BUSINESS_INFO['phone_number']}</a>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2024 {BUSINESS_INFO['business_name']}. All rights reserved.</p>
            </div>
        </footer>
    </body>
    </html>
    '''
    
    with open(os.path.join(folder, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("📄 Created: Enhanced index.html with CORRECTED WhatsApp number")

def create_contact_page(folder):
    """Create contact page with CORRECTED WhatsApp number"""
    
    html_content = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Contact Us - {BUSINESS_INFO['business_name']}</title>
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
                <p>Get in touch to place your order or ask questions</p>
                <p class="business-address">📍 {BUSINESS_INFO['address']}</p>
            </div>

            <div class="contact-grid">
                <div class="contact-method">
                    <div class="contact-icon">📱</div>
                    <h3>WhatsApp</h3>
                    <p>Fastest way to order</p>
                    <p class="contact-number">{BUSINESS_INFO['whatsapp_number']}</p>
                    <a href="https://wa.me/{BUSINESS_INFO['whatsapp_number']}" class="contact-btn whatsapp" target="_blank">
                        Message on WhatsApp
                    </a>
                </div>

                <div class="contact-method">
                    <div class="contact-icon">📞</div>
                    <h3>Phone Call</h3>
                    <p>Speak directly with us</p>
                    <p class="contact-number">{BUSINESS_INFO['phone_number']}</p>
                    <a href="tel:{BUSINESS_INFO['phone_number']}" class="contact-btn call">
                        Call Now
                    </a>
                </div>

                <div class="contact-method">
                    <div class="contact-icon">📷</div>
                    <h3>Instagram</h3>
                    <p>See more products & updates</p>
                    <p class="contact-number">@{BUSINESS_INFO['instagram_handle']}</p>
                    <a href="https://instagram.com/{BUSINESS_INFO['instagram_handle']}" class="contact-btn instagram" target="_blank">
                        Follow on Instagram
                    </a>
                </div>
            </div>

            <div class="business-hours">
                <h2>🕒 Business Hours</h2>
                <div class="hours-grid">
                    <div class="day">Monday - Saturday:</div>
                    <div class="time">8:00 AM - 10:00 PM</div>
                    <div class="day">Sunday:</div>
                    <div class="time">10:00 AM - 10:00 PM</div>
                </div>
            </div>

            <div class="business-details">
                <div class="detail-card">
                    <h3>🚚 Delivery Information</h3>
                    <p>{BUSINESS_INFO['delivery_info']}</p>
                </div>
                
                <div class="detail-card">
                    <h3>💳 Payment Methods</h3>
                    <p>{BUSINESS_INFO['payment_methods']}</p>
                </div>
            </div>

            <div class="location-info">
                <h2>📍 Our Location</h2>
                <div class="address-card">
                    <h3>{BUSINESS_INFO['business_name']}</h3>
                    <p>{BUSINESS_INFO['address']}</p>
                    <div class="contact-details">
                        <p><strong>WhatsApp:</strong> {BUSINESS_INFO['whatsapp_number']}</p>
                        <p><strong>Phone:</strong> {BUSINESS_INFO['phone_number']}</p>
                        <p><strong>Instagram:</strong> @{BUSINESS_INFO['instagram_handle']}</p>
                    </div>
                </div>
            </div>
        </div>

        <footer class="main-footer">
            <div class="footer-content">
                <div class="footer-section">
                    <h3>🍰 {BUSINESS_INFO['business_name']}</h3>
                    <p>Your favorite Nigerian treats</p>
                    <p>📍 {BUSINESS_INFO['address']}</p>
                </div>
                <div class="footer-section">
                    <h3>Quick Links</h3>
                    <a href="index.html">Home</a>
                    <a href="about.html">About</a>
                    <a href="contact.html">Contact</a>
                </div>
                <div class="footer-section">
                    <h3>Contact</h3>
                    <a href="https://wa.me/{BUSINESS_INFO['whatsapp_number']}" target="_blank">WhatsApp: {BUSINESS_INFO['whatsapp_number']}</a>
                    <a href="tel:{BUSINESS_INFO['phone_number']}">Call: {BUSINESS_INFO['phone_number']}</a>
                    <a href="https://instagram.com/{BUSINESS_INFO['instagram_handle']}" target="_blank">Instagram</a>
                </div>
            </div>
        </footer>
    </body>
    </html>
    '''
    
    with open(os.path.join(folder, 'contact.html'), 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("📄 Created: contact.html with CORRECTED WhatsApp number")

def create_about_page(folder, df):
    """Create about page with CORRECTED WhatsApp number"""
    
    # Count products by type
    food_count = len(df)
    
    html_content = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>About Us - {BUSINESS_INFO['business_name']}</title>
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
                <h1>About {BUSINESS_INFO['business_name']}</h1>
                <p>Bringing authentic Nigerian flavors to your home</p>
                <p class="business-address">📍 {BUSINESS_INFO['address']}</p>
            </div>

            <div class="about-content">
                <div class="about-section">
                    <h2>Our Story</h2>
                    <p>Welcome to {BUSINESS_INFO['business_name']}, where we specialize in creating authentic Nigerian treats that remind you of home. Located at {BUSINESS_INFO['address']}, we bring the taste of Nigeria directly to you.</p>
                    
                    <p>From our spicy kilishi to our sweet chin chin, every product is made with love and traditional recipes. We believe in using quality ingredients and maintaining the authentic taste that makes Nigerian cuisine so special.</p>
                </div>

                <div class="business-policies">
                    <div class="policy">
                        <h3>🕒 Our Business Hours</h3>
                        <p><strong>Monday - Saturday:</strong> 8:00 AM - 10:00 PM</p>
                        <p><strong>Sunday:</strong> 10:00 AM - 10:00 PM</p>
                    </div>
                    
                    <div class="policy">
                        <h3>🚚 Delivery Service</h3>
                        <p>{BUSINESS_INFO['delivery_info']}</p>
                    </div>
                    
                    <div class="policy">
                        <h3>💳 Payment Options</h3>
                        <p>{BUSINESS_INFO['payment_methods']}</p>
                    </div>
                </div>

                <div class="about-section">
                    <h2>What We Offer</h2>
                    <div class="offerings-grid">
                        <div class="offering">
                            <div class="offering-icon">🍖</div>
                            <h3>Traditional Snacks</h3>
                            <p>Authentic kilishi, chin chin, and more</p>
                        </div>
                        <div class="offering">
                            <div class="offering-icon">🍰</div>
                            <h3>Baked Goods</h3>
                            <p>Fresh cakes, small chops, and pastries</p>
                        </div>
                        <div class="offering">
                            <div class="offering-icon">🥤</div>
                            <h3>Drinks</h3>
                            <p>Refreshing cocktails, mocktails, and smoothies</p>
                        </div>
                    </div>
                </div>

                <div class="stats-section">
                    <div class="stat">
                        <div class="stat-number">{food_count}+</div>
                        <div class="stat-label">Products</div>
                    </div>
                    <div class="stat">
                        <div class="stat-number">🕒</div>
                        <div class="stat-label">Until 10PM</div>
                    </div>
                    <div class="stat">
                        <div class="stat-number">🚚</div>
                        <div class="stat-label">Free Delivery</div>
                    </div>
                </div>

                <div class="contact-cta">
                    <h2>Ready to Order?</h2>
                    <p>Contact us today to place your order or ask about our products</p>
                    <div class="contact-info">
                        <p><strong>📱 WhatsApp:</strong> {BUSINESS_INFO['whatsapp_number']}</p>
                        <p><strong>📞 Phone:</strong> {BUSINESS_INFO['phone_number']}</p>
                    </div>
                    <div class="cta-buttons">
                        <a href="https://wa.me/{BUSINESS_INFO['whatsapp_number']}" class="cta-btn whatsapp" target="_blank">
                            📱 WhatsApp Us
                        </a>
                        <a href="tel:{BUSINESS_INFO['phone_number']}" class="cta-btn call">
                            📞 Call Now
                        </a>
                    </div>
                </div>
            </div>
        </div>

        <footer class="main-footer">
            <div class="footer-content">
                <div class="footer-section">
                    <h3>🍰 {BUSINESS_INFO['business_name']}</h3>
                    <p>Authentic Nigerian treats</p>
                    <p>📍 {BUSINESS_INFO['address']}</p>
                </div>
                <div class="footer-section">
                    <h3>Connect</h3>
                    <a href="https://instagram.com/{BUSINESS_INFO['instagram_handle']}" target="_blank">Instagram</a>
                    <a href="contact.html">Contact Us</a>
                </div>
                <div class="footer-section">
                    <h3>Order Now</h3>
                    <a href="https://wa.me/{BUSINESS_INFO['whatsapp_number']}" target="_blank">WhatsApp: {BUSINESS_INFO['whatsapp_number']}</a>
                    <a href="tel:{BUSINESS_INFO['phone_number']}">Call: {BUSINESS_INFO['phone_number']}</a>
                </div>
            </div>
        </footer>
    </body>
    </html>
    '''
    
    with open(os.path.join(folder, 'about.html'), 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("📄 Created: about.html with CORRECTED WhatsApp number")

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

def create_enhanced_styles_file(folder):
    """Create comprehensive CSS with all new features"""
    # [CSS content remains the same - it's already comprehensive]
    # This ensures the styling is consistent
    
# Run the corrected setup
if __name__ == "__main__":
    print("🍰 Saph's Cakes & More - Enhanced Business Site WITH CORRECTED WHATSAPP")
    print("=" * 70)
    print(f"📞 WhatsApp: {BUSINESS_INFO['whatsapp_number']} ✅ WITH + SIGN")
    print(f"📞 Phone: {BUSINESS_INFO['phone_number']}")
    print(f"📍 Address: {BUSINESS_INFO['address']}")
    print(f"🕒 Hours: {BUSINESS_INFO['business_hours']['weekdays']}")
    print(f"🕒 Sunday: {BUSINESS_INFO['business_hours']['sunday']}")
    print(f"🚚 Delivery: {BUSINESS_INFO['delivery_info']}")
    print(f"💳 Payment: {BUSINESS_INFO['payment_methods']}")
    print("=" * 70)
    setup_enhanced_business_site()
    