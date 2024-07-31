<script>
	import TodoItem from './TodoItem.svelte';

	export let todos = [];
	export let showCompleted = false;
	export let filterText = '';

	$: filteredTodos = todos
		.filter(todo => !showCompleted || todo.completed)
		.filter(todo => todo.title.toLowerCase().includes(filterText.toLowerCase()));
</script>

<ul>
	{#each filteredTodos as todo}
		<TodoItem {todo} on:update on:delete />
	{/each}
</ul>
