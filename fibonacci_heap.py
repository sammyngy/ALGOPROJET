class Heap(object):
    """
    Une heap est une structure de données sous forme d'arbre.

    https://en.wikipedia.org/wiki/Heap_(data_structure)
    """

    def insert(self, value: int) -> None:
        """
        Ajoute une valeur dans l'arbre
        """
        pass

    def find_min(self) -> int:
        """
        Retourne la valeur minimum dans l'arbre
        """
        pass

    def delete_min(self) -> int:
        """
        Supprime et retourne la valeur minimum dans l'arbre
        """
        pass

    def decrease_key(self, current_value: int, new_value :int) -> None:
        """
        Modify une valeur dans l'arbre
        """
        pass

    def merge(self, fibonnaci_heap: object) -> None:
        """
        Fusionne deux arbres
        """
        pass


class FibonacciHeap(Heap):
    """
    Une fibonnaci heap est un arbre permettant de stocker et trier des donnés efficacement

    https://en.wikipedia.org/wiki/Fibonacci_heap

    L'implémentation est décrite en anglais : https://en.wikipedia.org/wiki/Fibonacci_heap#Implementation_of_operations
    et en français : https://fr.wikipedia.org/wiki/Tas_de_Fibonacci#Implémentation_des_opérations
    """
    def __init__(self):
        self.trees = []
        self.branch = None
   
    

    def insert(self, value: int) -> None:
        """
        Ajoute une valeur dans l'arbre
        """
        self.trees.append(value)

     

    def find_min(self) -> int:
        """
        Retourne la valeur minimum dans l'arbre
        """
        min_value = None 
        for value in self.trees:
            if not min_value:
                min_value = value
            elif value < min_value:
                min_value = value
        print(min_value)
        return min_value

       

    def delete_min(self) -> int:
        """
        Supprime et retourne la valeur minimum dans l'arbre
        """
        min_value = self.find_min()
        if min_value is not None:
            self.trees.remove(min_value)
        pass

    def merge(self, fibonnaci_heap: Heap) -> None:
        """
        Fusionne deux arbres
        """
        new = self.trees + heap
        print(new)
        pass


heap = FibonacciHeap()
heap.insert(5)
heap.insert(1)
heap.insert(10)
heap.insert(0)
heap.insert(42)
heap.insert(15)
heap.insert(7)
heap.insert(19)
heap.insert(20)
heap.insert(2)
heap.insert(84)
heap.insert(50)
heap.find_min()
heap.delete_min()

heap.merge(heap)