#! /bin/bash

# refresh derived resources
inkscape icon.svg -w 24 -h 24 -o iconx24.png
inkscape icon.svg -w 64 -h 64 -o icon.png


# grab version and parse it into metadata.json
cp metadata_source.json metadata_package.json
version=`cat version.txt`
# remove all but the latest version in package metadata
python parse_metadata_json.py
sed -i -e "s/VERSION/$version/g" metadata.json

# cut the download, sha and size fields
sed -i '/download_url/d' metadata.json
sed -i '/download_size/d' metadata.json
sed -i '/install_size/d' metadata.json
sed -i '/download_sha256/d' metadata.json

# prepare the package
mkdir plugins
cp iconx24.png plugins
cp __init__.py plugins
cp action_board_clean.py plugins
cp Clean_board_GUI.py plugins
cp board_clean.py plugins
cp version.txt plugins
mkdir resources
cp icon.png resources

zip -r Board_cleaner-$version-pcm.zip plugins resources metadata.json

# clean up
rm -r resources
rm -r plugins
rm metadata.json

# get the sha, size and fill them in the metadata
cp metadata_source.json metadata.json
version=`cat version.txt`
sed -i -e "s/VERSION/$version/g" metadata.json
zipsha=`sha256sum Board_cleaner-$version-pcm.zip | xargs | cut -d' ' -f1`
sed -i -e "s/SHA256/$zipsha/g" metadata.json
unzipsize=`unzip -l Board_cleaner-$version-pcm.zip | tail -1 | xargs | cut -d' ' -f1`
sed -i -e "s/INSTALL_SIZE/$unzipsize/g" metadata.json
dlsize=`ls -al Board_cleaner-$version-pcm.zip | tail -1 | xargs | cut -d' ' -f5`
sed -i -e "s/DOWNLOAD_SIZE/$dlsize/g" metadata.json
