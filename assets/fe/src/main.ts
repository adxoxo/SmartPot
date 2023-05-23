import './app.css'
import App from './App.svelte'
import './styles/bootstrap'

const app = new App({
  target: document.getElementById('app'),
})

export default app

createApp(App).mount('#app');