<?php

$sock = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
$con = socket_connect($sock, 'localhost', 6011);

$msg = "Hello, World!\n";

$send = socket_write($sock, $msg, strlen($msg));
$read = socket_read($sock, 100, $mode = PHP_NORMAL_READ);

echo $read;


socket_close($sock);


?>