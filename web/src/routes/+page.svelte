<script>
	import { onMount } from 'svelte';
	import TodoList from '../lib/components/TodoList.svelte';


	let todos = [];
	let error = null;

	onMount(async () => {
		try {
			const response = await fetch('http://localhost:5000/todos');
			todos = await response.json();
		} catch (err) {
			error = "Error fetching todos: " + err.message;
		}
	});

	let showCompleted = false;
	let filterText = '';

	function handleUpdate(event) {
		// Update todo in the original todos array or send API request
	}

	function handleDelete(event) {
		// Delete todo from the original todos array or send API request
	}
</script>

<div class="container">
	<div class="todo-list-wrapper">
		<h2>Todo List</h2>
		<TodoList {todos} bind:showCompleted bind:filterText on:update={handleUpdate} on:delete={handleDelete} />
	</div>
</div>

<style>
    .container {
        display: grid; /* Use grid for overall layout */
        place-items: center; /* Center content horizontally and vertically */
        min-height: 100vh; /* Ensure container fills viewport height */
    }

    .todo-list-wrapper {
        background-color: #f0f0f5; /* Light background color */
        padding: 20px;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); /* Subtle shadow */
    }

    h2 {
        text-align: center;
        margin-bottom: 15px;
    }

    ul {
        list-style: none;
        padding: 0;
    }

    /* ... (styles for TodoItem component) */
</style>