<h2 data-start="1728" data-end="1750">Project Overview</h2>
<p data-start="1752" data-end="1789">Цей проєкт реалізує <strong data-start="1772" data-end="1788">ETL pipeline</strong>:</p>
<ol data-start="1791" data-end="2337">
<li data-start="1791" data-end="2023">
<p data-start="1794" data-end="1821"><strong data-start="1794" data-end="1819">Job1 (API → RAW JSON)</strong></p>
<ul data-start="1825" data-end="2023">
<li data-start="1825" data-end="1861">
<p data-start="1827" data-end="1861">Отримує дані продажів з REST API</p>
</li>
<li data-start="1865" data-end="1970">
<p data-start="1867" data-end="1903">Зберігає їх у JSON-файли у форматі</p>
<pre class="overflow-visible!" data-start="1909" data-end="1970"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>raw/sales/&lt;</span><span><span class="hljs-built_in">date</span></span><span>&gt;/sales_&lt;</span><span><span class="hljs-built_in">date</span></span><span>&gt;_&lt;page&gt;.json
</span></span></code></div></div></pre>
</li>
<li data-start="1974" data-end="2023">
<p data-start="1976" data-end="2023">Ідемпотентна: перед записом очищає директорію</p>
</li>
</ul>
</li>
<li data-start="2025" data-end="2188">
<p data-start="2028" data-end="2056"><strong data-start="2028" data-end="2054">Job2 (RAW JSON → AVRO)</strong></p>
<ul data-start="2060" data-end="2188">
<li data-start="2060" data-end="2095">
<p data-start="2062" data-end="2095">Конвертує всі JSON-файли у AVRO</p>
</li>
<li data-start="2099" data-end="2188">
<p data-start="2101" data-end="2121">Зберігає у форматі</p>
<pre class="overflow-visible!" data-start="2127" data-end="2188"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>stg/sales/&lt;</span><span><span class="hljs-built_in">date</span></span><span>&gt;/sales_&lt;</span><span><span class="hljs-built_in">date</span></span><span>&gt;_&lt;page&gt;.avro
</span></span></code></div></div></pre>
</li>
<li data-start="1974" data-end="2023">
<p data-start="1976" data-end="2023">Ідемпотентна: перед записом очищає директорію</p>
</li>
</ul>
</li>
<li data-start="2190" data-end="2337">
<p data-start="2193" data-end="2218"><strong data-start="2193" data-end="2216">Юніт-тести (pytest)</strong></p>
<ul data-start="2222" data-end="2337">
<li data-start="2222" data-end="2243">
<p data-start="2224" data-end="2243">Mock API для job1</p>
</li>
<li data-start="2247" data-end="2275">
<p data-start="2249" data-end="2275">Перевірка генерації JSON</p>
</li>
<li data-start="2279" data-end="2311">
<p data-start="2281" data-end="2311">Перевірка конвертації у AVRO</p>
</li>
<li data-start="2315" data-end="2337">
<p data-start="2317" data-end="2337">Використано fastavro</p>
</li>
</ul>
</li>
</ol>
<h1 data-start="1688" data-end="1726">Data Engineering Homework (lec02)</h1><hr data-start="2339" data-end="2342">
<h2 data-start="2344" data-end="2367">Project Structure</h2>
<pre class="overflow-visible!" data-start="2369" data-end="2701"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>lec02/
│
├── job1/
│   ├── </span><span><span class="hljs-selector-tag">main</span></span><span><span class="hljs-selector-class">.py</span></span><span>
│   ├── bll/
│   │    └── sales_api</span><span><span class="hljs-selector-class">.py</span></span><span>
│   └── dal/
│        └── storage</span><span><span class="hljs-selector-class">.py</span></span><span>
│
├── job2/
│   ├── </span><span><span class="hljs-selector-tag">main</span></span><span><span class="hljs-selector-class">.py</span></span><span>
│   ├── bll/
│   │    └── converter</span><span><span class="hljs-selector-class">.py</span></span><span>
│   └── dal/
│        └── storage</span><span><span class="hljs-selector-class">.py</span></span><span>
│
├── tests/
│   ├── test_job1</span><span><span class="hljs-selector-class">.py</span></span><span>
│   ├── test_job2</span><span><span class="hljs-selector-class">.py</span></span><span>
│   └── conftest</span><span><span class="hljs-selector-class">.py</span></span><span>
│
├── pyproject</span><span><span class="hljs-selector-class">.toml</span></span><span>
└── README</span><span><span class="hljs-selector-class">.md</span></span><span>
</span></span></code></div></div></pre>
<hr data-start="2703" data-end="2706">
<h2 data-start="2708" data-end="2726">Running Job1</h2>
<p data-start="2728" data-end="2753">Start API extraction job:</p>
<pre class="overflow-visible!" data-start="2755" data-end="2792"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-powershell"><span><span>python job1/main.py
</span></span></code></div></div></pre>
<p data-start="2794" data-end="2812">Send POST request:</p>
<pre class="overflow-visible!" data-start="2814" data-end="2993"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>curl -X POST http://localhost:8081/ \
  -H </span><span><span class="hljs-string">"Content-Type: application/json"</span></span><span> \
  -d </span><span><span class="hljs-string">"{ \"date\": \"2022-08-09\", \"raw_dir\": \"./file_storage/raw/sales/2022-08-09\" }"</span></span><span>
</span></span></code></div></div></pre>
<hr data-start="2995" data-end="2998">
<h2 data-start="3000" data-end="3018">Running Job2</h2>
<p data-start="3020" data-end="3041">Start Avro converter:</p>
<pre class="overflow-visible!" data-start="3043" data-end="3080"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-powershell"><span><span>python job2/main.py
</span></span></code></div></div></pre>
<p data-start="3082" data-end="3095">POST request:</p>
<pre class="overflow-visible!" data-start="3097" data-end="3304"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>curl -X POST http://localhost:8082/ \
  -H </span><span><span class="hljs-string">"Content-Type: application/json"</span></span><span> \
  -d </span><span><span class="hljs-string">"{ \"raw_dir\": \"./file_storage/raw/sales/2022-08-09\", \"stg_dir\": \"./file_storage/stg/sales/2022-08-09\" }"</span></span><span>
</span></span></code></div></div></pre>
<hr data-start="3306" data-end="3309">
<h2 data-start="3000" data-end="3018">Running check_jobs script</h2>
<p data-start="3020" data-end="3041">Start script:</p>
<pre class="overflow-visible!" data-start="3043" data-end="3080"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-powershell"><span><span>python check_jobs.py
</span></span></code></div></div></pre>
<hr data-start="3306" data-end="3309">

<h2 data-start="3311" data-end="3326">Run tests</h2>
<pre class="overflow-visible!" data-start="3328" data-end="3349"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre! language-bash"><span><span>pytest -v
</span></span></code></div></div></pre>
<hr data-start="3351" data-end="3354">
<h2 data-start="3356" data-end="3372">Tech Stack</h2>
<ul data-start="3374" data-end="3458">
<li data-start="3374" data-end="3389">
<p data-start="3376" data-end="3389">Python 3.12</p>
</li>
<li data-start="3390" data-end="3399">
<p data-start="3392" data-end="3399">Flask</p>
</li>
<li data-start="3400" data-end="3412">
<p data-start="3402" data-end="3412">Requests</p>
</li>
<li data-start="3413" data-end="3425">
<p data-start="3415" data-end="3425">Fastavro</p>
</li>
<li data-start="3426" data-end="3436">
<p data-start="3428" data-end="3436">Pytest</p>
</li>
<li data-start="3437" data-end="3458">
<p data-start="3439" data-end="3458">PEP8 &amp; type hints</p>
</li>
</ul>
<hr data-start="3460" data-end="3463">
<h2 data-start="3465" data-end="3480">Author</h2>
<p data-start="3482" data-end="3542"><strong data-start="3482" data-end="3498">Ruslan Konyk</strong></p>
