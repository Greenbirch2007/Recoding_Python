


class LookingGlass:

    def __enter__(self):
        import sys
        self.original_write = sys.stdout.write
        sys.stdout.write =  self.reverse_write
        return 'JABASRWERWR'

    def reverse_write(self,text):
        self.original_write(text[::-1])

    def __exit__(self, exc_type, exc_val, traceback):
        import sys
        sys.stdout.write = self.original_write
        if exc_type is ZeroDivisionError:
            print('Please Do Not divide by zero!')
            return True