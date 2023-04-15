const form = document.querySelector('form');
form.addEventListener('submit', handleSubmit);

function handleSubmit(event) {
	event.preventDefault();
	
	const data = new FormData(event.target);
	
	fetch('/predict', {
		method: 'POST',
		body: data
	})
	.then(response => response.json())
	.then(prediction => {
		const result = document.querySelector('#result');
		result.textContent = `Your chance of admission is ${prediction}%`;
	})
	.catch(error => {
		console.error(error);
	})
}
