import logging
import argparse
from helper.client import ClientHelper
from pywowlib.archives.wow_filesystem import WoWFileData
from pywowlib import WoWVersionManager, WoWVersions

def set_logging():
    logging.basicConfig(format='[%(asctime)s] [PID:%(process)d TID:%(thread)d] [%(levelname)s] [%(name)s] [%(funcName)s():%(lineno)s] %(message)s', level=logging.DEBUG)

def set_arguments():
    parser = argparse.ArgumentParser(description="Extract game data from client to be used server-side")
    parser.add_argument('--extract-map', '-e', help="Extract Maps from the game archives", default=False, required=False, action='store_true')
    parser.add_argument('--extract-dbc', '-d', help="Extract DBCs from the game archives", default=False, required=False, action='store_true')
    parser.add_argument('--generate-vmap', '-v', help="Generate Vmaps from the game archives", default=False, required=False, action='store_true')
    parser.add_argument('--generate-mmap', '-m', help="Generate Mmaps from the game archives", default=False, required=False, action='store_true')
    return parser.parse_args()

def print_banner():
    logging.info("")
    logging.info("        __  __      _  _  ___  ___  ___      ")
    logging.info("       |  \\/  |__ _| \\| |/ __|/ _ \\/ __|  ")
    logging.info("       | |\\/| / _` | .` | (_ | (_) \\__ \\  ")
    logging.info("       |_|  |_\\__,_|_|\\_|\\___|\\___/|___/ ")
    logging.info("")
    logging.info("  ________________________________________________")
    logging.info("    For help and support please visit:            ")
    logging.info("    Website / Forum / Wiki: https://getmangos.eu  ")
    logging.info("  ________________________________________________")

def print_parameters(args):
    logging.info("------ Extractor Options ------")
    logging.info("WoW version: {}".format(WoWVersions.get_version_name(WoWVersionManager().client_version)))
    logging.info("----- General settings -----")
    #logging.info("Client Path: %s", _clientPath)
    #logging.info("Output Path: %s", _outputPath)
    logging.info("----- Map extractor arguments -----")
    logging.info("Extract Maps: {}".format(vars(args).get('extract_map', False)))
    logging.info("Extract DBCs: {}".format(vars(args).get('extract_dbc', False)))
    logging.info("----- VMap generator arguments ----")
    logging.info("Generate VMaps: {}".format(vars(args).get('generate_vmap', False)))
    logging.info("----- MMap generator arguments ----")
    logging.info("Generate Mmaps: {}".format(vars(args).get('generate_mmap', False)))
    logging.info("")

def main():
    set_logging()
    args = set_arguments()
    print_banner()
    wow_path="D:\\Users\\Cedric\\Dev\\client\\CLASSIC"
    ClientHelper.get_build_version(path=wow_path) # Sets the WoW.exe version
    if WoWVersionManager().client_version != WoWVersions.UNKNOWN:
        print_parameters(args)
    #file_data = WoWFileData(wow_path=wow_path, project_path="")
    #print(file_data.files)

    #for mpq, flag in file_data.files:
        #print(mpq.namelist())
    #    pass

if __name__ == "__main__":
    main()