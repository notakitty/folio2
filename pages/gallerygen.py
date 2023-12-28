# Python script to generate HTML for image gallery

def create_html_line(filename, directory):
    """Generate an HTML line for an image."""
    return f'    <a href="{directory}/{filename}">\n        <img src="{directory}/{filename}" alt="{filename.split(".")[0]}">\n    </a>'

def main():
    directory = "/folio2/assets/illustration"
    input_file = "illustration.txt"  # File containing the list of image filenames
    output_file = "gallery.html"     # Output HTML file

    with open(input_file, 'r') as file:
        filenames = file.readlines()

    with open(output_file, 'w') as file:
        file.write('<div id="lightgallery">\n')
        for filename in filenames:
            filename = filename.strip()  # Remove any leading/trailing whitespace
            html_line = create_html_line(filename, directory)
            file.write(html_line + "\n")
        file.write('</div>')

if __name__ == "__main__":
    main()
