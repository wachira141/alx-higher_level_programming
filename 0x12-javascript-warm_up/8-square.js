#!/usr/bin/node
const size = Math.floor(process.argv[2]);
if (isNaN(size))
{
	console.log("Missing size");
} else {
for (let y = 0; y < size; y++)
	{
		let draw = '';
for (let x = 0; x < size; x ++) draw += 'X';
		console.log(draw);
	}
}
