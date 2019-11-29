function simple_scheduler(fn, n) {
	setTimeout(fn, n);
}

function scheduler(fn, n, callback, ...args) {
	setTimeout(() => {
		fn.apply(this, args);
		if (callback) {
			callback();
		}
	}, n);
}
