#!/bin/bash
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
PARENT_DIR=$(dirname "${SCRIPT_DIR}")

pushd $PARENT_DIR

# # Setup system python
# sudo dnf install poetry
# python3 -m keyring --disable # keeps kdewallet quiet

# # Setup appliction python env
# cd "${PARENT_DIR}"
# poetry install

# Install 
default_tws_api_install_dir=~/code/tws-api-pythonclient
read -p "Enter tws api install dir (default: ${default_tws_api_install_dir})" install_dir
install_dir="${install_dir:-$default_tws_api_install_dir}"
echo $install_dir
rm -r /tmp/tws-api
mkdir /tmp/tws-api
curl -q -sSL https://interactivebrokers.github.io/downloads/twsapi_macunix.1033.01.zip \
    -o /tmp/tws-api/tws-api.zip
unzip /tmp/tws-api/tws-api.zip -d /tmp/tws-api
echo "Moving TWS API python client to ${install_dir}"
mv /tmp/tws-api/IBJts/source/pythonclient "${install_dir}"
poetry run pip install -e ${install_dir}


popd