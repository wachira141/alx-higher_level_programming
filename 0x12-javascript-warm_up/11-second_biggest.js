#!/usr/bin/node
if (process.argv.length <= 3)
{
	console.log(0);
} else
{
	let big = Number(process.argv[3]);
for (let i = 3; i < process.argv.length; i++)
	{
		if (big < Number(process.argv[i])) big = Number(process.argv[i]);
	}
console.log(big);
}
