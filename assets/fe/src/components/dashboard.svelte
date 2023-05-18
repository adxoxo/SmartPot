<script lang="ts">
import { Gauge } from 'framework7-svelte';

</script>

<main>
    <h1>Welcome, Scott!</h1>
    <h3> This is the status of your plant </h3>
    <section id="plantStatus">
        <div>
            <div class="text-align-center">
                <Gauge
                type="circle"
                value={0.44}
                valueText="44%"
                valueTextColor="#ff9800"
                borderColor="#ff9800"
            />
            </div>
            
            <div class="text-align-center">
                <Gauge
                type="circle"
                value={0.44}
                valueText="44%"
                valueTextColor="#ff9800"
                borderColor="#ff9800"
            />
            </div>

            <div class="text-align-center">
                <Gauge
                type="circle"
                value={0.44}
                valueText="44%"
                valueTextColor="#ff9800"
                borderColor="#ff9800"
            />
            </div>

            <div class="text-align-center">
                <Gauge
                type="circle"
                value={0.44}
                valueText="44%"
                valueTextColor="#ff9800"
                borderColor="#ff9800"
            />
            </div>
        </div>
      <canvas id="plantStatusChart"></canvas>
    </section>
</main>