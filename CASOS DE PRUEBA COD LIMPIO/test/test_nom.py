#Importar biblioteca unittes

import unittest

from nomina import calcular_total_devengado, calcular_deducciones, calcular_salario_neto
#crear clase con casos de prueba 

class pruebas_Nom(unittest.TestCase):
    
    def test_caso_1(self):
        # Datos de entrada
        salario_base = 2000000
        horas_extra = 0
        tarifa_hora_extra = 0
        porcentaje_salud = 4
        porcentaje_pension = 4
        otras_deducciones = 0
        
        # Valores esperados
        esperado_total_devengado = 2000000
        esperado_total_deducciones = 160000
        esperado_salario_neto = 1840000
        
        # Cálculos
        total_devengado = calcular_total_devengado(salario_base, horas_extra, tarifa_hora_extra)
        total_deducciones = calcular_deducciones(salario_base, porcentaje_salud, porcentaje_pension, otras_deducciones)
        salario_neto = calcular_salario_neto(total_devengado, total_deducciones)
        
        #Mostrar resultado en consoloa
        print(f"\nCaso 1:")
        print(f"Total devengado calculado: {total_devengado}, esperado: {esperado_total_devengado}")
        print(f"Total deducciones calculado: {total_deducciones}, esperado: {esperado_total_deducciones}")
        print(f"Salario neto calculado: {salario_neto}, esperado: {esperado_salario_neto}")
        
        # Verificaciones
        self.assertEqual(total_devengado, esperado_total_devengado, "Error en el cálculo de total devengado")
        self.assertEqual(total_deducciones, esperado_total_deducciones, "Error en el cálculo de total deducciones")
        self.assertEqual(salario_neto, esperado_salario_neto, "Error en el cálculo de salario neto")
        
    def test_caso_2(self):
        # Datos de entrada
        salario_base = 2200000
        horas_extra = 10
        tarifa_hora_extra = 15000
        porcentaje_salud = 4
        porcentaje_pension = 4
        otras_deducciones = 0
        
        # Valores esperados
        esperado_total_devengado = 2350000
        esperado_total_deducciones = 176000
        esperado_salario_neto = 2174000
        
        # Cálculos
        total_devengado = calcular_total_devengado(salario_base, horas_extra, tarifa_hora_extra)
        total_deducciones = calcular_deducciones(salario_base, porcentaje_salud, porcentaje_pension, otras_deducciones)
        salario_neto = calcular_salario_neto(total_devengado, total_deducciones)
        
        #Mostrar resultado en consola
        print(f"\nCaso 2:")
        print(f"Total devengado calculado: {total_devengado}, esperado: {esperado_total_devengado}")
        print(f"Total deducciones calculado: {total_deducciones}, esperado: {esperado_total_deducciones}")
        print(f"Salario neto calculado: {salario_neto}, esperado: {esperado_salario_neto}")
        
        # Verificaciones
        self.assertEqual(total_devengado, esperado_total_devengado, "Error en el cálculo de total devengado")
        self.assertEqual(total_deducciones, esperado_total_deducciones, "Error en el cálculo de total deducciones")
        self.assertEqual(salario_neto, esperado_salario_neto, "Error en el cálculo de salario neto")
        
    def test_caso_3(self):
        # Datos de entrada
        salario_base = 3000000
        horas_extra = 5
        tarifa_hora_extra = 20000
        porcentaje_salud = 4
        porcentaje_pension = 4
        otras_deducciones = 60000  
        
        # Valores esperados
        esperado_total_devengado = 3100000
        esperado_total_deducciones = 300000
        esperado_salario_neto = 2800000
        
        # Cálculos
        total_devengado = calcular_total_devengado(salario_base, horas_extra, tarifa_hora_extra)
        total_deducciones = calcular_deducciones(salario_base, porcentaje_salud, porcentaje_pension, otras_deducciones)
        salario_neto = calcular_salario_neto(total_devengado, total_deducciones)
        
        #Mostrar resultado en consola
        print(f"\nCaso 3:")
        print(f"Total devengado calculado: {total_devengado}, esperado: {esperado_total_devengado}")
        print(f"Total deducciones calculado: {total_deducciones}, esperado: {esperado_total_deducciones}")
        print(f"Salario neto calculado: {salario_neto}, esperado: {esperado_salario_neto}")
        
        # Verificaciones
        self.assertEqual(total_devengado, esperado_total_devengado, "Error en el cálculo de total devengado")
        self.assertEqual(total_deducciones, esperado_total_deducciones, "Error en el cálculo de total deducciones")
        self.assertEqual(salario_neto, esperado_salario_neto, "Error en el cálculo de salario neto")
        
        #caso prueba 4 #EN PROCESO
        
    def test_caso_4(self):
    #"""Caso 4: Salario mínimo con muchas horas extras"""
    # Datos de entrada
        salario_base = 1423500
        horas_extra = 80
        tarifa_hora_extra = 12000
        porcentaje_salud = 4
        porcentaje_pension = 4
        otras_deducciones = 0

    # Valores esperados
        esperado_total_devengado = 2383500
        esperado_total_deducciones = 190680
        esperado_salario_neto = 2192820

    # Cálculos
        total_devengado = calcular_total_devengado(salario_base, horas_extra, tarifa_hora_extra)
        total_deducciones = calcular_deducciones(total_devengado, porcentaje_salud, porcentaje_pension, otras_deducciones)
        salario_neto = calcular_salario_neto(total_devengado, total_deducciones)
        
    # Mostrar resultados en consola
        print(f"\nCaso 4:")
        print(f"Total devengado calculado: {total_devengado}, esperado: {esperado_total_devengado}")
        print(f"Total deducciones calculado: {total_deducciones}, esperado: {esperado_total_deducciones}")
        print(f"Salario neto calculado: {salario_neto}, esperado: {esperado_salario_neto}")

    # Verificaciones
        self.assertEqual(total_devengado, esperado_total_devengado, "Error en el cálculo de total devengado")
        self.assertEqual(total_deducciones, esperado_total_deducciones, "Error en el cálculo de total deducciones")
        self.assertEqual(salario_neto, esperado_salario_neto, "Error en el cálculo de salario neto")
        
    def test_caso_5(self):
        #Caso 5: Licencia no remunerada (sin ingresos, pero con deducciones)"""
        # Datos de entrada
        salario_base = 3000000
        horas_extra = 0
        tarifa_hora_extra = 0
        porcentaje_salud = 4
        porcentaje_pension = 4
        otras_deducciones = 0
            
        # Valores esperados
        esperado_total_devengado = 0  # No trabajó, no hay devengado
        esperado_total_deducciones = 240000  # 4% salud + 4% pensión sobre 3.000.000
        esperado_salario_neto = -240000  # Deuda con la empresa
        
        # Cálculos
        total_devengado = 0
        total_deducciones = calcular_deducciones(salario_base, porcentaje_salud, porcentaje_pension, otras_deducciones)
        salario_neto = calcular_salario_neto(total_devengado, total_deducciones)
        
        print(f"\nCaso 5:")
        print(f"Total devengado calculado: {total_devengado}, esperado: {esperado_total_devengado}")
        print(f"Total deducciones calculado: {total_deducciones}, esperado: {esperado_total_deducciones}")
        print(f"Salario neto calculado: {salario_neto}, esperado: {esperado_salario_neto}")
        
        # Verificaciones
        self.assertEqual(total_devengado, esperado_total_devengado, "Error en el cálculo de total devengado")
        self.assertEqual(total_deducciones, esperado_total_deducciones, "Error en el cálculo de total deducciones")
        self.assertEqual(salario_neto, esperado_salario_neto, "Error en el cálculo de salario neto")
        
    def test_caso_6(self):  
        #"""Caso 6: Salario alto con retención en la fuente"""
         # Datos de entrada
        salario_base = 15000000
        horas_extra = 0
        tarifa_hora_extra = 0
        porcentaje_salud = 4
        porcentaje_pension = 4
        otras_deducciones = 0
        retencion_fuente = (10 / 100 ) * salario_base # 10% de retención en la fuente

    #     # Valores esperados
        esperado_total_devengado = 15000000  # No hay horas extras
        esperado_total_deducciones = 2700000  # Salud (4%) + Pensión (4%) + Retención (10%)
        esperado_salario_neto = 12300000  # Salario después de deducciones

    #     # Cálculos
        total_devengado = calcular_total_devengado(salario_base, horas_extra, tarifa_hora_extra)
        total_deducciones = calcular_deducciones(salario_base, porcentaje_salud, porcentaje_pension, otras_deducciones + retencion_fuente)
        salario_neto = calcular_salario_neto(total_devengado, total_deducciones)

    # # Mostrar valores para depuración
        print(f"\nCaso 6:")
        print(f"Total devengado: {total_devengado} (esperado: {esperado_total_devengado})")
        print(f"Retención en la fuente: {retencion_fuente}")
        print(f"Total deducciones: {total_deducciones} (esperado: {esperado_total_deducciones})")
        print(f"Salario neto: {salario_neto} (esperado: {esperado_salario_neto})")

    # # Verificaciones
        self.assertEqual(total_devengado, esperado_total_devengado, "Error en el cálculo de total devengado")
        self.assertEqual(total_deducciones, esperado_total_deducciones, "Error en el cálculo de total deducciones")
        self.assertEqual(salario_neto, esperado_salario_neto, "Error en el cálculo de salario neto")
           
    def error_de_salrio_negativo7 (self):
       
        S_base	= -2000000 
        H_extras = 0	
        Tarifa_hora_extra = 0	
        Deducción_salud	= 0.4
        Deducción_pensión = 0.4	
        Otras_deducciones = 0
        TotalDevengado = -2000000	
        Total_deducciones = -160000	
        Total_a_pagar = -1840000




    

    
# Ejecutar las pruebas
if __name__ == '__main__':
    unittest.main()
    


    
    