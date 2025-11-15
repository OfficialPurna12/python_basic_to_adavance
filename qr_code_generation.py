import qrcode
import os
import re
from datetime import datetime

def validate_email(email):
    """Validate email format"""
    if not email:
        return True  # Optional field
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_phone(phone):
    """Validate phone number (basic check)"""
    if not phone:
        return True  # Optional field
    # Remove common separators
    cleaned = re.sub(r'[\s\-\(\)]', '', phone)
    return cleaned.isdigit() and len(cleaned) >= 7

def validate_date(date_str):
    """Validate date in YYYYMMDD format"""
    if not date_str:
        return True  # Optional field
    try:
        datetime.strptime(date_str, '%Y%m%d')
        return True
    except ValueError:
        return False

def validate_url(url):
    """Validate URL format"""
    if not url:
        return True  # Optional field
    pattern = r'^https?://'
    if not re.match(pattern, url):
        return f"http://{url}"  # Add http:// if missing
    return url

def get_input(prompt, validator=None, error_msg="Invalid input", optional=False):
    """Get and validate user input"""
    while True:
        value = input(prompt).strip()
        
        if not value and optional:
            return ""
        
        if not value and not optional:
            print("⚠ This field is required. Please enter a value.")
            continue
        
        if validator:
            if validator == validate_url:
                result = validator(value)
                if isinstance(result, str):
                    return result
            elif validator(value):
                return value
            else:
                print(f"⚠ {error_msg}")
                continue
        
        return value

def generate_qr():
    print("\n" + "="*50)
    print("    CONTACT QR CODE GENERATOR")
    print("    (iPhone & Android Compatible)")
    print("="*50 + "\n")
    print("📝 Fill in your contact details (press Enter to skip optional fields)\n")

    # Collect and validate inputs
    name = get_input("Full Name*: ", optional=False)
    phone = get_input("Phone Number: ", validate_phone, "Invalid phone format (e.g., +1234567890)", optional=True)
    email = get_input("Email: ", validate_email, "Invalid email format", optional=True)
    address = get_input("Address: ", optional=True)
    company = get_input("Company Name: ", optional=True)
    company_address = get_input("Company Address: ", optional=True)
    company_id = get_input("Company ID: ", optional=True)
    website = get_input("Website: ", validate_url, "Invalid URL format", optional=True)
    dob = get_input("Date of Birth (YYYYMMDD): ", validate_date, "Invalid date format (use YYYYMMDD)", optional=True)

    # Build vCard with proper formatting
    # Note: iPhone displays FN (Full Name) and ORG (Organization) in the preview
    vcard_lines = [
        "BEGIN:VCARD",
        "VERSION:3.0",
        f"FN:{name}",  # This is shown as the main name
        f"N:{name.split()[-1] if ' ' in name else name};{name.split()[0] if ' ' in name else ''};;;"  # Structured name
    ]
    
    if phone:
        vcard_lines.append(f"TEL;TYPE=CELL:{phone}")  # Added TYPE for better categorization
    if email:
        vcard_lines.append(f"EMAIL;TYPE=INTERNET:{email}")
    if address:
        vcard_lines.append(f"ADR;TYPE=HOME:;;{address};;;")
    if company:
        vcard_lines.append(f"ORG:{company}")  # This shows in iPhone preview
        if company_address:
            vcard_lines.append(f"ADR;TYPE=WORK:;;{company_address};;;")
    if website:
        vcard_lines.append(f"URL:{website}")
    if dob:
        vcard_lines.append(f"BDAY:{dob}")
    
    # Add custom fields as NOTE
    notes = []
    if company_id:
        notes.append(f"Company ID: {company_id}")
    
    if notes:
        vcard_lines.append(f"NOTE:{' | '.join(notes)}")
    
    vcard_lines.append("END:VCARD")
    vcard = "\n".join(vcard_lines)

    # Create output directory
    output_dir = "qrcodes"
    os.makedirs(output_dir, exist_ok=True)

    # Generate filename
    safe_name = re.sub(r'[^\w\s-]', '', name).strip().replace(' ', '_')
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(output_dir, f"{safe_name}_contact_{timestamp}.png")

    # Generate QR code with better quality
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
        box_size=10,
        border=4,
    )
    qr.add_data(vcard)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

    # Success message
    print("\n" + "="*50)
    print("✔ QR Code Generated Successfully!")
    print("="*50)
    print(f"📁 Location: {filename}")
    print(f"📱 Scan with any smartphone camera to save contact")
    print("\n💡 Tip: The QR code works with iPhone, Android, and most QR readers\n")

if __name__ == "__main__":
    try:
        generate_qr()
    except KeyboardInterrupt:
        print("\n\n❌ Operation cancelled by user")
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        print("Please try again or report this issue.")