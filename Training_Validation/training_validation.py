from Data_Validation.validate_data import Data_Validation
from os import listdir
from Transform_Data.transform_data import Transform_Data

class Training_Validation:

    def __init__(self):
        self.path = "Training_Batch_Files"
        self.dv = Data_Validation()
        self.td = Transform_Data()


    def validate_data(self):
        lengthOfTimeStampInFile, lengthOfDateStampInFile,numberofColumns,sampleFileName = self.dv.getValuesFromSchema()
        regex = self.dv.manualRegexCreation()
        self.dv.validatefile(regex,lengthOfDateStampInFile,lengthOfTimeStampInFile)
        self.dv.validateColumn(numberofColumns)
        self.dv.validateMissingValuesInWholeColumn()
        self.td.putNull()
<<<<<<< Updated upstream
=======
        self.db.createTable("Training_Data",column_names)
        # self.db.savetoDB("Training_Data")

>>>>>>> Stashed changes



