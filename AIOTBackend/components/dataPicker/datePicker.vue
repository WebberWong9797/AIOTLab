<template>
<div id="dataPickerDiv">
<p>{{this.$store.state.pickerDateInfo.startDate}}</p>
<p>{{this.$store.state.pickerDateInfo.endDate}}</p>
<date-range-picker
            ref="picker"
            :opens="opens"
            :locale-data="{ firstDay: 1, format: 'DD-MM-YYYY HH:mm:ss' }"
            :minDate="minDate" :maxDate="maxDate"
            :singleDatePicker="singleDatePicker"
            :timePicker="timePicker"
            :timePicker24Hour="timePicker24Hour"
            :showWeekNumbers="showWeekNumbers"
            :showDropdowns="showDropdowns"
            :autoApply="autoApply"
            v-model="dateRange"
            :linkedCalendars="linkedCalendars"
    >
<template v-slot:input="picker" style="min-width: 350px;">
            {{ picker.startDate }} - {{ picker.endDate }}
        </template>
    </date-range-picker>
    </div>
</template>
<script>
import DateRangePicker from 'vue2-daterange-picker'
import 'vue2-daterange-picker/dist/vue2-daterange-picker.css'
  export default {
      components: {DateRangePicker},
           name:'datePicker',
           data(){
                return{
                     opens:"right",
                     minDate:null,
                     maxDate:null,
                     singleDatePicker:false,
                     timePicker:false,
                     timePicker24Hour:true,
                     showWeekNumbers:false,
                     showDropdowns:true,
                     autoApply:false,
                     timePicker:true,
                dateRange:{
                     startDate:new Date(Date.now()),
                     endDate:new Date(Date.now()),
                         },
                linkedCalendars:true,
                      }
                 },
           watch:{
              dateRange:function(){
                   const result={
                      startDate:this.dateRange.startDate.toISOString(),
                      endDate:this.dateRange.endDate.toISOString(),
                   }
                   this.$store.commit("setPickerDateInfo", result);
                }
           },
  }
</script>
<style>
.form-control{
     color:black;
}
.ranges{
     color:black;
}
</style>