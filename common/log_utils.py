import os


def get_log_path(log_folder, main_file):
    return os.path.join(log_folder, os.path.basename(main_file).replace('.py', '.log'))
