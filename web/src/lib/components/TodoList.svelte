<script>
	import TodoItem from './TodoItem.svelte';
	import config from '$lib/config.js';
	import { Icon, Plus, Minus, Check, XMark } from "svelte-hero-icons";
	import IconButton from '$lib/components/IconButton.svelte';

	export let todos = [];
	export let showCompleted = false;
	export let filterText = '';

	// A single todo for adding items.
	export let todo = {};

	let isAdding = false;
	let addedTitle = '';

	$: filteredTodos = todos
		.filter(todo => !showCompleted || todo.completed)
		.filter(todo => todo.title.toLowerCase().includes(filterText.toLowerCase()));

	function handleAddStart() {
		isAdding = true;
		addedTitle = todo.title;
	}

	async function handleAddSave() {
		console.log("handleAddSave: ", addedTitle);
		console.log(todo);
		if (addedTitle.trim() !== '') {
			todo.title = addedTitle;
			try {
				const response = await fetch(config.apiUrl + `/todos`, {
					method: 'POST',
					headers: {
						'Content-Type': 'application/json'
					},
					body: JSON.stringify({ title: addedTitle })
				});
			} catch (err) {
				console.error(err);
				// Handle error (show a message to the user, etc.)
			}
			isAdding = false;
		}
	}

	function handleAddCancel() {
		isAdding = false;
		addedTitle = todo.title;
	}


</script>

<ul>
	{#if isAdding}
		<li>
			<input type="text" bind:value={addedTitle} />
			<IconButton label="Save new todo"
						onClick={handleAddSave}
									color="green"
						icon="Check" />
			<IconButton label="Cancel new todo"
						onClick={handleAddCancel}
									color="red"
						icon="XMark" />
		</li>
	{:else}
		<li>
			<IconButton label="Add new todo"
						onClick={handleAddStart}
									color="blue"
						icon="Plus" />
		</li>
		{#each filteredTodos as todo}
			<TodoItem {todo} on:update on:delete />
		{/each}
	{/if}
</ul>
