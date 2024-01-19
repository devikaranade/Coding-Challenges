import argparse
import sys

def count_lines(file_content):
    lines = file_content.splitlines()
    return len(lines)

def count_bytes(file_content):
    return len(file_content.encode())

def count_words(file_content):
    words = file_content.split()
    return len(words)

def count_characters(file_content):
    return len(file_content)

def main():
    parser = argparse.ArgumentParser(description="Count Words, Lines, and Bytes from a File or Standard Input")
    parser.add_argument('filename', nargs='?', default=None, help='File to perform counting (default is standard input)')
    parser.add_argument('-l', '--lines', action='store_true', help='Count lines')
    parser.add_argument('-c', '--bytes', action='store_true', help='Count bytes')
    parser.add_argument('-w', '--words', action='store_true', help='Count words')
    parser.add_argument('-m', '--characters', action='store_true', help='Count characters')

    args = parser.parse_args()

    if args.filename:
        try:
            with open(args.filename, 'r', encoding='utf-8') as file:
                file_content = file.read()
        except FileNotFoundError:
            print(f"Error: File '{args.filename}' not found.")
            sys.exit(1)
    else:
        file_content = sys.stdin.read()

    if not any([args.lines, args.bytes, args.words, args.characters]):
        byte_count = count_bytes(file_content)
        line_count = count_lines(file_content)
        word_count = count_words(file_content)
        
        print(f"{line_count} {word_count} {byte_count} {args.filename or 'STDIN'}")
    else:
        if args.lines:
            line_count = count_lines(file_content)
            print(f"Line count: {line_count}")

        if args.bytes:
            byte_count = count_bytes(file_content)
            print(f"Byte count: {byte_count}")

        if args.words:
            word_count = count_words(file_content)
            print(f"Word count: {word_count}")

        if args.characters:
            character_count = count_characters(file_content)
            print(f"Character count: {character_count}")

if __name__ == "__main__":
    main()
