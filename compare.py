import argparse

def main():
    #print("Hello World!")

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('file', nargs='+',
                        help='file to compare')
    parser.add_argument('--sum', dest='accumulate', action='store_const',
                        const=sum, default=max,
                        help='sum the integers (default: find the max)')

    args = parser.parse_args()

    print(args.file)


if __name__ == "__main__":
    main()
