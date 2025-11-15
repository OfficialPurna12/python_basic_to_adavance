import qrcode
import os

def generate_qr():
    print("\n=== CONTACT QR (iPhone Supported) ===")

    name = input("Enter your full name: ")
    phone = input("Enter your phone number: ")
    email = input("Enter your email: ")
    address = input("Enter your address: ")
    company = input("Enter your company name: ")
    company_address = input("Enter your company address : ")
    company_id = input("Enter your company Id : ")
    website = input("Enter your website: ")
    dob = input("Enter your date of birth (YYYYMMDD): ")

    # iPhone readable vCard format
    vcard = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL:{phone}
EMAIL:{email}
ADR:;;{address};;;
ORG:{company}
URL:{website}
BDAY:{dob}
COP_ID : {company_id}
COP_Address : {company_address}
END:VCARD
"""

    output_dir = "qrcodes"
    os.makedirs(output_dir, exist_ok=True)

    safe_name = name.replace(" ", "_")
    filename = os.path.join(output_dir, f"{safe_name}_contact_qr.png")

    img = qrcode.make(vcard)
    img.save(filename)

    print(f"\n✔ iPhone-Compatible Contact QR Generated!")
    print(f"📁 Saved at: {filename}")

generate_qr()
