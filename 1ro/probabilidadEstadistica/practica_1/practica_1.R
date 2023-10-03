setwd("C:/Users/kaise/OneDrive/Documentos/Uni/1ro/probabilidadEstadistica/practica1")
install.packages("UsingR")
install.packages("ggplot2")
paises.8 <- read.table("paises-8.csv", header = T, sep = ";",stringsAsFactors = T)


#6R:

cov(paises.8$Esp.vida.Fem, paises.8$Alfabet, use = "complete.obs")#212.991

cor(paises.8$Esp.vida.Fem, paises.8$Alfabet, use = "complete.obs")#0.8833315 

summary(lm(paises.8$Esp.vida.Fem ~ paises.8$Alfabet))#78.03% 

#Recta de Regresión;
ggplot(paises.8, aes(Alfabet, Esp.vida.Fem)) + ggtitle("Recta de Regresión:") + xlab("Porcentaje de Alfabetización") + ylab("Esperanza de Vida Femenina") + geom_point(colour = "pink") + geom_smooth(method = "lm", se = FALSE, colour = "black")

#En este punto nos disponemos a estudiar la relación entre la esperanza de vida
#femenina y el nivel de alfabetización de los países en la base de datos.
#La covarianza de 212.991 nos afirma la relación entre dichas variables: 
#a mayor alfabetización tenga el país, más esperanza de vida presentan las féminas.
#En concreto, dicha relación es bastante considerable puesto que el cálculo de su
#correlación, con un valor de 0.8833315, nos indica lo estrechamente relacionadas
#que están. Es tal que el 78.03% de la esperanza de vida femenina se explica 
#mediante la alfabetización del país. Todo lo anterior queda reflejado en el siguiente
#gráfico donde la línea roja representa la recta de regresión:

#[Insertar gráfico de recta de regresión]

#7R:

table(paises.8$Religion)#28 países.
paisesCat <- paises.8[paises.8$Religion == "Catolica",]
head(paisesCat)

cov(paisesCat$Esp.vida.Fem, paisesCat$Alfabet, use = "complete.obs")#148,8675

cor(paisesCat$Esp.vida.Fem, paisesCat$Alfabet, use = "complete.obs")#0.907876 

summary(lm(paisesCat$Esp.vida.Fem ~ paisesCat$Alfabet))#0.8242

#Recta de Regresión:
ggplot(paisesCat, aes(Alfabet, Esp.vida.Fem)) + ggtitle("Recta de Regresión de los países mayoritariamente Católicos:") + xlab("Porcentaje de Alfabetización") + ylab("Esperanza de Vida Femenina") + geom_point(colour = "gold") + geom_smooth(method = "lm", se = FALSE, colour = "black")


#Para este apartado analizamos cual es la influencia de la religión católica
#en la relación antes estudiada. Hay que tomar en cuenta que en nuestra base de datos
#dicha religión es mayoritaria en 28 de los 69 países, dicho de otra manera, representa
#el 0,4058% de la información. 

#Como era de esperar su covarianza de 148,8675 nos confirma
#que los países católicos, en media, a mayor alfabetización mayor esperanza de
#vida femenina. En este caso la correlación es algo mayor, con un 0.907876 y 
#se explica el 82,42% de la esperanza de vida femenina gracias a la alfabetización.
#Todo ello nos indica que en los países mayoritariamente católicos la relación entre 
#la esperanza de vida de las mujeres y la alfabetización, dicha relación es un poco
#mayor que la observada en la muestra total donde se encuentran el resto de países.

#[insertar Recta de Regresión]



#Como se puede ver en el gráfico inferior los países católicos (puntos dorados) en media tienen mayor
#porcentaje de alfabetización. Es por ello que la pendiente de su recta (recta dorada) es más inclinada 
#llegando así a representar mejor a los valores más altos de la esperanza de vida femenina. Los puntos
#negros representan al resto de países y la recta rosada es la recta de regresión del conjunto de todos los países.

#[insertar gráfico donde se comparan con religiones y solo católica q es el código de abajo]

plot(paises.8$Alfabet, paises.8$Esp.vida.Fem, main = "Comparativa:", xlab = "Porcentaje de Alfabetización", ylab =  "Esperanza de Vida Femenina", col = "black")
points(paisesCat$Alfabet, paisesCat$Esp.vida.Fem, col = "gold")
abline(lm(paises.8$Esp.vida.Fem ~ paises.8$Alfabet), col = "pink")
abline(lm(paisesCat$Esp.vida.Fem ~ paisesCat$Alfabet), col = "gold")