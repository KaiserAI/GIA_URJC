
.data
vector_enteros: .word 0, 0, 0, 0
		.word 0, 0, 0, 0
		.word 0, 0, 0, 0,
		.word 0, 0, 0, 0
			      
tamanio_vector: .word 16
mensaje: 	.asciiz "Esta es la cantidad de ceros del vector: " 
	

.text

main:
    		# Cargar de la dirección y tamaño del vector: 
    		la $t0, vector_enteros
    		lw $t1, tamanio_vector
    
    		# Mostrar mensaje:
    		li $v0, 4         
    		la $a0, mensaje 
    		syscall    
    
while:
 	
	        lw $t2, 0($t0)
		lw $t3, ($t0)
	
        	beq $t1, $zero, end     # Terminar si tamaño es cero.
	
    		beq $t3, $zero, contador  # Sumar si es cero.
          
       
         	# Siguiente posición del vector y disminuir el contador.
        	addi $t0, $t0, 4
        	addi $t1, $t1, -1   
       
        	j while # Regreso al bucle.
        
        	# Aumentar contador de ceros, avanzar en el vector y disminuir contador.
contador:
    		addi $t4, $t4, 1     
    		addi $t0, $t0, 4    
    		addi $t1, $t1, -1    
    		j while            
     
    		# Imprimir valor del contador y terminar.               
end:
    		li $v0, 1         
     	   	move $a0, $t4     
     	   	syscall           
    	    	li $v0, 10        
     	   	syscall          
