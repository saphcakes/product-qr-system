import pandas as pd

def diagnose_csv():
    print("🔍 Diagnosing your CSV file...")
    print("=" * 50)
    
    try:
        # Read CSV with different encoding options if needed
        try:
            df = pd.read_csv('products.csv')
        except UnicodeDecodeError:
            df = pd.read_csv('products.csv', encoding='latin-1')
        
        print("📊 CSV File Structure:")
        print(f"Number of rows: {len(df)}")
        print(f"Number of columns: {len(df.columns)}")
        print(f"Column names: {df.columns.tolist()}")
        
        print("\n🔍 First 2 rows of data:")
        print("=" * 40)
        for col in df.columns:
            print(f"{col}: {df.iloc[0][col]}")
        
        print("\n📋 All column details:")
        print("=" * 40)
        for i, col in enumerate(df.columns):
            sample_value = str(df.iloc[0][col])[:50] if pd.notna(df.iloc[0][col]) else "EMPTY"
            print(f"{i+1}. '{col}' → '{sample_value}...'")
            
    except FileNotFoundError:
        print("❌ Error: products.csv file not found!")
        print("💡 Please make sure products.csv is in the same folder")
    except Exception as e:
        print(f"❌ Error reading CSV: {e}")

if __name__ == "__main__":
    diagnose_csv()