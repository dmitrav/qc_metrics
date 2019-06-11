import os, sqlite3

class qcdb:
    def __init__(self):
        self.file = "qcdb.sqlite"
        self.path = "/mnt/nas2/"
        self.indicators = ()

    def createDB(self):
        db = sqlite3.connect(os.path.join(self.path, self.file))
        c = db.cursor()

        c.execute('''create table samples
            (   AcqTime text,
                User text,
                ContentMD5 text,
                Comment text,
                Mix text,
                Method text,
                Instrument text,
                InstrumentModel text,
                InstrumentSerial text,
                InstrumentFW text,
                InstrumentSW text,
                Prop1 numeric,
                Prop2 numeric,
                Prop3 numeric,
                Prop4 numeric,
                Prop5 numeric   
                ) ''')

        c.execute('''create table indicators
            (ind_id integer primary key,
                short text,
                long text
                ) ''')

        c.execute("insert into indicators values (1,'Prop1','blah blah')")
        c.execute("insert into indicators values (2,'Prop2','blah blah')")
        c.execute("insert into indicators values (3,'Prop3','blah blah')")
        c.execute("insert into indicators values (4,'Prop4','blah blah')")
        c.execute("insert into indicators values (5,'Prop5','blah blah')")

        db.commit()
        db.close()

    def addRecord(self,d):
        db = sqlite3.connect(os.path.join(self.path, self.file))
        c = db.cursor()

        keys = (d["AcqTime"][0:19].replace("T", " "), d["User"],d["ContentMD5"], d["Mix"],
                d["Comment"], d["Method"], d["Instrument"], d["InstrumentModel"], d["InstrumentSerial"],
                d["InstrumentFW"], d["InstrumentSW"],d["prop1"],d["prop2"],d["prop3"],d["prop4"],d["prop5"])

        c.execute("insert into samples values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)", keys)


if __name__ == '__main__':
    # this is just for debugging
    pass