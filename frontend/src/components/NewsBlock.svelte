<script>
	export let feedEntry;
</script>

<div class="group grid grid-cols-1 sm:grid-cols-3">
	<div>
		{#if feedEntry.media_content}
			<a target="_blank"  href={feedEntry.link}>
				<img
					class="hover:opacity-60 m-0 w-full max-w-[15rem] md:max-w-md object-cover object-top aspect-[4/3]"
					src={feedEntry.media_content[0].url}
					alt={feedEntry.title}
					loading="lazy"
				/>
			</a>
		{:else}
			<a target="_blank" href={feedEntry.link}>
				<div
					class="hover:opacity-60 bg-gray-200 h-full w-full max-w-[15rem] md:max-w-md object-cover object-top aspect-[4/3]"
				/>
			</a>
		{/if}
	</div>
	<div class="col-span-2 sm:pl-4">
		<div class="text-sm">
			Score:
			<span class="font-bold {feedEntry.sentiment > 0 ? 'text-emerald-600' : 'text-red-600'}">
				{feedEntry.sentiment.toFixed(4)}
			</span>
		</div>

		<a target="_blank" class="no-underline" href={feedEntry.link}>
			<h2 class="m-0 font-serif leading-tight hover:opacity-50">{feedEntry.title}</h2>
			<h5 class="mt-1 leading-tight {feedEntry.author ? 'visibile' : 'invisible'}">
				By {feedEntry.author}
			</h5>
			<p class="prose max-w-prose leading-normal prose-gray">{@html feedEntry.summary}</p>
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
