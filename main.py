from vfd import VariableFrequencyDrive

vfd1 = VariableFrequencyDrive("VFD-007", 7.5, 380, "54", (0, 400))
vfd2 = VariableFrequencyDrive("Altivar 320", 15.0, 480, "21", (0.1, 500))
vfd3 = VariableFrequencyDrive("SINAMICS V20", 2.2, 230, "20", (0, 200))

print(vfd1.info())
print(vfd2.info())
print(vfd3.info())

# Примеры использования геттеров и сеттеров
print(f"\nМощность vfd1: {vfd1.power} кВт")
print(f"Напряжение vfd1: {vfd1.input_voltage} В")

# Попытка изменить мощность на некорректное значение
try:
    vfd1.power = -5  # вызовет ValueError
except ValueError as e:
    print(f"Ошибка: {e}")

# Вычисляемое свойство speed_range
print(f"\nДиапазон скоростей vfd1: {vfd1.speed_range}")
print(f"Диапазон скоростей vfd2: {vfd2.speed_range}")
print(f"Диапазон скоростей vfd3: {vfd3.speed_range}")