## pypaste.py -- a command line tool to put codes on pastebins on the fly

# Installation script                               Sun Aug  2 19:42:53 IST 2009

# ======================================================================
# Copyright (C) 2009 Abhishek Mishra <ideamonk@gmail.com>
# Time-stamp: Sat Aug  1 20:27:22 IST 2009
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.
# ======================================================================

echo "Making ~/.pypaste"
mkdir -p ~/.pypaste/modules

echo "Copying files ..."
cp -R ./* ~/.pypaste/

mv ~/.pypaste/pypaste.py ~/.pypaste/pypaste
chmod +x ~/.pypaste/pypaste

# removes temporary swap/backup files
echo "Removing temporary files from install location"
rm -f ~/.pypaste/install.*

# effective on a new bash
echo "Adding ~/.pypaste to your path (in ~/.bashrc)"
echo "PATH=$PATH:/home/$USER/.pypaste" >> ~/.bashrc
echo "export PATH" >> ~/.bashrc

# for immediate use
export PATH=$PATH:/home/$USER/.pypaste

echo "Installation Complete!"
echo "do pypaste for info :) in any terminal other than this."
