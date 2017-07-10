#!/bin/sh

source /root/install/inst.conf
HANDLE='echo -e "\033[31mInstallation failed in install/config.sh:${FUNCNAME[0]}:${LINENO}, exit.\033[0m"; exit 1'
trap "$HANDLE" ERR

DISK=`lsblk | grep / | awk '{print $1}' | sed 's/└─sd\|\`-sd/\/dev\/sd/g;s/1//g'`

ln -sf $TIMEZONE /etc/localtime

sed -i $LOCALE /etc/locale.gen
echo LANG=en_US.UTF-8 > /etc/locale.conf
locale-gen

echo $HOSTNAME > /etc/hostname

systemctl enable dhcpcd

echo y | pacman -S grub
grub-install $DISK
grub-mkconfig -o /boot/grub/grub.cfg

echo y | pacman -S python python-pip
echo '[global]' >> /etc/pip.conf
echo "index-url = ${PIPMIR}" >> /etc/pip.conf
pip install sh

echo -e '\ny' | pacman -S git vim zsh ntfs-3g tree netcat wget axel htop rlwrap p7zip
echo y | pacman -Rsn reiserfsprogs xfsprogs jfsutils pcmciautils mdadm lvm2 vi nano

ln -sf /usr/bin/vim /usr/bin/vi
ln -sf /usr/bin/vim /usr/bin/nano

git clone https://github.com/voyage65535/arch-install.git ~/arch-install

passwd
exit
