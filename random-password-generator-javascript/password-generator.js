/* 
 * Random password generator (JavaScript)
 * 
 * Copyright (c) 2014 Nayuki Minase
 * All rights reserved. Contact Nayuki for licensing.
 * http://nayuki.eigenstate.org/page/random-password-generator-javascript
 */

"use strict";


function generate() {
	var charset = "";
	if (document.getElementById("numbers"  ).checked) charset += "0123456789";
	if (document.getElementById("lowercase").checked) charset += "abcdefghijklmnopqrstuvwxyz";
	if (document.getElementById("uppercase").checked) charset += "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
	if (document.getElementById("symbols"  ).checked) charset += "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~";
	if (document.getElementById("space"    ).checked) charset += " ";
	
	var password = "";
	var statistics = "";
	if (charset == "") {
		alert("Error: Character set is empty");
	} else {
		var length;
		if (document.getElementById("by-length").checked)
			length = parseInt(document.getElementById("length").value, 10);
		else if (document.getElementById("by-entropy").checked)
			length = Math.ceil(parseFloat(document.getElementById("entropy").value) * Math.log(2) / Math.log(charset.length));
		else
			throw "Assertion error";
		
		if (length < 0 || length > 10000)
			alert("Invalid password length");
		else {
			for (var i = 0; i < length; i++)
				password += charset.charAt(randomInt(charset.length));
			
			var entropy = Math.log(charset.length) * length / Math.log(2);
			var entropystr;
			if (entropy < 70)
				entropystr = entropy.toFixed(2);
			else if (entropy < 200)
				entropystr = entropy.toFixed(1);
			else
				entropystr = entropy.toFixed(0);
			statistics = "Length = " + length + " chars, Charset size = " + charset.length + " symbols, Entropy = " + entropystr + " bits";
		}
	}
	setElementText("password", password);
	setElementText("statistics", statistics);
}


// Returns a random integer in the range [0, n) using a variety of methods
function randomInt(n) {
	var x = randomIntMathRandom(n);
	x = (x + randomIntBrowserCrypto(n)) % n;
	return x;
}


// Not secure or high quality, but always available
function randomIntMathRandom(n) {	
	var x = Math.floor(Math.random() * n);
	if (x < 0 || x >= n)
		throw "Arithmetic exception";
	return x;
}


// Uses a secure, unpredictable random number generator if available; otherwise returns 0
function randomIntBrowserCrypto(n) {
	if (typeof Uint32Array == "function" && "crypto" in window && "getRandomValues" in window.crypto) {
		// Generate an unbiased sample
		var x = new Uint32Array(1);
		do window.crypto.getRandomValues(x);
		while (x[0] - x[0] % n > 4294967296 - n);
		return x[0] % n;
	} else
		return 0;
}


function setElementText(name, text) {
	var elem = document.getElementById(name);
	while (elem.firstChild != null)
		elem.removeChild(elem.firstChild);
	elem.appendChild(document.createTextNode(text));
}
