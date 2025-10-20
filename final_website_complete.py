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
    """Create the final website with ALL features"""
    
    print("🎯 CREATING COMPLETE WEBSITE WITH ALL FEATURES")
    print("=" * 60)
    
    try:
        # Read your products.csv
        df = pd.read_csv('products.csv')
        print(f"✅ Loaded {len(df)} products from products.csv")
        
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
    
    print(f"\n🎉 COMPLETE WEBSITE WITH ALL FEATURES READY!")
    print(f"📁 Check the '{docs_folder}' folder for your files")
    print(f"🌐 Your live site: https://saphcakes.github.io/product-qr-system/")

def create_index_page(df, folder):
    """Create main page with custom cakes section and reordered sections"""
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
                <p class="tagline">Authentic Nigerian Treats & Custom Cakes Made with Love ❤️</p>
                <p class="hero-address">📍 {BUSINESS_INFO['address']}</p>
                
                <div class="instagram-cta">
                    <a href="https://instagram.com/{BUSINESS_INFO['instagram_handle']}" class="instagram-link" target="_blank">
                        📷 Follow @{BUSINESS_INFO['instagram_handle']} for more creations
                    </a>
                </div>
                
                <div class="hero-actions">
                    <a href="#products" class="cta-btn">View Products</a>
                    <a href="#custom-cakes" class="cta-btn">Custom Cakes</a>
                    <a href="https://wa.me/{BUSINESS_INFO['whatsapp_number']}" class="cta-btn-whatsapp" target="_blank">📱 Get Quote</a>
                </div>
            </header>

            <!-- Custom Cakes Section -->
            <section id="custom-cakes" class="custom-cakes-section">
                <h2>🎂 Custom Celebration Cakes</h2>
                <p class="section-subtitle">Beautiful custom cakes for every special occasion</p>
                
                <div class="custom-cakes-grid">
                    <div class="cake-type">
                        <div class="cake-icon">🎉</div>
                        <h3>Birthday Cakes</h3>
                        <p>Make your celebration unforgettable with personalized birthday cakes in any theme, flavor, and size.</p>
                    </div>
                    
                    <div class="cake-type">
                        <div class="cake-icon">💍</div>
                        <h3>Wedding Cakes</h3>
                        <p>Elegant and stunning wedding cakes that match your theme and create beautiful memories.</p>
                    </div>
                    
                    <div class="cake-type">
                        <div class="cake-icon">🎓</div>
                        <h3>Special Events</h3>
                        <p>Graduations, anniversaries, baby showers, and corporate events - we create cakes for all occasions.</p>
                    </div>
                </div>
                
                <div class="custom-cakes-info">
                    <h3>How It Works:</h3>
                    <div class="process-steps">
                        <div class="step">
                            <div class="step-number">1</div>
                            <h4>Consultation</h4>
                            <p>Tell us about your event, theme, and preferences</p>
                        </div>
                        <div class="step">
                            <div class="step-number">2</div>
                            <h4>Custom Quote</h4>
                            <p>We provide pricing based on size, design complexity, and ingredients</p>
                        </div>
                        <div class="step">
                            <div class="step-number">3</div>
                            <h4>Creation & Delivery</h4>
                            <p>We bake and deliver your perfect custom cake</p>
                        </div>
                    </div>
                    
                    <div class="pricing-note">
                        <p><strong>💵 Pricing:</strong> Custom cake prices vary based on size, design complexity, and current market prices of ingredients. Contact us for a personalized quote.</p>
                    </div>
                    
                    <div class="cta-cakes">
                        <a href="https://wa.me/{BUSINESS_INFO['whatsapp_number']}?text=Hello! I'd like to get a quote for a custom cake" class="cta-btn-whatsapp large" target="_blank">
                            📱 Get Custom Cake Quote
                        </a>
                        <p class="cta-note">Send us a message with your event details for a personalized quote</p>
                    </div>
                </div>
            </section>

            <!-- Regular Products Section -->
            <section id="products" class="products-section">
                <h2>Our Delicious Ready-to-Order Products</h2>
                <p class="section-subtitle">Click any product to view details and order</p>
                
                <div class="products-grid">
                    {products_html}
                </div>
            </section>

            <!-- QR Codes Section (Moved Below Products) -->
            <section class="qr-codes-section">
                <h2>📱 QR Codes for Easy Sharing</h2>
                <p>Download QR codes to share products with customers - perfect for packaging, menus, and social media</p>
                <div class="qr-codes-grid">
                    <div class="qr-code-item">
                        <img src="qr-101.png" alt="QR Code for Kilishi" class="qr-code-image">
                        <p>Kilishi QR Code</p>
                        <a href="qr-101.png" download class="download-btn">Download</a>
                    </div>
                    <div class="qr-code-item">
                        <img src="qr-102.png" alt="QR Code for Chin Chin" class="qr-code-image">
                        <p>Chin Chin QR Code</p>
                        <a href="qr-102.png" download class="download-btn">Download</a>
                    </div>
                    <div class="qr-code-item">
                        <img src="qr-103.png" alt="QR Code for Small Chops" class="qr-code-image">
                        <p>Small Chops QR Code</p>
                        <a href="qr-103.png" download class="download-btn">Download</a>
                    </div>
                    <div class="qr-code-item">
                        <p>+4 More QR Codes</p>
                        <p class="qr-note">Available for all products</p>
                        <a href="#products" class="download-btn">View All</a>
                    </div>
                </div>
                <div class="qr-instructions">
                    <h3>How to Use QR Codes:</h3>
                    <ul>
                        <li>🖨️ Print and stick on product packaging</li>
                        <li>🏪 Display in your store or on menus</li>
                        <li>📸 Customers scan with any smartphone camera</li>
                        <li>🌐 Directly opens product page with details</li>
                        <li>📱 Perfect for social media sharing</li>
                    </ul>
                </div>
            </section>
        </div>

        <footer class="main-footer">
            <div class="footer-content">
                <div class="footer-section">
                    <h3>{BUSINESS_INFO['business_name']}</h3>
                    <p>Custom Cakes & Authentic Nigerian Treats</p>
                    <p>📍 {BUSINESS_INFO['address']}</p>
                </div>
                <div class="footer-section">
                    <h3>Quick Links</h3>
                    <a href="index.html">All Products</a>
                    <a href="index.html#custom-cakes">Custom Cakes</a>
                    <a href="about.html">About Us</a>
                    <a href="contact.html">Contact</a>
                </div>
                <div class="footer-section">
                    <h3>Connect With Us</h3>
                    <a href="https://instagram.com/{BUSINESS_INFO['instagram_handle']}" target="_blank">📷 Instagram</a>
                    <a href="https://wa.me/{BUSINESS_INFO['whatsapp_number']}" target="_blank">📱 WhatsApp</a>
                    <a href="tel:{BUSINESS_INFO['phone_number']}">📞 Call Us</a>
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
    print("📄 Created: index.html with custom cakes and reordered sections")

def create_contact_page(folder):
    """Create contact page with FIXED Instagram link"""
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
                <p>Get in touch to place orders or get quotes for custom cakes</p>
                <p class="business-address">📍 {BUSINESS_INFO['address']}</p>
            </div>

            <div class="contact-grid">
                <div class="contact-method">
                    <div class="contact-icon">📱</div>
                    <h3>WhatsApp</h3>
                    <p>Fastest way to order or get quotes</p>
                    <p class="contact-number">{BUSINESS_INFO['whatsapp_number']}</p>
                    <a href="https://wa.me/{BUSINESS_INFO['whatsapp_number']}" class="contact-btn whatsapp" target="_blank">Message on WhatsApp</a>
                </div>

                <div class="contact-method">
                    <div class="contact-icon">📞</div>
                    <h3>Phone Call</h3>
                    <p>Speak directly with us</p>
                    <p class="contact-number">{BUSINESS_INFO['phone_number']}</p>
                    <a href="tel:{BUSINESS_INFO['phone_number']}" class="contact-btn call">Call Now</a>
                </div>

                <div class="contact-method">
                    <div class="contact-icon">📷</div>
                    <h3>Instagram</h3>
                    <p>See our latest creations and updates</p>
                    <p class="contact-number">@{BUSINESS_INFO['instagram_handle']}</p>
                    <a href="https://instagram.com/{BUSINESS_INFO['instagram_handle']}" class="contact-btn instagram" target="_blank">Follow on Instagram</a>
                </div>
            </div>

            <div class="business-hours-contact">
                <h2>🕒 Business Hours</h2>
                <div class="hours-grid">
                    <div class="day">Monday - Saturday:</div>
                    <div class="time">8:00 AM - 10:00 PM</div>
                    <div class="day">Sunday:</div>
                    <div class="time">10:00 AM - 10:00 PM</div>
                </div>
            </div>

            <div class="contact-notes">
                <div class="note">
                    <h3>🎂 For Custom Cakes</h3>
                    <p>Contact us at least 3-5 days before your event for custom cake orders. We'll discuss your preferences and provide a personalized quote.</p>
                </div>
                <div class="note">
                    <h3>🚚 Delivery Information</h3>
                    <p>{BUSINESS_INFO['delivery_info']}</p>
                </div>
            </div>
        </div>

        <footer class="main-footer">
            <div class="footer-content">
                <div class="footer-section">
                    <h3>{BUSINESS_INFO['business_name']}</h3>
                    <p>Custom Cakes & Nigerian Treats</p>
                    <p>📍 {BUSINESS_INFO['address']}</p>
                </div>
                <div class="footer-section">
                    <h3>Contact</h3>
                    <a href="https://wa.me/{BUSINESS_INFO['whatsapp_number']}" target="_blank">WhatsApp</a>
                    <a href="tel:{BUSINESS_INFO['phone_number']}">Call Us</a>
                    <a href="https://instagram.com/{BUSINESS_INFO['instagram_handle']}" target="_blank">Instagram</a>
                </div>
            </div>
        </footer>
    </body>
    </html>
    '''
    
    with open(os.path.join(folder, 'contact.html'), 'w', encoding='utf-8') as f:
        f.write(html_content)
    print("📄 Created: contact.html with FIXED Instagram link")

# [Keep the other functions: create_product_page, create_about_page, create_qr_codes, create_styles]
# But I'll update the create_styles function to include new styles

def create_styles(folder):
    """Create CSS styles with custom cakes section and fixed Instagram button"""
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
    .tagline { font-size: 1.2rem; color: #666; margin-bottom: 1rem; }
    .hero-address { color: #333; margin-bottom: 1.5rem; }
    
    .instagram-cta { margin: 1.5rem 0; }
    .instagram-link { background: linear-gradient(45deg, #405DE6, #5851DB, #833AB4, #C13584, #E1306C, #FD1D1D); 
                     color: white; padding: 1rem 2rem; border-radius: 25px; text-decoration: none; 
                     font-weight: bold; display: inline-block; transition: transform 0.3s ease; }
    .instagram-link:hover { transform: scale(1.05); }
    
    .hero-actions { margin-top: 2rem; display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; }
    .cta-btn, .cta-btn-whatsapp { padding: 1rem 2rem; border-radius: 5px; text-decoration: none; font-weight: bold; transition: all 0.3s ease; }
    .cta-btn { background: #008751; color: white; }
    .cta-btn:hover { background: #006641; transform: translateY(-2px); }
    .cta-btn-whatsapp { background: #25D366; color: white; }
    .cta-btn-whatsapp:hover { background: #1DA851; transform: translateY(-2px); }
    .cta-btn-whatsapp.large { padding: 1.2rem 2.5rem; font-size: 1.1rem; }
    
    /* Custom Cakes Section */
    .custom-cakes-section { background: white; padding: 3rem 2rem; border-radius: 15px; margin: 3rem 0; text-align: center; }
    .custom-cakes-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 2rem; margin: 2rem 0; }
    .cake-type { background: #f8f9fa; padding: 2rem; border-radius: 10px; text-align: center; }
    .cake-icon { font-size: 3rem; margin-bottom: 1rem; }
    .cake-type h3 { color: #008751; margin-bottom: 1rem; }
    
    .process-steps { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 2rem; margin: 2rem 0; }
    .step { text-align: center; }
    .step-number { background: #008751; color: white; width: 40px; height: 40px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 1rem; font-weight: bold; }
    .step h4 { color: #333; margin-bottom: 0.5rem; }
    
    .pricing-note { background: #fff3cd; border: 1px solid #ffeaa7; padding: 1.5rem; border-radius: 8px; margin: 1.5rem 0; text-align: left; }
    .cta-cakes { margin-top: 2rem; }
    .cta-note { margin-top: 1rem; color: #666; font-size: 0.9rem; }
    
    .products-section { margin: 3rem 0; }
    .section-subtitle { text-align: center; color: #666; margin-bottom: 2rem; }
    
    .products-grid { display: grid; gap: 2rem; }
    .product-item { background: white; padding: 1.5rem; border-radius: 10px; display: flex; gap: 1.5rem; align-items: center; transition: transform 0.3s ease; }
    .product-item:hover { transform: translateY(-5px); box-shadow: 0 10px 25px rgba(0,0,0,0.1); }
    .product-thumbnail { width: 120px; height: 120px; object-fit: cover; border-radius: 8px; }
    .product-info { flex: 1; }
    .price { font-size: 1.5rem; color: #008751; font-weight: bold; margin: 0.5rem 0; }
    .actions { display: flex; gap: 1rem; margin-top: 1rem; flex-wrap: wrap; }
    .view-btn, .whatsapp-btn-small, .qr-btn { padding: 0.5rem 1rem; border-radius: 5px; text-decoration: none; color: white; font-size: 0.9rem; transition: all 0.3s ease; }
    .view-btn { background: #008751; }
    .view-btn:hover { background: #006641; }
    .whatsapp-btn-small { background: #25D366; }
    .whatsapp-btn-small:hover { background: #1DA851; }
    .qr-btn { background: #E1306C; }
    .qr-btn:hover { background: #C13584; }
    
    /* QR Codes Section */
    .qr-codes-section { background: white; padding: 2rem; border-radius: 10px; margin: 3rem 0; text-align: center; }
    .qr-codes-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 1.5rem; margin: 2rem 0; }
    .qr-code-item { background: #f8f9fa; padding: 1.5rem; border-radius: 10px; }
    .qr-code-image { width: 120px; height: 120px; object-fit: contain; margin-bottom: 1rem; }
    .download-btn { background: #008751; color: white; padding: 0.5rem 1rem; border-radius: 5px; text-decoration: none; font-size: 0.9rem; transition: all 0.3s ease; }
    .download-btn:hover { background: #006641; }
    .qr-note { font-size: 0.8rem; color: #666; margin: 0.5rem 0; }
    .qr-instructions { background: #e8f5e8; padding: 1.5rem; border-radius: 8px; margin-top: 1.5rem; text-align: left; }
    .qr-instructions ul { list-style: none; padding: 0; }
    .qr-instructions li { margin: 0.5rem 0; padding-left: 1.5rem; }
    
    /* Contact Page Styles */
    .business-address { color: #666; margin-bottom: 1rem; }
    .contact-number { font-weight: bold; color: #333; margin: 0.5rem 0; }
    .contact-btn.instagram { background: linear-gradient(45deg, #405DE6, #E1306C); color: white; }
    .contact-btn.instagram:hover { transform: translateY(-2px); box-shadow: 0 5px 15px rgba(224, 58, 132, 0.4); }
    
    .business-hours-contact { background: white; padding: 1.5rem; border-radius: 8px; margin: 2rem 0; }
    .hours-grid { display: grid; grid-template-columns: auto auto; gap: 1rem; margin-top: 1rem; }
    .contact-notes { display: grid; gap: 1.5rem; margin: 2rem 0; }
    .note { background: #f8f9fa; padding: 1.5rem; border-radius: 8px; }
    
    /* Keep the rest of your existing styles... */
    
    @media (max-width: 768px) {
        .product-item { flex-direction: column; text-align: center; }
        .hero-actions, .action-buttons { flex-direction: column; }
        .nav-container { flex-direction: column; gap: 1rem; }
        .qr-codes-grid { grid-template-columns: repeat(2, 1fr); }
        .actions { justify-content: center; }
        .custom-cakes-grid, .process-steps { grid-template-columns: 1fr; }
        .hours-grid { grid-template-columns: 1fr; }
    }
    '''
    
    with open(os.path.join(folder, 'styles.css'), 'w') as f:
        f.write(css_content)
    print("🎨 Created: styles.css with custom cakes and fixed Instagram")

# [Keep the other functions unchanged]
def create_product_page(product, folder, all_products):
    """Create product page - same as before"""
    # [Your existing create_product_page function here]
    pass

def create_about_page(df, folder):
    """Create about page - same as before"""
    # [Your existing create_about_page function here]
    pass

def create_qr_codes(df, folder):
    """Generate QR codes - same as before"""
    # [Your existing create_qr_codes function here]
    pass

if __name__ == "__main__":
    create_final_website()
    