#!/usr/bin/env python

from os import system, makedirs
from os.path import expanduser
from sys import stdout, stderr
from sh import pacman, sh, wget, sed, systemctl
from sh.contrib import git

def color():
    wget('https://raw.githubusercontent.com/pagekite/colormake/master/colormake.pl', O='/usr/bin/colormake.pl', _out=stdout, _err=stderr)
    wget('https://raw.githubusercontent.com/pagekite/colormake/master/colormake', O='/usr/bin/colormake', _out=stdout, _err=stderr)
    wget('https://raw.githubusercontent.com/pagekite/colormake/master/clmake', O='/usr/bin/clmake', _out=stdout, _err=stderr)
    wget('https://raw.githubusercontent.com/denilsonsa/prettyping/master/prettyping', O='/usr/bin/prettyping', _out=stdout, _err=stderr)

    system('chmod a+x /usr/bin/colormake.pl')
    system('chmod a+x /usr/bin/colormake')
    system('chmod a+x /usr/bin/clmake')
    system('chmod a+x /usr/bin/prettyping')

def zsh():
    system('wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O - | sh')
    sed('s/"robbyrussell"/"agnoster"/g', i=expanduser('~/.zshrc'))
    git.clone('https://github.com/zsh-users/zsh-completions', expanduser('~/.oh-my-zsh/custom/plugins/zsh-completions'), _out=stdout, _err=stderr)

def zshrc():
    zshrc = '''
plugins=(git zsh-completions)
autoload -U compinit && compinit

alias diff='diff --color=auto'
alias grep='grep --color=auto'
alias make='colormake'
alias ping='prettyping'

export LESS=-R
export LESS_TERMCAP_mb=$'\E[1;31m'
export LESS_TERMCAP_md=$'\E[1;36m'
export LESS_TERMCAP_me=$'\E[0m'
export LESS_TERMCAP_se=$'\E[0m'
export LESS_TERMCAP_so=$'\E[01;44;33m'
export LESS_TERMCAP_ue=$'\E[0m'
export LESS_TERMCAP_us=$'\E[1;32m'

zmodload zsh/zpty
pty()
{
    zpty pty-${UID} ${1+$@}
    if [[ ! -t 1 ]];then
        setopt local_traps
        trap '' INT
    fi
    zpty -r pty-${UID}
    zpty -d pty-${UID}
}
ptyless()
{
    pty $@ | less
}

alias hosts='wget https://raw.githubusercontent.com/racaljk/hosts/master/hosts -O /etc/hosts'

    '''
    f = open(expanduser('~/.zshrc'), 'a')
    f.write(zshrc)
    f.close()

def vimrc():
    git.clone('https://github.com/amix/vimrc.git', expanduser('~/.vim_runtime'), _out=stdout, _err=stderr)
    sh(expanduser('~/.vim_runtime/install_awesome_vimrc.sh'), _out=stdout, _err=stderr)

def pkgmgr():
    sed('s/#Color/Color/g', i='/etc/pacman.conf')
    paconf = '''
[archlinuxcn]
Server = https://mirrors.tuna.tsinghua.edu.cn/archlinuxcn/$arch

[arch4edu]
SigLevel = Never
Server = https://mirrors.tuna.tsinghua.edu.cn/arch4edu/$arch

    '''
    f = open('/etc/pacman.conf', 'a')
    f.write(paconf)
    f.close()

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
    f = open('/etc/exports', 'a')
    f.write('\n/srv/nfs4 192.168.0.*(rw,sync,fsid=0,no_wdelay,no_root_squash,no_subtree_check)\n')
    f.close()
    systemctl('enable', 'nfs-server')
    systemctl('start', 'nfs-server')

def misc():
    wget('https://raw.githubusercontent.com/racaljk/hosts/master/hosts', O='/etc/hosts', _out=stdout, _err=stderr)


if __name__ == '__main__':
    color()
    zsh()
    zshrc()
    vimrc()
    pkgmgr()
    sshd()
    nfsrv()
    #ssocks()
    #kcptun()
    misc()

