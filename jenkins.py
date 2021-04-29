#! /usr/bin/env python3
import argparse
import os
import subprocess
import shutil
import sys

#configure Argparse
parser = argparse.ArgumentParser(description='parser alon')
parser.add_argument('--generator', '-g', help='build generator')
parser.add_argument('--folder', '-f', help='Name of build folder')
parser.add_argument('--btype', '-b', help='Type of build')
parser.add_argument('--install-dir', '-i', help='Custom install directory')
args = parser.parse_args()


#main function that runs in the command line
def do_call(args):

    args2 = ' '.join(args)
    # oneline = ''
    # for i in args:
    #     oneline += '{} '.format(i)

    print('[{}]>{}'.format(os.getcwd(), args2))
    try:
        subprocess.run(args, env=os.environ)
    except subprocess.CalledProcessError as error:
        print(error)
        print(error.output)
        sys.exit(1)


# install_dir = args.install_dir
buildtype = args.btype
folder = args.folder
# generator = args.ger
# print("Folder enterd: ",folder)

print("""#////////////////////////////////////////////////""")

#checks for install and build dircetories and removes //////////////////
if os.path.exists('build'):
    shutil.rmtree('build')


def run_build(folder, buildtype, install_dir):

    print('-' * 80)
    args = ['cmake', '-S', '.']

    if install_dir:
        args += ['-DCMAKE_INSTALL_PREFIX={}'.format(install_dir)]
    else:
        print("install dir not specified")
        print('-' * 80)
        sys.exit()

    if folder:
        args += ['-B{}'.format(folder)]
    else:
        print("Build folder not specified")
        print('-' * 80)
        sys.exit()

    if buildtype or buildtype == 'None':
        args += ['-DCMAKE_BUILD_TYPE={}'.format(buildtype)]
    else:
        print("Build TYPE not specified")
        print('-' * 80)
        sys.exit()

    #configuring CMAKE
    do_call(args)

    args = []
    args = [
        'cmake', '--build', folder, '--config', buildtype, '--target',
        'install'
    ]

    #building CMAKE
    do_call(args)


#//////////////////////////////////////////////////////////
run_build(folder, buildtype, args.install_dir)
