# 📝 Documentación de Pruebas de la Calculadora

Este documento describe las pruebas implementadas y propuestas para la aplicación de calculadora en Python (`calculator.py`).

---

## 1. Pruebas Unitarias Implementadas

Las pruebas unitarias están implementadas en el archivo `calculator.py` dentro de la clase `TestCalculator` (utilizando el módulo `unittest` de Python).

| ID de Prueba | Método Testeado | Descripción | Resultado Esperado |
| :----------: | :-------------: | :---------- | :----------------- |
| **UT-001** | `add(a, b)`     | Verifica que la suma de dos números positivos sea correcta. (`10 + 5`) | `15` |
| **UT-002** | `divide(a, b)`  | Verifica que el método levante un `ValueError` al intentar dividir por cero. | Lanzamiento de excepción `ValueError` |

---

## 2. Caso de Prueba de Integración (IT-001)

### 📌 Caso de Prueba: Operaciones Encadenadas

**Propósito:** Verificar el correcto funcionamiento del sistema cuando múltiples funciones se utilizan de forma secuencial, simulando una cadena de operaciones típica de un usuario. Este caso garantiza que la salida de una función se pueda utilizar correctamente como entrada para la siguiente sin errores de tipo o lógica.

| Paso | Acción | Valor Esperado del Resultado |
| :--: | :----- | :--------------------------- |
| 1    | Inicializar el resultado con una suma: `add(5, 3)` | `8` |
| 2    | Usar el resultado anterior para multiplicar: `multiply(8, 2)` | `16` |
| 3    | Usar el resultado anterior para restar: `subtract(16, 6)` | `10` |
| 4    | Usar el resultado anterior para dividir: `divide(10, 5)` | `2.0` |

**Resultado Final Esperado:** El resultado final de la cadena de operaciones es **$2.0$**.

---

## 3. Propuesta de Prueba de Rendimiento (PT-001)

### ⚙️ Prueba: Cálculo de Alta Frecuencia

**Propósito:** Evaluar la velocidad y el impacto del consumo de recursos del sistema bajo una carga de trabajo extrema y repetitiva. Esta prueba confirma que la calculadora mantiene un rendimiento óptimo al ser usada en entornos que requieren una gran cantidad de cálculos rápidos.

| Métrica | Descripción | Parámetros | Umbral de Éxito |
| :------ | :---------- | :--------- | :-------------- |
| **Tiempo de Ejecución** | Medir el tiempo total que tarda el sistema en realizar una operación simple un gran número de veces. | Repetir la operación `calc.add(1, 1)` **$100,000$ veces** dentro de un bucle. | La ejecución completa debe ser **inferior a $100$ milisegundos**. |
| **Consumo de Recursos** | Monitorear la carga de CPU y el consumo de memoria del proceso de Python durante la ejecución del bucle. | N/A | La carga de CPU debe ser **mínima** tras la finalización del bucle, y **no debe haber fugas de memoria** evidentes. |
