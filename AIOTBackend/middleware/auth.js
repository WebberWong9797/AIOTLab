export default function ({ redirect, $strapi }) {
  if (!$strapi.user) {
    return redirect('/home')
  } else {
    return redirect('/dashboard')
  }
}
