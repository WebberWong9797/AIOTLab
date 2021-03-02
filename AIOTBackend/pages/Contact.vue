<template>
  <b-container
    id="contact"
    class="pa-0 grey lighten-3 flex-wrap align-start fill-height"
    fluid
    tag="section"
  >
    <iframe
      allowfullscreen
      frameborder="0"
      height="500"
      src="https://www.google.com/maps/embed/v1/place?q=place_id:ChIJp4s0hO_4AzQRNh9tTWscVpQ&key=AIzaSyCNrOx-EHH27qOd30om_b624wH1d9RQznQ"
      style="border: 0"
      width="100%"
    />

    <b-row class="contact ma-0">
      <b-col cols="12" md="4">
        <h1 class="display-1 mb-8 font-weight-bold">Contact Info:</h1>

        <div class="mb-4">
          <strong>Sengital Address</strong><br />
          Flat H, 19/F, Shield Industrial Centre, No. 84-92 Chai Wan Kok Street,
          Tsuen Wan, N.T., Hong Kong
        </div>

        <div class="mb-4">
          <strong>Contact Number: </strong> (852) 2144-2628
        </div>

        <div class="mb-4"><strong>Contact Fax: </strong> (852) 2144-2623</div>

        <div class="mb-4">
          <strong>Contact Email(General): </strong> info@sengital.com <br />
          <strong>Contact Email(Sales): </strong> sales@sengital.com
        </div>
      </b-col>

      <b-col cols="12" md="5" class="emailForm">
        <b-row class="mb-6">
          <b-col class="form" cols="12" md="6">
            <b-form-input
              class="formIn"
              flat
              hide-details
              placeholder="Your Name"
              solo
            />
          </b-col>

          <b-col class="form" cols="12" md="6">
            <b-form-input
              class="formIn"
              flat
              hide-details
              placeholder="Your Email"
              solo
            />
          </b-col>
          <br />
          <b-col class="form" cols="12">
            <b-form-input
              class="formIn"
              flat
              hide-details
              placeholder="Your Title"
              solo
            />
          </b-col>
          <br />
          <b-col class="form" cols="12">
            <b-form-textarea
              class="formIn"
              flat
              hide-details
              placeholder="Your Message"
              solo
              height="200px"
            />
          </b-col>
        </b-row>

        <b-btn class="white--text" color="black" x-large>
          Send Message
        </b-btn>
      </b-col>
    </b-row>
  </b-container>
</template>

<script>
export default {
  layout: "navbar",
  data() {
    return {
      valid: true,
      name: "",
      nameRules: [
        (v) => !!v || "Name is required",
        (v) => (v && v.length <= 10) || "Name must be less than 10 characters",
      ],
      email: "",
      emailRules: [
        (v) => !!v || "E-mail is required",
        (v) => /.+@.+\..+/.test(v) || "E-mail must be valid",
      ],
      subject: "",
      subRules: [(v) => !!v || "subject is required"],
      msg: "",
      msgRules: [
        (v) => !!v || "message is required",
        (v) =>
          (v && v.length >= 10) || "Message must be more than 10 characters",
      ],
      lazy: false,
      contacts: [],
    };
  },
  methods: {
    validate() {
      this.$refs.form.validate();
    },
    reset() {
      this.$refs.form.reset();
    },
    resetValidation() {
      this.$refs.form.resetValidation();
    },
  },
};
</script>
<style lang="sass">
.contact
  justify-content: center
.emailForm
      align-self: center;
.form
  margin: 20px 0px
.formIn
  height: 50px
</style>
