<script>
	export let feedEntry;
</script>

<div class="group grid grid-cols-1  sm:grid-cols-3">
	<div>
		{#if feedEntry.media_content}
			<a target="_blank" href={feedEntry.link}>
				<img
					class="w-full max-w-xs object-cover object-top aspect-[4/3]"
					src={feedEntry.media_content[0].url}
					alt={feedEntry.title}
				/>
			</a>
		{/if}
	</div>
	<div class="col-span-2  sm:pl-4">
		<div class="text-sm">
			Score:
			<span class="font-bold {feedEntry.sentiment > 0 ? 'text-emerald-600' : 'text-red-600'}">
				{feedEntry.sentiment.toFixed(4)}
			</span>
		</div>

		<a target="_blank" href={feedEntry.link}>
			<h2 class="text-2xl font-bold font-serif leading-tight">{feedEntry.title}</h2>
			<h4 class="text-sm font-bold leading-tight">By {feedEntry.author}</h4>
			<p class="py-3 max-w-prose leading-normal">{feedEntry.summary}</p>
			<!-- {#if feedEntry.tags}
				<div class="text-sm">
					{#each feedEntry.tags as tag}
						<span>{tag.term}</span>
					{/each}
				</div>
			{/if} -->
		</a>
	</div>
</div>
