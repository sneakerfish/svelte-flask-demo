<script>
	import { createEventDispatcher } from 'svelte';
	// Only import what you need!
	import { Icon, Plus, Minus, Check, XMark } from "svelte-hero-icons";
	import config from '$lib/config';

	export let todo = {};

	let dispatch = createEventDispatcher();

	let isEditing = false;
	let editedTitle = todo.title;

	function toggleComplete() {
		todo.completed = !todo.completed;
		dispatch('update', todo); // Dispatch update event
	}

	function handleEditStart() {
		isEditing = true;
		editedTitle = todo.title;
	}

	async function handleEditSave() {
		console.log("handleEditSave: ", editedTitle);
		console.log(todo);
		if (editedTitle.trim() !== '') {
			todo.title = editedTitle;
			try {
				const response = await fetch(config.apiUrl + `/todos/${todo.id}`, {
					method: 'PUT',
					headers: {
						'Content-Type': 'application/json'
					},
					body: JSON.stringify({ title: editedTitle })
				});
			} catch (err) {
				console.error(err);
				// Handle error (show a message to the user, etc.)
			}
			isEditing = false;
		}
	}

	function handleEditCancel() {
		isEditing = false;
		editedTitle = todo.title;
	}

	async function handleDelete() {
		try {
			const response = await fetch(config.apiUrl + `/todos/${todo.id}`, { method: 'DELETE' });
			if (!response.ok) {
				throw new Error(`Error deleting todo: ${response.status}`);
			}

			dispatch('delete', todo);
		} catch (err) {
			console.error(err);
			// Handle error (show a message to the user, etc.)
		}
	}
</script>

<li>

	{#if isEditing}
		<input class="min-w-60 m-1.5"
			bind:value={editedTitle} on:keydown.enter={handleEditSave} />
		<button class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-1 px-1 rounded-full"
						aria-label="Save changes"
						on:click={handleEditSave}>
			<Icon src="{Check}" size="32"/>
			</button>
		<button class="bg-red-500 hover:bg-red-700 text-white font-bold py-1 px-1 rounded-full"
						aria-label="Cancel changes"
						on:click={handleEditCancel}>
			<Icon src="{XMark}" size="32" /></button>
	{:else}
		<input type="checkbox" class="checked:bg-gray-900 checked:border-transparent"
					 bind:checked={todo.completed} on:change={toggleComplete} />
		<span class="min-w-60 m-1.5"
			class:completed={todo.completed} on:dblclick={handleEditStart}>{todo.title}</span>
		<button class="bg-red-500 hover:bg-red-700 text-white font-bold py-1 px-1 rounded-full"
						aria-label="Delete todo item" on:click={handleDelete}>
			<Icon src="{Minus}" size="32" />
			</button>
	{/if}
</li>

<style>
    /* TodoItem.svelte styles */
    li {
        display: flex; /* Use flexbox to align items in the row */
        align-items: center; /* Vertically center items */
        margin-bottom: 10px; /* Add spacing between items */
        padding: 8px; /* Add padding to each item */
        border-radius: 4px; /* Round the corners of each item */
        transition: background-color 0.2s; /* Add a transition for hover effect */
    }
    .completed {
        text-decoration: line-through;
    }

		/* Add styles for the checkbox */
		[type="checkbox"] {
			-webkit-appearance: none; /* Remove default checkbox appearance */
			width: 20px; /* Set width of checkbox */
			height: 20px; /* Set height of checkbox */
			border: 2px solid #ccc; /* Add border to checkbox */
			border-radius: 4px; /* Round the corners of the checkbox */
			margin-right: 10px; /* Add spacing between checkbox and text */
			cursor: pointer; /* Change cursor to pointer on hover */
		}
</style>