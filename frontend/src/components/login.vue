<template>
    <div class="login-container">
      <h1>Login</h1>
      <form @submit.prevent="handleLogin" class="login-form">
        <input v-model="email" placeholder="Email" required class="input-field" />
        <input v-model="password" type="password" placeholder="Password" required class="input-field" />
        <button type="submit" class="login-button">Login</button>
      </form>
    </div>
  </template>
  
  <script>
  import Swal from 'sweetalert2';
  
  export default {
    data() {
      return {
        email: '',
        password: '',
      };
    },
    mounted() {
      this.checkLogoutSuccess(); // Verificar si se acaba de cerrar sesión
    },
    methods: {
      handleLogin() {
        const hardCodedEmail = 'admin@gmail.com';
        const hardCodedPassword = 'admin123';
  
        if (this.email === hardCodedEmail && this.password === hardCodedPassword) {
          // Guardar estado temporal en el localStorage para verificar en el CRUD
          localStorage.setItem('authenticated', 'true');
          localStorage.setItem('loginSuccess', 'true'); // Indica que hubo un login exitoso
  
          this.$router.push('/users');  // Redirige al CRUD de usuarios
        } else {
          // Mostrar alerta de credenciales incorrectas
          Swal.fire({
            title: '¡Error!',
            text: 'Credenciales incorrectas, por favor intenta de nuevo.',
            icon: 'error',
            background: '#2e2e2e',
            color: '#fff',
          });
        }
      },
      checkLogoutSuccess() {
        // Verificar si se acaba de cerrar sesión y mostrar el SweetAlert
        if (localStorage.getItem('logoutSuccess') === 'true') {
          Swal.fire({
            title: 'Sesión Cerrada',
            text: 'Has cerrado sesión exitosamente.',
            icon: 'success',
            background: '#2e2e2e',
            color: '#fff',
          });
          // Limpiar la señal de logoutSuccess
          localStorage.removeItem('logoutSuccess');
        }
      }
    }
  };
  </script>
  