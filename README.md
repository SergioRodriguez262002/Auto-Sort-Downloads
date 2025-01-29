# Auto-Sort-Downloads
<p>
This is a service that runs on my linux machines. It sorts downloads into folders based on the extention. If there is a file with an extension thats not already a file it creates it. 
</p>
<p>Run at your own risk.</p>

## How to run 
<p>Download auto_sort_downloads.service, adjust the filepath of the script. From your download directory, run these commands in terminal</p>

'cp /etc/systemd/system/auto_sort_service.service'

'sudo systemctl start auto_sort_service'

'sudo systemctl enable auto_sort_service'

'sudo systemctl daemon-reload'