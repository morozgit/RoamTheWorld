<template>
    <div class="tracks-list">
      <TrackCard 
        v-for="track in tracks" 
        :key="track.id" 
        :track="track" 
      />
    </div>
  </template>

<script>
import axios from "@/main";
import TrackCard from '@/components/TrackCard.vue';

export default {
  components: {
    TrackCard
  },
  data() {
    return {
      tracks: []
    };
  },
  async mounted() {
    const location_id = this.$route.params.location_id;
    await this.fetchLocationTracks(location_id);
    console.log(this.$route);
    document.title = "Roam the world";
  },
  methods: {
    async fetchLocationTracks(location_id) {
      try {
        const response = await axios.get(`${import.meta.env.VITE_API_URL}/location/${location_id}`);
        this.tracks = response.data;
      } catch (error) {
        console.error('Error fetching tracks:', error);
      }
    }
  }
}
</script>

<style scoped>
.tracks-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  padding-top: 60px; /* Отступ сверху */
  padding-bottom: 60px; /* Отступ снизу */
}
</style>