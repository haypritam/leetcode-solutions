import os
import markdown

# Define the subfolder names
subfolders = ["easy", "medium", "hard"]

# Initialize the markdown content
markdown_content = []

# Helper function to get problem name from folder/file name
def get_problem_name(filename):
    return filename.split('.')[0].replace('_', ' ').title()

# Helper function to get the language from a filename
def get_language(filename):
    ext = filename.split('.')[-1]
    if ext == 'cpp':
        return 'C++'
    elif ext == 'py':
        return 'Python'
    elif ext == 'js':
        return 'JavaScript'
    elif ext == 'rs':
        return 'Rust'
    else:
        return ext.upper()

# Generate the table for a given subfolder
def generate_table(subfolder):
    table = []
    table.append("| LeetCode ID | Problem | Solutions |")
    table.append("| ----------- | ------- | ---------- |")

    folder_path = os.path.join(subfolder)
    print(f"Checking folder: {folder_path}")  # Debug statement
    try:
        for folder_name in os.listdir(folder_path):
            print(f"Processing folder: {folder_name}")  # Debug statement
            problem_id = folder_name.split('-')[0]
            p_link = folder_name.split('-')[1]
            problem_link = f"https://leetcode.com/problems/{p_link.lower().replace('_', '-')}"

            solutions = []
            link_name = folder_name.split('-')[1].lower()
            extensions = ['cpp', 'js', 'py', 'rs']
            languages = ['C++', 'JavaScript', 'Python', 'Rust']
            
            for ext, lang in zip(extensions, languages):
                solution_link = f"[{lang}]({subfolder}/{folder_name}/{link_name}.{ext})"
                solutions.append(solution_link)

            solutions_str = " &bull; ".join(solutions)
            table.append(f"| {problem_id} | [{p_link.replace('_', ' ')}]({problem_link}) | {solutions_str} |")
    except Exception as e:
        print(f"An error occurred: {e}")

    return "\n".join(table)

# Generate tables for all subfolders
for subfolder in subfolders:
    markdown_content.append(f"## {subfolder.capitalize()} Problems\n")
    markdown_content.append(generate_table(subfolder))
    markdown_content.append("\n")

# Save the README.md file in the same folder as the script
with open("README.md", "w") as readme_file:
    readme_file.write("\n".join(markdown_content))

# Convert the markdown to HTML if needed
html_content = markdown.markdown("\n".join(markdown_content))

print("README.md has been generated successfully.")
