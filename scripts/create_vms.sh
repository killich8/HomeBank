#!/usr/bin/env bash
set -euo pipefail


VBM="/mnt/c/Program Files/Oracle/VirtualBox/VBoxManage.exe"


BASE_FOLDER_WIN=$(wslpath -w "/mnt/c/HomeBank-VMs")
ISO_PATH_WIN=$(wslpath -w "/mnt/c/Users/youne/Downloads/ubuntu-24.04.3-live-server-amd64.iso")


BASE_FOLDER_UNIX=$(wslpath -u "$BASE_FOLDER_WIN")
mkdir -p "$BASE_FOLDER_UNIX"

create_vm() {
  local NAME=$1 RAM=$2 DISK_MB=$3
  echo "Creating VM: $NAME"


  "$VBM" createvm --name "$NAME" --ostype "Ubuntu_64" --register --basefolder "$BASE_FOLDER_WIN"
  "$VBM" modifyvm "$NAME" --memory "$RAM" --cpus 1 --vram 16

  local DISK_PATH_WIN="${BASE_FOLDER_WIN}\\${NAME}\\${NAME}.vdi"
  "$VBM" createmedium disk --filename "$DISK_PATH_WIN" --size "$DISK_MB"

  "$VBM" storagectl "$NAME" --name "SATA Controller" --add sata --controller IntelAhci
  "$VBM" storageattach "$NAME" --storagectl "SATA Controller" --port 0 --device 0 --type hdd --medium "$DISK_PATH_WIN"

  "$VBM" storagectl "$NAME" --name "IDE Controller" --add ide
  "$VBM" storageattach "$NAME" --storagectl "IDE Controller" --port 0 --device 0 --type dvddrive --medium "$ISO_PATH_WIN"
  "$VBM" modifyvm "$NAME" --boot1 dvd --boot2 disk --boot3 none --boot4 none


  "$VBM" modifyvm "$NAME" --nic1 nat
}

# VMs
create_vm FW-01      512  10000
create_vm BASTION-01 512  10000
create_vm LB-01     1024  15000
create_vm LB-02     1024  15000
create_vm APP-01    1536  20000
create_vm APP-02    1536  20000
create_vm DB-01     2048  30000
create_vm DB-02     2048  30000
create_vm MON-01    3072  40000

echo "All VMs created."
