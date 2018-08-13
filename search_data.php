<?php
header('Access-Control-Allow-Origin: *'); 


$connection=mysqli_connect('localhost','root','','Bikesh');
if(isset($_POST['write_search_query'])){
    //js sents the write data
$read_search_query=$_POST['write_search_query'];
if(mysqli_query($connection,"UPDATE search_data SET search_data='$read_search_query' WHERE id='1' ")){
    echo 'success';
}else{
    echo 'failed';
}


}

if(isset($_POST['read_search_query'])){
    //python reads that written data     
    $result=mysqli_query($connection,"SELECT search_data FROM search_data WHERE id='1' ");//always 1 
    if($result){
        $result=mysqli_fetch_assoc($result);
        echo $result['search_data'];
    }else{
        echo 'failed';
    }
    $result=mysqli_fetch_assoc($result);
    echo $result['search_data'];
    
}
    


    







?>