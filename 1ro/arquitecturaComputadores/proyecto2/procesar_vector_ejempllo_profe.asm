##############################################################################
#                                                                            #
# SUMA DE LOS ELEMENTOS DE UN VECTOR                                         #
#                                                                            #
##############################################################################
#
# CÓDIGO EN C
#
##########################################
#
# int V[5] = {10,20,30,40,50}
# int suma;
# register int i; // Temporal
#
# int main(void) {
#	suma = 0;
#	for (i = 0; i < 5; i++) {
#		suma = suma+V[i];
#	}
#	return0;
# }
#
##########################################
# Tamaño de un entero: 4 bytes
# Tamaño del vector completo: 20 bytes
# suma: registro $s0
# i:    registro $t0
# temporales: $t0 ... $t5
##########################################
	.data
# int V[5] = {10,20,30,40,50}
V:	.word	10,20,30,40,50
# int suma;
suma:	.space	4
# register int i; // i: $t0

	.text
main:
#	suma = 0;
	li	$s0,0
#	for (i = 0; i < 5; i++) {
for:
#		i = 0;
	li	$t0,0
cond_for:
	li	$t1,5
	beq	$t0,$t1,end_for
#		suma = suma+v[i];
	la	$t2,V		# Poner puntero al comienzo del vector
	mul	$t3,$t0,4	# Calcular distancia hasta el elemento i-ésimo
	addu	$t4,$t2,$t3	# Poner puntero al elemento i-ésimo
	lw	$t5,0($t4)	# Leer elemento i-ésimo
	addu	$s0,$s0,$t5	# Acumular suma sobre $s0
#	}
	addiu	$t0,$t0,1	# Actualización del contador: i++
	b	cond_for
end_for:
# Grabar resultado
	sw	$s0,suma
#	return 0;
	li	$v0,17
	li	$a0,0
	syscall
# }
end_main:
