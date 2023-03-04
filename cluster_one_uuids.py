import argparse
import json
import os
import struct
import traceback
import uuid


"""
@folder_path is the path where the onenote files to be clustered are stored.
Returns a dictionary.
"""
def cluster_files(folder_path):
    clusters = {}
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if not os.path.isfile(file_path):
            continue

        file_uuid = extract_uuid_from_file(file_path)
        if file_uuid not in clusters:
            clusters[file_uuid] = [file_name]
        else:
            clusters[file_uuid].append(file_name)
    return clusters


"""
Returns a string representing the uid or 'NOT_ONE_FILE'/'EXCEPTION'.
"""
def extract_uuid_from_file(file_path):
    try:
        with open(file_path, 'rb') as fh:
            uuid_file_type, uuid_file = struct.unpack('<16s16s', fh.read(32))
            uuid_file_type = uuid.UUID(bytes_le=uuid_file_type)
            if str(uuid_file_type) not in ('7b5c52e4-d88c-4da7-aeb1-5378d02996d3', 
                                           '43ff2fa1-efd9-4c76-9ee2-10ea5722765f'):
                return 'NOT_ONE_FILE'
            return str(uuid.UUID(bytes_le=uuid_file))
    except:
        print('Error while parsing file {}. Trace = {}.'.format(file_path, traceback.format_exc()))
        return 'EXCEPTION'


def _parse_commandline_args():
    parser = argparse.ArgumentParser(description='Cluster onenote files via UUIDs.')
    parser.add_argument("-f", "--folder", action="store", default='.', 
                        help="Folder containing files to cluster", required=True, type=str)

    return parser.parse_args()


def main():
    args = _parse_commandline_args()
    dict_clusters = cluster_files(args.folder)
    print('Clusters: \n{}'.format(json.dumps(dict_clusters, indent=4)))


if __name__ == '__main__':
    main()
