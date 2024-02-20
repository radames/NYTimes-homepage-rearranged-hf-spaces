<script>
	import NewsBlock from './components/NewsBlock.svelte';
	let feeds = [
		{
			label: 'NYTimes',
			value: 'https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml'
		},
		{
			label: 'SF Gate Bay Area',
			value: 'https://www.sfgate.com/bayarea/feed/Bay-Area-News-429.php'
		},
		{
			label: 'BBC News',
			value: 'https://feeds.bbci.co.uk/news/rss.xml'
		},
		{
			label: 'Buzz Feed World',
			value: 'https://www.buzzfeed.com/world.xml'
		},
		{
			label: 'Al Jazeera',
			value: 'https://aljazeera.com/xml/rss/all.xml'
		},
		{
			label: 'Hacker News Front Page',
			value: 'https://hnrss.org/frontpage'
		},
		{
			label: 'Reddit World News',
			value: 'https://www.reddit.com/r/worldnews/.rss'
		}
	];
	let selectedFeedUrl = feeds[0].value;
	let predictions;
	let lastUpdate;
	let positiveOrder = true;
	async function fecthPredictions(feedUrl) {
		console.log(feedUrl);
		try {
			predictions = await fetch(`/api/news?feed_url=${feedUrl}`).then((d) => d.json());
		} catch (e) {
			// hack to develop locally without having to run the server
			predictions = await fetch('test.json').then((d) => d.json());
		}
		lastUpdate = new Date(predictions.last_update);
		predictions = predictions.entries.sort((a, b) => b.sentiment - a.sentiment);
		positiveOrder = true;
		console.log(lastUpdate, predictions);
	}

	function toggleOrder() {
		positiveOrder = !positiveOrder;
		predictions = predictions
			.slice()
			.sort((a, b) => (positiveOrder ? b.sentiment - a.sentiment : a.sentiment - b.sentiment));
	}
</script>

<article class="prose px-6 py-3 max-w-4xl mx-auto">
	<h1 class="font-serif mb-0">The New York Times Sentiment Analysis</h1>
	<h5 class="mt-0 {lastUpdate ? 'visibile' : 'invisible'}">
		<b>Last Updated:</b>
		{lastUpdate ? lastUpdate.toLocaleString() : ''}
	</h5>

	<p class="py-3 max-w-prose leading-normal">
		This project is an experiment running sentiment analysis on the current
		<a
			class="text-blue-500 underline hover:no-underline"
			target="_blank"
			href="https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml">New York Times</a
		>
		homepage headlines RSS. It also provides a sorting button to toggle between {positiveOrder
			? 'good and bad news'
			: 'bad and good news'} first😛 . It's built with a
		<a
			class="text-blue-500 underline hover:no-underline"
			target="_blank"
			href="https://huggingface.co/spaces/radames/NYTimes-homepage-rearranged/tree/main/client"
		>
			custom SvelveKit front-end
		</a>
		, served by a
		<a
			class="text-blue-500 underline hover:no-underline"
			target="_blank"
			href="https://huggingface.co/spaces/radames/NYTimes-homepage-rearranged/blob/main/app.py"
		>
			Flask application
		</a>
		and using
		<a
			class="text-blue-500 underline hover:no-underline"
			target="_blank"
			href="https://huggingface.co/siebert/sentiment-roberta-large-english"
		>
			transformers pipeline for the sentiment analysis.
		</a>
	</p>
	<details>
		<summary class="cursor-pointer">Notes</summary>
		<h4>Install Node with NVM</h4>
		<p class="max-w-prose leading-normal">
			This <a
				class="text-blue-500 underline hover:no-underline"
				target="_blank"
				href="https://huggingface.co/spaces/radames/NYTimes-homepage-rearranged/blob/main/install-node.sh"
				>Node script</a
			>

			install node LTS and create symbolic links to <code>/home/user/.local/bin/</code> as it seems
			like we don't have permission to update <code>$PATH</code> env
		</p>
		<h4>main.py</h4>
		<p class="max-w-prose leading-normal">
			Because the Spaces run a python application, see
			<a
				class="text-blue-500 underline hover:no-underline"
				target="_blank"
				href="https://huggingface.co/docs/hub/spaces#:~:text=0.88.0%2C%200.89.0%2C%201.0.0.-,app_file,-%3A%20string%0APath%20to"
			>
				<code> app_file </code>
			</a>
			on docs. <b>main.py</b> is just a simple python subprocess to run
			<code> make build-all </code>
			See
			<a
				class="text-blue-500 underline hover:no-underline"
				target="_blank"
				href="https://huggingface.co/spaces/radames/NYTimes-homepage-rearranged/blob/main/Makefile"
			>
				<code>Makefile</code>
			</a>
		</p>
		<h4>SvelteKit Node Adapter?</h4>
		<p class="max-w-prose leading-normal">
			SvelteKit eventually can be used as our primary web application with
			<a
				class="text-blue-500 underline hover:no-underline"
				target="_blank"
				href="https://github.com/sveltejs/kit/tree/master/packages/adapter-node"
			>
				<code>@sveltejs/adapter-node</code></a
			>
			adaptor and Flask the API application with your ML project. However, there is an unsolved issue
			to enable
			<a
				href="https://github.com/sveltejs/kit/issues/595"
				class="text-blue-500 underline hover:no-underline"
			>
				dynamic basepath</a
			>, which blocks the possibility to embedded deployment or using a relative path.
		</p>
	</details>

	<p class="max-w-prose leading-normal">
		You can try other news feeds <select
			class="inline-block text-xs bg-gray-200 border border-gray-200 text-gray-700 px-0 py-0 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
			bind:value={selectedFeedUrl}
		>
			{#each feeds as feed (feed.value)}
				<option value={feed.value}>{feed.label}</option>
			{/each}
		</select>; however the NYTimes feed comes with more information than the other feeds, such as
		the thumbnail image, author, and more.
	</p>
	<div class="py-4" />
	<button
		class="{positiveOrder
			? 'bg-emerald-600'
			: 'bg-red-600'} hover:bg-zinc-300 text-white font-bold py-2 px-4 rounded"
		on:click={toggleOrder}
	>
		{!positiveOrder ? 'Sorted by negative scores' : 'Sorted by positive scores'}
	</button>
	{#await fecthPredictions(selectedFeedUrl)}
		<div class="py-4">
			<svg class="animate-spin inline-block" width="25" height="25" viewBox="0 0 100 100">
				<path d="M0,50 a1,1 0 0,0 100,0" fill="lightgrey" />
			</svg>
			Loading feed and running sentiment analysis on headlines...
		</div>
	{:then data}
		<ul class="m-0 p-0">
			{#each predictions as entry, i}
				<li class="py-5">
					<NewsBlock feedEntry={entry} />
					<div class="border-b border-gray-200 py-2" />
				</li>
			{/each}
		</ul>
	{:catch error}
		<p>An error occurred!</p>
	{/await}
</article>
