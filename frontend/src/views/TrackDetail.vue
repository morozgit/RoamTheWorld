<template>
    <div>
      <div v-if="loading">Загрузка...</div>
      <div v-else-if="error">{{ error }}</div>
      <div v-else-if="track">
        <h1>{{ track.name || 'Без названия' }}</h1>
        <!-- Кликабельное изображение -->
        <img
          :src="imageSrc"
          alt="Track Image"
          v-if="track.image_url"
          @click="openModal"
        />
        <p>{{ track.description || 'Описание отсутствует' }}</p>
  
        <!-- Модальное окно -->
        <div v-if="isModalOpen" class="modal" @click.self="closeModal">
          <img :src="imageSrc" alt="Track Image" class="modal-image" />
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import { ref, onMounted, computed } from 'vue';
  import { useRoute } from 'vue-router';
  import axios from 'axios';
  
  export default {
    name: 'TrackDetail',
    setup() {
      const route = useRoute();
      const track = ref(null);
      const loading = ref(true);
      const error = ref('');
      const isModalOpen = ref(false);
  
      const trackId = computed(() => route.params.track_id);
        console.log("trackId", trackId.value);
      const fetchTrack = async () => {
        try {
          const response = await axios.get(`${import.meta.env.VITE_API_URL}/track/${trackId.value}`);
          track.value = response.data;
        } catch (err) {
          console.error('Error fetching track:', err.response ? err.response.data : err.message);
          error.value = 'Не удалось загрузить данные';
        } finally {
          loading.value = false;
        }
      };
  
      const imageSrc = computed(() => {
        if (track.value && track.value.image_url) {
          return track.value.image_url;
        }
        return '';
      });
  
      const openModal = () => {
        isModalOpen.value = true;
      };
  
      const closeModal = () => {
        isModalOpen.value = false;
      };
  
      onMounted(fetchTrack);
  
      return {
        track,
        loading,
        error,
        isModalOpen,
        imageSrc,
        openModal,
        closeModal,
      };
    },
  };
  </script>
  
  <style scoped>
  /* Заголовок */
  h1 {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 10px;
    padding-top: 70px;
  }
  
  /* Описание */
  p {
    font-size: 16px;
    color: #f1e8e8;
  }
  
  /* Оформление изображения */
  img {
    width: 200px;
    height: 200px;
    object-fit: cover;
    border-radius: 10%;
    margin-right: 15px;
    float: left;
    cursor: pointer; /* Указывает, что изображение кликабельно */
  }
  
  /* Модальное окно */
  .modal {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background-color: rgba(0, 0, 0, 0.8);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
  }
  
  .modal-image {
    width: auto;
    height: auto;
    object-fit: contain;
  }
  
  </style>
  