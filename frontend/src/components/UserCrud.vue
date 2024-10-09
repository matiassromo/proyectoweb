<template>
    <div class="crud-container">
      <!-- Botón de Cerrar Sesión -->
      <button @click="logout" class="logout-button">Cerrar Sesión</button>
  
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
        isEditing: false
      };
    },
    mounted() {
      this.checkLoginSuccess(); // Verificar si se debe mostrar el SweetAlert de ingreso exitoso
      this.fetchUsers(); // Cargar los usuarios cuando el componente se monta
    },
    methods: {
      checkLoginSuccess() {
        // Verificar si se acaba de hacer login y mostrar el SweetAlert
        if (localStorage.getItem('loginSuccess') === 'true') {
          Swal.fire({
            title: '¡Ingreso exitoso!',
            text: 'Has ingresado correctamente.',
            icon: 'success',
            background: '#2e2e2e',
            color: '#fff',
          });
          // Limpiar el estado de loginSuccess para que no se repita
          localStorage.removeItem('loginSuccess');
        }
      },
  
      // Cerrar sesión
      logout() {
        Swal.fire({
          title: '¿Estás seguro?',
          text: 'Se cerrará tu sesión actual.',
          icon: 'warning',
          showCancelButton: true,
          confirmButtonColor: '#3085d6',
          cancelButtonColor: '#d33',
          confirmButtonText: 'Cerrar Sesión',
          cancelButtonText: 'Cancelar',
          background: '#2e2e2e',
          color: '#fff',
        }).then((result) => {
          if (result.isConfirmed) {
            // Limpiar el estado de autenticación y marcar que se cerró la sesión
            localStorage.removeItem('authenticated');
            localStorage.setItem('logoutSuccess', 'true'); // Marcar que la sesión se cerró
            // Redirigir al login
            this.$router.push('/');
          }
        });
      },
  
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
  
      async handleSubmit() {
        if (this.isEditing) {
          this.updateUser();
        } else {
          this.createUser();
        }
      },
  
      async createUser() {
        try {
          const response = await fetch("http://127.0.0.1:8000/api/users/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(this.newUser)
          });
          if (response.ok) {
            this.newUser.name = "";
            this.newUser.email = "";
            this.fetchUsers();
            Swal.fire({
              title: "¡Usuario Creado!",
              text: "El usuario se ha agregado correctamente.",
              icon: "success",
              background: "#2e2e2e",
              color: "#fff"
            });
          } else {
            console.error("Error al crear el usuario");
          }
        } catch (error) {
          console.error("Error de red al crear usuario:", error);
        }
      },
  
      editUser(user) {
        this.newUser = { ...user };
        this.isEditing = true;
      },
  
      async updateUser() {
        try {
          const response = await fetch(`http://127.0.0.1:8000/api/users/${this.newUser.id}`, {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ name: this.newUser.name, email: this.newUser.email })
          });
          if (response.ok) {
            this.newUser.name = "";
            this.newUser.email = "";
            this.isEditing = false;
            this.fetchUsers();
            Swal.fire({
              title: "¡Usuario Actualizado!",
              text: "El usuario se ha actualizado correctamente.",
              icon: "success",
              background: "#2e2e2e",
              color: "#fff"
            });
          } else {
            console.error("Error al actualizar el usuario");
          }
        } catch (error) {
          console.error("Error de red al actualizar usuario:", error);
        }
      },
  
      confirmDelete(id) {
        Swal.fire({
          title: "¿Estás seguro?",
          text: "¡No podrás revertir esto!",
          icon: "warning",
          showCancelButton: true,
          confirmButtonColor: "#3085d6",
          cancelButtonColor: "#d33",
          confirmButtonText: "Sí, eliminarlo",
          cancelButtonText: "Cancelar",
          background: "#2e2e2e",
          color: "#fff"
        }).then((result) => {
          if (result.isConfirmed) {
            this.deleteUser(id);
            Swal.fire({
              title: "¡Eliminado!",
              text: "El usuario ha sido eliminado.",
              icon: "success",
              background: "#2e2e2e",
              color: "#fff"
            });
          }
        });
      },
  
      async deleteUser(id) {
        try {
          const response = await fetch(`http://127.0.0.1:8000/api/users/${id}`, {
            method: "DELETE"
          });
          if (response.ok) {
            this.fetchUsers();
          } else {
            console.error("Error al eliminar el usuario");
          }
        } catch (error) {
          console.error("Error de red al eliminar usuario:", error);
        }
      },
  
      cancelEdit() {
        this.newUser = { id: null, name: "", email: "" };
        this.isEditing = false;
      }
    }
  };
  </script>
  
  <style scoped>
  .logout-button {
    position: fixed;
    top: 20px;
    right: 20px;
    background-color: #d33;
    color: #fff;
    border: none;
    padding: 10px 15px;
    cursor: pointer;
    border-radius: 5px;
  }
  
  .logout-button:hover {
    background-color: #ff4d4d;
  }
  </style>
  