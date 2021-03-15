<?php
 $data_file = fopen("exap.txt", "a")
 $name = $_POST["name"])
 $email = $_POST["email"])
 $tel = $_POST["tel"])
 $msg = $_POST["msg"])
 $text_to_write = $name . " " . $email . " " . $tel . " " . $msg ;
 fwrite($data_file,$text_to_write)
 fclose($data_file)

?>