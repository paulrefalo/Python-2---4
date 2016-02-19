"""
classFactory: function to return tailored classes
"""

def build_row(table, cols):
    """Build a class that creates instances of specific rows"""
    class DataRow:
        """Generic data row clas, specialized by surrouding function"""
        def __init__(self, data):
            """Uses data and column names to inject attributes"""
            assert len(data) == len(self.cols)
            for colname, dat in zip(self.cols, data):
                setattr(self, colname, dat)
        def __repr__(self):
            return "{0}_record({1})".format(self.table, ", ".join(["{0!r}".format(getattr(self, c)) for c in self.cols]))
        def retrieve(self, curs, condition=None):
            if ( condition ):
                sql = "SELECT * FROM %s WHERE %s" %(table, condition)
            else:
                sql = "SELECT * FROM %s" %(table)
                
            curs.execute(sql)
            for row in curs.fetchall():
                yield DataRow(row)
            
                                                            
        
    DataRow.table = table
    DataRow.cols = cols.split()
    return DataRow