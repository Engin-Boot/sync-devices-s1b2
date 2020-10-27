import unittest
import InventoryManager as mainfile


class TestReadLogs(unittest.TestCase):

    def test_when_inventory_file_is_not_present_at_path_then_return_0_and_print_error_statement(self):
        #checking both checkProcedureAndOperate() and checkInventoryFile()

        mainfile.InventoryPath = "temp-test.csv"
        value=mainfile.checkProcedureAndOperate("cardiac")

        self.assertTrue(value == 0)
        self.assertTrue(mainfile.checkInventoryFile("temp-test.csv")==False)


    def test_when_the_inventory_file_is_in_correct_format(self):
        
        testfilepath = "test-watcher3.csv"
        value = mainfile.checkInventoryFile(testfilepath)
        self.assertTrue(value == True)


    def test_when_the_inventory_file_is_in_incorrect_format(self):
        
        testfilepath = "test-watcher1.csv"
        value = mainfile.checkInventoryFile(testfilepath)
        self.assertTrue(value == False)


    def test_when_the_procedure_performed_is_not_present_in_procedure_record_then_return_0_and_print_error_statement(self):
       
        value=mainfile.checkProcedureAndOperate("heart")
        self.assertTrue(value==0)


    def test_when_inventory_count_of_a_item_is_more_then_3_then_mail_is_not_sent_and_0_is_return(self):
        count=6
        value=mainfile.checkItemCountAndSendMail(count,"cardiac")
        self.assertTrue(value==0)


    def test_when_modified_patientinfo_csv_file_is_read_then_its_last_line_procedure_column_data_is_stored(self):
        #deep,10,M,brain,
        testfilepath="test-watcher1.csv"
        value=mainfile.import_csv(testfilepath)
        self.assertTrue(value=="brain")


    def test_when_patientinfo_csv_file_is_not_in_correct_format(self):
        testfilepath="test-watcher2.csv"
        value=mainfile.checkPatientFileFormat(testfilepath)
        self.assertTrue(value==False)


    def test_when_patientinfo_csv_file_is_in_correct_format(self):
        #deep,10,M,brain,
        testfilepath = "test-watcher1.csv"
        value = mainfile.checkPatientFileFormat(testfilepath)
        self.assertTrue(value == True)

if __name__ == '__main__':
    unittest.main()
