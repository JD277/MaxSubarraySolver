class MaxSubarraySolver:
    def __init__(self, gains):
        """
        Inicializa el solucionador con el arreglo de ganancias diarias.
        :param gains: Lista de enteros (ganancias o pérdidas por día)
        """
        if not gains:
            raise ValueError("El arreglo de ganancias no puede estar vacío.")
        self.gains = gains
        self.n = len(gains)

    def _max_crossing_subarray(self, low, mid, high):
        """
        Calcula la subsecuencia de máxima suma que cruza el punto medio.
        Devuelve los índices de inicio y fin, y la suma máxima.
        """
        # Máxima suma desde mid hacia la izquierda
        left_sum = float('-inf')
        total = 0
        max_left = mid
        for i in range(mid, low - 1, -1):
            total += self.gains[i]
            if total > left_sum:
                left_sum = total
                max_left = i

        # Máxima suma desde mid+1 hacia la derecha
        right_sum = float('-inf')
        total = 0
        max_right = high
        for i in range(mid + 1, high + 1):
            total += self.gains[i]
            if total > right_sum:
                right_sum = total
                max_right = i

        return max_left, max_right, left_sum + right_sum

    def solve_divide_conquer(self, low=0, high=None):
        """
        Algoritmo Divide y Vencerás para encontrar la subsecuencia contigua
        de máxima suma. Devuelve (inicio, fin, suma_máxima).
        """
        if high is None:
            high = self.n - 1

        # Caso base: un solo elemento
        if low == high:
            return low, high, self.gains[low]

        mid = (low + high) // 2

        # Resolver recursivamente izquierda y derecha
        left_low, left_high, left_sum = self.solve_divide_conquer(low, mid)
        right_low, right_high, right_sum = self.solve_divide_conquer(mid + 1, high)
        cross_low, cross_high, cross_sum = self._max_crossing_subarray(low, mid, high)

        # Devolver el mejor de los tres casos
        if left_sum >= right_sum and left_sum >= cross_sum:
            return left_low, left_high, left_sum
        elif right_sum >= left_sum and right_sum >= cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum

    def solve(self):
        """
        Método público para resolver el problema.
        Devuelve un diccionario con:
        - 'inicio': índice de inicio (1-indexed, como en el enunciado)
        - 'fin': índice de fin (1-indexed)
        - 'suma': suma máxima obtenida
        """
        inicio, fin, suma = self.solve_divide_conquer()
        # Convertir a 1-indexed para coincidir con el enunciado (día 1, no día 0)
        return {
            'inicio': inicio + 1,
            'fin': fin + 1,
            'suma': suma
        }
    
algorithm = MaxSubarraySolver([-2, 1, -3, 4, -1, 2, 1, -5, 4])
result = algorithm.solve()
print(result)