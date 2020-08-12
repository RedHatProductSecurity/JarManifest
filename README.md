JarManifest
===========
Extract manifest information from Java library files (jars).

Description
-----------
Use this library to look at jar META-INF/MANIFEST files and extract Implementation-Title, and Implementation-Version. Based on the specification of jars found [here](https://docs.oracle.com/javase/7/docs/technotes/guides/jar/jar.html)

Installation
------------

	pip install virtualenv

A jarmanfiest.cfg file should you copied to your python's `etc` directory

Usage
-----

```python
$ python3
>>> from jarmanifest import manifest
>>> manifest.getAttributes('/tmp/spring/META-INF/MANIFEST.MF')
[{'implementationtitle': 'org.springframework.core', 'implementationversion': '3.1.3.RELEASE'}]
```

