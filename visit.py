import tkinter as tk
from tkinter import messagebox

# Data dictionary for districts and places
district_visited_place_in_nepal = {
    "Kathmandu": ["Thamel", "Zoo", "Boudha", "Pashupati Temple", "Durbar Square"],
    "Pokhara": ["Fewa Lake", "Lake Side", "Tal Barahi Temple", "Gupteshwor Mahadev Cave", "Devi's Fall", "World Peace Pagoda"],
    "Rukum": ["Shital Pokhari", "Kankre Bihar", "Sahit Smriti Park", "Digree Temple", "Viral Bridge", "Kamal Pokhari"],
    "Mustang": ["Muktinath Temple", "Kagbeni", "Jomsom", "Lo Manthang", "Kaligandaki River", "Dhakmar", "Marpha Monastery", "Marpha"],
    "Lumbini": ["World Peace Pagoda", "Maya Devi Temple", "Bardiya National Park", "Thai Monastery", "Birthplace of Gautam Buddha", "Myanmar Golden Temple", "Bageswari Mandir"],
    "Ilam": ["Seti Devi Temple", "Singabahini Temple", "Sandakpur", "Chhintapu", "Phikal Bazaar"],
    "Dolpa": ["Shey Phoksundo National Park", "Shey Gompa", "Putha Hiunchuli", "Great Himalayas", "Churen Himal", "Dho", "Tinje", "Chaakra"]
}

# Adding and updating districts
district_visited_place_in_nepal["Solukhumbu"] = ["Sagarmatha"]

# Tkinter GUI Application
def search_places():
    district = entry_district.get().capitalize()
    if district in district_visited_place_in_nepal:
        places = "\n".join(district_visited_place_in_nepal[district])
        result_label.config(text=f"Visiting places in {district}:\n{places}", fg="green")
    else:
        result_label.config(text="Sorry, district not available now.", fg="red")

# Main GUI Window
root = tk.Tk()
root.title("Tourism in Nepal")
root.geometry("500x400")
root.configure(bg="#f0f8ff")

# Title Label
title_label = tk.Label(root, text="Nepal Tourism District Explorer", font=("Helvetica", 16, "bold"), bg="#4682b4", fg="white", pady=10)
title_label.pack(fill=tk.X)

# Input Section
frame_input = tk.Frame(root, bg="#f0f8ff")
frame_input.pack(pady=20)

input_label = tk.Label(frame_input, text="Enter Your Favorite Tourism District:", font=("Arial", 12), bg="#f0f8ff")
input_label.grid(row=0, column=0, padx=5, pady=5)

entry_district = tk.Entry(frame_input, font=("Arial", 12), width=20)
entry_district.grid(row=0, column=1, padx=5, pady=5)

search_button = tk.Button(frame_input, text="Search", font=("Arial", 12), bg="#4682b4", fg="white", command=search_places)
search_button.grid(row=0, column=2, padx=5, pady=5)

# Result Section
result_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f8ff", wraplength=450)
result_label.pack(pady=20)

# Footer
footer_label = tk.Label(root, text="Explore the beauty of Nepal!", font=("Helvetica", 10, "italic"), bg="#4682b4", fg="white", pady=5)
footer_label.pack(side=tk.BOTTOM, fill=tk.X)

# Start the main event loop
root.mainloop()