<?php

for ($i = 0; $i < 10; $i++) {
    echo "Prueba de for";
}

$mi_array = [1, 2, 3];
$valor = $mi_array[0];


function calcular($a) {
    if ($a < 10) {
        return;
    }
    return $a * 2;
}

$resultado = calcular(5);



class MiClase {}
$instancia = new MiClase();

?>