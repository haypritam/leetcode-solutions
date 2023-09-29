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
    for folder_name in os.listdir(folder_path):
        problem_id = folder_name.split('-')[0]
        p_link=folder_name.split("-")[1]
        problem_link = f"https://leetcode.com/problems/{p_link.lower().replace('_', '-')}"

        solutions = []
        link_name=folder_name.split("-")[1].lower()
        solution_link=f"[C++]({subfolder}/{folder_name}/{link_name}.cpp)"
        solutions.append(solution_link)
        solution_link=f"[javascript]({subfolder}/{folder_name}/{link_name}.js)"
        solutions.append(solution_link)
        solution_link=f"[Python]({subfolder}/{folder_name}/{link_name}.py)"
        solutions.append(solution_link)
        solution_link=f"[Rust]({subfolder}/{folder_name}/{link_name}.rs)"
        solutions.append(solution_link)

        solutions_str = " &bull; ".join(solutions)
        table.append(f"| {problem_id} | [{p_link.replace('_', ' ')}]({problem_link}) | {solutions_str} |")

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
