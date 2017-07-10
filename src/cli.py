#!/usr/bin/env python

import data
from data import github_raw
from shutil import copy
from os import system, makedirs
from os.path import expanduser
from sys import stdout, stderr
from sh import pacman, sh, wget, sed, systemctl
from sh.contrib import git

def color():
    for i in data.color:
        wget(data.color[i], O=i, _out=stdout, _err=stderr)
        system('chmod a+x '+i)

def zsh():
    system('wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O - | sh')
    git.clone('https://github.com/zsh-users/zsh-completions', expanduser('~/.oh-my-zsh/custom/plugins/zsh-completions'), _out=stdout, _err=stderr)
    copy(data.zshrc, '~/.zshrc')

def vim():
    git.clone('https://github.com/amix/vimrc.git', expanduser('~/.vim_runtime'), _out=stdout, _err=stderr)
    sh(expanduser('~/.vim_runtime/install_awesome_vimrc.sh'), _out=stdout, _err=stderr)

def pkgmgr():
    copy(data.pacman, '/etc/pacman.conf')
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

