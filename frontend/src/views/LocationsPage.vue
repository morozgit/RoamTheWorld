<template>
  <div class="location-list">
    <LocationCard 
      v-for="location in locations" 
      :key="location.id" 
      :location="location" 
    />
  </div>
</template>

<script>
import LocationCard from '@/components/LocationCard.vue';
import axios from "@/main";

export default {
  components: {
    LocationCard
  },
  data() {
    return {
      locations: []
    };
  },
  methods: {
    async fetchAllLocations() {
      try {
        const response = await axios.get(import.meta.env.VITE_API_URL + '/location/all_locations');
        this.locations = response.data;
      } catch (error) {
        console.error('Error fetching locations:', error);
      }
    }
  },
  mounted() {
    this.fetchAllLocations();
    document.title = "Roam the world";
  }
};
</script>


<style scoped>
.location-list {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-around;
  padding-top: 60px; /* Отступ сверху */
  padding-bottom: 60px; /* Отступ снизу */
}
</style>
