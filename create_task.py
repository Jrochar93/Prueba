import psycopg2
import sys

def create_task(title, description, is_completed):
    try:
        # Configuración de la conexión a la base de datos de Odoo
        connection = psycopg2.connect(
            dbname="nombre_de_tu_base_de_datos",
            user="tu_usuario",
            password="tu_contraseña",
            host="localhost",
            port="5432"
        )
        cursor = connection.cursor()

        # Preparar la consulta SQL para insertar una nueva tarea
        insert_query = """
        INSERT INTO task_management (name, description, is_completed, create_date)
        VALUES (%s, %s, %s, NOW())
        """
        # Ejecutar la consulta SQL
        cursor.execute(insert_query, (title, description, is_completed))
        
        # Confirmar los cambios
        connection.commit()
        print("Task created successfully")

    except Exception as error:
        print(f"Error: {error}")
        sys.exit(1)

    finally:
        # Cerrar la conexión
        if connection:
            cursor.close()
            connection.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python create_task.py <title> <description> <is_completed>")
        sys.exit(1)

    title = sys.argv[1]
    description = sys.argv[2]
    is_completed = sys.argv[3].lower() == 'true'

    create_task(title, description, is_completed)
