<script>
	import NewsBlock from '../components/NewsBlock.svelte';

	let predictions;
	let lastUpdate;
	let positiveOrder = true;
	async function fecthPredictions() {
		try {
			predictions = await fetch('news').then((d) => d.json());
		} catch (e) {
			// hack to develop locally without having to run the server
			predictions = await fetch('static/test.json').then((d) => d.json());
		}
		lastUpdate = predictions.last_update;
		predictions = predictions.entries.sort((a, b) => b.sentiment - a.sentiment);
		console.log(predictions);
	}

	function toggleOrder() {
		positiveOrder = !positiveOrder;
		predictions = predictions
			.slice()
			.sort((a, b) => (positiveOrder ? b.sentiment - a.sentiment : a.sentiment - b.sentiment));
	}
</script>

<div class="px-6 py-3 max-w-4xl mx-auto">
	<h1 class="text-4xl font-bold font-serif py-5 leading-tight">The New York Times Homepage</h1>

	<button
		class="{positiveOrder ? 'bg-emerald-600' :'bg-red-600'} bg-blue-500 hover:bg-zinc-300 text-white font-bold py-2 px-4 rounded"
		on:click={toggleOrder}
	>
		{!positiveOrder ? 'Sorted by negative' : 'Sorted by positive'}
	</button>

	{#await fecthPredictions()}
		<p>Loading and running sentiment analysis on the latest news...</p>
	{:then data}
		<ul>
			{#each predictions as entry, i}
				<li class="py-5">
					<NewsBlock feedEntry={entry} />
					<div class="border-b border-gray-200 py-2"></div>
				</li>
			{/each}
		</ul>
	{:catch error}
		<p>An error occurred!</p>
	{/await}
</div>
