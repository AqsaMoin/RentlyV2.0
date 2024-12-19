<?php
session_start();
require 'db_connect.php';

// Enable error reporting for debugging
error_reporting(E_ALL);
ini_set('display_errors', 1);

if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_SESSION['user_id'])) {
    $user_id = $_SESSION['user_id'];
    $product_id = $_POST['product_id'];

    echo "Product ID: " . htmlspecialchars($product_id); // Debugging line

    // Check if the product exists
    $product_check_stmt = $conn->prepare("SELECT id FROM products WHERE id = ?");
    $product_check_stmt->bind_param("i", $product_id);
    $product_check_stmt->execute();
    $product_check_stmt->store_result();
    
    if ($product_check_stmt->num_rows > 0) {
        // Add to cart logic (e.g., insert into a cart table)
        $stmt = $conn->prepare("INSERT INTO cart (user_id, product_id) VALUES (?, ?)");
        $stmt->bind_param("ii", $user_id, $product_id);

        if ($stmt->execute()) {
            // Ensure no output before header()
            header("Location: ../html/cart.html");
            exit();
        } else {
            echo "Error: " . $stmt->error;
        }

        $stmt->close();
    } else {
        echo "Error: Product not found.";
    }

    $product_check_stmt->close();
    $conn->close();
} else {
    echo "Invalid request.";
}
?>
