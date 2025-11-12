<?php

$variable1 = 100;
$variable_float = 3.1416;
$mi_string = "Hola mundo!";
$otro_string = 'Prueba 123';

$total = $variable1 + $variable_float;

# Función para probar ID y más variables
function calcularTotal($num1, $num2) {
    $resultado = $num1 + $num2;
    return $resultado;
}

$valor_final = calcularTotal($total, 50);

echo $valor_final;

?>
