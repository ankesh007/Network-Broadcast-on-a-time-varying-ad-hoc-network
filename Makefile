submit:
	rm -rf assignment3/
	rm -rf assignment3.zip
	mkdir assignment3
	cp -r doc/ assignment3/
	cp -r src/ assignment3/
	cp -r Problem\ Statement assignment3/
	zip -r assignment3.zip assignment3/./
	rm -rf assignment3/

