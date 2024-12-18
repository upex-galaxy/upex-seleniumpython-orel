class MyExampleClass:
    """
    Clase de ejemplo para practicar métodos y atributos.
    """

    # Atributos de clase (compartidos por todas las instancias)
    class_attribute = "Valor compartido"

    def __init__(self, instance_attribute1, instance_attribute2):
        """
        Constructor: inicializa los atributos de instancia.
        """
        # Atributos de instancia (específicos para cada objeto)
        self.instance_attribute1 = instance_attribute1
        self.instance_attribute2 = instance_attribute2

    # Métodos de instancia (requieren un objeto para ser llamados)
    def instance_method(self):
        """
        Método de instancia: puede acceder y modificar atributos de instancia.
        """
        print(f"El atributo 1 es: {self.instance_attribute1}")
        print(f"El atributo 2 es: {self.instance_attribute2}")

    def update_instance_attributes(self, new_value1, new_value2):
        """
        Método para actualizar los atributos de instancia.
        """
        self.instance_attribute1 = new_value1
        self.instance_attribute2 = new_value2
        print("Atributos actualizados correctamente.")

    # Método de clase (opera sobre atributos de clase)
    @classmethod
    def class_method(cls, new_class_value):
        """
        Método de clase: trabaja con atributos de clase.
        """
        cls.class_attribute = new_class_value
        print(f"Atributo de clase actualizado a: {cls.class_attribute}")

    # Método estático (no depende de la clase ni de los objetos)
    @staticmethod
    def static_method():
        """
        Método estático: no accede a atributos ni de clase ni de instancia.
        """
        print("Este es un método estático, útil para utilidades o cálculos independientes.")


