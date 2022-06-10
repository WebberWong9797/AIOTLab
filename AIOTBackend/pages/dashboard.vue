<template>
  <div class="row">
    <!-- Big Chart -->
    <!--<datePicker />-->
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

    <!-- Small charts 
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
    -->
    <div class="col-lg-5">
      <card type="tasks" :header-classes="{ 'text-right': isRTL }">
        <template slot="header" class="d-inline">
          <h6
            class="title d-inline col-lg-12"
            style="font-size: 1.2rem; margin-bottom: 20px;"
          >
            Date Picker
          </h6>
          <p class="card-category d-inline col-lg-1">
            &nbsp;&nbsp;{{ startDate }}
          </p>
          <p class="card-category d-inline col-lg-1">-</p>
          <p class="card-category d-inline col-lg-1">{{ endDate }}</p>
          <base-input
            id="startDate"
            v-model="startDate"
            type="date"
            :min="minDate"
            :max="maxDate"
            class="col-lg-12 col-md-3 col-sm-4 col-xs-6 col-xs-6"
            label="Start Date: "
          ></base-input>
          <base-input
            id="endDate"
            v-model="endDate"
            type="date"
            :min="minDate"
            :max="maxDate"
            class="col-lg-12 col-md-3 col-sm-4 col-xs-6 col-xs-6"
            label="End Date: "
          ></base-input>
          <div class="col-lg-3"></div>
          <base-button
            type="primary"
            class="edit-btn col-lg-4 col-md-3 col-sm-4 col-xs-6 col-xs-6"
            @click="apply()"
          >
            <span class="caption text-uppercase">&nbsp;Apply</span>
          </base-button>
          <base-button
            type="success"
            class="edit-btn col-lg-4 col-md-3 col-sm-4 col-xs-6 col-xs-6"
            @click="reset()"
          >
            <span class="caption text-uppercase">&nbsp;Reset</span>
          </base-button>
        </template>
      </card>
    </div>
    <div class="col-lg-7">
      <card card-body-classes="table-full-width">
        <h4 slot="header" class="title">Edit Record</h4>
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
import moment from "moment";
import BaseButton from "~/components/BaseButton.vue";

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
    BaseButton,
    BarChart,
    TaskList,
    [Table.name]: Table,
    [TableColumn.name]: TableColumn,
    datePicker,
  },
  data() {
    return {
      minDate: moment("2020-08-01").format("YYYY-MM-DD"),
      maxDate: moment("2020-08-28").format("YYYY-MM-DD"),
      startDate: moment("2020-08-01").format("YYYY-MM-DD"),
      endDate: moment("2020-08-28").format("YYYY-MM-DD"),
      ChartData: [],
      chartlabel: [],
      tableData: [],
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
    apply() {
      let start = parseInt(moment(this.startDate).format("DD"));
      let end = parseInt(moment(this.endDate).format("DD"));
      console.log(start, end);
      bigChartData = [];
      bigChartLabels = [];
      let temp = [],
        humid = [],
        ph = [];
      for (let i = start - 1; i <= end - 1; i++) {
        temp.push(this.chartData[0][i]);
        humid.push(this.chartData[1][i]);
        ph.push(this.chartData[2][i]);
        bigChartLabels.push(i + 1);
      }
      bigChartData = [temp, humid, ph];
      //console.log(bigChartData)
      this.initBigChart(0);
    },
    reset() {
      bigChartData = this.chartData;
      bigChartLabels = this.chartlabel;
      this.initBigChart(0);
    },
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
    const recordCount = await this.$strapi.$records.count();
    let record = await this.$strapi.$records.find();
    console.log(moment(record.published_at).format("YYYY-MM-DD hh:mm"));
    for (let i = recordCount - 5; i < recordCount; i++) {
      this.tableData.push({
        id: record[i].id,
        name: record[i].pic,
        Time: moment(record[i].published_at).format("YYYY-MM-DD hh:mm"),
        Machine: record[i].mac_sn,
        WorkDid: record[i].work,
      });
    }
    //console.log(this.$strapi.user)
    try {
      const dataCount = await this.$strapi.$sensors.count();
      /*updated_at,between,this.$store.state.pickerDateInfo.endDate,
       and,this.$store.state.pickerDateInfo.endDate*/
      console.log(dataCount);
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
      this.chartData = bigChartData;
      console.log(this.chartData);
      for (let i = 0; i < dataCount / datasize; i++) bigChartLabels[i] = i + 1;
      this.chartlabel = bigChartLabels;
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
.title {
  margin-right: 50px;
}
</style>
