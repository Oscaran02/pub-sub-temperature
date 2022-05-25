# pub-sub-temperature
## Tareas faltantes
### Oscar
* Cada medición debe ir acompañada del tiempo (u hora) en el cual se produjo
* Monitores: son procesos que reciben las medidas de los sensores, validan que los datos no contengan errores y se encuentren en rangos razonables. Los monitores almacenan todas las medidas sin errores, aunque estén fuera del rango. Cada vez que encuentran una medida fuera del rango deben generar una alarma al sistema de calidad
* Sistema de Calidad (SC)
* La comunicación entre los monitores y el sistema de calidad se puede realizar utilizando cualquiera de los otros patrones que ofrezca la librería ZeroMQ 

### Diana y Gabriel
* Debe existir también otro proceso encargado de chequear que todos los monitores están o no en funcionamiento (health check). 
* Defina variables que permitan medir el rendimiento de su sistema, por ejemplo: tiempo de almacenamiento de cada medición (tiempo en llegar desde el sensor a la BD), tiempo en que tarda la llegada de cada alarma al sistema de calidad (desde el monitor que la detecta, hasta que se imprime), utilización de los procesadores, etc.  Debe definir al menos dos tipos de variables. 
* es incorporar un elemento a su sistema que afecte su desempeño
* Aumentar la carga: disminuir el tiempo de generación de medidas desde los sensores o aumentar el número de sensores

### Veremos
* Operaciones que van realizando cada uno de los procesos y resultado de la operación

## Documento 
* Plantee una hipótesis. 
* Realice medidas (experimentación) para comparar el sistema A con el B 
* Análisis sus resultados
* Exponga las conclusiones
