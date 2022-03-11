import re
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_path", type=str)
    parser.add_argument("output_path", type=str)
    args = parser.parse_args()

    tc = []
    with open(args.input_path, 'r') as f:
        for l in f:
            print(l.strip())
            m = re.match("(\w+)\(([\w|\.]+)\)", l.strip())
            case_name = m.group(1)
            class_name = m.group(2)
            tc.append(class_name + "::" + case_name)

    with open(args.output_path, 'w') as f:
        f.write("\n".join(tc))