<script>
	import { Icon, Plus, Minus, Check, XMark } from "svelte-hero-icons";

	export let color = "blue"; // Default color
	export let label = ""; // Accessibility label
	export let onClick = () => {}; // OnClick event handler
	export let size = 32; // Default size
	export let icon; // name of the icon

	if (icon === "Plus") {
		icon = Plus;
	} else if (icon === "Minus") {
		icon = Minus;
	} else if (icon === "Check") {
		icon = Check;
	} else if (icon === "XMark") {
		icon = XMark;
	}

</script>

<button
	class="rounded-full text-white font-bold py-1 px-1 {`bg-${color}-500 hover:bg-${color}-700`}"
	aria-label={label}
	on:click={onClick}
>
	<Icon src="{icon}" size="32"/>
</button>