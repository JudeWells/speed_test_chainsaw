import os
import linecache
import shutil

def get_total_lines(file_path):
    with open(file_path) as f:
        return sum(1 for _ in f)


def extract_lines(file_path, block_size, total_lines_to_extract):
    # total_lines = get_total_lines(file_path)
    total_lines = 188_900_000
    # Calculate how many blocks to extract and the step size between blocks
    blocks_to_extract = total_lines_to_extract // block_size
    step = total_lines // blocks_to_extract

    extracted_lines = []

    for i in range(blocks_to_extract):
        start_line = i * step + 1
        end_line = start_line + block_size
        for line_number in range(start_line, end_line):
            extracted_lines.append(linecache.getline(file_path, line_number))

    return extracted_lines

def create_sample_file(outpath):
    file_path = "/SAN/bioinf/afdb_domain/datasets/index/all_models_unique.zip_index"
    block_size = 40
    total_lines_to_extract = 5000

    extracted_lines = extract_lines(file_path, block_size, total_lines_to_extract)
    print('Len extracted lines: ', len(extracted_lines))
    # Write extracted lines to a new file
    with open(outpath, 'w') as f:
        for line in extracted_lines:
            f.write(line)
    print('Writing lines complete')

def main():
    BASE_DIR = '/SAN/cath/cath_v4_3_0/alphafold/chainsaw_on_alphafold/speed_test_chainsaw'
    os.chdir(BASE_DIR)
    filelist_name = "sampled_pdbs.txt"
    zip_dir = '/SAN/bioinf/afdb_domain/zipfiles'
    sampled_zip_dir = os.path.join(BASE_DIR, 'sampled_zips')
    os.makedirs(sampled_zip_dir, exist_ok=True)
    if not os.path.exists(filelist_name):
        create_sample_file(filelist_name)
    with open(filelist_name) as f:
        lines = f.readlines()
    print('Sucessfully opened sampled lines file')
    file_names = list(set([l.split()[2] for l in lines]))
    for fname in file_names:
        # copy file to new location
        shutil.copy(os.path.join(zip_dir, fname), sampled_zip_dir)
        if os.path.exists(sampled_zip_dir, fname):
            print('Successfully copied file: ', fname)



if __name__ == "__main__":
    main()