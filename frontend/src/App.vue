<template>
  <div>
    <h1>Gestión de Usuarios</h1>

    <!-- Formulario para agregar o editar un usuario -->
    <form @submit.prevent="handleSubmit">
      <input v-model="newUser.name" placeholder="Nombre" required />
      <input v-model="newUser.email" placeholder="Email" required />
      <button type="submit">{{ isEditing ? "Guardar Cambios" : "Agregar Usuario" }}</button>
      <button v-if="isEditing" type="button" @click="cancelEdit">Cancelar</button>
    </form>

    <!-- Mostrar la lista de usuarios -->
    <h2>Lista de Usuarios</h2>
    <ul>
      <li v-for="user in users" :key="user.id">
        {{ user.name }} ({{ user.email }})
        <button @click="editUser(user)" style="margin-left: 10px;">Editar</button>
        <button @click="confirmDelete(user.id)" style="margin-left: 10px;">Eliminar</button>
      </li>
    </ul>
  </div>
</template>

<script>
import Swal from "sweetalert2"; // Importar SweetAlert2

export default {
  data() {
    return {
      users: [], // Lista de usuarios
      newUser: {
        id: null,
        name: "",
        email: ""
      },
      isEditing: false // Indicador para saber si estamos en modo edición
    };
  },
  mounted() {
    this.fetchUsers(); // Cargar los usuarios cuando el componente se monta
  },
  methods: {
    // Obtener la lista de usuarios
    async fetchUsers() {
      try {
        const response = await fetch("http://127.0.0.1:8000/api/users/");
        if (response.ok) {
          const data = await response.json();
          this.users = data;
        } else {
          console.error("Error al obtener la lista de usuarios");
        }
      } catch (error) {
        console.error("Error de red al obtener usuarios:", error);
      }
    },

    // Crear un nuevo usuario o actualizar si está en modo edición
    async handleSubmit() {
      if (this.isEditing) {
        this.updateUser();
      } else {
        this.createUser();
      }
    },

    // Crear un nuevo usuario
async createUser() {
  try {
    const response = await fetch("http://127.0.0.1:8000/api/users/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(this.newUser)
    });
    if (response.ok) {
      this.newUser.name = "";
      this.newUser.email = "";
      this.fetchUsers(); // Actualizar la lista de usuarios
      
      // Mostrar alerta de éxito
      Swal.fire({
        title: "¡Usuario Creado!",
        text: "El usuario se ha agregado correctamente.",
        icon: "success",
        background: "#2e2e2e", // Fondo oscuro
        color: "#fff"          // Texto blanco
      });
    } else {
      console.error("Error al crear el usuario");
    }
  } catch (error) {
    console.error("Error de red al crear usuario:", error);
  }
},

// Editar un usuario existente
editUser(user) {
  this.newUser = { ...user }; // Copiar los datos del usuario al formulario, incluyendo el ID
  this.isEditing = true; // Cambiar a modo edición
},


// Actualizar un usuario existente
async updateUser() {
  try {
    const response = await fetch(`http://127.0.0.1:8000/api/users/${this.newUser.id}`, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        name: this.newUser.name,
        email: this.newUser.email
      })
    });
    if (response.ok) {
      this.newUser.name = "";
      this.newUser.email = "";
      this.isEditing = false;
      this.fetchUsers(); // Actualizar la lista de usuarios
      
      // Mostrar alerta de éxito
      Swal.fire({
        title: "¡Usuario Actualizado!",
        text: "El usuario se ha actualizado correctamente.",
        icon: "success",
        background: "#2e2e2e", // Fondo oscuro
        color: "#fff"          // Texto blanco
      });
    } else {
      console.error("Error al actualizar el usuario");
    }
  } catch (error) {
    console.error("Error de red al actualizar usuario:", error);
  }
},
    // Confirmar y eliminar un usuario con SweetAlert2
    confirmDelete(id) {
      Swal.fire({
        title: "¿Estás seguro?",
        text: "¡No podrás revertir esto!",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",  // Color del botón de confirmación
        cancelButtonColor: "#d33",      // Color del botón de cancelación
        confirmButtonText: "Sí, eliminarlo",
        cancelButtonText: "Cancelar",
        background: "#2e2e2e",          // Fondo oscuro
        color: "#fff",                  // Color del texto
      }).then((result) => {
        if (result.isConfirmed) {
          this.deleteUser(id); // Si confirma, eliminar el usuario
          Swal.fire({
            title: "¡Eliminado!",
            text: "El usuario ha sido eliminado.",
            icon: "success",
            background: "#2e2e2e",      // Fondo oscuro para el mensaje de éxito
            color: "#fff",              // Color de texto para el mensaje de éxito
          });
        }
      });
    },


    // Eliminar un usuario
    async deleteUser(id) {
      try {
        const response = await fetch(`http://127.0.0.1:8000/api/users/${id}`, {
          method: "DELETE"
        });
        if (response.ok) {
          this.fetchUsers(); // Volver a cargar la lista de usuarios
        } else {
          console.error("Error al eliminar el usuario");
        }
      } catch (error) {
        console.error("Error de red al eliminar usuario:", error);
      }
    },

    // Cancelar la edición
    cancelEdit() {
      this.newUser = { id: null, name: "", email: "" };
      this.isEditing = false;
    }
  }
};
</script>

<style scoped>
form {
  margin-bottom: 20px;
}

input {
  margin-right: 10px;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  margin-bottom: 10px;
}

button {
  margin-left: 10px;
}
</style>
