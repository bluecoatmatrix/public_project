import argparse


def main():
    parser = argparse.ArgumentParser(description="Patient information grouping")
    parser.add_argument("-f", "--file", type=argparse.FileType("r"), help="Input file for patient", required=True)
    args = parser.parse_args()

    patient_list = []
    name_map = {}

    try:
        line = args.file.readline()
        while line:
            patient_list.append(line)
            line = args.file.readline()
        args.file.close()
    except IOError as e:
        print("There is an error to read file" + e)

    for patient in patient_list:
        patient_name = get_name(patient)
        if patient_name in name_map.keys():
            name_map[patient_name] += patient
        else:
            name_map[patient_name] = patient

    group_id = 0
    for name in name_map.keys():
        print("{}:\n{}".format(group_id, name_map[name].rstrip("\n")))
        group_id += 1


def get_name(info):
    # fetch and format patient name
    info_list = info.split(",")
    if len(info_list) != 4:
        raise Exception("The patient information is invalid!!!")

    full_name = info_list[1]
    last_first = full_name.split("^")
    if len(last_first) < 1 or len(last_first) > 3:
        raise Exception("The patient name is invalid!!!")

    name = last_first[0].lower()+last_first[1].lower()
    return name


if __name__ == "__main__":
    main()
