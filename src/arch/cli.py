#!/usr/bin/env python

from arch import inst_conf, github_raw
from arch import color as colour
from os   import system, makedirs
from sys  import stdout, stderr
from sh   import sed, systemctl, git
from wrap import sh, wget, pacman


def color():
    for i in colour:
        wget(colour[i], O=i)
        system('chmod a+x '+i)
    pacman(S='pinfo', _in='y')

def zsh():
    system('wget https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O - | sh')
    git.clone('https://github.com/zsh-users/zsh-completions', '/root/.oh-my-zsh/custom/plugins/zsh-completions', _out=stdout, _err=stderr)
    inst_conf('~', '.zshrc')

def vim():
    git.clone('https://github.com/amix/vimrc.git', '/root/.vim_runtime', _out=stdout, _err=stderr)
    sh('/root/.vim_runtime/install_awesome_vimrc.sh')

def pkgmgr():
    inst_conf('/', 'pacman.conf')
    pacman('-Syy')
    pacman(S='archlinuxcn-keyring', _in='y')

def sshd():
    pacman(S='openssh', _in='y')
    sed('s/#PermitRootLogin prohibit-password/PermitRootLogin yes/g', i='/etc/ssh/sshd_config')
    systemctl('enable', 'sshd')
    systemctl('start', 'sshd')

def nfsrv():
    pacman(S='nfs-utils', _in='y')
    makedirs('/srv/nfs4')
    with open('/etc/exports', 'a') as f:
        f.write('\n  /srv/nfs4        192.168.0.*(rw,sync,fsid=0,no_wdelay,no_root_squash,no_subtree_check)\n\n')
    systemctl('enable', 'nfs-server')
    systemctl('start', 'nfs-server')

def misc():
    wget(github_raw+'racaljk/hosts/master/hosts', O='/etc/hosts')


if __name__ == '__main__':
    color()
    zsh()
    vim()
    pkgmgr()
    sshd()
    nfsrv()
    misc()

