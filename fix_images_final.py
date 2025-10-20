import pandas as pd

def use_reliable_images():
    df = pd.read_csv('products.csv')
    
    reliable_images = {
        101: "https://images.unsplash.com/photo-1586190848861-99aa4a171e90?w=500&h=500&fit=crop&auto=format",
        102: "https://images.unsplash.com/photo-1558961363-fa8fdf82db35?w=500&h=500&fit=crop&auto=format",
        103: "https://images.unsplash.com/photo-1563379926898-05f4575a45d8?w=500&h=500&fit=crop&auto=format",
        104: "https://images.unsplash.com/photo-1551024506-0bccd828d307?w=500&h=500&fit=crop&auto=format",
        105: "https://images.unsplash.com/photo-1470337458703-46ad1756a187?w=500&h=500&fit=crop&auto=format",
        106: "https://images.unsplash.com/photo-1570197788417-0e82375c9371?w=500&h=500&fit=crop&auto=format",
        107: "https://images.unsplash.com/photo-1488477181946-6428a0291777?w=500&h=500&fit=crop&auto=format",
    }
    
    for index, row in df.iterrows():
        pid = row['product_id']
        if pid in reliable_images:
            df.at[index, 'image_url'] = reliable_images[pid]
    
    df.to_csv('products.csv', index=False)
    print("✅ Updated with reliable image URLs")

use_reliable_images()
