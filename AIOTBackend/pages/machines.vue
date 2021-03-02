<template>
  <div class="row">
    <div class="col-md-12">
      <div class="card">
        <div class="card-header">
          <h5 class="title">100 Machines Details</h5>
          <p class="category">
            Edit the details and click save
          </p>
          <base-button
            type="primary"
            class="mr-3 col-lg-2 col-md-3 col-sm-4 col-xs-6 col-xs-6"
            @click="createPopup = true"
          >
            <i class="tim-icons icon-money-coins"></i>
            <span class="caption text-uppercase">&nbsp;New Machine</span>
          </base-button>
          <base-button
            type="primary"
            class="mr-3 col-lg-2 col-md-3 col-sm-4 col-xs-6 col-xs-6"
            @click="createConnection()"
          >
            <i class="tim-icons icon-money-coins"></i>
            <span class="caption text-uppercase">&nbsp;MQTT start</span>
          </base-button>
          <base-button
            type="primary"
            class="mr-3 col-lg-2 col-md-3 col-sm-4 col-xs-6 col-xs-6"
            @click="doPublish()"
          >
            <i class="tim-icons icon-money-coins"></i>
            <span class="caption text-uppercase">&nbsp;MQTT test</span>
          </base-button>
          <modal :show.sync="createPopup" :centered="false" :show-close="true">
            <div class="NewMachineHeader">New Machine Details</div>
            <base-input
              v-model="newMachine.S_N"
              class="newSN col-lg-6 col-md-3 col-sm-4 col-xs-6 col-xs-6"
              label="Serial Number: "
            ></base-input>
            <div class="NewMachineHeader">AERO</div>
            <b-row>
              <base-input
                v-model="newMachine.aero_temp"
                class="newM col-lg-4 col-md-3 col-sm-4 col-xs-6 col-xs-6"
                label="Temparature: "
              ></base-input>
              <base-input
                v-model="newMachine.aero_humid"
                class="newM col-lg-4 col-md-3 col-sm-4 col-xs-6 col-xs-6"
                label="Humidity: "
              ></base-input>
              <base-input
                v-model="newMachine.aero_ph"
                class="newM col-lg-4 col-md-3 col-sm-4 col-xs-6 col-xs-6"
                label="ph Value: "
              ></base-input>
            </b-row>
            <div class="NewMachineHeader">HYDRO</div>
            <b-row>
              <base-input
                v-model="newMachine.hydro_temp"
                class="newM col-lg-4 col-md-3 col-sm-4 col-xs-6 col-xs-6"
                label="Temparature: "
              ></base-input>
              <base-input
                v-model="newMachine.hydro_humid"
                class="newM col-lg-4 col-md-3 col-sm-4 col-xs-6 col-xs-6"
                label="Humidity: "
              ></base-input>
              <base-input
                v-model="newMachine.hydro_ph"
                class="newM col-lg-4 col-md-3 col-sm-4 col-xs-6 col-xs-6"
                label="ph Value: "
              ></base-input>
            </b-row>
            <base-button
              type="primary"
              class="mr-3 col-lg-4 col-md-3 col-sm-4 col-xs-6 col-xs-6"
              @click="createSensor()"
            >
              <i class="tim-icons icon-wallet-43"></i>
              <span class="caption text-uppercase"> Create </span>
            </base-button>
          </modal>
          <modal :show.sync="deletepopup" :centered="false" :show-close="true">
            <b-row
              ><div class="NewMachineHeader" style="color: red;">
                <u><i>Attention!!</i></u>
              </div></b-row
            >
            <b-row
              ><div>Are you sure to delete the machine details?</div></b-row
            >
            <b-row>
              <base-button
                type="danger"
                class="btn-fill edit-btn"
                @click="deletepopup = false"
              >
                <span class="caption text-uppercase">Cancel </span>
              </base-button>
              <base-button
                type="danger"
                class="btn-fill edit-btn"
                @click="deleteSensor()"
              >
                <span class="caption text-uppercase">Delete </span>
              </base-button>
            </b-row>
          </modal>
        </div>
        <div class="card-body all-icons">
          <div v-if="this.machines.length >= 4" class="row">
            <b-tabs class="mactabs">
              <b-tab v-for="(tab, index) in getTabsItem" :key="index">
                <template #title
                  ><span style="font-size: 20px !important;">{{
                    tab[0].id + 1 + "-" + (tab[tab.length - 1].id + 1)
                  }}</span></template
                >
                <div
                  class="font-icon-list col-lg-12 col-md-3 col-sm-4 col-xs-6 col-xs-6"
                  v-for="i in tab"
                  :key="i.id"
                >
                  <div class="machines-details">
                    <h1>
                      Machine #{{ i.num }} &ensp;
                      <base-button
                        type="success"
                        class="btn-fill edit-btn"
                        @click="i.dis = !i.dis"
                      >
                        <i class="tim-icons icon-align-left-2"></i>
                        <span class="caption text-uppercase">Edit </span>
                      </base-button>
                      <base-button
                        type="danger"
                        class="btn-fill edit-btn"
                        @click="deletep(i.macid)"
                      >
                        <i class="tim-icons icon-align-left-2"></i>
                        <span class="caption text-uppercase">Delete </span>
                      </base-button>
                    </h1>

                    <b-row>
                      <h3
                        class="mr-3 col-lg-2 col-md-3 col-sm-4 col-xs-6 col-xs-6"
                      >
                        AERO
                      </h3>
                    </b-row>
                    <b-row style="padding-bottom: 15px">
                      <base-input
                        v-model="i.aero_temp"
                        class="col-lg-3 col-md-3 col-sm-4 col-xs-6 col-xs-6"
                        label="Temparature: "
                        :disabled="i.dis"
                      ></base-input>
                      <base-input
                        v-model="i.aero_humid"
                        class="col-lg-3 col-md-3 col-sm-4 col-xs-6 col-xs-6"
                        label="Humidity: "
                        :disabled="i.dis"
                      ></base-input>
                      <base-input
                        v-model="i.aero_ph"
                        class="col-lg-3 col-md-3 col-sm-4 col-xs-6 col-xs-6"
                        label="Ph value: "
                        :disabled="i.dis"
                      ></base-input>
                    </b-row>
                    <b-row>
                      <h3
                        class="mr-3 col-lg-2 col-md-3 col-sm-4 col-xs-6 col-xs-6"
                      >
                        Hydro
                      </h3>
                    </b-row>
                    <b-row style="padding-bottom: 15px">
                      <base-input
                        class="col-lg-3 col-md-3 col-sm-4 col-xs-6 col-xs-6"
                        v-model="i.hydro_temp"
                        label="Temparature: "
                        :disabled="i.dis"
                      ></base-input>
                      <base-input
                        v-model="i.hydro_humid"
                        class="col-lg-3 col-md-3 col-sm-4 col-xs-6 col-xs-6"
                        label="Humidity: "
                        :disabled="i.dis"
                      ></base-input>
                      <base-input
                        v-model="i.hydro_ph"
                        class="col-lg-3 col-md-3 col-sm-4 col-xs-6 col-xs-6"
                        label="Ph value: "
                        :disabled="i.dis"
                      ></base-input>
                    </b-row>
                    <b-row class="save"
                      ><div
                        class="mr-3 col-lg-9 col-md-3 col-sm-4 col-xs-6 col-xs-6"
                      ></div>
                      <base-button
                        type="primary"
                        class="mr-3 col-lg-2 col-md-3 col-sm-4 col-xs-6 col-xs-6"
                        :disabled="i.dis"
                        @click="updateSensor(i.id, i.macid)"
                      >
                        <i class="tim-icons icon-wallet-43"></i>
                        <span class="caption text-uppercase">Save </span>
                      </base-button></b-row
                    >
                  </div>
                </div>
              </b-tab>
            </b-tabs>
          </div>
          <div v-else-if="this.machines.length > 0">
            <div
              class="font-icon-list col-lg-8 col-md-3 col-sm-4 col-xs-6 col-xs-6"
              v-for="i in machines"
              :key="i.id"
            >
              <div class="machines-details">
                <h1>
                  Machine #{{ i.num }} &ensp;
                  <base-button
                    type="success"
                    class="btn-fill edit-btn"
                    @click="i.dis = !i.dis"
                  >
                    <i class="tim-icons icon-align-left-2"></i>
                    <span class="caption text-uppercase">Edit </span>
                  </base-button>
                  <base-button
                    type="danger"
                    class="btn-fill edit-btn"
                    @click="deletep(i.macid)"
                  >
                    <i class="tim-icons icon-align-left-2"></i>
                    <span class="caption text-uppercase">Delete </span>
                  </base-button>
                </h1>

                <b-row>
                  <h3 class="mr-3 col-lg-2 col-md-3 col-sm-4 col-xs-6 col-xs-6">
                    AERO
                  </h3>
                </b-row>
                <b-row style="padding-bottom: 15px">
                  <base-input
                    v-model="i.aero_temp"
                    class="col-lg-3 col-md-3 col-sm-4 col-xs-6 col-xs-6"
                    label="Temparature: "
                    :disabled="i.dis"
                  ></base-input>
                  <base-input
                    v-model="i.aero_humid"
                    class="col-lg-3 col-md-3 col-sm-4 col-xs-6 col-xs-6"
                    label="Humidity: "
                    :disabled="i.dis"
                  ></base-input>
                  <base-input
                    v-model="i.aero_ph"
                    class="col-lg-3 col-md-3 col-sm-4 col-xs-6 col-xs-6"
                    label="Ph value: "
                    :disabled="i.dis"
                  ></base-input>
                </b-row>
                <b-row>
                  <h3 class="mr-3 col-lg-2 col-md-3 col-sm-4 col-xs-6 col-xs-6">
                    Hydro
                  </h3>
                </b-row>
                <b-row style="padding-bottom: 15px">
                  <base-input
                    class="col-lg-3 col-md-3 col-sm-4 col-xs-6 col-xs-6"
                    v-model="i.hydro_temp"
                    label="Temparature: "
                    :disabled="i.dis"
                  ></base-input>
                  <base-input
                    v-model="i.hydro_humid"
                    class="col-lg-3 col-md-3 col-sm-4 col-xs-6 col-xs-6"
                    label="Humidity: "
                    :disabled="i.dis"
                  ></base-input>
                  <base-input
                    v-model="i.hydro_ph"
                    class="col-lg-3 col-md-3 col-sm-4 col-xs-6 col-xs-6"
                    label="Ph value: "
                    :disabled="i.dis"
                  ></base-input>
                </b-row>
                <b-row class="save"
                  ><div
                    class="mr-3 col-lg-9 col-md-3 col-sm-4 col-xs-6 col-xs-6"
                  ></div>
                  <base-button
                    type="primary"
                    class="mr-3 col-lg-2 col-md-3 col-sm-4 col-xs-6 col-xs-6"
                    :disabled="i.dis"
                    @click="updateSensor(i.id, i.macid)"
                  >
                    <i class="tim-icons icon-wallet-43"></i>
                    <span class="caption text-uppercase">Save </span>
                  </base-button></b-row
                >
              </div>
            </div>
          </div>
          <div v-else><h1>No machine in CMS</h1></div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
//mqtt proto
//https://github.com/emqx/MQTT-Client-Examples/blob/master/mqtt-client-Vue.js/src/views/Home.vue
import BaseButton from "~/components/BaseButton.vue";
import Modal from "~/components/Modal.vue";
import mqtt from "mqtt";
export default {
  components: {
    BaseButton,
    Modal,
  },
  name: "icons",

  data() {
    return {
      machines: [],
      createPopup: false,
      deletepopup: false,
      deleteid: null,
      newMachine: {
        S_N: "",
        aero_temp: null,
        aero_humid: null,
        aero_ph: null,
        hydro_temp: null,
        hydro_humid: null,
        hydro_ph: null,
      },
      mqttconnection: {
        host: "10.0.0.70:9001",
        port: 9001,
        endpoint: "",
        clean: true, // Reserved session
        connectTimeout: 4000, // Time out
        reconnectPeriod: 4000, // Reconnection interval
        // Certification Information
        //mqttjs_3be2c321',
        username: "tiger",
        password: "tiger",
      },
      publish: {
        topic: 'iot/app/sam/testing',
        qos: 0,
        payload: '{ "msg": "Hello, I am browser." }',
      },
      client: {
        connected: false,
      },
    };
  },
  async created() {
      const { host, port, endpoint, ...options } = this.mqttconnection;
      const connectUrl = `ws://${host}:${port}${endpoint}`
      try {
        this.client = mqtt.connect(connectUrl, options);
      } catch (error) {
        console.log("mqtt.connect error", error);
      }
      this.client.on("connect", () => {
        console.log("Connection succeeded!");
      });
      this.client.on("error", (error) => {
        console.log("Connection failed", error);
      });
      this.client.on("message", (topic, message) => {
        this.receiveNews = this.receiveNews.concat(message);
        console.log(`Received message ${message} from topic ${topic}`);
      });
  },
  async mounted() {
    const dataCount = await this.$strapi.$machines.count();
    let mac = await this.$strapi.$machines.find();
    for (let i = 0; i < dataCount; i++) {
      this.machines.push({
        id: i,
        macid: mac[i].id,
        num: mac[i].S_N,
        aero_temp: mac[i].aero_temp,
        hydro_temp: mac[i].hydro_temp,
        aero_humid: mac[i].aero_humid,
        hydro_humid: mac[i].hydro_humid,
        aero_ph: mac[i].aero_ph,
        hydro_ph: mac[i].hydro_ph,
        dis: true,
      });
    }
  },
  computed: {
    getTabsItem() {
      const tabsItem = [];
      for (let i = 0; i < this.machines.length / 4; i++) {
        let subitems = [];
        for (let j = i * 4; j < i * 4 + 4; j++) {
          subitems.push(this.machines[j]);
        }
        tabsItem.push(subitems);
      }
      return tabsItem;
    },
  },
  methods: {
    createConnection() {

    },
    doPublish() {
      const { topic, qos, payload } = this.publish;
      try{
        this.client.publish(topic, payload, qos, (error) => {
        if (error) {
          console.log("Publish error", error);
        }
      });
      }
      catch(error){
        console.log("Publish error", error);
      }
      
    },
    editSensor(id) {
      this.machines[id].dis = !this.machines[id].dis;
    },
    async updateSensor(id, macid) {
      await this.$strapi.$machines.update(macid, {
        aero_temp: this.machines[id].aero_temp || 0,
        hydro_temp: this.machines[id].hydro_temp || 0,
        aero_humid: this.machines[id].aero_humid || 0,
        hydro_humid: this.machines[id].hydro_humid || 0,
        aero_ph: this.machines[id].aero_ph || 0,
        hydro_ph: this.machines[id].hydro_ph || 0,
      });
      this.machines[id].dis = true;
    },
    async createSensor() {
      try{
        await this.$strapi.$machines.create({
        S_N: this.newMachine.S_N || "",
        aero_temp: this.newMachine.aero_temp || 0,
        hydro_temp: this.newMachine.hydro_temp || 0,
        aero_humid: this.newMachine.aero_humid || 0,
        hydro_humid: this.newMachine.hydro_humid || 0,
        aero_ph: this.newMachine.aero_ph || 0,
        hydro_ph: this.newMachine.hydro_ph || 0,
      });
      this.createPopup = false;
      window.location.reload(true);
      }
      catch(error){

      }
      
    },
    deletep(id) {
      this.deletepopup = true;
      this.deleteid = id;
    },
    async deleteSensor() {
      await this.$strapi.$machines.delete(this.deleteid);
      window.location.reload(true);
    },
  },
};
</script>
<style>
.machines-details {
  text-align: left;
  padding: 45px 20px 30px;
  border: 1px solid #e44cc4;
  border-radius: 0.1875rem;
  margin: 15px 0;
  min-height: 168px;
  width: 100%;
}
.edit-btn {
  height: 13px;
}
.nav-tabs {
  min-width: 1000px;
}
.NewMachineHeader {
  font-size: x-large;
}
.newSN {
  padding-left: 0;
}
input.form-control {
  color: #e14eca;
}
.form-control:focus,
.form-group .el-input__inner:focus,
.el-date-picker .el-input .el-input__inner:focus {
  color: #89d2d2 !important;
}
.mactabs{
  width: 100%;
}
</style>
