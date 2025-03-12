
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_content = f.read()
        return file_content

def main():
    print(get_book_text("./books/frankenstein.txt"))



main()