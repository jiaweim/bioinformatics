# Wget

2022-05-17, 13:39
***

## 简介

GNU Wget 是一个免费软件包，可使用 HTTP, HTTPS, FTP 和 FTPS 检索和下载文件。

用 wget 下载很方便，可以下载单个文件、多个文件，甚至整个网站。例如，下载 book.douban.com 的第一页：

```sh
$ wget https://book.douban.com
--2022-05-17 15:07:49--  https://book.douban.com/
Resolving book.douban.com (book.douban.com)... 81.70.124.99, 49.233.242.15, 140.143.177.206
Connecting to book.douban.com (book.douban.com)|81.70.124.99|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: unspecified [text/html]
Saving to: ‘index.html’

index.html              [ <=>                ] 161.09K  --.-KB/s    in 0.1s    

2022-05-17 15:07:49 (1.55 MB/s) - ‘index.html’ saved [164955]
```

wget 可以递归下载、后台下载、继续下载没有下载完的文件等等。

## 参考

- https://www.gnu.org/software/wget/
