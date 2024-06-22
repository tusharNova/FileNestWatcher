# FileNestWatcher

FileNestWatcher is a Python-based file monitoring tool that automatically uploads new or modified files from a local directory to a server using a PHP-based uploader. The project ensures that the nested directory structure of the local files is preserved on the server.

## Features
- Monitors a specified directory for new or modified files
- Automatically uploads files to a server with their respective nested directory paths.
- PHP script handles file uploads and creates necessary directories on the server.

## Prerequisites
- Python 3.x
- PHP 5.x or later
- A web server (e.g., Apache, Nginx) to host the PHP script


## Installation

1.  Clone the Repository
   ```sh
     git clone https://github.com/yourusername/filenestwatcher.git
     cd filenestwatcher
  ```
2. Install Python Dependencies
   ```sh
      pip install watchdog requests
   ```
3. Set Up the PHP Uploader
   1. Create a file named `upload.php` in your web server's document root (e.g., /var/www/html/).
   2. Copy the following PHP code into the `upload.php` file:
     ```sh
     <?php
      
      function create_nested_directory($path) {
          if (!file_exists($path)) {
              mkdir($path, 0777, true);
          }
      }
      
     
      $uploadDirectory = dirname(__FILE__) . '/';
      
      
      if ($_SERVER['REQUEST_METHOD'] === 'POST') {
          foreach ($_FILES as $fileArray) {
              foreach ($fileArray['name'] as $key => $filePath) {
                  $fileTmpPath = $fileArray['tmp_name'][$key];
                  $destPath = $uploadDirectory . $filePath;
      
                 
                  $directoryPath = dirname($destPath);
                  create_nested_directory($directoryPath);
      
                  if (move_uploaded_file($fileTmpPath, $destPath)) {
                      echo "The file " . basename($filePath) . " has been uploaded successfully.<br>";
                  } else {
                      echo "There was an error uploading the file " . basename($filePath) . ".<br>";
                  }
              }
          }
      }
      ?>
     ```

4. Configure the Python Script
      Edit the `file_watcher.py` script and update the following variables:
      ```sh
      directory_to_watch = "path/to/your/folder"  # Update this path
      server_url = "http://yourserver.com/upload.php"  # Update this URL

      ```
5. Run the Python Script
      ```sh 
         python file_watcher.py
      ```

## Usage
1. Ensure your web server is running and the `upload.php` script is accessible via the specified URL.
2. The Python script will start monitoring the specified directory for new or modified files.
3. When a file is created or modified, it will be automatically uploaded to the server, preserving the directory structure.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## Contact
For any questions or suggestions, please contact [tusharmankar02@gmail.com].

hr
Feel free to modify the content to better suit your needs and provide specific details where placeholders are used.



