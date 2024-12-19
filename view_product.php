<?php
require 'db_connect.php';

// Fetch all product details including image paths
$stmt = $conn->prepare("SELECT id, product_name, description, price, image FROM products");
$stmt->execute();
$stmt->bind_result($id, $product_name, $description, $price, $image_path);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>View Products</title>
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/5.3.0/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container">
        <h2 class="mt-5">Available Products</h2>
        <div class="row">
            <?php while ($stmt->fetch()): ?>
                <div class="col-md-4 mb-4">
                    <div class="card">
                        <img src="<?php echo htmlspecialchars($image_path); ?>" class="card-img-top" alt="Product Image">
                        <div class="card-body">
                            <h5 class="card-title"><?php echo htmlspecialchars($product_name); ?></h5>
                            <p class="card-text"><?php echo nl2br(htmlspecialchars($description)); ?></p>
                            <p class="card-text">$<?php echo htmlspecialchars($price); ?></p>
                        </div>
                    </div>
                </div>
            <?php endwhile; ?>
            <br>
            <p>This is the end of the results:(</p>
            <p>We will add more products for you in the near future</p>
        </div>
    </div>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/5.3.0/js/bootstrap.bundle.min.js"></script>
</body>
</html>

<?php
$stmt->close();
$conn->close();
?>
