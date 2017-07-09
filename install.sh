#!/bin/sh

source install/inst.conf
HANDLE='echo -e "\033[31mInstallation failed in install.sh:${FUNCNAME[0]}:${LINENO}, exit.\033[0m"; exit 1'
trap "$HANDLE" ERR

read -p 'Input your target disk: ' DISK
echo -e 'n\n\n\n\n\nw' | fdisk $DISK

PART="${DISK}1"
mkfs.ext4 $PART

mkdir -p $ROOTFS
mount $PART $ROOTFS
rm -r $ROOTFS/lost+found

sed -i '6 a#China' /etc/pacman.d/mirrorlist
sed -i "7 a${MIRROR}" /etc/pacman.d/mirrorlist

pacstrap $ROOTFS base base-devel
genfstab -U $ROOTFS >> $ROOTFS/etc/fstab

ABSPATH="${ROOTFS}/root/archinst"
NEXT="${ABSPATH:${#ROOTFS}}/install/config.sh"
mkdir -p $ABSPATH
cp -r . $ABSPATH
arch-chroot $ROOTFS /bin/sh $NEXT

