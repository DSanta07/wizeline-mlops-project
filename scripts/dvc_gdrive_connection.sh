#!/bin/bash

# drive_url: 'https://drive.google.com/drive/folders/1JZrO03cLrge-WbLawwfXHr7E1eVNXypD'

# Add remote GDrive remote folder as storage for DVC
dvc remote add -d storage_data gdrive://1JZrO03cLrge-WbLawwfXHr7E1eVNXypD

# Push the changes to remote storage
dvc push

# Set the credentials (for each GDrive remote)
dvc remote modify storage_data gdrive_client_id '1064966860231-7tt09cj65b1rt2l165hk0ddfhhujqr2i.apps.googleusercontent.com'
dvc remote modify storage_data gdrive_client_secret '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'