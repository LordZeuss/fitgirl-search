from bs4 import BeautifulSoup
import requests
import webbrowser

def get_magnet_links(url):
    request = requests.get(url)
    page = BeautifulSoup(request.text, "html.parser")
    magnet_links = page.find_all("a", href=lambda href: href and href.startswith("magnet:"))
    return magnet_links

def get_torrent_file_link(url):
    request = requests.get(url)
    page = BeautifulSoup(request.text, "html.parser")
    torrent_links = page.find_all("a", string=".torrent file only")
    return torrent_links[0].get('href') if torrent_links else None

def present_question_options(options):
    print("\nChoose one of the following questions:")
    for index, question in enumerate(options, start=1):
        print(f"{index}. {question}")
    selected_question = input("Select a question by entering its number: ")
    return selected_question

search = input("Search for a Game: ")
url = f"https://fitgirl-repacks.site/?s={search}"

request = requests.get(url)
page = BeautifulSoup(request.text, "html.parser")

entry_titles = page.find_all(class_="entry-title")

options = []

for index, entry_title in enumerate(entry_titles, start=1):
    link = entry_title.find("a", rel="bookmark")
    if link:
        text = link.text
        options.append((text, link.get('href')))
        print(f"{index}. {text}")

selected_option = input("Select an option by entering its number: ")

try:
    selected_index = int(selected_option)
    if 1 <= selected_index <= len(options):
        selected_text, selected_url = options[selected_index - 1]

        question_options = [
            "View Magnet Link(s)",
            "Download Torrent File",
            "Open Webpage"
        ]

        selected_question = present_question_options(question_options)

        try:
            selected_question_index = int(selected_question)
            if selected_question_index == 1:
                magnet_links = get_magnet_links(selected_url)
                for index, magnet_link in enumerate(magnet_links[:2], start=1):
                    href = magnet_link.get('href')
                    print(f"{'1337x' if index == 1 else 'RuTor'} Magnet Link: {href}")
                    if index < len(magnet_links[:2]):
                        print("\n")
            elif selected_question_index == 2:
                torrent_link = get_torrent_file_link(selected_url)
                if torrent_link:
                    print(f"Torrent File Link: {torrent_link}")
                    webbrowser.open(torrent_link)
                else:
                    print("No torrent download link found on the page.")
            elif selected_question_index == 3:
                if selected_url.startswith("http"):
                    webbrowser.open(selected_url)
                else:
                    print("Cannot open game page.")
            else:
                print("Invalid option number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    else:
        print("Invalid option number.")
except ValueError:
    print("Invalid input. Please enter a valid number.")

print("")
exit = input("Press enter to exit:")