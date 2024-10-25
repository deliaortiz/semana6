class Producto():
    def __init__(self, nombre, precio):
        self.__nombre = nombre
        self.__precio = precio

    def get_nombre(self):
        return self.__nombre
    
    def get_precio(self):
        return self.__precio
    
    def mostrar_producto(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")
    
class Camisa(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self.__talla = talla

    def get_talla(self):
        return self.__talla

    def mostrar_producto(self):
        return f"Camisa: {self.get_nombre()}, Precio: {self.get_precio()}, Talla: {self.get_talla()}"
    
class Pantalon(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self.__talla = talla

    def get_talla(self):
        return self.__talla

    def mostrar_producto(self):
        return f"Pantalon: {self.get_nombre()}, Precio: {self.get_precio()}, Talla: {self.get_talla()}"
    
class Zapatos(Producto):
    def __init__(self, nombre, precio , talla):
        super().__init__(nombre, precio)
        self.__talla = talla

    def get_talla(self):
        return self.__talla
    
    def mostrar_producto(self):
        return f"Zapato: {self.get_nombre()}, Precio: {self.get_precio()}, Talla: {self.get_talla()}"
    
class Categoria():
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto (self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        print(f"Categoria: {self.nombre}")
        for producto in self.productos:
            print(producto.mostrar_producto())
        
class Tienda ():
    def __init__(self):
        self.categorias = []

    def agregar_categoria(self, categoria):
                self.categorias.append(categoria)

    def mostrar_inventario(self):
        for categoria in self.categorias:
                categoria.mostrar_productos()
        
    def procesar_compra(self, productos_seleccionados):
            total = sum(producto.get_precio() for producto in productos_seleccionados)
            print(f"Total de la compra: ${total:.2f}")

if __name__ == "__main__":

    #Crear producto
    camisa1 = Camisa("Camisa Azul",20.00, "M")
    pantalon1 = Pantalon("Pantalón Negro",30.00,"L")
    zapato1 = Zapatos("Zapato",50.00,"40")

    categoria_ropa = Categoria ("Ropa")
    categoria_ropa.agregar_producto(camisa1)
    categoria_ropa.agregar_producto(pantalon1)

    categoria_calzado = Categoria("Calzado")
    categoria_calzado.agregar_producto(zapato1)
    #crear tienda y agregar categorias
    tienda = Tienda()
    tienda.agregar_categoria(categoria_ropa)
    tienda.agregar_categoria(categoria_calzado)

    tienda.mostrar_inventario()
    productos_seleccionados = [camisa1, pantalon1]
    tienda.procesar_compra(productos_seleccionados)