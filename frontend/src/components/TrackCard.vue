<template>
    <div class="track-card" @click="goToDetail">
      <img :src="imageSrc" alt="Track Image" />
      <h3>{{ track.name }}</h3>
      <h3>{{ track.short_description }}</h3>
    </div>
  </template>
  
  <script>
  export default {
    props: {
      track: {
        type: Object,
        required: true,
      },
    },
    computed: {
      imageSrc() {
        return this.track.image_url ? this.track.image_url : '/images/default-image.jpg';
      },
    },
    methods: {
      goToDetail() {
        this.$router.push({ name: 'TrackDetail', params: { track_id: this.track.id } });
      },
    },
  };
  </script>

<style scoped>
.track-card {
  border: 1px solid #ddd;
  padding: 15px;
  margin: 10px;
  cursor: pointer;
  text-align: center;
}

.track-card img {
  width: 100%;
  height: 200px;
  object-fit: cover;
}
</style>