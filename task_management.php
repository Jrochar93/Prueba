<?php
// Configuración de la conexión a la base de datos
$host = 'localhost';
$dbname = 'nombre_de_tu_base_de_datos';
$user = 'tu_usuario';
$pass = 'tu_contraseña';

// Conexión a la base de datos
try {
    $pdo = new PDO("pgsql:host=$host;dbname=$dbname", $user, $pass);
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

    // Consulta SQL para obtener todas las tareas
    $sql = 'SELECT name, description, is_completed, date_deadline FROM task_management';
    $stmt = $pdo->query($sql);

    // Mostrar las tareas en una tabla HTML
    echo "<table border='1'>";
    echo "<tr><th>Título</th><th>Descripción</th><th>Estado</th><th>Fecha Límite</th></tr>";
    
    while ($row = $stmt->fetch(PDO::FETCH_ASSOC)) {
        echo "<tr>";
        echo "<td>" . htmlspecialchars($row['name']) . "</td>";
        echo "<td>" . htmlspecialchars($row['description']) . "</td>";
        echo "<td>" . ($row['is_completed'] ? 'Completada' : 'Pendiente') . "</td>";
        echo "<td>" . htmlspecialchars($row['date_deadline']) . "</td>";
        echo "</tr>";
    }
    
    echo "</table>";
    
} catch (PDOException $e) {
    echo "Error: " . $e->getMessage();
}

// Cerrar la conexión
$pdo = null;
?>
