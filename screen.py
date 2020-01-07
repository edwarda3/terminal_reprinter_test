import random

class Screen:


    def __init__(self, *args, **kwargs):
        self._initialize(kwargs)
        self._clear_screen()

    def _initialize(self, kwargs):
        self._dimensions = kwargs.get('dimensions', self._get_screen_dimensions())
        (self.max_rows, self.max_cols) = self._dimensions
        self.rows = []

    def _get_screen_dimensions(self):
        import os
        rows, columns = os.popen('stty size', 'r').read().split()
        return (int(rows), int(columns))

    def store_row(self, string):
        (dim_r, dim_c) = self._dimensions
        if(len(self.rows) == dim_r):
            raise Exception(f"Too many rows! max: {dim_r}, have: {str(self.rows)}")
        # if(len(string) > dim_c):
        #     raise Exception(f"String is too long! max: {dim_c}, string is {len(string)} long: "{string})
        # if(len(string) < dim_c):
        #     padding_spaces = dim_c - len(string)
        #     string += ' '*padding_spaces
        self.rows.append(string)

    def draw(self):
        (dim_r, dim_c) = self._dimensions
        if(len(self.rows) < dim_r):
            padding_rows = dim_r - len(self.rows)
            self.rows.extend([' '*dim_c]*padding_rows)
        self._draw_from_rows(self.rows)
        self.rows = []

    def _clear_screen(self):
        (dim_r, dim_c) = self._dimensions
        clear = [' '*dim_c]*dim_r
        print('\n'.join(clear))

    def _draw_from_rows(self, rows):
        (dim_r, dim_c) = self._dimensions
        string_builder = f'\033{dim_r}A' #Back to top
        for row in rows:
            string_builder += '\033[2K' #Delete line
            string_builder += row + '\n'

        print(string_builder + str(random.random()))

