from pyscript import document

non_metals = {
    "H":  {"name": "Hydrogen", "atomic_number": 1, "atomic_mass": 1.008},
    "HE": {"name": "Helium", "atomic_number": 2, "atomic_mass": 4.0026},
    "C":  {"name": "Carbon", "atomic_number": 6, "atomic_mass": 12.011},
    "N":  {"name": "Nitrogen", "atomic_number": 7, "atomic_mass": 14.007},
    "O":  {"name": "Oxygen", "atomic_number": 8, "atomic_mass": 16.0},
    "F":  {"name": "Fluorine", "atomic_number": 9, "atomic_mass": 18.998},
    "NE": {"name": "Neon", "atomic_number": 10, "atomic_mass": 20.180},
    "P":  {"name": "Phosphorus", "atomic_number": 15, "atomic_mass": 30.974},
    "S":  {"name": "Sulfur", "atomic_number": 16, "atomic_mass": 32.06},
    "CL": {"name": "Chlorine", "atomic_number": 17, "atomic_mass": 35.45},
    "AR": {"name": "Argon", "atomic_number": 18, "atomic_mass": 39.948},
    "SE": {"name": "Selenium", "atomic_number": 34, "atomic_mass": 78.971},
    "BR": {"name": "Bromine", "atomic_number": 35, "atomic_mass": 79.904},
    "KR": {"name": "Krypton", "atomic_number": 36, "atomic_mass": 83.798},
    "I":  {"name": "Iodine", "atomic_number": 53, "atomic_mass": 126.90},
    "XE": {"name": "Xenon", "atomic_number": 54, "atomic_mass": 131.29},
    "RN": {"name": "Radon", "atomic_number": 86, "atomic_mass": 222.0}
}

def search_element(event):
    input_element = document.getElementById("symbol-input")
    symbol = input_element.value.strip().upper()
    result_div = document.getElementById("result-display")
    
    fallback = {"name": "UNKNOWN", "atomic_number": "N/A", "atomic_mass": "N/A"}
    data = non_metals.get(symbol, fallback)
    
    success_html = f"""
    <div style='display: grid; grid-template-columns: repeat(2, 1fr); gap: 12px; font-family: monospace;'>
        <div><span style='color: #818cf8;'>SYMBOL:</span> {symbol.title()}</div>
        <div><span style='color: #818cf8;'>NAME:</span> {data['name']}</div>
        <div><span style='color: #818cf8;'>ATOMIC NO:</span> {data['atomic_number']}</div>
        <div><span style='color: #818cf8;'>MASS:</span> {data['atomic_mass']} u</div>
    </div>
    """
    
    error_html = f"<span class='error-text'>❌ ERROR: Symbol '{symbol}' not identified in the dictionary of Non-Metal Table.</span>"
    
    output_router = {
        True: success_html,
        False: error_html
    }
    
    is_valid_symbol = symbol in non_metals
    
    result_div.innerHTML = output_router[is_valid_symbol]

    # References for the Inline CSS Grid Structural Rules for Pyscript/Python Software

    # Python Software Foundation. (2026). Input and output: Fancier output formatting. Python 3.15.2 Documentation.
    # https://docs.python.org/3/tutorial/inputoutput.html

    # MDN Web Docs. (2026). CSS grid layout. Mozilla.
    # https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout
