# 命令行性能工具

## Apache bench

### 介绍

Apache Bench原本是针对Apache HTTP服务器设计的，但同样适用于其他类型的HTTP服务器。该工具与标准Apache源码一起发布，是免费且开源的，基于Apache License。

> Apache Bench返回的最有用的信息是服务器每秒能够处理的请求次数（RPS），不过由于测试的页面不同，RPS会有所差异。通常，静态页面的RPS大于动态页面，页面体积越小，RPS越大。因此，RPS是相对的，在选择主机时，可以使用同一个页面进行测试，这样得到的数据相对来说更有可比性。

### 安装

__通过源码安装__

* 下载

下载地址：https://www.apachelounge.com/download/

选择当前最新的zip包进行下载：

![](../images/ab_download.png)

* 解压

在解压的 `Apache24/bin/`目录下找到`ab`和`abs`可执行文件。

![](../images/ab_bin.png)


> ab.exe：这是Apache Bench（简称ab）的Windows可执行文件。ab主要用于测试HTTP服务器的性能，通过模拟多个并发请求来评估服务器在高并发环境下的负载能力和响应时间。它能够生成详细的测试报告，包括每秒请求数（Requests per second）、用户平均请求等待时间（Time per request）等关键性能指标。
> 
> abs.exe：abs是ab的增强版或特定版本，专门用于测试HTTPS服务器的性能。与ab.exe类似，abs.exe也能够模拟多个并发请求，并生成详细的测试报告。然而，它的主要区别在于支持HTTPS协议，因此更适合用于评估HTTPS服务器的性能和安全性。

* 配置环境变量

略


### 使用


**基本命令格式**：

```shell
ab [options] [http[s]://]hostname[:port]/path
```

其中，`[options]`代表各种可选参数，用于配置测试的具体细节；`[http[s]://]hostname[:port]/path`代表要测试的HTTP（或HTTPS）服务器的地址、端口和路径。



**参数说明**：

```shell
ab --help
```

`ab`（Apache Bench）命令的参数及其说明信息：

| 参数              | 说明                                                                                               |
| ----------------- | -------------------------------------------------------------------------------------------------- |
| `-n requests`     | 要执行的请求数                                                                                      |
| `-c concurrency`  | 一次要执行的多请求数（并发数）                                                                      |
| `-t timelimit`    | 测试所用的最大时间（秒），这隐含着`-n 50000`                                                        |
| `-s timeout`      | 等待每个响应的最大时间（秒），默认是30秒                                                            |
| `-b windowsize`   | TCP发送/接收缓冲区的大小（字节）                                                                    |
| `-B address`      | 在建立出站连接时要绑定的地址                                                                        |
| `-p postfile`     | 包含要POST的数据的文件，记得还要设置`-T`                                                            |
| `-u putfile`      | 包含要PUT的数据的文件，记得还要设置`-T`                                                             |
| `-T content-type` | 用于POST/PUT数据的Content-type头部，例如`'application/x-www-form-urlencoded'`，默认是`'text/plain'` |
| `-v verbosity`    | 打印多少故障排除信息                                                                                |
| `-w`              | 以HTML表格的形式打印结果                                                                            |
| `-i`              | 使用HEAD代替GET                                                                                     |
| `-x attributes`   | 作为表格属性插入的字符串                                                                            |
| `-y attributes`   | 作为tr属性插入的字符串                                                                              |
| `-z attributes`   | 作为td或th属性插入的字符串                                                                          |
| `-C attribute`    | 添加Cookie，例如`'Apache=1234'`（可重复）                                                           |
| `-H attribute`    | 添加任意头部行，例如`'Accept-Encoding: gzip'`，在所有正常头部行之后插入（可重复）                   |
| `-A attribute`    | 添加Basic WWW认证，属性是冒号分隔的用户名和密码                                                     |
| `-P attribute`    | 添加Basic代理认证，属性是冒号分隔的用户名和密码                                                     |
| `-X proxy:port`   | 要使用的代理服务器和端口号                                                                          |
| `-V`              | 打印版本号并退出                                                                                    |
| `-k`              | 使用HTTP KeepAlive功能                                                                              |
| `-d`              | 不显示服务百分比的表格                                                                              |
| `-S`              | 不显示置信估计和警告                                                                                |
| `-q`              | 当请求数超过150时，不显示进度                                                                       |
| `-l`              | 接受可变文档长度（用于动态页面）                                                                    |
| `-g filename`     | 将收集的数据输出到gnuplot格式的文件                                                                 |
| `-e filename`     | 输出包含服务百分比的CSV文件                                                                         |
| `-r`              | 在套接字接收错误时不退出                                                                            |
| `-m method`       | 方法名称                                                                                            |
| `-h`              | 显示使用信息（此消息）                                                                              |


**示例**

* 模拟10个并发用户，每个用户发送100个请求到`http://testurl.com/xxxx`：
	
```shell
ab -n 1000 -c 10 http://127.0.0.1:5000/add_one
```

* 使用POST方法发送数据，数据存储在`post_data.txt`文件中，并设置Content-type为`application/json`：
	
```shell
ab -n 100 -c 10 -p .\tools\post_data.txt -T 'application/json' http://127.0.0.1:5000/login
```

**测试结果**


```shell
ab -n 100 -c 10 http://127.0.0.1:5000/add_one

This is ApacheBench, Version 2.3 <$Revision: 1913912 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking 127.0.0.1 (be patient).....done


Server Software:        Werkzeug/3.1.3
Server Hostname:        127.0.0.1
Server Port:            5000

Document Path:          /add_one
Document Length:        57 bytes

Concurrency Level:      10
Time taken for tests:   22.250 seconds
Complete requests:      100
Failed requests:        0
Total transferred:      22200 bytes
HTML transferred:       5700 bytes
Requests per second:    4.49 [#/sec] (mean)
Time per request:       2225.002 [ms] (mean)
Time per request:       222.500 [ms] (mean, across all concurrent requests)
Transfer rate:          0.97 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.4      0       1
Processing:  2013 2023   4.9   2024    2033
Waiting:     2001 2004   1.8   2004    2008
Total:       2013 2023   4.8   2024    2033

Percentage of the requests served within a certain time (ms)
  50%   2024
  66%   2025
  75%   2026
  80%   2027
  90%   2029
  95%   2033
  98%   2033
  99%   2033
 100%   2033 (longest request)
```

以下是对这些结果的解释：

以下是将上述内容使用Markdown表格重新生成的版本：

| 项目               | 描述                               | 值                          |
| ------------------ | ---------------------------------- | --------------------------- |
| **服务器信息**     |                                    |                             |
| 服务器软件         | Werkzeug版本                       | 3.1.3                       |
| 服务器主机名       | IP地址                             | 127.0.0.1                   |
| 服务器端口         | 监听的端口                         | 5000                        |
| 文档路径           | 请求的URL路径                      | /add_one                    |
| 文档长度           | 响应的文档长度                     | 57字节                      |
| **性能指标**       |                                    |                             |
| 并发级别           | 并发请求数                         | 10                          |
| 测试耗时           | 整个测试花费的时间                 | 22.250秒                    |
| 完成请求数         | 完成的请求总数                     | 100                         |
| 失败请求数         | 失败的请求数                       | 0                           |
| 总传输量           | 总共传输的数据量                   | 22200字节                   |
| HTML传输量         | 传输的HTML内容总量                 | 5700字节                    |
| 每秒请求数         | 平均每秒处理的请求数               | 4.49[#/sec]                 |
| 每个请求耗时       | 平均每个请求花费的时间             | 2225.002[ms]                |
| 传输速率           | 接收到的数据传输速率               | 0.97[Kbytes/sec]            |
| **连接时间**       |                                    |                             |
| 连接时间           | 最小值/平均值/标准差/中位数/最大值 | 0/0/0.4/0/1[ms]             |
| 处理时间           | 最小值/平均值/标准差/中位数/最大值 | 2013/2023/4.9/2024/2033[ms] |
| 等待时间           | 最小值/平均值/标准差/中位数/最大值 | 2001/2004/1.8/2004/2008[ms] |
| 总时间             | 最小值/平均值/标准差/中位数/最大值 | 2013/2023/4.8/2024/2033[ms] |
| **百分比响应时间** |                                    |                             |
| 50%请求耗时        |                                    | 2024[ms]                    |
| 66%请求耗时        |                                    | 2025[ms]                    |
| 75%请求耗时        |                                    | 2026[ms]                    |
| 80%请求耗时        |                                    | 2027[ms]                    |
| 90%请求耗时        |                                    | 2029[ms]                    |
| 95%请求耗时        |                                    | 2033[ms]                    |
| 98%请求耗时        |                                    | 2033[ms]                    |
| 99%请求耗时        |                                    | 2033[ms]                    |
| 最长请求耗时       |                                    | 2033[ms]                    |


__性能结果分析__

从结果来看，这个Flask应用的性能并不高，平均每秒只能处理4.49个请求，每个请求的平均处理时间是2225毫秒。这可能是因为Flask和Werkzeug是为了开发和测试而设计的，而不是为了高性能的生产环境。如果你需要处理大量的并发请求，你可能需要考虑使用更高效的WSGI服务器（如Gunicorn或uWSGI）和/或优化你的应用代码。


### 注意事项

1. 在进行压力测试时，应确保测试环境与实际生产环境尽可能一致，以获得更准确的结果。
2. 测试过程中可能会产生大量日志和错误信息，建议提前配置好日志存储路径和错误处理机制。
3. 根据测试需求调整并发数和请求数等参数，以获得不同压力下的服务器性能表现。


## Vegeta

### 介绍

Vegeta（贝吉塔）是一个多功能的HTTP负载测试工具，它是基于对具有恒定请求率的HTTP服务进行钻取的需求而构建的， “It is cover 9000”

> “超过9000了！”，也简称为“超过9000!”，是2006年流行起来的一个网络梗，与1997年4月19日播出的《龙珠Z》动画电视连续剧《悟空归来》的一集的英语本地化有关。这个短语通常用作无数量词来描述大量的东西。这个短语的变体也被用作一种形式的trolling。
> 这个短语指的是赛亚人角色贝吉塔用日语说出的原始台词的变化，演员布莱恩·德拉蒙用英语配音

![](../images/vegeta_logo.jpg)


### 安装

> 注：vegeta 不支持Windows。

* 下载

https://github.com/tsenart/vegeta/releases

* 解压之后得到可执行文件。

* 拷贝到环境变量配置目录。

```shell
which vegeta
/usr/bin/vegeta
```

### 命令


**基本命令格式**：

```shell
Usage: vegeta [global flags] <command> [command flags]
```

其中，`[global flags]`全局标签，可选项；`<command>[command flags]` 命令以及对应的参数。


**参数说明**：

```shell
vegeta --help
```


以下是根据 `vegeta --help` 的输出整理的 `vegeta` 压测工具的参数说明表格：

|        命令/参数        |                         说明                         |            默认值            |
| :---------------------: | :--------------------------------------------------: | :--------------------------: |
|    **global flags**     |                                                      |                              |
|        -cpus int        |                    使用的CPU数量                     |              16              |
|     -profile string     |              启用[cpu, heap]的性能分析               |              无              |
|        -version         |                    打印版本并退出                    |              无              |
|   **attack command**    |                                                      |                              |
|      -body string       |                      请求体文件                      |              无              |
|      -cert string       |              TLS客户端PEM编码的证书文件              |              无              |
|        -chunked         |              使用分块传输编码发送请求体              |              无              |
|    -connect-to value    |    要使用的(ip or host):port的映射而不是目标URL (ip or host):port。可以重复多次。  | 无 |
|    -connections int     |             每个目标主机的最大空闲连接数             |            10000             |
|     -dns-ttl value      |      缓存DNS查找的持续时间[-1 = 禁用, 0 = 永远]      |              0s              |
|   -duration duration    |                测试持续时间[0 = 永远]                |              无              |
|     -format string      |                 目标格式[http, json]                 |            "http"            |
|          -h2c           |             发送不带TLS加密的HTTP/2请求              |              无              |
|      -header value      |                        请求头                        |              无              |
|         -http2          |             当服务器支持时发送HTTP/2请求             |             true             |
|        -insecure        |               忽略无效的服务器TLS证书                |              无              |
|       -keepalive        |                     使用持久连接                     |             true             |
|       -key string       |              TLS客户端PEM编码的私钥文件              |              无              |
|      -laddr value       |                      本地IP地址                      |           0.0.0.0            |
|          -lazy          |                     延迟读取目标                     |              无              |
|     -max-body value     |       从响应体中捕获的最大字节数[-1 = 无限制]        |              -1              |
|  -max-connections int   |               每个目标主机的最大连接数               |              无              |
|    -max-workers uint    |                      最大工作数                      |     18446744073709551615     |
|      -name string       |                       攻击名称                       |              无              |
|     -output string      |                       输出文件                       |           "stdout"           |
| -prometheus-addr string |         Prometheus导出器监听地址[空 = 禁用]          |              无              |
|   -proxy-header value   |                   Proxy CONNECT头                    |              无              |
|       -rate value       |             每时间单位的请求数[0 = 无限]             |            50/1s             |
|     -redirects int      |     要跟随的重定向次数。-1表示不跟随但标记为成功     |              10              |
|    -resolvers value     |   用于DNS解析的地址列表(ip:port)。禁用本地系统DNS    |              无              |
|    -root-certs value    |             TLS根证书文件(逗号分隔列表)              |              无              |
|    -session-tickets     |            启用使用会话票据的TLS会话恢复             |              无              |
|     -targets string     |                       目标文件                       |           "stdin"            |
|    -timeout duration    |                       请求超时                       |             30s              |
|   -unix-socket string   |   通过Unix套接字连接。这会覆盖目标URL中的主机地址    |              无              |
|      -workers uint      |                      初始工作数                      |              10              |
|   **encode command**    |                                                      |                              |
|     -output string      |                       输出文件                       |           "stdout"           |
|       -to string        |               输出编码[csv, gob, json]               |            "json"            |
|    **plot command**     |                                                      |                              |
|     -output string      |                       输出文件                       |           "stdout"           |
|     -threshold int      |        数据点阈值，超过该阈值的系列会被下采样        |             4000             |
|      -title string      |              生成的HTML页面的标题和页眉              |        "Vegeta Plot"         |
|   **report command**    |                                                      |                              |
|     -buckets string     |            直方图桶，例如: "[0,1ms,10ms]"            |              无              |
|     -every duration     |                       报告间隔                       |              无              |
|     -output string      |                       输出文件                       |           "stdout"           |
|      -type string       | 要生成的报告类型[text, json, hist[buckets], hdrplot] |            "text"            |


### 示例

**常用参数说明**

```shell
vegeta attack -rate=100 -duration=30s -targets=targets.txt | vegeta report
vegeta attack -max-workers=100 -rate=0 -duration=10s -targets=targets.txt | vegeta report
```
`-rate=100`：每秒发送 100 个请求。
`-max-workers=100`：指定攻击中使用的最大worker数。它可以用来控制攻击所使用的并发级别。 配合`-rate=0`使用
`-duration=30s`：测试持续 30 秒。
`-targets=targets.txt`：指定目标文件。


**1. 简单的`GET`接口**


* 请求脚本：`targets.txt`

```txt
GET http://192.168.0.5:5000/
```

* 执行命令

```shell
vegeta attack -rate=100 -duration=30s -targets=targets.txt | vegeta report
```

**2. 简单的`POST`带参数接口**

* 请求脚本：`targets.txt`

```txt
POST http://192.168.0.5:5000/login
content-type: application/json
@/home/fnngj/tools/load-testing/user.json
```

* 参数文件：`user.json`

```json
{"username": "admin", "password": "a123456"}
```

* 执行命令

```shell
vegeta attack -rate=100 -duration=30s -targets=targets2.txt | vegeta report
```

**3. 生成报告**

* 生成bin文件

```shell
vegeta attack -connections=100 -duration=60s -targets=targets.txt > results.bin
```

* 生成JSON报告

```shell
vegeta report -type=json results.bin > results.json
```

* 生成txt报告

```shell
vegeta report -type=text results.bin > results.txt
```

* 生成直方图

```shell
cat results.bin | vegeta report -type='hist[0,2ms,4ms,6ms]'

Bucket         #     %       Histogram
[0s,    2ms]   0     0.00%
[2ms,   4ms]   1384  92.27%  #####################################################################
[4ms,   6ms]   99    6.60%   ####
[6ms,   +Inf]  17    1.13%
```

计算并打印给定`Bucket`的基于文本的直方图。

* 生成HTML报告

```
cat results.bin | vegeta plot > plot.html
```

> 拷贝到Windows下：cp plot.html /mnt/d/github/AutoTestClass/learn-performance-class/package/plot.html

![](../images/vegeta-plot.png)
