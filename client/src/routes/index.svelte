<script>
	const fecthPredictions = fetch('news').then((d) => d.json());
</script>

<h1>The New York Times Homepage</h1>

{#await fecthPredictions}
	<p>Loading and running sentiment analysis on the latest news...</p>
{:then data}
	<ul>
		{#each data as entry, i}
			<li>
				<a target="_blank" href={entry.link}>
					{i + 1}: {entry.title}
				</a>
			</li>
		{/each}
	</ul>
{:catch error}
	<p>An error occurred!</p>
{/await}
