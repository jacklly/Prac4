"""Use project class for usable system"""

from project import Project
import datetime


def main():
    """Main program"""
    choice = ""
    projects_list = []
    while choice != "Q":
        # While not quitting
        choice = display_menu()
        if choice == "L":
            # Load projects
            load_projects(projects_list)
        elif choice == "S":
            # Save projects
            save_projects(projects_list)
        elif choice == "D":
            # Display projects
            display_projects(projects_list)
        elif choice == "F":
            # Filter projects
            filter_projects(projects_list)
        elif choice == "A":
            # Add a project
            add_project(projects_list)
        elif choice == "U":
            # Update project
            update_project(projects_list)
        else:
            if choice != "Q":
                print("Please enter a valid option!")


def display_menu():
    """Display interactive menu"""
    choice = input("- (L)oad projects\n"
                   "- (S)ave projects\n"
                   "- (D)isplay projects\n"
                   "- (F)ilter projects\n"
                   "- (A)dd a new project\n"
                   "- (U)pdate project\n"
                   "- (Q)uit\n"
                   ">>>")
    choice = choice.upper()
    return choice


def load_projects(projects_list):
    """Load a set of projects from a file"""
    file = input("File to load from: ")
    with open(file, "r", encoding="utf-8-sig") as in_file:
        text = in_file.read()
        text = text.split("\n")
        for line in text:
            line = line.split("\t")
            projects_list.append(Project(line[0], line[1], line[2], line[3], line[4]))


def save_projects(projects_list):
    """Save projects to file"""
    file = input("File to save to: ")
    with open(file, "w", encoding="utf-8-sig") as out_file:
        for project in projects_list:
            print(f"{project.name}\t{project.date}\t{project.priority}\t{project.cost_estimate}\t"
                  f"{project.completion_percentage}", file=out_file)


def display_projects(projects_list):
    """Print projects"""
    print("Incomplete Projects:")
    for project in projects_list:
        if not project.completed():
            print(project)
    print("Completed Projects:")
    for project in projects_list:
        if project.completed():
            print(project)


def filter_projects(projects_list):
    """Display projects after a certain date"""
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    for project in projects_list:
        project_date = datetime.datetime.strptime(project.date, "%d/%m/%Y").date()
        if project_date > date:
            print(project)


def add_project(projects_list):
    """Add a project to the list"""
    print("Let's add a new project")
    name = input("Name: ")
    start = input("Start date (dd/mm/yyyy): ")
    priority = input("Priority: ")
    cost = input("Cost estimate: ")
    percent = input("Percent complete: ")
    projects_list.append(Project(name, start, priority, cost, percent))


def update_project(projects_list):
    """Update a projects completion"""
    for i, project in enumerate(projects_list):
        print(f"{i} {project}")
    project_choice = int(input("Project choice: "))
    print(projects_list[project_choice])
    percentage = input("New percentage: ")
    if percentage != "":
        projects_list[project_choice].completion_percentage = percentage
    priority = input("New priority: ")
    if priority != "":
        projects_list[project_choice].priority = priority


main()
