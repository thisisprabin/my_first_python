# Python

<h2>Installation steps in Windows</h2>
<p>To download click on the <a href="https://www.python.org/downloads/">link</a></p>
<p>Well that is just too easy you don't need to do anything it sets everything at the installation time not even the path variable but you do need to type a few commands to install in Linux, So follow these commands</p>

<h2>Installation steps in Ubuntu 14.04</h2>
<p>You need to use sudo command so <code>sudo -i</code></p>
<p>Enter you pasword, then make directory.</p>
<code>mkdir test</code><br>
<code>cd test</code>
<p>Then go python.org and select which file you want to download and then paste it in to the terminal.</p>
<code>wget https://www.python.org/downloads/release/python-353/</code>
<p>and hit enter, this will download python file into your system. Then</p>
<code>./configure</code>
<p>Compile the python files <code>make</code></p>
<p>Then install <code>make install</code></p>
<p>So if you goto <code>/usr/local/bin</code> then type <code>ls</code>you see the python files.</p>
<p>To run type <code>Python3.5</code> according to the above steps. So you can run it by get yourself into that folder or you can set the pythonpath variable.</p>
<code>export PYTHONPATH="$PYTHONPATH:/usr/local/bin"</code>
<p>and hit enter</p>
<p>Now if you type <code>Python3.5</code> you will get the 3.5 version and if you type <code>Python</code> you will get the older one.</p>




