<template>
    <div>
      <h1>Gestión de Usuarios</h1>
      
      <!-- Formulario para agregar un nuevo usuario -->
      <form @submit.prevent="createUser">
        <input v-model="newUser.name" placeholder="Nombre" required />
        <input v-model="newUser.email" placeholder="Email" required />
        <button type="submit">Agregar Usuario</button>
      </form>
  
      <!-- Mostrar la lista de usuarios -->
      <h2>Lista de Usuarios</h2>
      <ul>
        <li v-for="user in users" :key="user.id">
          {{ user.name }} ({{ user.email }})
          <button @click="deleteUser(user.id)">Eliminar</button>
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        users: [], // Almacena la lista de usuarios
        newUser: {
          name: "", // Nombre del nuevo usuario
          email: "" // Email del nuevo usuario
        }
      };
    },
    mounted() {
      // Cargar usuarios cuando se monta el componente
      this.fetchUsers();
    },
    methods: {
      // Obtener la lista de usuarios del backend
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
      // Crear un nuevo usuario en el backend
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
            this.newUser.name = ""; // Limpiar el formulario
            this.newUser.email = "";
            this.fetchUsers(); // Actualizar la lista de usuarios
          } else {
            console.error("Error al crear el usuario");
          }
        } catch (error) {
          console.error("Error de red al crear usuario:", error);
        }
      },
      // Eliminar un usuario en el backend
      async deleteUser(id) {
        try {
          const response = await fetch(`http://127.0.0.1:8000/api/users/${id}`, {
            method: "DELETE"
          });
          if (response.ok) {
            this.fetchUsers(); // Actualizar la lista después de eliminar
          } else {
            console.error("Error al eliminar el usuario");
          }
        } catch (error) {
          console.error("Error de red al eliminar usuario:", error);
        }
      }
    }
  };
  </script>
  
  <style scoped>
  /* Estilos básicos para el formulario y la lista */
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
  