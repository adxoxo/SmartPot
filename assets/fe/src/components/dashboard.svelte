<script lang="ts">
    import { Gauge } from 'framework7-svelte';
    import { onMount } from "svelte";


    let tempaveragePercent;
    let tempaverage_actualPercent;

    onMount(async () => {
    try {
        const response = await fetch('http://localhost:8000/api/data/temphumid/'); // Replace with your Django REST API URL
        const data = await response.json();
        tempaveragePercent = data.average.average_percent;
        tempaverage_actualPercent = data.average.average_actualpercent;
    } catch (error) {
        console.error(error);
    }
    });
</script>

<main>
    <h1>Welcome, Scott!</h1>
    <h3> This is the status of your plant </h3>
    <section id="plantStatus">
        <div class="container">
            <div class="row flex-row-reverse">
                <div class="col-md-3">
                    <div class="text-align-center">
                        <Gauge
                        type="circle"
                        value={0.44}
                        valueText="44%"
                        valueTextColor="#ff9800"
                        borderColor="#ff9800"
                        />
                    </div>
                    <p> Soil Moisture </p>
                </div>

                <div class="col-md-3">
                    <div class="text-align-center">
                        <Gauge
                        type="circle"
                        value={0.44}
                        valueText="44%"
                        valueTextColor="#ff9800"
                        borderColor="#ff9800"
                        />
                    </div>
                    <p> Light </p>
                </div>

                <div class="col-md-3">
                    <div class="text-align-center">
                        <Gauge
                        type="circle"
                        value={0.44}
                        valueText="44%"
                        valueTextColor="#ff9800"
                        borderColor="#ff9800"
                        />
                    </div>
                    <p> Humidity </p>
                </div>

                <div class="col-md-3">
                    <div class="text-align-center">
                        <Gauge
                        type="circle"
                        value={tempaveragePercent}
                        valueText="{tempaverage_actualPercent}%"
                        valueTextColor="#ff9800"
                        borderColor="#ff9800"
                        />
                    </div>
                    <p> Temperature </p>
                </div>


            </div>
        </div>
      <canvas id="plantStatusChart"></canvas>
    </section>
</main>