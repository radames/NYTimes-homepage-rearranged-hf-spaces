<script>
	export let feedEntry;
</script>

<div class="group flex">
	{#if feedEntry.media_content}
		<a target="_blank" href={feedEntry.link}>
			<img src={feedEntry.media_content[0].url} />
		</a>
	{/if}
    <b>{feedEntry.sentiment.toFixed(3)}</b>

	<a target="_blank" href={feedEntry.link}>
		<h2>{feedEntry.title}</h2>
		<h4>{feedEntry.author}</h4>
		<p>{feedEntry.summary}</p>
		{#if feedEntry.tags}
			{#each feedEntry.tags as tag}
				<span>{tag.term}</span>
			{/each}
		{/if}
	</a>
</div>
