<script>
	import NewsBlock from '../components/NewsBlock.svelte';

	let predictions;
	let positiveOrder = true;
	async function fecthPredictions() {
		try {
			predictions = await fetch('news').then((d) => d.json());
		} catch (e) {
			predictions = await fetch('static/test.json').then((d) => d.json());
		}
		predictions = predictions.sort((a, b) => b.sentiment - a.sentiment);
		console.log(predictions);
	}

	function toggleOrder() {
		positiveOrder = !positiveOrder;
		predictions = predictions
			.slice()
			.sort((a, b) => (positiveOrder ? b.sentiment - a.sentiment : a.sentiment - b.sentiment));
	}
</script>

<h1 class="text-3xl font-bold">The New York Times Homepage</h1>

<button
	class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
	on:click={toggleOrder}
>
	Click me
</button>

{#await fecthPredictions()}
	<p>Loading and running sentiment analysis on the latest news...</p>
{:then data}
	<ul>
		{#each predictions as entry, i}
			<li>
				<NewsBlock feedEntry={entry} />
			</li>
		{/each}
	</ul>
{:catch error}
	<p>An error occurred!</p>
{/await}
