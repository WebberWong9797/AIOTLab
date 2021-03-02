<template>
  <div class="row">
    <!-- Big Chart -->
    <div class="col-12">
      <card type="chart">
        <template slot="header">
          <div class="row">
            <div class="col-sm-6" :class="isRTL ? 'text-right' : 'text-left'">
              <h5 class="card-category">Past Data for AHAS</h5>
              <h2 class="card-title">Performance</h2>
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
        </div>
      </card>
    </div>

    <!-- Small charts -->
    <div class="col-lg-4" :class="{ 'text-right': isRTL }">
      <card type="chart">
        <template slot="header">
          <h5 class="card-category">Update Events</h5>
          <h3 class="card-title">
            <i class="tim-icons icon-bell-55 text-primary "></i> Total : 244
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
          <h5 class="card-category">Daily Sales</h5>
          <h3 class="card-title">
            <i class="tim-icons icon-delivery-fast text-info "></i> $3,500
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
          <h5 class="card-category">Completed tasks</h5>
          <h3 class="card-title">
            <i class="tim-icons icon-send text-success "></i> Total Task Left: 6
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
        <h4 slot="header" class="card-title">Updated Events</h4>
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
            label="Status"
            property="Status"
          ></el-table-column>
          <el-table-column
            min-width="150"
            sortable
            label="Events Details"
            property="Details"
          ></el-table-column>
          <el-table-column
            min-width="150"
            sortable
            align="right"
            header-align="right"
            label="Date/Time"
            property="DateTime"
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

export default {
  name: "dashboard",
  middleware: "auth",
  components: {
    LineChart,
    BarChart,
    TaskList,
    [Table.name]: Table,
    [TableColumn.name]: TableColumn,
  },
  data() {
    return {
      bigChartDatasetOptions: {
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
      },
      bigChartData: [[0], [0], [0]],
      bigChartLabels: [],
      tableData: [
        {
          id: 1,
          name: "Henry",
          Status: "Updated",
          Details: "SN01-Details Changes",
          DateTime: "18-12-2020",
        },
        {
          id: 2,
          name: "Webber",
          Status: "Updated",
          Details: "CMS Update",
          DateTime: "18-12-2020",
        },
        {
          id: 3,
          name: "Henry",
          Status: "Updated",
          Details: "AHAS Added new machine",
          DateTime: "18-12-2020",
        },
        {
          id: 4,
          name: "Vicky",
          Status: "Updated",
          Details: "Bless Website",
          DateTime: "18-12-2020/19:00",
        },
        {
          id: 5,
          name: "Tiger",
          Status: "Updated",
          Details: "Hardware updated",
          DateTime: "18-12-2020",
        },
      ],
      bigLineChart: {
        activeIndex: 0,
        chartData: {
          datasets: [
            {
              ...this.bigChartDatasetOptions,
              //data: [[0],[0],[0]],
            },
          ],
          labels: this.bigChartLabels,
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
              label: "Data",
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
              data: [80, 100, 70, 80, 120, 80],
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
          labels: ["USA", "GER", "AUS", "UK", "RO", "BR"],
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
        { name: "Temparature", icon: "tim-icons icon-single-02" },
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
            ...this.bigChartDatasetOptions,
            data: this.bigChartData[index],
          },
        ],
        labels: this.bigChartLabels,
      };
      this.$refs.bigChart.updateGradients(chartData);
      this.bigLineChart.chartData = chartData;
      this.bigLineChart.activeIndex = index;
    },
  },
  async created() {
    // try {
    //   const dataCount = await this.$strapi.$sensors.count();
    //   console.log(dataCount);
    //   let datasize = 100;
    //   let temp = [],
    //     humid = [],
    //     ph = [];
    //   let t = 0,
    //     h = 0,
    //     p = 0;
    //   for (let i = 0; i < dataCount / datasize; i++) {
    //     let sensors = await this.$strapi.$sensors.find({
    //       _limit: datasize,
    //       _start: i * 100,
    //     });
    //     console.log(sensors);
    //     for (let j = 0; j < sensors.length; j++) {
    //       t += sensors[j].Temp;
    //       h += sensors[j].Humid;
    //       p += sensors[j].pH;
    //     }
    //     temp[i] = Math.floor(t / datasize);
    //     humid[i] = Math.floor(h / datasize);
    //     ph[i] = Math.floor(p / datasize);
    //     t = 0;
    //     h = 0;
    //     p = 0;
    //   }

    //   this.bigChartData = [temp, humid, ph];
    //   for (let i = 0; i < dataCount / datasize; i++) this.bigChartLabels[i] = i;
    //   console.log(this.bigChartData);
    //   this.initBigChart(1);
    // } catch (error) {
    //   console.log(error);
    // }
  },
};
</script>
<style></style>
