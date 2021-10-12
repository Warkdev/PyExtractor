import logging
import os
from pywowlib import WoWVersionManager, WoWVersions

class ClientHelper():
    @staticmethod
    def get_build_version(path):
        exe_names = ['WoW.exe', 'Wow.exe', 'wow.exe', 'World of Warcraft.exe']
        str_lookup = "(build "
        map_version = {
            '5875': WoWVersions.CLASSIC,
            '6005': WoWVersions.CLASSIC,
            '6141': WoWVersions.CLASSIC,
            '8606': WoWVersions.TBC,
            '12340': WoWVersions.WOTLK,
            '15595': WoWVersions.CATA,
            '18414': WoWVersions.MOP,
            '20574': WoWVersions.WOD,
            '21742': WoWVersions.LEGION,
            '31478': WoWVersions.BFA,
            '37130': WoWVersions.SHADOWLANDS,
            '40441': WoWVersions.NEW_CLASSIC,
            '40488': WoWVersions.NEW_TBC_CLASSIC
        }

        for exe in exe_names:
            path_file = "{}/{}".format(path, exe)
            if os.path.isfile(path_file):
                logging.info("Found matching Executable file: {}".format(path_file))
                with open(path_file, "rb") as exe_file:
                    buffer = exe_file.read(16384)
                    while buffer:
                        decoded = buffer.decode(encoding='ansi')
                        index = decoded.find(str_lookup)
                        if index != -1:
                            #logging.debug("Found matching string {}".format(buffer))
                            temp = decoded[index:(index+25)]
                            end = temp.find(")")
                            build = temp[len(str_lookup):end]
                            logging.info("Found build version: {}".format(build))
                            WoWVersionManager().set_client_version(map_version.get(build, WoWVersions.UNKNOWN))
                            break
                        buffer = exe_file.read(16384)
                    exe_file.close()
                    break
        else:
            logging.info("No Executable found!")