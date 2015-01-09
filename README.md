# simplevideodownload

Script to dowload and extract audio from a url (youtube, vimeo or similar)
To see the supported video webs see [https://github.com/rg3/youtube-dl](youtube-dl)

Image available at docker hub [https://registry.hub.docker.com/u/eferro/simplevideodownload/](eferro/simplevideodownload)

## Use
```
sudo docker run -v $(pwd):/download -i -t eferro/simplevideodownload <url>
```

