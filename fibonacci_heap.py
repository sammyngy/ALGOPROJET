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
            
        return min_value

    def delete_min(self) -> int:
        """
        Supprime et retourne la valeur minimum dans l'arbre
        """
        min_value = self.find_min()
        if min_value is not None:
            self.trees.remove(min_value)
        
    def merge(self, fibonnaci_heap: Heap) -> None:
        """
        Fusionne deux arbres
        """
        main_tree = heap.trees
        added_tree = heap2.trees
        merged_trees = added_tree + main_tree

        return merged_trees 

# main_tree
heap = FibonacciHeap()
heap.insert(15)
heap.insert(7)
heap.insert(19)
heap.insert(20)
print("Arbre 1 crée : ", heap.trees)
print("Minimum à supprimer : ", heap.find_min())
heap.delete_min()
print('----------------------------')

# added_tree
heap2 = FibonacciHeap()
heap2.insert(2)
heap2.insert(84)
heap2.insert(50)
print("Arbre 2 crée : ", heap2.trees)
print("Minimum à supprimer : ", heap2.find_min())
heap2.delete_min()
heap2.merge(heap2)

print('----------------------------')
print("Fusion des arbres : ", heap2.merge(heap))
