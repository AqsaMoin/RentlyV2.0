<?php
require 'db_connect.php';
session_start();

// Enable error reporting for debugging
error_reporting(E_ALL);
ini_set('display_errors', 1);

if ($_SERVER['REQUEST_METHOD'] == 'POST' && isset($_SESSION['user_id'])) {
    $id = $_SESSION['id'];
    $user_id = $_SESSION['user_id'];
    $product_id = $_POST['product_id'];
    $price = $_POST['amount'];
    $date = $_POST['payment_date'];

    // Insert payment record
    $stmt_payment = $conn->prepare("INSERT INTO payments (user_id, product_id, amount) VALUES (?, ?, ?)");
    $stmt_payment->bind_param("iiids", $id,$user_id, $product_id, $price,$date);

    if ($stmt_payment->execute()) {
        // Insert transaction record
        $stmt_transaction = $conn->prepare("INSERT INTO transactions (id,user_id, product_id, transaction_date,amount) VALUES (?,?,?, ?, ?)");
        $stmt_transaction->bind_param("iiisd", $id,$user_id, $product_id, $transaction_date,$price);

        if ($stmt_transaction->execute()) {
            // Redirect to success page
            header("Location: ../html/purchase_success.html");
            exit();
        } else {
            echo "Error: " . $stmt_transaction->error;
        }

        $stmt_transaction->close();
    } else {
        echo "Error: " . $stmt_payment->error;
    }

    $stmt_payment->close();
    $conn->close();
} else {
    echo "Invalid request.";
}
?>
