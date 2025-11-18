<?php

$a = 10;
$b = $a + $c; // Error Semántico (M2): $c no está definido

function miFuncion() {
    $x = 1; // Variable local
    $y = $x + 5; // OK: $x está en este scope
}

function otraFuncion() {
    $z = $x; // Error Semántico (M2): $x no está en este scope
}

function miFuncion() {
    // Error Semántico (M1): Función 'miFuncion' re-declarada
}

class MiClase {}

class MiClase {
    // Error Semántico (M1): Clase 'MiClase' re-declarada
}

?>