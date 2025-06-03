import unittest
import os
import shutil
import tempfile
from organizeDir import organize_by_extension


class TestOrganizeByExtension(unittest.TestCase):
    
    def setUp(self):
        """Create a temporary directory for testing"""
        self.test_dir = tempfile.mkdtemp()
        
    def tearDown(self):
        """Clean up the temporary directory"""
        shutil.rmtree(self.test_dir)
    
    def create_test_file(self, filename):
        """Helper to create a test file"""
        file_path = os.path.join(self.test_dir, filename)
        with open(file_path, 'w') as f:
            f.write("test content")
        return file_path
    
    def test_organize_files_with_extensions(self):
        """Test organizing files with different extensions"""
        # Create test files
        self.create_test_file("test.txt")
        self.create_test_file("image.jpg")
        self.create_test_file("script.py")
        
        # Run organize function
        organize_by_extension(self.test_dir)
        
        # Check that extension directories were created
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "txt")))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "jpg")))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "py")))
        
        # Check that files were moved to correct directories
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "txt", "test.txt")))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "jpg", "image.jpg")))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "py", "script.py")))
    
    def test_organize_files_without_extension(self):
        """Test organizing files with no extension"""
        # Create test file without extension
        self.create_test_file("README")
        self.create_test_file("makefile")
        
        # Run organize function
        organize_by_extension(self.test_dir)
        
        # Check that no_extension directory was created
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "no_extension")))
        
        # Check that files were moved to no_extension directory
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "no_extension", "README")))
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "no_extension", "makefile")))
    
    def test_skip_directories(self):
        """Test that directories are skipped during organization"""
        # Create a subdirectory
        sub_dir = os.path.join(self.test_dir, "existing_folder")
        os.mkdir(sub_dir)
        
        # Create a test file
        self.create_test_file("test.txt")
        
        # Run organize function
        organize_by_extension(self.test_dir)
        
        # Check that the existing directory is still there and unchanged
        self.assertTrue(os.path.exists(sub_dir))
        self.assertTrue(os.path.isdir(sub_dir))
        
        # Check that the file was organized correctly
        self.assertTrue(os.path.exists(os.path.join(self.test_dir, "txt", "test.txt")))
    
    def test_empty_directory(self):
        """Test organizing an empty directory"""
        # Run organize function on empty directory
        organize_by_extension(self.test_dir)
        
        # Directory should remain empty (only original contents)
        contents = os.listdir(self.test_dir)
        self.assertEqual(len(contents), 0)
    
    def test_multiple_files_same_extension(self):
        """Test organizing multiple files with the same extension"""
        # Create multiple text files
        self.create_test_file("file1.txt")
        self.create_test_file("file2.txt")
        self.create_test_file("file3.txt")
        
        # Run organize function
        organize_by_extension(self.test_dir)
        
        # Check that txt directory was created
        txt_dir = os.path.join(self.test_dir, "txt")
        self.assertTrue(os.path.exists(txt_dir))
        
        # Check that all files were moved to txt directory
        txt_contents = os.listdir(txt_dir)
        self.assertIn("file1.txt", txt_contents)
        self.assertIn("file2.txt", txt_contents)
        self.assertIn("file3.txt", txt_contents)
        self.assertEqual(len(txt_contents), 3)


if __name__ == "__main__":
    unittest.main()
