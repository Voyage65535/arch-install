#!/usr/bin/env python

import src
from src import home, root, github_raw
from shutil import copy
from os import system, makedirs
from sys import stdout, stderr
from sh import pacman, sh, wget, sed, systemctl
from sh.contrib import git

def color():
    for i in src.color:
        wget(src.color[i], O=i, _out=stdout, _err=stderr)
        system('chmod a+x '+i)
    pacman(S='pinfo', _in='y', _out=stdout, _err=stderr)

def zsh():
    system('wget https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O - | sh')
    git.clone('https://github.com/zsh-users/zsh-completions', '/root/.oh-my-zsh/custom/plugins/zsh-completions', _out=stdout, _err=stderr)
    home('.zshrc')

def vim():
    git.clone('https://github.com/amix/vimrc.git', '/root/.vim_runtime', _out=stdout, _err=stderr)
    sh('/root/.vim_runtime/install_awesome_vimrc.sh', _out=stdout, _err=stderr)

def pkgmgr():
    root('pacman.conf')
    pacman('-Syy', _out=stdout, _err=stderr)
    pacman(S='archlinuxcn-keyring', _in='y', _out=stdout, _err=stderr)

def sshd():
    pacman(S='openssh', _in='y', _out=stdout, _err=stderr)
    sed('s/#PermitRootLogin prohibit-password/PermitRootLogin yes/g', i='/etc/ssh/sshd_config')
    systemctl('enable', 'sshd')
    systemctl('start', 'sshd')

def nfsrv():
    pacman(S='nfs-utils', _in='y', _out=stdout, _err=stderr)
    makedirs('/srv/nfs4')
    with open('/etc/exports', 'a') as f:
        f.write('\n  /srv/nfs4        192.168.0.*(rw,sync,fsid=0,no_wdelay,no_root_squash,no_subtree_check)\n\n')
    systemctl('enable', 'nfs-server')
    systemctl('start', 'nfs-server')

def misc():
    wget(github_raw+'racaljk/hosts/master/hosts', O='/etc/hosts', _out=stdout, _err=stderr)


if __name__ == '__main__':
    color()
    zsh()
    vim()
    pkgmgr()
    sshd()
    nfsrv()
    #ssocks()
    #kcptun()
    misc()

