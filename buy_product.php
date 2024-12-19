<?php
require 'db_connect.php';
session_start();

if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_SESSION['user_id'])) {
    $user_id = $_SESSION['user_id'];
    $product_id = $_POST['product_id'];

    // Buy logic (e.g., insert into a transactions table)
    $stmt = $conn->prepare("INSERT INTO transactions (user_id, product_id, amount) SELECT ?, id, price FROM products WHERE id = ?");
    $stmt->bind_param("ii", $user_id, $product_id);

    if ($stmt->execute()) {
        echo "Purchase successful!";
        header("Location: ../html/payment.html"); // Redirect to a success page (implement this as needed)
        exit();
    } else {
        echo "Error: " . $stmt->error;
    }

    $stmt->close();
    $conn->close();
}
?>
