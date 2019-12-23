# Baseball
為自己創造一個幫球網站

<h2>pip install mysqlclient 解決方法</h2>

<p>/usr/local/mysql/bin 會有 mysql_config檔</p>

<p>nano -c mysql_config (-c 是顯示行數)</p>

<h5>在第112行修改code</h5>
原本：
libs=“-L$pkglibdir”
libs=“$libs -l “
	
改成：
ibs=“-L$pkglibdir”
libs= -lmysqlclient -lssl -lcrypto

改完還是不行
輸入xcode-select —install (電腦更新可能安裝程式必須要更新）
   
參考：https://ruddra.com/posts/install-mysqlclient-macos/
