<template>
  <div class="row">
    <!-- Big Chart -->
    <datePicker/>
    <div class="col-12">
      <card type="chart" class="bigChart">
        <template slot="header">
          <div class="row">
            <div class="col-sm-6" :class="isRTL ? 'text-right' : 'text-left'">
              <h5 class="card-category">Time-series Charts</h5>
              <h2 class="card-title">Profile</h2>
            </div>
            <div class="col-sm-6 d-flex d-sm-block">
              <div
                class="btn-group btn-group-toggle"
                :class="isRTL ? 'float-left' : 'float-right'"
                data-toggle="buttons"
              >
                <label
                  v-for="(option, index) in bigLineChartCategories"
                  :key="option.name"
                  class="btn btn-sm btn-primary btn-simple"
                  :class="{ active: bigLineChart.activeIndex === index }"
                  :id="index"
                >
                  <input
                    type="radio"
                    @click="initBigChart(index)"
                    name="options"
                    autocomplete="off"
                    :checked="bigLineChart.activeIndex === index"
                  />
                  <span class="d-none d-sm-block">{{ option.name }}</span>
                  <span class="d-block d-sm-none">
                    <i :class="option.icon"></i>
                  </span>
                </label>
              </div>
            </div>
          </div>
        </template>
        <div class="chart-area">
          <line-chart
            style="height: 100%"
            ref="bigChart"
            :chart-data="bigLineChart.chartData"
            :gradient-colors="bigLineChart.gradientColors"
            :gradient-stops="bigLineChart.gradientStops"
            :extra-options="bigLineChart.extraOptions"
          >
          </line-chart>
          <div class="xlabel">Days</div>
        </div>
      </card>
    </div>

    <!-- Small charts -->
    <div class="col-lg-4" :class="{ 'text-right': isRTL }">
      <card type="chart">
        <template slot="header">
          <h5 class="card-category">Time Series Chart</h5>
          <h3 class="card-title">
            <i class="tim-icons icon-bell-55 text-primary "></i>Plant Growth Rate
          </h3>
        </template>
        <div class="chart-area">
          <line-chart
            style="height: 100%"
            :chart-data="purpleLineChart.chartData"
            :gradient-colors="purpleLineChart.gradientColors"
            :gradient-stops="purpleLineChart.gradientStops"
            :extra-options="purpleLineChart.extraOptions"
          >
          </line-chart>
        </div>
      </card>
    </div>
    <div class="col-lg-4" :class="{ 'text-right': isRTL }">
      <card type="chart">
        <template slot="header">
          <h5 class="card-category">BarChart</h5>
          <h3 class="card-title">
            <i class="tim-icons icon-delivery-fast text-info "></i> Task List
          </h3>
        </template>
        <div class="chart-area">
          <bar-chart
            style="height: 100%"
            :chart-data="blueBarChart.chartData"
            :gradient-stops="blueBarChart.gradientStops"
            :extra-options="blueBarChart.extraOptions"
          >
          </bar-chart>
        </div>
      </card>
    </div>
    <div class="col-lg-4" :class="{ 'text-right': isRTL }">
      <card type="chart">
        <template slot="header">
          <h5 class="card-category">Time Series Chart</h5>
          <h3 class="card-title">
            <i class="tim-icons icon-send text-success "></i> PID Control 
          </h3>
        </template>
        <div class="chart-area">
          <line-chart
            style="height: 100%"
            :chart-data="greenLineChart.chartData"
            :gradient-stops="greenLineChart.gradientStops"
            :extra-options="greenLineChart.extraOptions"
          >
          </line-chart>
        </div>
      </card>
    </div>
    <div class="col-lg-5">
      <card type="tasks" :header-classes="{ 'text-right': isRTL }">
        <template slot="header" class="d-inline">
          <h6 class="title d-inline">Tasks (5)</h6>
          <p class="card-category d-inline">Today</p>

          <base-dropdown
            menu-on-right=""
            tag="div"
            title-classes="btn btn-link btn-icon"
            class="float-right"
          >
            <i slot="title" class="tim-icons icon-settings-gear-63"></i>
            <a class="dropdown-item" href="#pablo"> Action </a>
            <a class="dropdown-item" href="#pablo"> Another action </a>
            <a class="dropdown-item" href="#pablo"> Something else </a>
          </base-dropdown>
        </template>
        <div class="table-full-width table-responsive">
          <task-list></task-list>
        </div>
      </card>
    </div>
    <div class="col-lg-7">
      <card card-body-classes="table-full-width">
        <h4 slot="header" class="card-title">Striped table</h4>
        <el-table :data="tableData">
          <el-table-column
            min-width="150"
            sortable
            label="Name"
            property="name"
          ></el-table-column>
          <el-table-column
            min-width="150"
            sortable
            label="Machine"
            property="Machine"
          ></el-table-column>
          <el-table-column
            min-width="150"
            sortable
            label="WorkDid"
            property="WorkDid"
          ></el-table-column>
          <el-table-column
            min-width="150"
            sortable
            align="right"
            header-align="right"
            label="Time"
            property="Time"
          ></el-table-column>
        </el-table>
      </card>
    </div>
  </div>
</template>
<script>
import LineChart from "@/components/Charts/LineChart";
import BarChart from "@/components/Charts/BarChart";
import * as chartConfigs from "@/components/Charts/config";
import TaskList from "@/components/Dashboard/TaskList";
import config from "@/config";
import { Table, TableColumn } from "element-ui";
import datePicker from "@/components/dataPicker/datePicker.vue";

let bigChartData = [[0], [0], [0]];
let bigChartLabels = ["Date"];
let bigChartDatasetOptions = {
  fill: true,
  borderColor: config.colors.primary,
  borderWidth: 2,
  borderDash: [],
  borderDashOffset: 0.0,
  pointBackgroundColor: config.colors.primary,
  pointBorderColor: "rgba(255,255,255,0)",
  pointHoverBackgroundColor: config.colors.primary,
  pointBorderWidth: 20,
  pointHoverRadius: 4,
  pointHoverBorderWidth: 15,
  pointRadius: 4,
};

export default {
  name: "dashboard",
  components: {
    LineChart,
    BarChart,
    TaskList,
    [Table.name]: Table,
    [TableColumn.name]: TableColumn,
    datePicker,
  },
  data() {
    return {
      startDate:(new Date(Date.now())),
      endDate:(new Date(Date.now())),
      tableData: [
        {
          id: 1,
          name: "Dakota Rice",
          Time: "19:20:50",
          Machine: "Machine01",
          WorkDid: "Updated",
        },
        {
          id: 2,
          name: "Minerva Hooper",
          Time: "20:11:23",
          Machine: "Machine22",
          WorkDid: "Deleted",
        },
        {
          id: 3,
          name: "Sage Rodriguez",
          Time: "08:22:21",
          Machine: "Machine02",
          WorkDid: "Updated",
        },
        {
          id: 4,
          name: "Philip Chaney",
          Time: "22:31:00",
          Machine: "Machine32",
          WorkDid: "Updated",
        },
        {
          id: 5,
          name: "Doris Greene",
          Time: "14:20:00",
          Machine: "Machine02",
          WorkDid: "Updated",
        },
      ],
      bigLineChart: {
        activeIndex: 0,
        chartData: {
          datasets: [
            {
              ...bigChartDatasetOptions,
              data: bigChartData[0],
            },
          ],
          labels: bigChartLabels,
        },
        extraOptions: chartConfigs.purpleChartOptions,
        gradientColors: config.colors.primaryGradient,
        gradientStops: [1, 0.4, 0],
        categories: [],
      },
      purpleLineChart: {
        extraOptions: chartConfigs.purpleChartOptions,
        chartData: {
          labels: ["JUL", "AUG", "SEP", "OCT", "NOV", "DEC"],
          datasets: [
            {
              label: "Date",
              fill: true,
              borderColor: config.colors.primary,
              borderWidth: 2,
              borderDash: [],
              borderDashOffset: 0.0,
              pointBackgroundColor: config.colors.primary,
              pointBorderColor: "rgba(255,255,255,0)",
              pointHoverBackgroundColor: config.colors.primary,
              pointBorderWidth: 20,
              pointHoverRadius: 4,
              pointHoverBorderWidth: 15,
              pointRadius: 4,
              data: [80, 100, 105, 110, 120, 80],
            },
          ],
        },
        gradientColors: config.colors.primaryGradient,
        gradientStops: [1, 0.2, 0],
      },
      greenLineChart: {
        extraOptions: chartConfigs.greenChartOptions,
        chartData: {
          labels: ["JUL", "AUG", "SEP", "OCT", "NOV"],
          datasets: [
            {
              label: "My First dataset",
              fill: true,
              borderColor: config.colors.danger,
              borderWidth: 2,
              borderDash: [],
              borderDashOffset: 0.0,
              pointBackgroundColor: config.colors.danger,
              pointBorderColor: "rgba(255,255,255,0)",
              pointHoverBackgroundColor: config.colors.danger,
              pointBorderWidth: 20,
              pointHoverRadius: 4,
              pointHoverBorderWidth: 15,
              pointRadius: 4,
              data: [90, 27, 60, 12, 80],
            },
          ],
        },
        gradientColors: [
          "rgba(66,134,121,0.15)",
          "rgba(66,134,121,0.0)",
          "rgba(66,134,121,0)",
        ],
        gradientStops: [1, 0.4, 0],
      },
      blueBarChart: {
        extraOptions: chartConfigs.barChartOptions,
        chartData: {
          labels: ["Area1", "Area2", "Area3", "Area4", "Area5", "Area6"],
          datasets: [
            {
              label: "Countries",
              fill: true,
              borderColor: config.colors.info,
              borderWidth: 2,
              borderDash: [],
              borderDashOffset: 0.0,
              data: [53, 20, 10, 80, 100, 45],
            },
          ],
        },
        gradientColors: config.colors.primaryGradient,
        gradientStops: [1, 0.4, 0],
      },
    };
  },
  computed: {
    enableRTL() {
      return this.$route.query.enableRTL;
    },
    isRTL() {
      return this.$rtl.isRTL;
    },
    bigLineChartCategories() {
      return [
        { name: "Temperature", icon: "tim-icons icon-single-02" },
        {
          name: "Humidity",
          icon: "tim-icons icon-gift-2",
        },
        { name: "pH Value", icon: "tim-icons icon-tap-02" },
      ];
    },
  },
  methods: {
    initBigChart(index) {
      let chartData = {
        datasets: [
          {
            ...bigChartDatasetOptions,
            data: bigChartData[index],
          },
        ],
        labels: bigChartLabels,
      };
      this.$refs.bigChart.updateGradients(chartData);
      this.bigLineChart.chartData = chartData;
      this.bigLineChart.activeIndex = index;
    },
  },
  async created() {
    //console.log(this.$strapi.user)
    try {
      const dataCount = await this.$strapi.$sensors.count();
       /*updated_at,between,this.$store.state.pickerDateInfo.endDate,
       and,this.$store.state.pickerDateInfo.endDate*/
      console.log(dataCount);
      console.log(this.$store.state.pickerDateInfo.startDate)
      console.log(this.$store.state.pickerDateInfo.endDate)
      let datasize = 100;
      let temp = [],
        humid = [],
        ph = [];
      let t = 0,
        h = 0,
        p = 0;
      for (let i = 0; i < dataCount / datasize; i++) {
        let sensors = await this.$strapi.$sensors.find({
          _limit: datasize,
          _start: i * 100,
        });
        //console.log(sensors);
        for (let j = 0; j < sensors.length; j++) {
          t += sensors[j].Temp;
          h += sensors[j].Humid;
          p += sensors[j].pH;
        }
        temp[i] = Math.floor(t / datasize);
        humid[i] = Math.floor(h / datasize);
        ph[i] = Math.floor(p / datasize);
        t = 0;
        h = 0;
        p = 0;
      }

      bigChartData = [temp, humid, ph];
      for (let i = 0; i < dataCount / datasize; i++) bigChartLabels[i] = i + 1;
      //console.log(bigChartData);
      this.initBigChart(0);
    } catch (error) {
      console.log(error);
    }
  },
  mounted() {
    this.initBigChart(0);
  },
};
</script>
<style>
.bigChart {
  padding-bottom: 10px;
}
.xlabel {
  padding-left: 50%;
}
</style>
