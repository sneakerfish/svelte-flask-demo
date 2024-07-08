<script>
	import { onMount } from 'svelte';

	let todos = [];
	let error = null;

	onMount(async () => {
		try {
			const response = await fetch('http://localhost:5000/todos');
			todos = await response.json();
			console.log(todos);
		} catch (err) {
			error = "Error fetching todos: " + err.message;
		}
	});
</script>

{#if error}
	<p>{error}</p>
{:else}
	<table>
		<thead>
		<tr>
			<th>ID</th>
			<th>Title</th>
			<th>Completed</th>
		</tr>
		</thead>
		<tbody>
		{#each todos as todo}
			<tr>
				<td>{todo.id}</td>
				<td>{todo.title}</td>
				<td>{todo.completed ? 'Yes' : 'No'}</td>
			</tr>
		{/each}
		</tbody>
	</table>
{/if}
