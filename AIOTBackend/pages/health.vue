<template>
  <div class="plant">
    <b-tabs class="mactabs">
      <b-tab v-for="(tab, index) in machines" :key="index">
        <template #title
          ><span style="font-size: 20px !important; color: white !important;">{{
            tab.sn
          }}</span></template
        >
        <b-row v-for="(tab, index) in getTabsItem" :key="index">
          <b-col class="col-md-3 col-12" v-for="(plant, i) in tab" :key="i">
            <card v-if="plant !== undefined">
              <h4 slot="header" class="card-title">{{ plant.created }}</h4>
              <img :src="plant.plantpic" />
              <div class="healthpoint">Healthy: {{ plant.healthy }}</div>
              <div class="healthpoint">Unhealthy: {{ plant.unhealthy }}</div>
            </card>
          </b-col>
        </b-row>
      </b-tab>
    </b-tabs>
  </div>
</template>
<script>
import { BaseAlert } from "@/components";

export default {
  name: "notifications",
  components: {
    BaseAlert,
  },
  data() {
    return {
      type: ["", "info", "success", "warning", "danger"],
      plants: [],
      machines: [],
      notifications: {
        topCenter: false,
      },
    };
  },
  async mounted() {
    const dataCount = await this.$strapi.$plants.count();
    let plant = await this.$strapi.$plants.find();
    for (let i = 0; i < dataCount; i++) {
      this.plants.push({
        id: i,
        created: plant[i].createdAt,
        healthy: plant[i].healthy,
        unhealthy: plant[i].unhealthy,
        plantpic: "https://cms.aiotlab.hk" + plant[i].plantPic[2].url,
      });
    }
    //console.log(this.plants);
    const data = await this.$strapi.$machines.count();
    let mac = await this.$strapi.$machines.find();
    for (let i = 0; i < data; i++) {
      this.machines.push({
        id: i,
        macid: mac[i].id,
        sn: mac[i].S_N,
      });
    }
    console.log(this.machines);
  },
  computed: {
    getTabsItem() {
      const tabsItem = [];
      for (let i = 0; i < this.plants.length / 4; i++) {
        let subitems = [];
        for (let j = i * 4; j < i * 4 + 4; j++) {
          if (this.plants[j] !== null) subitems.push(this.plants[j]);
        }
        tabsItem.push(subitems);
      }
      console.log(tabsItem);
      return tabsItem;
    },
  },
  methods: {
    notifyVue(verticalAlign, horizontalAlign) {
      let color = Math.floor(Math.random() * 4 + 1);
      this.$notify({
        message:
          "Welcome to <b>Vue Black Dashboard Pro</b> - a beautiful resource for every web developer",
        timeout: 30000,
        icon: "tim-icons icon-bell-55",
        horizontalAlign: horizontalAlign,
        verticalAlign: verticalAlign,
        type: this.type[color],
      });
    },
  },
};
</script>
<style>
.card .alert {
  position: relative !important;
  width: 100%;
}
.healthpoint {
  color: white;
  margin-top: 10px;
}
</style>
