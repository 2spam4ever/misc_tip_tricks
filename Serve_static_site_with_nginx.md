# Add cache config for static files

```nginx
server {
        listen 80;
        server_name test.jasonrigden.com; <= CHANGE ME
        root /home/jason/www; <= CHANGE ME
        index index.html;
        
	    # Media: images, icons, video, audio, HTC
	    location ~* \.(?:jpg|jpeg|gif|png|ico|cur|gz|svg|mp4|ogg|ogv|webm|htc)$ {
	      access_log off;
	      add_header Cache-Control "max-age=2592000";
	    }

	    # CSS and Javascript
	    location ~* \.(?:css|js)$ {
	      add_header Cache-Control "max-age=31536000";
	      access_log off;
	    }
}
```

# Enable compress when transfer data

change `/etc/nginx/nginx.conf`

```nginx
##
# Gzip Settings
##
gzip_static on;
gzip on;
```
