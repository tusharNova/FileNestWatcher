<?php
// Function to create the nested directory structure
function create_nested_directory($path) {
    if (!file_exists($path)) {
        mkdir($path, 0777, true);
    }
}

// Directory to save uploaded files (same directory as the PHP script)
$uploadDirectory = dirname(__FILE__) . '/';

// Check if the form was submitted
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    foreach ($_FILES as $fileArray) {
        // Iterate over the files array
        foreach ($fileArray['name'] as $key => $filePath) {
            $fileTmpPath = $fileArray['tmp_name'][$key];
            $destPath = $uploadDirectory . $filePath;

            // Create the nested directory structure
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
