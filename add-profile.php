<?php
require 'db_connect.php';
session_start();

if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_SESSION['user_id'])) {
    $user_id = $_SESSION['user_id'];
    $first_name = $_POST['first_name'];
    $last_name = $_POST['last_name'];

    // Insert profile data into the profiles table
    $stmt = $conn->prepare("INSERT INTO profiles (user_id, first_name, last_name) VALUES (?, ?, ?)");
    $stmt->bind_param("iss", $user_id, $first_name, $last_name);

    if ($stmt->execute()) {
        echo "Profile added successfully!";
    } else {
        echo "Error: " . $stmt->error;
    }

    $stmt->close();
    $conn->close();
}
?>
