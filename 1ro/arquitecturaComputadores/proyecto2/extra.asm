.data
pedir_z: .asciiz "Introduce el valor de z: "
pedir_semilla: .asciiz "Introduce el valor de la semilla: "
mensaje_z_negativo: .asciiz "El valor de z no puede ser negativo: "
variable_z: .word 4
semilla: .word 4


.text
main:
    # Pide al usuario que introduzca un valor
    li $v0, 4
    la $a0, pedir_z
    syscall

    # Lee el valor introducido por el usuario
    li $v0, 5
    syscall

    # Almacena el valor en la variable
    sw $s0, variable_z
    
    # Pide al usuario que introduzca un valor
    li $v0, 4
    la $a0, pedir_semilla
    syscall
    
    # Lee el valor introducido por el usuario
    li $v0, 5
    syscall
    
     # Almacena el valor en la variable
    sw $s1, semilla

 # Comprobar si el valor de z es negativo
    bltz $s0, z_negativo
  
      
   # Salir del programa
    li $v0, 10
    syscall
    
 
 #Si z es negativo q salga mensaje
 z_negativo:
        li $v0, 4
 	la $a0, mensaje_z_negativo
    	syscall
    	
     
   # Salir del programa
    li $v0, 10
    syscall
    
 