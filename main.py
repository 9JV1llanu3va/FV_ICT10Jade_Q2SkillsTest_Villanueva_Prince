from pyscript import document

non_metals = {
    "H":  ("Hydrogen", 1, 1.008),
    "HE": ("Helium", 2, 4.0026),
    "C":  ("Carbon", 6, 12.011),
    "N":  ("Nitrogen", 7, 14.007),
    "O":  ("Oxygen", 8, 16.0),
    "F":  ("Fluorine", 9, 18.998),
    "NE": ("Neon", 10, 20.180),
    "P":  ("Phosphorus", 15, 30.974),
    "S":  ("Sulfur", 16, 32.06),
    "CL": ("Chlorine", 17, 35.45),
    "AR": ("Argon", 18, 39.948),
    "SE": ("Selenium", 34, 78.971),
    "BR": ("Bromine", 35, 79.904),
    "KR": ("Krypton", 36, 83.798),
    "I":  ("Iodine", 53, 126.90),
    "XE": ("Xenon", 54, 131.29),
    "RN": ("Radon", 86, 222.0)
}

def periodic(e):
    input_element = document.getElementById("symbol-input")
    result_div = document.getElementById("result-display")
    
    element_Name = input_element.value.strip().upper()
    
    var2 = non_metals.get(element_Name, ("Element not found", "-", "-"))
    

    success_html = f"""
    <div style='display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; font-family: monospace;'>
        <div><span style='color: #818cf8;'>Symbol:</span> {element_Name.title()}</div>
        <div><span style='color: #818cf8;'>Element:</span> {var2[0]}</div>
        <div><span style='color: #818cf8;'>Atomic Number:</span> {var2[1]}</div>
        <div><span style='color: #818cf8;'>Atomic Mass:</span> {var2[2]} u</div>
    </div>
    """
    
    error_html = f"""
    <div style='font-family: monospace;'>
        <div class='error-text'>❌ Symbol: {element_Name}</div>
        <div style='color: #6b7280; margin-top: 4px;'>Result: {var2[0]}</div>
    </div>
    """
    
   
    router = {
        True: success_html,
        False: error_html
    }
    
    is_valid = element_Name in non_metals
    result_div.innerHTML = router[is_valid]
    
    # References for the Inline CSS Grid Structural Rules for Pyscript/Python Software

    # Python Software Foundation. (2026). Input and output: Fancier output formatting. Python 3.15.2 Documentation.
    # https://docs.python.org/3/tutorial/inputoutput.html

    # MDN Web Docs. (2026). CSS grid layout. Mozilla.
    # https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout