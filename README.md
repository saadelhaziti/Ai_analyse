<div id="top">

<!-- HEADER STYLE: CLASSIC -->
<div align="center">

<img src="readmeai/assets/logos/purple.svg" width="30%" style="position: relative; top: 0; right: 0;" alt="Project Logo"/>


# AI Analyse Platform


An advanced platform for retail data analysis, chatbot integration, and visualization using Python, Docker, MinIO, Elasticsearch, and Ollama.

<!-- BADGES -->
<!-- local repository, no metadata badges. -->

<em>Built with the tools and technologies:</em>

<img src="https://img.shields.io/badge/JSON-000000.svg?style=default&logo=JSON&logoColor=white" alt="JSON">
<img src="https://img.shields.io/badge/Ollama-000000.svg?style=default&logo=Ollama&logoColor=white" alt="Ollama">
<img src="https://img.shields.io/badge/BSD-AB2B28.svg?style=default&logo=BSD&logoColor=white" alt="BSD">
<img src="https://img.shields.io/badge/TOML-9C4121.svg?style=default&logo=TOML&logoColor=white" alt="TOML">
<img src="https://img.shields.io/badge/JavaScript-F7DF1E.svg?style=default&logo=JavaScript&logoColor=black" alt="JavaScript">
<img src="https://img.shields.io/badge/GNU%20Bash-4EAA25.svg?style=default&logo=GNU-Bash&logoColor=white" alt="GNU%20Bash">
<img src="https://img.shields.io/badge/Elasticsearch-005571.svg?style=default&logo=Elasticsearch&logoColor=white" alt="Elasticsearch">
<img src="https://img.shields.io/badge/Kibana-005571.svg?style=default&logo=Kibana&logoColor=white" alt="Kibana">
<br>
<img src="https://img.shields.io/badge/Docker-2496ED.svg?style=default&logo=Docker&logoColor=white" alt="Docker">
<img src="https://img.shields.io/badge/XML-005FAD.svg?style=default&logo=XML&logoColor=white" alt="XML">
<img src="https://img.shields.io/badge/Python-3776AB.svg?style=default&logo=Python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/bat-31369E.svg?style=default&logo=bat&logoColor=white" alt="bat">
<img src="https://img.shields.io/badge/MinIO-C72E49.svg?style=default&logo=MinIO&logoColor=white" alt="MinIO">
<img src="https://img.shields.io/badge/Apache-D22128.svg?style=default&logo=Apache&logoColor=white" alt="Apache">
<img src="https://img.shields.io/badge/YAML-CB171E.svg?style=default&logo=YAML&logoColor=white" alt="YAML">

</div>
<br>

---

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
    - [Project Index](#project-index)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Usage](#usage)
    - [Testing](#testing)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## Overview



---

## Features


- Retail data analysis and visualization
- Chatbot integration for interactive queries
- Data storage with MinIO and Elasticsearch
- LLM-powered CSV and SQL prompt generation

---


## Project Structure

```
├── chatbot/              # Chatbot logic, routes, controllers, schemas, services
├── DB_Save/              # Data saving logic for MinIO and Elasticsearch
├── llm_engine/           # LLM prompt generation and registry
├── Models/               # Data models and interfaces
├── retail_db/            # Retail CSV data and DB initialization
├── users/                # User management, routes, services
├── Visualizer_csv/       # CSV analysis and visualization
├── Visualizer_DB/        # DB visualization and save logic
├── create_db.py          # DB creation script
├── docker-compose.yml    # Docker orchestration
├── Dockerfile*           # Docker build files
├── requirements.txt      # Python dependencies
├── main.py               # Main entrypoint
```

### Project Index

<details open>
	<summary><b><code>/</code></b></summary>
	<!-- __root__ Submodule -->
	<details>
		<summary><b>__root__</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ __root__</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='/create_db.py'>create_db.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='/docker-compose.yml'>docker-compose.yml</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='/Dockerfile'>Dockerfile</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='/Dockerfile.init_minio'>Dockerfile.init_minio</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='/Dockerfile.ollama'>Dockerfile.ollama</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='/init.sql'>init.sql</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='/init_minio.py'>init_minio.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='/main.py'>main.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='/requirements.txt'>requirements.txt</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='/start_ollama.sh'>start_ollama.sh</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='/wait_for_postgres.py'>wait_for_postgres.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- chatbot Submodule -->
	<details>
		<summary><b>chatbot</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ chatbot</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='/chatbot/routes.py'>routes.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
			</table>
			<!-- controllers Submodule -->
			<details>
				<summary><b>controllers</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ chatbot.controllers</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='/chatbot/controllers/chatbot_controller.py'>chatbot_controller.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- schemas Submodule -->
			<details>
				<summary><b>schemas</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ chatbot.schemas</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='/chatbot/schemas/chat_schema.py'>chat_schema.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- services Submodule -->
			<details>
				<summary><b>services</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ chatbot.services</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='/chatbot/services/chatbot_services.py'>chatbot_services.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='/chatbot/services/chat_manager.py'>chat_manager.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='/chatbot/services/retail_rag.py'>retail_rag.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
					<!-- retail_data_store Submodule -->
					<details>
						<summary><b>retail_data_store</b></summary>
						<blockquote>
							<div class='directory-path' style='padding: 8px 0; color: #666;'>
								<code><b>⦿ chatbot.services.retail_data_store</b></code>
							<table style='width: 100%; border-collapse: collapse;'>
							<thead>
								<tr style='background-color: #f8f9fa;'>
									<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
									<th style='text-align: left; padding: 8px;'>Summary</th>
								</tr>
							</thead>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='/chatbot/services/retail_data_store/retail_faiss_index.faiss'>retail_faiss_index.faiss</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
							</table>
						</blockquote>
					</details>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<!-- DB_Save Submodule -->
	<details>
		<summary><b>DB_Save</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ DB_Save</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='/DB_Save/routes.py'>routes.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
			</table>
			<!-- controller Submodule -->
			<details>
				<summary><b>controller</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ DB_Save.controller</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='/DB_Save/controller/controller_elasticSearch.py'>controller_elasticSearch.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='/DB_Save/controller/Minio_controller.py'>Minio_controller.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- Models_save Submodule -->
			<details>
				<summary><b>Models_save</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ DB_Save.Models_save</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='/DB_Save/Models_save/ElasticSearch.py'>ElasticSearch.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='/DB_Save/Models_save/Minio.py'>Minio.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='/DB_Save/Models_save/minio_config.py'>minio_config.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='/DB_Save/Models_save/Minio_forma_save.py'>Minio_forma_save.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<!-- llm_engine Submodule -->
	<details>
		<summary><b>llm_engine</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ llm_engine</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='/llm_engine/prepare_csv_prompt.py'>prepare_csv_prompt.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='/llm_engine/prompt_loader.py'>prompt_loader.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='/llm_engine/prompt_registry.json'>prompt_registry.json</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
			</table>
			<!-- prompts Submodule -->
			<details>
				<summary><b>prompts</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ llm_engine.prompts</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='/llm_engine/prompts/csv_analysis.j2'>csv_analysis.j2</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='/llm_engine/prompts/sql_analysis.j2'>sql_analysis.j2</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<!-- Models Submodule -->
	<details>
		<summary><b>Models</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ Models</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='/Models/abstract.py'>abstract.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='/Models/db_credentials.py'>db_credentials.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='/Models/Interface.py'>Interface.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='/Models/recom.py'>recom.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='/Models/schema.py'>schema.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- retail_db Submodule -->
	<details>
		<summary><b>retail_db</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ retail_db</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='/retail_db/dbinit.py'>dbinit.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- users Submodule -->
	<details>
		<summary><b>users</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ users</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='/users/routes.py'>routes.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
			</table>
			<!-- controller Submodule -->
			<details>
				<summary><b>controller</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ users.controller</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='/users/controller/Project_controller.py'>Project_controller.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='/users/controller/User_controller.py'>User_controller.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- Models Submodule -->
			<details>
				<summary><b>Models</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ users.Models</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='/users/Models/model.py'>model.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='/users/Models/schemas.py'>schemas.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- services Submodule -->
			<details>
				<summary><b>services</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ users.services</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='/users/services/database.py'>database.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='/users/services/Project_Services.py'>Project_Services.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='/users/services/security.py'>security.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='/users/services/User_Services.py'>User_Services.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<!-- venv Submodule -->
	<details>
		<summary><b>venv</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ venv</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='/venv/pyvenv.cfg'>pyvenv.cfg</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
			</table>
			<!-- Lib Submodule -->
			<details>
				<summary><b>Lib</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ venv.Lib</b></code>
					<!-- site-packages Submodule -->
					<details>
						<summary><b>site-packages</b></summary>
						<blockquote>
							<div class='directory-path' style='padding: 8px 0; color: #666;'>
								<code><b>⦿ venv.Lib.site-packages</b></code>
							<table style='width: 100%; border-collapse: collapse;'>
							<thead>
								<tr style='background-color: #f8f9fa;'>
									<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
									<th style='text-align: left; padding: 8px;'>Summary</th>
								</tr>
							</thead>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/distutils-precedence.pth'>distutils-precedence.pth</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
								<tr style='border-bottom: 1px solid #eee;'>
									<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/typing_extensions.py'>typing_extensions.py</a></b></td>
									<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
								</tr>
							</table>
							<!-- aiohappyeyeballs Submodule -->
							<details>
								<summary><b>aiohappyeyeballs</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.aiohappyeyeballs</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohappyeyeballs/impl.py'>impl.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohappyeyeballs/py.typed'>py.typed</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohappyeyeballs/types.py'>types.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohappyeyeballs/utils.py'>utils.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohappyeyeballs/_staggered.py'>_staggered.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- aiohappyeyeballs-2.6.1.dist-info Submodule -->
							<details>
								<summary><b>aiohappyeyeballs-2.6.1.dist-info</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.aiohappyeyeballs-2.6.1.dist-info</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohappyeyeballs-2.6.1.dist-info/INSTALLER'>INSTALLER</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohappyeyeballs-2.6.1.dist-info/LICENSE'>LICENSE</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohappyeyeballs-2.6.1.dist-info/METADATA'>METADATA</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohappyeyeballs-2.6.1.dist-info/RECORD'>RECORD</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohappyeyeballs-2.6.1.dist-info/WHEEL'>WHEEL</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- aiohttp Submodule -->
							<details>
								<summary><b>aiohttp</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.aiohttp</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/abc.py'>abc.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/base_protocol.py'>base_protocol.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/client.py'>client.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/client_exceptions.py'>client_exceptions.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/client_middlewares.py'>client_middlewares.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/client_middleware_digest_auth.py'>client_middleware_digest_auth.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/client_proto.py'>client_proto.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/client_reqrep.py'>client_reqrep.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/client_ws.py'>client_ws.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/compression_utils.py'>compression_utils.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/connector.py'>connector.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/cookiejar.py'>cookiejar.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/formdata.py'>formdata.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/hdrs.py'>hdrs.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/helpers.py'>helpers.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/http.py'>http.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/http_exceptions.py'>http_exceptions.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/http_parser.py'>http_parser.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/http_websocket.py'>http_websocket.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/http_writer.py'>http_writer.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/log.py'>log.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/multipart.py'>multipart.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/payload.py'>payload.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/payload_streamer.py'>payload_streamer.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/py.typed'>py.typed</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/pytest_plugin.py'>pytest_plugin.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/resolver.py'>resolver.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/streams.py'>streams.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/tcp_helpers.py'>tcp_helpers.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/test_utils.py'>test_utils.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/tracing.py'>tracing.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/typedefs.py'>typedefs.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/web.py'>web.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/web_app.py'>web_app.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/web_exceptions.py'>web_exceptions.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/web_fileresponse.py'>web_fileresponse.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/web_log.py'>web_log.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/web_middlewares.py'>web_middlewares.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/web_protocol.py'>web_protocol.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/web_request.py'>web_request.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/web_response.py'>web_response.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/web_routedef.py'>web_routedef.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/web_runner.py'>web_runner.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/web_server.py'>web_server.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/web_urldispatcher.py'>web_urldispatcher.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/web_ws.py'>web_ws.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/worker.py'>worker.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/_cookie_helpers.py'>_cookie_helpers.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/_cparser.pxd'>_cparser.pxd</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/_find_header.pxd'>_find_header.pxd</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/_headers.pxi'>_headers.pxi</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/_http_parser.pyx'>_http_parser.pyx</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/_http_writer.pyx'>_http_writer.pyx</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
									<!-- .hash Submodule -->
									<details>
										<summary><b>.hash</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.aiohttp..hash</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/.hash/hdrs.py.hash'>hdrs.py.hash</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/.hash/_cparser.pxd.hash'>_cparser.pxd.hash</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/.hash/_find_header.pxd.hash'>_find_header.pxd.hash</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/.hash/_http_parser.pyx.hash'>_http_parser.pyx.hash</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/.hash/_http_writer.pyx.hash'>_http_writer.pyx.hash</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
									<!-- _websocket Submodule -->
									<details>
										<summary><b>_websocket</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.aiohttp._websocket</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/_websocket/helpers.py'>helpers.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/_websocket/mask.pxd'>mask.pxd</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/_websocket/mask.pyx'>mask.pyx</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/_websocket/models.py'>models.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/_websocket/reader.py'>reader.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/_websocket/reader_c.pxd'>reader_c.pxd</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/_websocket/reader_c.py'>reader_c.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/_websocket/reader_py.py'>reader_py.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/_websocket/writer.py'>writer.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
											<!-- .hash Submodule -->
											<details>
												<summary><b>.hash</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.aiohttp._websocket..hash</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/_websocket/.hash/mask.pxd.hash'>mask.pxd.hash</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/_websocket/.hash/mask.pyx.hash'>mask.pyx.hash</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp/_websocket/.hash/reader_c.pxd.hash'>reader_c.pxd.hash</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<!-- aiohttp-3.12.15.dist-info Submodule -->
							<details>
								<summary><b>aiohttp-3.12.15.dist-info</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.aiohttp-3.12.15.dist-info</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp-3.12.15.dist-info/INSTALLER'>INSTALLER</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp-3.12.15.dist-info/METADATA'>METADATA</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp-3.12.15.dist-info/RECORD'>RECORD</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp-3.12.15.dist-info/top_level.txt'>top_level.txt</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp-3.12.15.dist-info/WHEEL'>WHEEL</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
									<!-- licenses Submodule -->
									<details>
										<summary><b>licenses</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.aiohttp-3.12.15.dist-info.licenses</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp-3.12.15.dist-info/licenses/LICENSE.txt'>LICENSE.txt</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
											<!-- vendor Submodule -->
											<details>
												<summary><b>vendor</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.aiohttp-3.12.15.dist-info.licenses.vendor</b></code>
													<!-- llhttp Submodule -->
													<details>
														<summary><b>llhttp</b></summary>
														<blockquote>
															<div class='directory-path' style='padding: 8px 0; color: #666;'>
																<code><b>⦿ venv.Lib.site-packages.aiohttp-3.12.15.dist-info.licenses.vendor.llhttp</b></code>
															<table style='width: 100%; border-collapse: collapse;'>
															<thead>
																<tr style='background-color: #f8f9fa;'>
																	<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																	<th style='text-align: left; padding: 8px;'>Summary</th>
																</tr>
															</thead>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiohttp-3.12.15.dist-info/licenses/vendor/llhttp/LICENSE'>LICENSE</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
															</table>
														</blockquote>
													</details>
												</blockquote>
											</details>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<!-- aiosignal Submodule -->
							<details>
								<summary><b>aiosignal</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.aiosignal</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiosignal/py.typed'>py.typed</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- aiosignal-1.4.0.dist-info Submodule -->
							<details>
								<summary><b>aiosignal-1.4.0.dist-info</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.aiosignal-1.4.0.dist-info</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiosignal-1.4.0.dist-info/INSTALLER'>INSTALLER</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiosignal-1.4.0.dist-info/METADATA'>METADATA</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiosignal-1.4.0.dist-info/RECORD'>RECORD</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiosignal-1.4.0.dist-info/top_level.txt'>top_level.txt</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiosignal-1.4.0.dist-info/WHEEL'>WHEEL</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
									<!-- licenses Submodule -->
									<details>
										<summary><b>licenses</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.aiosignal-1.4.0.dist-info.licenses</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/aiosignal-1.4.0.dist-info/licenses/LICENSE'>LICENSE</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<!-- annotated_types Submodule -->
							<details>
								<summary><b>annotated_types</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.annotated_types</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/annotated_types/py.typed'>py.typed</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/annotated_types/test_cases.py'>test_cases.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- annotated_types-0.7.0.dist-info Submodule -->
							<details>
								<summary><b>annotated_types-0.7.0.dist-info</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.annotated_types-0.7.0.dist-info</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/annotated_types-0.7.0.dist-info/INSTALLER'>INSTALLER</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/annotated_types-0.7.0.dist-info/METADATA'>METADATA</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/annotated_types-0.7.0.dist-info/RECORD'>RECORD</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/annotated_types-0.7.0.dist-info/WHEEL'>WHEEL</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
									<!-- licenses Submodule -->
									<details>
										<summary><b>licenses</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.annotated_types-0.7.0.dist-info.licenses</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/annotated_types-0.7.0.dist-info/licenses/LICENSE'>LICENSE</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<!-- anyio Submodule -->
							<details>
								<summary><b>anyio</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.anyio</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/anyio/from_thread.py'>from_thread.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/anyio/lowlevel.py'>lowlevel.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/anyio/py.typed'>py.typed</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/anyio/pytest_plugin.py'>pytest_plugin.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/anyio/to_interpreter.py'>to_interpreter.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/anyio/to_process.py'>to_process.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/anyio/to_thread.py'>to_thread.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
									<!-- abc Submodule -->
									<details>
										<summary><b>abc</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.anyio.abc</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/anyio/abc/_eventloop.py'>_eventloop.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/anyio/abc/_resources.py'>_resources.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/anyio/abc/_sockets.py'>_sockets.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/anyio/abc/_streams.py'>_streams.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/anyio/abc/_subprocesses.py'>_subprocesses.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/anyio/abc/_tasks.py'>_tasks.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/anyio/abc/_testing.py'>_testing.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
									<!-- streams Submodule -->
									<details>
										<summary><b>streams</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.anyio.streams</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/anyio/streams/buffered.py'>buffered.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/anyio/streams/file.py'>file.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/anyio/streams/memory.py'>memory.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/anyio/streams/stapled.py'>stapled.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/anyio/streams/text.py'>text.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/anyio/streams/tls.py'>tls.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
									<!-- _backends Submodule -->
									<details>
										<summary><b>_backends</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.anyio._backends</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/anyio/_backends/_asyncio.py'>_asyncio.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/anyio/_backends/_trio.py'>_trio.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
									<!-- _core Submodule -->
									<details>
										<summary><b>_core</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.anyio._core</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/anyio/_core/_asyncio_selector_thread.py'>_asyncio_selector_thread.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/anyio/_core/_contextmanagers.py'>_contextmanagers.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/anyio/_core/_eventloop.py'>_eventloop.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/anyio/_core/_exceptions.py'>_exceptions.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/anyio/_core/_fileio.py'>_fileio.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/anyio/_core/_resources.py'>_resources.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/anyio/_core/_signals.py'>_signals.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/anyio/_core/_sockets.py'>_sockets.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/anyio/_core/_streams.py'>_streams.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/anyio/_core/_subprocesses.py'>_subprocesses.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/anyio/_core/_synchronization.py'>_synchronization.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/anyio/_core/_tasks.py'>_tasks.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/anyio/_core/_tempfile.py'>_tempfile.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/anyio/_core/_testing.py'>_testing.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/anyio/_core/_typedattr.py'>_typedattr.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<!-- anyio-4.10.0.dist-info Submodule -->
							<details>
								<summary><b>anyio-4.10.0.dist-info</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.anyio-4.10.0.dist-info</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/anyio-4.10.0.dist-info/entry_points.txt'>entry_points.txt</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/anyio-4.10.0.dist-info/INSTALLER'>INSTALLER</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/anyio-4.10.0.dist-info/METADATA'>METADATA</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/anyio-4.10.0.dist-info/RECORD'>RECORD</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/anyio-4.10.0.dist-info/top_level.txt'>top_level.txt</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/anyio-4.10.0.dist-info/WHEEL'>WHEEL</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
									<!-- licenses Submodule -->
									<details>
										<summary><b>licenses</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.anyio-4.10.0.dist-info.licenses</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/anyio-4.10.0.dist-info/licenses/LICENSE'>LICENSE</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<!-- attr Submodule -->
							<details>
								<summary><b>attr</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.attr</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/attr/converters.py'>converters.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/attr/converters.pyi'>converters.pyi</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/attr/exceptions.py'>exceptions.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/attr/exceptions.pyi'>exceptions.pyi</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/attr/filters.py'>filters.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/attr/filters.pyi'>filters.pyi</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/attr/py.typed'>py.typed</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/attr/setters.py'>setters.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/attr/setters.pyi'>setters.pyi</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/attr/validators.py'>validators.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/attr/validators.pyi'>validators.pyi</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/attr/_cmp.py'>_cmp.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/attr/_cmp.pyi'>_cmp.pyi</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/attr/_compat.py'>_compat.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/attr/_config.py'>_config.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/attr/_funcs.py'>_funcs.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/attr/_make.py'>_make.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/attr/_next_gen.py'>_next_gen.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/attr/_typing_compat.pyi'>_typing_compat.pyi</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/attr/_version_info.py'>_version_info.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/attr/_version_info.pyi'>_version_info.pyi</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/attr/__init__.pyi'>__init__.pyi</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- attrs Submodule -->
							<details>
								<summary><b>attrs</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.attrs</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/attrs/converters.py'>converters.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/attrs/exceptions.py'>exceptions.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/attrs/filters.py'>filters.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/attrs/py.typed'>py.typed</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/attrs/setters.py'>setters.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/attrs/validators.py'>validators.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/attrs/__init__.pyi'>__init__.pyi</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- attrs-25.3.0.dist-info Submodule -->
							<details>
								<summary><b>attrs-25.3.0.dist-info</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.attrs-25.3.0.dist-info</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/attrs-25.3.0.dist-info/INSTALLER'>INSTALLER</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/attrs-25.3.0.dist-info/METADATA'>METADATA</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/attrs-25.3.0.dist-info/RECORD'>RECORD</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/attrs-25.3.0.dist-info/WHEEL'>WHEEL</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
									<!-- licenses Submodule -->
									<details>
										<summary><b>licenses</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.attrs-25.3.0.dist-info.licenses</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/attrs-25.3.0.dist-info/licenses/LICENSE'>LICENSE</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<!-- certifi Submodule -->
							<details>
								<summary><b>certifi</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.certifi</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/certifi/core.py'>core.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/certifi/py.typed'>py.typed</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/certifi/__main__.py'>__main__.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- certifi-2025.8.3.dist-info Submodule -->
							<details>
								<summary><b>certifi-2025.8.3.dist-info</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.certifi-2025.8.3.dist-info</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/certifi-2025.8.3.dist-info/INSTALLER'>INSTALLER</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/certifi-2025.8.3.dist-info/METADATA'>METADATA</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/certifi-2025.8.3.dist-info/RECORD'>RECORD</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/certifi-2025.8.3.dist-info/top_level.txt'>top_level.txt</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/certifi-2025.8.3.dist-info/WHEEL'>WHEEL</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
									<!-- licenses Submodule -->
									<details>
										<summary><b>licenses</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.certifi-2025.8.3.dist-info.licenses</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/certifi-2025.8.3.dist-info/licenses/LICENSE'>LICENSE</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<!-- charset_normalizer Submodule -->
							<details>
								<summary><b>charset_normalizer</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.charset_normalizer</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/charset_normalizer/api.py'>api.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/charset_normalizer/cd.py'>cd.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/charset_normalizer/constant.py'>constant.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/charset_normalizer/legacy.py'>legacy.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/charset_normalizer/md.py'>md.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/charset_normalizer/models.py'>models.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/charset_normalizer/py.typed'>py.typed</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/charset_normalizer/utils.py'>utils.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/charset_normalizer/version.py'>version.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/charset_normalizer/__main__.py'>__main__.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
									<!-- cli Submodule -->
									<details>
										<summary><b>cli</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.charset_normalizer.cli</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/charset_normalizer/cli/__main__.py'>__main__.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<!-- charset_normalizer-3.4.3.dist-info Submodule -->
							<details>
								<summary><b>charset_normalizer-3.4.3.dist-info</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.charset_normalizer-3.4.3.dist-info</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/charset_normalizer-3.4.3.dist-info/entry_points.txt'>entry_points.txt</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/charset_normalizer-3.4.3.dist-info/INSTALLER'>INSTALLER</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/charset_normalizer-3.4.3.dist-info/METADATA'>METADATA</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/charset_normalizer-3.4.3.dist-info/RECORD'>RECORD</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/charset_normalizer-3.4.3.dist-info/top_level.txt'>top_level.txt</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/charset_normalizer-3.4.3.dist-info/WHEEL'>WHEEL</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
									<!-- licenses Submodule -->
									<details>
										<summary><b>licenses</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.charset_normalizer-3.4.3.dist-info.licenses</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/charset_normalizer-3.4.3.dist-info/licenses/LICENSE'>LICENSE</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<!-- click Submodule -->
							<details>
								<summary><b>click</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.click</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/click/core.py'>core.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/click/decorators.py'>decorators.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/click/exceptions.py'>exceptions.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/click/formatting.py'>formatting.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/click/globals.py'>globals.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/click/parser.py'>parser.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/click/py.typed'>py.typed</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/click/shell_completion.py'>shell_completion.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/click/termui.py'>termui.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/click/testing.py'>testing.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/click/types.py'>types.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/click/utils.py'>utils.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/click/_compat.py'>_compat.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/click/_termui_impl.py'>_termui_impl.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/click/_textwrap.py'>_textwrap.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/click/_winconsole.py'>_winconsole.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- click-8.2.1.dist-info Submodule -->
							<details>
								<summary><b>click-8.2.1.dist-info</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.click-8.2.1.dist-info</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/click-8.2.1.dist-info/INSTALLER'>INSTALLER</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/click-8.2.1.dist-info/METADATA'>METADATA</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/click-8.2.1.dist-info/RECORD'>RECORD</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/click-8.2.1.dist-info/WHEEL'>WHEEL</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
									<!-- licenses Submodule -->
									<details>
										<summary><b>licenses</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.click-8.2.1.dist-info.licenses</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/click-8.2.1.dist-info/licenses/LICENSE.txt'>LICENSE.txt</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<!-- colorama Submodule -->
							<details>
								<summary><b>colorama</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.colorama</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/colorama/ansi.py'>ansi.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/colorama/ansitowin32.py'>ansitowin32.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/colorama/initialise.py'>initialise.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/colorama/win32.py'>win32.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/colorama/winterm.py'>winterm.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- colorama-0.4.6.dist-info Submodule -->
							<details>
								<summary><b>colorama-0.4.6.dist-info</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.colorama-0.4.6.dist-info</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/colorama-0.4.6.dist-info/INSTALLER'>INSTALLER</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/colorama-0.4.6.dist-info/METADATA'>METADATA</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/colorama-0.4.6.dist-info/RECORD'>RECORD</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/colorama-0.4.6.dist-info/WHEEL'>WHEEL</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
									<!-- licenses Submodule -->
									<details>
										<summary><b>licenses</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.colorama-0.4.6.dist-info.licenses</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/colorama-0.4.6.dist-info/licenses/LICENSE.txt'>LICENSE.txt</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<!-- distro Submodule -->
							<details>
								<summary><b>distro</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.distro</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/distro/distro.py'>distro.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/distro/py.typed'>py.typed</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/distro/__main__.py'>__main__.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- distro-1.9.0.dist-info Submodule -->
							<details>
								<summary><b>distro-1.9.0.dist-info</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.distro-1.9.0.dist-info</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/distro-1.9.0.dist-info/entry_points.txt'>entry_points.txt</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/distro-1.9.0.dist-info/INSTALLER'>INSTALLER</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/distro-1.9.0.dist-info/LICENSE'>LICENSE</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/distro-1.9.0.dist-info/METADATA'>METADATA</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/distro-1.9.0.dist-info/RECORD'>RECORD</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/distro-1.9.0.dist-info/top_level.txt'>top_level.txt</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/distro-1.9.0.dist-info/WHEEL'>WHEEL</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- dotenv Submodule -->
							<details>
								<summary><b>dotenv</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.dotenv</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/dotenv/cli.py'>cli.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/dotenv/ipython.py'>ipython.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/dotenv/main.py'>main.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/dotenv/parser.py'>parser.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/dotenv/py.typed'>py.typed</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/dotenv/variables.py'>variables.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/dotenv/version.py'>version.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/dotenv/__main__.py'>__main__.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- frozenlist Submodule -->
							<details>
								<summary><b>frozenlist</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.frozenlist</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/frozenlist/py.typed'>py.typed</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/frozenlist/_frozenlist.pyx'>_frozenlist.pyx</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/frozenlist/__init__.pyi'>__init__.pyi</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- frozenlist-1.7.0.dist-info Submodule -->
							<details>
								<summary><b>frozenlist-1.7.0.dist-info</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.frozenlist-1.7.0.dist-info</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/frozenlist-1.7.0.dist-info/INSTALLER'>INSTALLER</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/frozenlist-1.7.0.dist-info/METADATA'>METADATA</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/frozenlist-1.7.0.dist-info/RECORD'>RECORD</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/frozenlist-1.7.0.dist-info/top_level.txt'>top_level.txt</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/frozenlist-1.7.0.dist-info/WHEEL'>WHEEL</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
									<!-- licenses Submodule -->
									<details>
										<summary><b>licenses</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.frozenlist-1.7.0.dist-info.licenses</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/frozenlist-1.7.0.dist-info/licenses/LICENSE'>LICENSE</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<!-- git Submodule -->
							<details>
								<summary><b>git</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.git</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/git/cmd.py'>cmd.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/git/compat.py'>compat.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/git/config.py'>config.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/git/db.py'>db.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/git/diff.py'>diff.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/git/exc.py'>exc.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/git/py.typed'>py.typed</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/git/remote.py'>remote.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/git/types.py'>types.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/git/util.py'>util.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
									<!-- index Submodule -->
									<details>
										<summary><b>index</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.git.index</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/git/index/base.py'>base.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/git/index/fun.py'>fun.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/git/index/typ.py'>typ.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/git/index/util.py'>util.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
									<!-- objects Submodule -->
									<details>
										<summary><b>objects</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.git.objects</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/git/objects/base.py'>base.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/git/objects/blob.py'>blob.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/git/objects/commit.py'>commit.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/git/objects/fun.py'>fun.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/git/objects/tag.py'>tag.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/git/objects/tree.py'>tree.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/git/objects/util.py'>util.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
											<!-- submodule Submodule -->
											<details>
												<summary><b>submodule</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.git.objects.submodule</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/git/objects/submodule/base.py'>base.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/git/objects/submodule/root.py'>root.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/git/objects/submodule/util.py'>util.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
										</blockquote>
									</details>
									<!-- refs Submodule -->
									<details>
										<summary><b>refs</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.git.refs</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/git/refs/head.py'>head.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/git/refs/log.py'>log.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/git/refs/reference.py'>reference.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/git/refs/remote.py'>remote.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/git/refs/symbolic.py'>symbolic.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/git/refs/tag.py'>tag.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
									<!-- repo Submodule -->
									<details>
										<summary><b>repo</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.git.repo</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/git/repo/base.py'>base.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/git/repo/fun.py'>fun.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<!-- gitdb Submodule -->
							<details>
								<summary><b>gitdb</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.gitdb</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/gitdb/base.py'>base.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/gitdb/const.py'>const.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/gitdb/exc.py'>exc.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/gitdb/fun.py'>fun.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/gitdb/pack.py'>pack.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/gitdb/stream.py'>stream.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/gitdb/typ.py'>typ.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/gitdb/util.py'>util.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
									<!-- db Submodule -->
									<details>
										<summary><b>db</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.gitdb.db</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/gitdb/db/base.py'>base.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/gitdb/db/git.py'>git.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/gitdb/db/loose.py'>loose.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/gitdb/db/mem.py'>mem.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/gitdb/db/pack.py'>pack.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/gitdb/db/ref.py'>ref.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
									<!-- test Submodule -->
									<details>
										<summary><b>test</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.gitdb.test</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/gitdb/test/lib.py'>lib.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/gitdb/test/test_base.py'>test_base.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/gitdb/test/test_example.py'>test_example.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/gitdb/test/test_pack.py'>test_pack.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/gitdb/test/test_stream.py'>test_stream.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/gitdb/test/test_util.py'>test_util.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
									<!-- utils Submodule -->
									<details>
										<summary><b>utils</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.gitdb.utils</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/gitdb/utils/encoding.py'>encoding.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<!-- gitdb-4.0.12.dist-info Submodule -->
							<details>
								<summary><b>gitdb-4.0.12.dist-info</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.gitdb-4.0.12.dist-info</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/gitdb-4.0.12.dist-info/INSTALLER'>INSTALLER</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/gitdb-4.0.12.dist-info/LICENSE'>LICENSE</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/gitdb-4.0.12.dist-info/METADATA'>METADATA</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/gitdb-4.0.12.dist-info/RECORD'>RECORD</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/gitdb-4.0.12.dist-info/top_level.txt'>top_level.txt</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/gitdb-4.0.12.dist-info/WHEEL'>WHEEL</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- gitpython-3.1.45.dist-info Submodule -->
							<details>
								<summary><b>gitpython-3.1.45.dist-info</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.gitpython-3.1.45.dist-info</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/gitpython-3.1.45.dist-info/INSTALLER'>INSTALLER</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/gitpython-3.1.45.dist-info/METADATA'>METADATA</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/gitpython-3.1.45.dist-info/RECORD'>RECORD</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/gitpython-3.1.45.dist-info/top_level.txt'>top_level.txt</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/gitpython-3.1.45.dist-info/WHEEL'>WHEEL</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
									<!-- licenses Submodule -->
									<details>
										<summary><b>licenses</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.gitpython-3.1.45.dist-info.licenses</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/gitpython-3.1.45.dist-info/licenses/LICENSE'>LICENSE</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<!-- h11 Submodule -->
							<details>
								<summary><b>h11</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.h11</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/h11/py.typed'>py.typed</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/h11/_abnf.py'>_abnf.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/h11/_connection.py'>_connection.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/h11/_events.py'>_events.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/h11/_headers.py'>_headers.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/h11/_readers.py'>_readers.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/h11/_receivebuffer.py'>_receivebuffer.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/h11/_state.py'>_state.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/h11/_util.py'>_util.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/h11/_version.py'>_version.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/h11/_writers.py'>_writers.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- h11-0.16.0.dist-info Submodule -->
							<details>
								<summary><b>h11-0.16.0.dist-info</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.h11-0.16.0.dist-info</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/h11-0.16.0.dist-info/INSTALLER'>INSTALLER</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/h11-0.16.0.dist-info/METADATA'>METADATA</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/h11-0.16.0.dist-info/RECORD'>RECORD</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/h11-0.16.0.dist-info/top_level.txt'>top_level.txt</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/h11-0.16.0.dist-info/WHEEL'>WHEEL</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
									<!-- licenses Submodule -->
									<details>
										<summary><b>licenses</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.h11-0.16.0.dist-info.licenses</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/h11-0.16.0.dist-info/licenses/LICENSE.txt'>LICENSE.txt</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<!-- httpcore Submodule -->
							<details>
								<summary><b>httpcore</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.httpcore</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpcore/py.typed'>py.typed</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpcore/_api.py'>_api.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpcore/_exceptions.py'>_exceptions.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpcore/_models.py'>_models.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpcore/_ssl.py'>_ssl.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpcore/_synchronization.py'>_synchronization.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpcore/_trace.py'>_trace.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpcore/_utils.py'>_utils.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
									<!-- _async Submodule -->
									<details>
										<summary><b>_async</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.httpcore._async</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpcore/_async/connection.py'>connection.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpcore/_async/connection_pool.py'>connection_pool.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpcore/_async/http11.py'>http11.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpcore/_async/http2.py'>http2.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpcore/_async/http_proxy.py'>http_proxy.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpcore/_async/interfaces.py'>interfaces.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpcore/_async/socks_proxy.py'>socks_proxy.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
									<!-- _backends Submodule -->
									<details>
										<summary><b>_backends</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.httpcore._backends</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpcore/_backends/anyio.py'>anyio.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpcore/_backends/auto.py'>auto.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpcore/_backends/base.py'>base.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpcore/_backends/mock.py'>mock.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpcore/_backends/sync.py'>sync.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpcore/_backends/trio.py'>trio.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
									<!-- _sync Submodule -->
									<details>
										<summary><b>_sync</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.httpcore._sync</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpcore/_sync/connection.py'>connection.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpcore/_sync/connection_pool.py'>connection_pool.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpcore/_sync/http11.py'>http11.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpcore/_sync/http2.py'>http2.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpcore/_sync/http_proxy.py'>http_proxy.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpcore/_sync/interfaces.py'>interfaces.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpcore/_sync/socks_proxy.py'>socks_proxy.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<!-- httpcore-1.0.9.dist-info Submodule -->
							<details>
								<summary><b>httpcore-1.0.9.dist-info</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.httpcore-1.0.9.dist-info</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpcore-1.0.9.dist-info/INSTALLER'>INSTALLER</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpcore-1.0.9.dist-info/METADATA'>METADATA</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpcore-1.0.9.dist-info/RECORD'>RECORD</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpcore-1.0.9.dist-info/WHEEL'>WHEEL</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- httpx Submodule -->
							<details>
								<summary><b>httpx</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.httpx</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpx/py.typed'>py.typed</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpx/_api.py'>_api.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpx/_auth.py'>_auth.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpx/_client.py'>_client.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpx/_config.py'>_config.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpx/_content.py'>_content.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpx/_decoders.py'>_decoders.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpx/_exceptions.py'>_exceptions.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpx/_main.py'>_main.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpx/_models.py'>_models.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpx/_multipart.py'>_multipart.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpx/_status_codes.py'>_status_codes.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpx/_types.py'>_types.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpx/_urlparse.py'>_urlparse.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpx/_urls.py'>_urls.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpx/_utils.py'>_utils.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpx/__version__.py'>__version__.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
									<!-- _transports Submodule -->
									<details>
										<summary><b>_transports</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.httpx._transports</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpx/_transports/asgi.py'>asgi.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpx/_transports/base.py'>base.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpx/_transports/default.py'>default.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpx/_transports/mock.py'>mock.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpx/_transports/wsgi.py'>wsgi.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<!-- httpx-0.28.1.dist-info Submodule -->
							<details>
								<summary><b>httpx-0.28.1.dist-info</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.httpx-0.28.1.dist-info</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpx-0.28.1.dist-info/entry_points.txt'>entry_points.txt</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpx-0.28.1.dist-info/INSTALLER'>INSTALLER</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpx-0.28.1.dist-info/METADATA'>METADATA</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpx-0.28.1.dist-info/RECORD'>RECORD</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/httpx-0.28.1.dist-info/WHEEL'>WHEEL</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- idna Submodule -->
							<details>
								<summary><b>idna</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.idna</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/idna/codec.py'>codec.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/idna/compat.py'>compat.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/idna/core.py'>core.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/idna/idnadata.py'>idnadata.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/idna/intranges.py'>intranges.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/idna/package_data.py'>package_data.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/idna/py.typed'>py.typed</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/idna/uts46data.py'>uts46data.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- idna-3.10.dist-info Submodule -->
							<details>
								<summary><b>idna-3.10.dist-info</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.idna-3.10.dist-info</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/idna-3.10.dist-info/INSTALLER'>INSTALLER</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/idna-3.10.dist-info/METADATA'>METADATA</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/idna-3.10.dist-info/RECORD'>RECORD</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/idna-3.10.dist-info/WHEEL'>WHEEL</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- jiter Submodule -->
							<details>
								<summary><b>jiter</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.jiter</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/jiter/py.typed'>py.typed</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/jiter/__init__.pyi'>__init__.pyi</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- jiter-0.10.0.dist-info Submodule -->
							<details>
								<summary><b>jiter-0.10.0.dist-info</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.jiter-0.10.0.dist-info</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/jiter-0.10.0.dist-info/INSTALLER'>INSTALLER</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/jiter-0.10.0.dist-info/METADATA'>METADATA</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/jiter-0.10.0.dist-info/RECORD'>RECORD</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/jiter-0.10.0.dist-info/WHEEL'>WHEEL</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- multidict Submodule -->
							<details>
								<summary><b>multidict</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.multidict</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/multidict/py.typed'>py.typed</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/multidict/_abc.py'>_abc.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/multidict/_compat.py'>_compat.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/multidict/_multidict_py.py'>_multidict_py.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- multidict-6.6.4.dist-info Submodule -->
							<details>
								<summary><b>multidict-6.6.4.dist-info</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.multidict-6.6.4.dist-info</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/multidict-6.6.4.dist-info/INSTALLER'>INSTALLER</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/multidict-6.6.4.dist-info/METADATA'>METADATA</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/multidict-6.6.4.dist-info/RECORD'>RECORD</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/multidict-6.6.4.dist-info/top_level.txt'>top_level.txt</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/multidict-6.6.4.dist-info/WHEEL'>WHEEL</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
									<!-- licenses Submodule -->
									<details>
										<summary><b>licenses</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.multidict-6.6.4.dist-info.licenses</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/multidict-6.6.4.dist-info/licenses/LICENSE'>LICENSE</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<!-- openai Submodule -->
							<details>
								<summary><b>openai</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.openai</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/pagination.py'>pagination.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/py.typed'>py.typed</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/version.py'>version.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/_base_client.py'>_base_client.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/_client.py'>_client.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/_compat.py'>_compat.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/_constants.py'>_constants.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/_exceptions.py'>_exceptions.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/_files.py'>_files.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/_legacy_response.py'>_legacy_response.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/_models.py'>_models.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/_module_client.py'>_module_client.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/_qs.py'>_qs.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/_resource.py'>_resource.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/_response.py'>_response.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/_streaming.py'>_streaming.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/_types.py'>_types.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/_version.py'>_version.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/__main__.py'>__main__.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
									<!-- cli Submodule -->
									<details>
										<summary><b>cli</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.openai.cli</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/cli/_cli.py'>_cli.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/cli/_errors.py'>_errors.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/cli/_models.py'>_models.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/cli/_progress.py'>_progress.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/cli/_utils.py'>_utils.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
											<!-- _api Submodule -->
											<details>
												<summary><b>_api</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.openai.cli._api</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/cli/_api/audio.py'>audio.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/cli/_api/completions.py'>completions.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/cli/_api/files.py'>files.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/cli/_api/image.py'>image.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/cli/_api/models.py'>models.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/cli/_api/_main.py'>_main.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
													<!-- chat Submodule -->
													<details>
														<summary><b>chat</b></summary>
														<blockquote>
															<div class='directory-path' style='padding: 8px 0; color: #666;'>
																<code><b>⦿ venv.Lib.site-packages.openai.cli._api.chat</b></code>
															<table style='width: 100%; border-collapse: collapse;'>
															<thead>
																<tr style='background-color: #f8f9fa;'>
																	<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																	<th style='text-align: left; padding: 8px;'>Summary</th>
																</tr>
															</thead>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/cli/_api/chat/completions.py'>completions.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
															</table>
														</blockquote>
													</details>
													<!-- fine_tuning Submodule -->
													<details>
														<summary><b>fine_tuning</b></summary>
														<blockquote>
															<div class='directory-path' style='padding: 8px 0; color: #666;'>
																<code><b>⦿ venv.Lib.site-packages.openai.cli._api.fine_tuning</b></code>
															<table style='width: 100%; border-collapse: collapse;'>
															<thead>
																<tr style='background-color: #f8f9fa;'>
																	<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																	<th style='text-align: left; padding: 8px;'>Summary</th>
																</tr>
															</thead>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/cli/_api/fine_tuning/jobs.py'>jobs.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
															</table>
														</blockquote>
													</details>
												</blockquote>
											</details>
											<!-- _tools Submodule -->
											<details>
												<summary><b>_tools</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.openai.cli._tools</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/cli/_tools/fine_tunes.py'>fine_tunes.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/cli/_tools/migrate.py'>migrate.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/cli/_tools/_main.py'>_main.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
										</blockquote>
									</details>
									<!-- helpers Submodule -->
									<details>
										<summary><b>helpers</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.openai.helpers</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/helpers/local_audio_player.py'>local_audio_player.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/helpers/microphone.py'>microphone.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
									<!-- lib Submodule -->
									<details>
										<summary><b>lib</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.openai.lib</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/lib/.keep'>.keep</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/lib/azure.py'>azure.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/lib/_old_api.py'>_old_api.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/lib/_pydantic.py'>_pydantic.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/lib/_tools.py'>_tools.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/lib/_validators.py'>_validators.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
											<!-- streaming Submodule -->
											<details>
												<summary><b>streaming</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.openai.lib.streaming</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/lib/streaming/_assistants.py'>_assistants.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/lib/streaming/_deltas.py'>_deltas.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
													<!-- chat Submodule -->
													<details>
														<summary><b>chat</b></summary>
														<blockquote>
															<div class='directory-path' style='padding: 8px 0; color: #666;'>
																<code><b>⦿ venv.Lib.site-packages.openai.lib.streaming.chat</b></code>
															<table style='width: 100%; border-collapse: collapse;'>
															<thead>
																<tr style='background-color: #f8f9fa;'>
																	<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																	<th style='text-align: left; padding: 8px;'>Summary</th>
																</tr>
															</thead>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/lib/streaming/chat/_completions.py'>_completions.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/lib/streaming/chat/_events.py'>_events.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/lib/streaming/chat/_types.py'>_types.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
															</table>
														</blockquote>
													</details>
													<!-- responses Submodule -->
													<details>
														<summary><b>responses</b></summary>
														<blockquote>
															<div class='directory-path' style='padding: 8px 0; color: #666;'>
																<code><b>⦿ venv.Lib.site-packages.openai.lib.streaming.responses</b></code>
															<table style='width: 100%; border-collapse: collapse;'>
															<thead>
																<tr style='background-color: #f8f9fa;'>
																	<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																	<th style='text-align: left; padding: 8px;'>Summary</th>
																</tr>
															</thead>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/lib/streaming/responses/_events.py'>_events.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/lib/streaming/responses/_responses.py'>_responses.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/lib/streaming/responses/_types.py'>_types.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
															</table>
														</blockquote>
													</details>
												</blockquote>
											</details>
											<!-- _parsing Submodule -->
											<details>
												<summary><b>_parsing</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.openai.lib._parsing</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/lib/_parsing/_completions.py'>_completions.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/lib/_parsing/_responses.py'>_responses.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
										</blockquote>
									</details>
									<!-- resources Submodule -->
									<details>
										<summary><b>resources</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.openai.resources</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/resources/batches.py'>batches.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/resources/completions.py'>completions.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/resources/embeddings.py'>embeddings.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/resources/files.py'>files.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/resources/images.py'>images.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/resources/models.py'>models.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/resources/moderations.py'>moderations.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/resources/webhooks.py'>webhooks.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
											<!-- audio Submodule -->
											<details>
												<summary><b>audio</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.openai.resources.audio</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/resources/audio/audio.py'>audio.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/resources/audio/speech.py'>speech.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/resources/audio/transcriptions.py'>transcriptions.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/resources/audio/translations.py'>translations.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
											<!-- beta Submodule -->
											<details>
												<summary><b>beta</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.openai.resources.beta</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/resources/beta/assistants.py'>assistants.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/resources/beta/beta.py'>beta.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
													<!-- realtime Submodule -->
													<details>
														<summary><b>realtime</b></summary>
														<blockquote>
															<div class='directory-path' style='padding: 8px 0; color: #666;'>
																<code><b>⦿ venv.Lib.site-packages.openai.resources.beta.realtime</b></code>
															<table style='width: 100%; border-collapse: collapse;'>
															<thead>
																<tr style='background-color: #f8f9fa;'>
																	<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																	<th style='text-align: left; padding: 8px;'>Summary</th>
																</tr>
															</thead>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/resources/beta/realtime/realtime.py'>realtime.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/resources/beta/realtime/sessions.py'>sessions.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/resources/beta/realtime/transcription_sessions.py'>transcription_sessions.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
															</table>
														</blockquote>
													</details>
													<!-- threads Submodule -->
													<details>
														<summary><b>threads</b></summary>
														<blockquote>
															<div class='directory-path' style='padding: 8px 0; color: #666;'>
																<code><b>⦿ venv.Lib.site-packages.openai.resources.beta.threads</b></code>
															<table style='width: 100%; border-collapse: collapse;'>
															<thead>
																<tr style='background-color: #f8f9fa;'>
																	<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																	<th style='text-align: left; padding: 8px;'>Summary</th>
																</tr>
															</thead>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/resources/beta/threads/messages.py'>messages.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/resources/beta/threads/threads.py'>threads.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
															</table>
															<!-- runs Submodule -->
															<details>
																<summary><b>runs</b></summary>
																<blockquote>
																	<div class='directory-path' style='padding: 8px 0; color: #666;'>
																		<code><b>⦿ venv.Lib.site-packages.openai.resources.beta.threads.runs</b></code>
																	<table style='width: 100%; border-collapse: collapse;'>
																	<thead>
																		<tr style='background-color: #f8f9fa;'>
																			<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																			<th style='text-align: left; padding: 8px;'>Summary</th>
																		</tr>
																	</thead>
																		<tr style='border-bottom: 1px solid #eee;'>
																			<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/resources/beta/threads/runs/runs.py'>runs.py</a></b></td>
																			<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																		</tr>
																		<tr style='border-bottom: 1px solid #eee;'>
																			<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/resources/beta/threads/runs/steps.py'>steps.py</a></b></td>
																			<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																		</tr>
																	</table>
																</blockquote>
															</details>
														</blockquote>
													</details>
												</blockquote>
											</details>
											<!-- chat Submodule -->
											<details>
												<summary><b>chat</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.openai.resources.chat</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/resources/chat/chat.py'>chat.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
													<!-- completions Submodule -->
													<details>
														<summary><b>completions</b></summary>
														<blockquote>
															<div class='directory-path' style='padding: 8px 0; color: #666;'>
																<code><b>⦿ venv.Lib.site-packages.openai.resources.chat.completions</b></code>
															<table style='width: 100%; border-collapse: collapse;'>
															<thead>
																<tr style='background-color: #f8f9fa;'>
																	<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																	<th style='text-align: left; padding: 8px;'>Summary</th>
																</tr>
															</thead>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/resources/chat/completions/completions.py'>completions.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/resources/chat/completions/messages.py'>messages.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
															</table>
														</blockquote>
													</details>
												</blockquote>
											</details>
											<!-- containers Submodule -->
											<details>
												<summary><b>containers</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.openai.resources.containers</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/resources/containers/containers.py'>containers.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
													<!-- files Submodule -->
													<details>
														<summary><b>files</b></summary>
														<blockquote>
															<div class='directory-path' style='padding: 8px 0; color: #666;'>
																<code><b>⦿ venv.Lib.site-packages.openai.resources.containers.files</b></code>
															<table style='width: 100%; border-collapse: collapse;'>
															<thead>
																<tr style='background-color: #f8f9fa;'>
																	<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																	<th style='text-align: left; padding: 8px;'>Summary</th>
																</tr>
															</thead>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/resources/containers/files/content.py'>content.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/resources/containers/files/files.py'>files.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
															</table>
														</blockquote>
													</details>
												</blockquote>
											</details>
											<!-- conversations Submodule -->
											<details>
												<summary><b>conversations</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.openai.resources.conversations</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/resources/conversations/conversations.py'>conversations.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/resources/conversations/items.py'>items.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
											<!-- evals Submodule -->
											<details>
												<summary><b>evals</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.openai.resources.evals</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/resources/evals/evals.py'>evals.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
													<!-- runs Submodule -->
													<details>
														<summary><b>runs</b></summary>
														<blockquote>
															<div class='directory-path' style='padding: 8px 0; color: #666;'>
																<code><b>⦿ venv.Lib.site-packages.openai.resources.evals.runs</b></code>
															<table style='width: 100%; border-collapse: collapse;'>
															<thead>
																<tr style='background-color: #f8f9fa;'>
																	<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																	<th style='text-align: left; padding: 8px;'>Summary</th>
																</tr>
															</thead>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/resources/evals/runs/output_items.py'>output_items.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/resources/evals/runs/runs.py'>runs.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
															</table>
														</blockquote>
													</details>
												</blockquote>
											</details>
											<!-- fine_tuning Submodule -->
											<details>
												<summary><b>fine_tuning</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.openai.resources.fine_tuning</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/resources/fine_tuning/fine_tuning.py'>fine_tuning.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
													<!-- alpha Submodule -->
													<details>
														<summary><b>alpha</b></summary>
														<blockquote>
															<div class='directory-path' style='padding: 8px 0; color: #666;'>
																<code><b>⦿ venv.Lib.site-packages.openai.resources.fine_tuning.alpha</b></code>
															<table style='width: 100%; border-collapse: collapse;'>
															<thead>
																<tr style='background-color: #f8f9fa;'>
																	<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																	<th style='text-align: left; padding: 8px;'>Summary</th>
																</tr>
															</thead>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/resources/fine_tuning/alpha/alpha.py'>alpha.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/resources/fine_tuning/alpha/graders.py'>graders.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
															</table>
														</blockquote>
													</details>
													<!-- checkpoints Submodule -->
													<details>
														<summary><b>checkpoints</b></summary>
														<blockquote>
															<div class='directory-path' style='padding: 8px 0; color: #666;'>
																<code><b>⦿ venv.Lib.site-packages.openai.resources.fine_tuning.checkpoints</b></code>
															<table style='width: 100%; border-collapse: collapse;'>
															<thead>
																<tr style='background-color: #f8f9fa;'>
																	<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																	<th style='text-align: left; padding: 8px;'>Summary</th>
																</tr>
															</thead>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/resources/fine_tuning/checkpoints/checkpoints.py'>checkpoints.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/resources/fine_tuning/checkpoints/permissions.py'>permissions.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
															</table>
														</blockquote>
													</details>
													<!-- jobs Submodule -->
													<details>
														<summary><b>jobs</b></summary>
														<blockquote>
															<div class='directory-path' style='padding: 8px 0; color: #666;'>
																<code><b>⦿ venv.Lib.site-packages.openai.resources.fine_tuning.jobs</b></code>
															<table style='width: 100%; border-collapse: collapse;'>
															<thead>
																<tr style='background-color: #f8f9fa;'>
																	<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																	<th style='text-align: left; padding: 8px;'>Summary</th>
																</tr>
															</thead>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/resources/fine_tuning/jobs/checkpoints.py'>checkpoints.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/resources/fine_tuning/jobs/jobs.py'>jobs.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
															</table>
														</blockquote>
													</details>
												</blockquote>
											</details>
											<!-- responses Submodule -->
											<details>
												<summary><b>responses</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.openai.resources.responses</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/resources/responses/input_items.py'>input_items.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/resources/responses/responses.py'>responses.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
											<!-- uploads Submodule -->
											<details>
												<summary><b>uploads</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.openai.resources.uploads</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/resources/uploads/parts.py'>parts.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/resources/uploads/uploads.py'>uploads.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
											<!-- vector_stores Submodule -->
											<details>
												<summary><b>vector_stores</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.openai.resources.vector_stores</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/resources/vector_stores/files.py'>files.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/resources/vector_stores/file_batches.py'>file_batches.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/resources/vector_stores/vector_stores.py'>vector_stores.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
										</blockquote>
									</details>
									<!-- types Submodule -->
									<details>
										<summary><b>types</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.openai.types</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/audio_model.py'>audio_model.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/audio_response_format.py'>audio_response_format.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/auto_file_chunking_strategy_param.py'>auto_file_chunking_strategy_param.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/batch.py'>batch.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/batch_create_params.py'>batch_create_params.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/batch_error.py'>batch_error.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/batch_list_params.py'>batch_list_params.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/batch_request_counts.py'>batch_request_counts.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/chat_model.py'>chat_model.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/completion.py'>completion.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/completion_choice.py'>completion_choice.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/completion_create_params.py'>completion_create_params.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/completion_usage.py'>completion_usage.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/container_create_params.py'>container_create_params.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/container_create_response.py'>container_create_response.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/container_list_params.py'>container_list_params.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/container_list_response.py'>container_list_response.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/container_retrieve_response.py'>container_retrieve_response.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/create_embedding_response.py'>create_embedding_response.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/embedding.py'>embedding.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/embedding_create_params.py'>embedding_create_params.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/embedding_model.py'>embedding_model.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/eval_create_params.py'>eval_create_params.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/eval_create_response.py'>eval_create_response.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/eval_custom_data_source_config.py'>eval_custom_data_source_config.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/eval_delete_response.py'>eval_delete_response.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/eval_list_params.py'>eval_list_params.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/eval_list_response.py'>eval_list_response.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/eval_retrieve_response.py'>eval_retrieve_response.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/eval_stored_completions_data_source_config.py'>eval_stored_completions_data_source_config.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/eval_update_params.py'>eval_update_params.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/eval_update_response.py'>eval_update_response.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/file_chunking_strategy.py'>file_chunking_strategy.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/file_chunking_strategy_param.py'>file_chunking_strategy_param.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/file_content.py'>file_content.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/file_create_params.py'>file_create_params.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/file_deleted.py'>file_deleted.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/file_list_params.py'>file_list_params.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/file_object.py'>file_object.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/file_purpose.py'>file_purpose.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/image.py'>image.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/images_response.py'>images_response.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/image_create_variation_params.py'>image_create_variation_params.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/image_edit_completed_event.py'>image_edit_completed_event.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/image_edit_params.py'>image_edit_params.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/image_edit_partial_image_event.py'>image_edit_partial_image_event.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/image_edit_stream_event.py'>image_edit_stream_event.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/image_generate_params.py'>image_generate_params.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/image_gen_completed_event.py'>image_gen_completed_event.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/image_gen_partial_image_event.py'>image_gen_partial_image_event.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/image_gen_stream_event.py'>image_gen_stream_event.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/image_model.py'>image_model.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/model.py'>model.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/model_deleted.py'>model_deleted.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/moderation.py'>moderation.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/moderation_create_params.py'>moderation_create_params.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/moderation_create_response.py'>moderation_create_response.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/moderation_image_url_input_param.py'>moderation_image_url_input_param.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/moderation_model.py'>moderation_model.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/moderation_multi_modal_input_param.py'>moderation_multi_modal_input_param.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/moderation_text_input_param.py'>moderation_text_input_param.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/other_file_chunking_strategy_object.py'>other_file_chunking_strategy_object.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/static_file_chunking_strategy.py'>static_file_chunking_strategy.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/static_file_chunking_strategy_object.py'>static_file_chunking_strategy_object.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/static_file_chunking_strategy_object_param.py'>static_file_chunking_strategy_object_param.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/static_file_chunking_strategy_param.py'>static_file_chunking_strategy_param.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/upload.py'>upload.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/upload_complete_params.py'>upload_complete_params.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/upload_create_params.py'>upload_create_params.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/vector_store.py'>vector_store.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/vector_store_create_params.py'>vector_store_create_params.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/vector_store_deleted.py'>vector_store_deleted.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/vector_store_list_params.py'>vector_store_list_params.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/vector_store_search_params.py'>vector_store_search_params.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/vector_store_search_response.py'>vector_store_search_response.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/vector_store_update_params.py'>vector_store_update_params.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/websocket_connection_options.py'>websocket_connection_options.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
											<!-- audio Submodule -->
											<details>
												<summary><b>audio</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.openai.types.audio</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/audio/speech_create_params.py'>speech_create_params.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/audio/speech_model.py'>speech_model.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/audio/transcription.py'>transcription.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/audio/transcription_create_params.py'>transcription_create_params.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/audio/transcription_create_response.py'>transcription_create_response.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/audio/transcription_include.py'>transcription_include.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/audio/transcription_segment.py'>transcription_segment.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/audio/transcription_stream_event.py'>transcription_stream_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/audio/transcription_text_delta_event.py'>transcription_text_delta_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/audio/transcription_text_done_event.py'>transcription_text_done_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/audio/transcription_verbose.py'>transcription_verbose.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/audio/transcription_word.py'>transcription_word.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/audio/translation.py'>translation.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/audio/translation_create_params.py'>translation_create_params.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/audio/translation_create_response.py'>translation_create_response.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/audio/translation_verbose.py'>translation_verbose.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
											<!-- beta Submodule -->
											<details>
												<summary><b>beta</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.openai.types.beta</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/assistant.py'>assistant.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/assistant_create_params.py'>assistant_create_params.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/assistant_deleted.py'>assistant_deleted.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/assistant_list_params.py'>assistant_list_params.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/assistant_response_format_option.py'>assistant_response_format_option.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/assistant_response_format_option_param.py'>assistant_response_format_option_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/assistant_stream_event.py'>assistant_stream_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/assistant_tool.py'>assistant_tool.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/assistant_tool_choice.py'>assistant_tool_choice.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/assistant_tool_choice_function.py'>assistant_tool_choice_function.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/assistant_tool_choice_function_param.py'>assistant_tool_choice_function_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/assistant_tool_choice_option.py'>assistant_tool_choice_option.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/assistant_tool_choice_option_param.py'>assistant_tool_choice_option_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/assistant_tool_choice_param.py'>assistant_tool_choice_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/assistant_tool_param.py'>assistant_tool_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/assistant_update_params.py'>assistant_update_params.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/code_interpreter_tool.py'>code_interpreter_tool.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/code_interpreter_tool_param.py'>code_interpreter_tool_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/file_search_tool.py'>file_search_tool.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/file_search_tool_param.py'>file_search_tool_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/function_tool.py'>function_tool.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/function_tool_param.py'>function_tool_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/thread.py'>thread.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/thread_create_and_run_params.py'>thread_create_and_run_params.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/thread_create_params.py'>thread_create_params.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/thread_deleted.py'>thread_deleted.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/thread_update_params.py'>thread_update_params.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
													<!-- realtime Submodule -->
													<details>
														<summary><b>realtime</b></summary>
														<blockquote>
															<div class='directory-path' style='padding: 8px 0; color: #666;'>
																<code><b>⦿ venv.Lib.site-packages.openai.types.beta.realtime</b></code>
															<table style='width: 100%; border-collapse: collapse;'>
															<thead>
																<tr style='background-color: #f8f9fa;'>
																	<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																	<th style='text-align: left; padding: 8px;'>Summary</th>
																</tr>
															</thead>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/conversation_created_event.py'>conversation_created_event.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/conversation_item.py'>conversation_item.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/conversation_item_content.py'>conversation_item_content.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/conversation_item_content_param.py'>conversation_item_content_param.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/conversation_item_created_event.py'>conversation_item_created_event.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/conversation_item_create_event.py'>conversation_item_create_event.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/conversation_item_create_event_param.py'>conversation_item_create_event_param.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/conversation_item_deleted_event.py'>conversation_item_deleted_event.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/conversation_item_delete_event.py'>conversation_item_delete_event.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/conversation_item_delete_event_param.py'>conversation_item_delete_event_param.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/conversation_item_input_audio_transcription_completed_event.py'>conversation_item_input_audio_transcription_completed_event.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/conversation_item_input_audio_transcription_delta_event.py'>conversation_item_input_audio_transcription_delta_event.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/conversation_item_input_audio_transcription_failed_event.py'>conversation_item_input_audio_transcription_failed_event.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/conversation_item_param.py'>conversation_item_param.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/conversation_item_retrieve_event.py'>conversation_item_retrieve_event.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/conversation_item_retrieve_event_param.py'>conversation_item_retrieve_event_param.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/conversation_item_truncated_event.py'>conversation_item_truncated_event.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/conversation_item_truncate_event.py'>conversation_item_truncate_event.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/conversation_item_truncate_event_param.py'>conversation_item_truncate_event_param.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/conversation_item_with_reference.py'>conversation_item_with_reference.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/conversation_item_with_reference_param.py'>conversation_item_with_reference_param.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/error_event.py'>error_event.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/input_audio_buffer_append_event.py'>input_audio_buffer_append_event.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/input_audio_buffer_append_event_param.py'>input_audio_buffer_append_event_param.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/input_audio_buffer_cleared_event.py'>input_audio_buffer_cleared_event.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/input_audio_buffer_clear_event.py'>input_audio_buffer_clear_event.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/input_audio_buffer_clear_event_param.py'>input_audio_buffer_clear_event_param.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/input_audio_buffer_committed_event.py'>input_audio_buffer_committed_event.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/input_audio_buffer_commit_event.py'>input_audio_buffer_commit_event.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/input_audio_buffer_commit_event_param.py'>input_audio_buffer_commit_event_param.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/input_audio_buffer_speech_started_event.py'>input_audio_buffer_speech_started_event.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/input_audio_buffer_speech_stopped_event.py'>input_audio_buffer_speech_stopped_event.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/rate_limits_updated_event.py'>rate_limits_updated_event.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/realtime_client_event.py'>realtime_client_event.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/realtime_client_event_param.py'>realtime_client_event_param.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/realtime_connect_params.py'>realtime_connect_params.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/realtime_response.py'>realtime_response.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/realtime_response_status.py'>realtime_response_status.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/realtime_response_usage.py'>realtime_response_usage.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/realtime_server_event.py'>realtime_server_event.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/response_audio_delta_event.py'>response_audio_delta_event.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/response_audio_done_event.py'>response_audio_done_event.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/response_audio_transcript_delta_event.py'>response_audio_transcript_delta_event.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/response_audio_transcript_done_event.py'>response_audio_transcript_done_event.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/response_cancel_event.py'>response_cancel_event.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/response_cancel_event_param.py'>response_cancel_event_param.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/response_content_part_added_event.py'>response_content_part_added_event.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/response_content_part_done_event.py'>response_content_part_done_event.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/response_created_event.py'>response_created_event.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/response_create_event.py'>response_create_event.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/response_create_event_param.py'>response_create_event_param.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/response_done_event.py'>response_done_event.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/response_function_call_arguments_delta_event.py'>response_function_call_arguments_delta_event.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/response_function_call_arguments_done_event.py'>response_function_call_arguments_done_event.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/response_output_item_added_event.py'>response_output_item_added_event.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/response_output_item_done_event.py'>response_output_item_done_event.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/response_text_delta_event.py'>response_text_delta_event.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/response_text_done_event.py'>response_text_done_event.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/session.py'>session.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/session_created_event.py'>session_created_event.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/session_create_params.py'>session_create_params.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/session_create_response.py'>session_create_response.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/session_updated_event.py'>session_updated_event.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/session_update_event.py'>session_update_event.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/session_update_event_param.py'>session_update_event_param.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/transcription_session.py'>transcription_session.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/transcription_session_create_params.py'>transcription_session_create_params.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/transcription_session_update.py'>transcription_session_update.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/transcription_session_updated_event.py'>transcription_session_updated_event.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/realtime/transcription_session_update_param.py'>transcription_session_update_param.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
															</table>
														</blockquote>
													</details>
													<!-- threads Submodule -->
													<details>
														<summary><b>threads</b></summary>
														<blockquote>
															<div class='directory-path' style='padding: 8px 0; color: #666;'>
																<code><b>⦿ venv.Lib.site-packages.openai.types.beta.threads</b></code>
															<table style='width: 100%; border-collapse: collapse;'>
															<thead>
																<tr style='background-color: #f8f9fa;'>
																	<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																	<th style='text-align: left; padding: 8px;'>Summary</th>
																</tr>
															</thead>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/annotation.py'>annotation.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/annotation_delta.py'>annotation_delta.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/file_citation_annotation.py'>file_citation_annotation.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/file_citation_delta_annotation.py'>file_citation_delta_annotation.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/file_path_annotation.py'>file_path_annotation.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/file_path_delta_annotation.py'>file_path_delta_annotation.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/image_file.py'>image_file.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/image_file_content_block.py'>image_file_content_block.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/image_file_content_block_param.py'>image_file_content_block_param.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/image_file_delta.py'>image_file_delta.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/image_file_delta_block.py'>image_file_delta_block.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/image_file_param.py'>image_file_param.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/image_url.py'>image_url.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/image_url_content_block.py'>image_url_content_block.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/image_url_content_block_param.py'>image_url_content_block_param.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/image_url_delta.py'>image_url_delta.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/image_url_delta_block.py'>image_url_delta_block.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/image_url_param.py'>image_url_param.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/message.py'>message.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/message_content.py'>message_content.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/message_content_delta.py'>message_content_delta.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/message_content_part_param.py'>message_content_part_param.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/message_create_params.py'>message_create_params.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/message_deleted.py'>message_deleted.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/message_delta.py'>message_delta.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/message_delta_event.py'>message_delta_event.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/message_list_params.py'>message_list_params.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/message_update_params.py'>message_update_params.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/refusal_content_block.py'>refusal_content_block.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/refusal_delta_block.py'>refusal_delta_block.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/required_action_function_tool_call.py'>required_action_function_tool_call.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/run.py'>run.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/run_create_params.py'>run_create_params.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/run_list_params.py'>run_list_params.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/run_status.py'>run_status.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/run_submit_tool_outputs_params.py'>run_submit_tool_outputs_params.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/run_update_params.py'>run_update_params.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/text.py'>text.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/text_content_block.py'>text_content_block.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/text_content_block_param.py'>text_content_block_param.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/text_delta.py'>text_delta.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/text_delta_block.py'>text_delta_block.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
															</table>
															<!-- runs Submodule -->
															<details>
																<summary><b>runs</b></summary>
																<blockquote>
																	<div class='directory-path' style='padding: 8px 0; color: #666;'>
																		<code><b>⦿ venv.Lib.site-packages.openai.types.beta.threads.runs</b></code>
																	<table style='width: 100%; border-collapse: collapse;'>
																	<thead>
																		<tr style='background-color: #f8f9fa;'>
																			<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																			<th style='text-align: left; padding: 8px;'>Summary</th>
																		</tr>
																	</thead>
																		<tr style='border-bottom: 1px solid #eee;'>
																			<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/runs/code_interpreter_logs.py'>code_interpreter_logs.py</a></b></td>
																			<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																		</tr>
																		<tr style='border-bottom: 1px solid #eee;'>
																			<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/runs/code_interpreter_output_image.py'>code_interpreter_output_image.py</a></b></td>
																			<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																		</tr>
																		<tr style='border-bottom: 1px solid #eee;'>
																			<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/runs/code_interpreter_tool_call.py'>code_interpreter_tool_call.py</a></b></td>
																			<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																		</tr>
																		<tr style='border-bottom: 1px solid #eee;'>
																			<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/runs/code_interpreter_tool_call_delta.py'>code_interpreter_tool_call_delta.py</a></b></td>
																			<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																		</tr>
																		<tr style='border-bottom: 1px solid #eee;'>
																			<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/runs/file_search_tool_call.py'>file_search_tool_call.py</a></b></td>
																			<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																		</tr>
																		<tr style='border-bottom: 1px solid #eee;'>
																			<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/runs/file_search_tool_call_delta.py'>file_search_tool_call_delta.py</a></b></td>
																			<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																		</tr>
																		<tr style='border-bottom: 1px solid #eee;'>
																			<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/runs/function_tool_call.py'>function_tool_call.py</a></b></td>
																			<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																		</tr>
																		<tr style='border-bottom: 1px solid #eee;'>
																			<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/runs/function_tool_call_delta.py'>function_tool_call_delta.py</a></b></td>
																			<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																		</tr>
																		<tr style='border-bottom: 1px solid #eee;'>
																			<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/runs/message_creation_step_details.py'>message_creation_step_details.py</a></b></td>
																			<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																		</tr>
																		<tr style='border-bottom: 1px solid #eee;'>
																			<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/runs/run_step.py'>run_step.py</a></b></td>
																			<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																		</tr>
																		<tr style='border-bottom: 1px solid #eee;'>
																			<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/runs/run_step_delta.py'>run_step_delta.py</a></b></td>
																			<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																		</tr>
																		<tr style='border-bottom: 1px solid #eee;'>
																			<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/runs/run_step_delta_event.py'>run_step_delta_event.py</a></b></td>
																			<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																		</tr>
																		<tr style='border-bottom: 1px solid #eee;'>
																			<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/runs/run_step_delta_message_delta.py'>run_step_delta_message_delta.py</a></b></td>
																			<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																		</tr>
																		<tr style='border-bottom: 1px solid #eee;'>
																			<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/runs/run_step_include.py'>run_step_include.py</a></b></td>
																			<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																		</tr>
																		<tr style='border-bottom: 1px solid #eee;'>
																			<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/runs/step_list_params.py'>step_list_params.py</a></b></td>
																			<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																		</tr>
																		<tr style='border-bottom: 1px solid #eee;'>
																			<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/runs/step_retrieve_params.py'>step_retrieve_params.py</a></b></td>
																			<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																		</tr>
																		<tr style='border-bottom: 1px solid #eee;'>
																			<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/runs/tool_call.py'>tool_call.py</a></b></td>
																			<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																		</tr>
																		<tr style='border-bottom: 1px solid #eee;'>
																			<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/runs/tool_calls_step_details.py'>tool_calls_step_details.py</a></b></td>
																			<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																		</tr>
																		<tr style='border-bottom: 1px solid #eee;'>
																			<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/runs/tool_call_delta.py'>tool_call_delta.py</a></b></td>
																			<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																		</tr>
																		<tr style='border-bottom: 1px solid #eee;'>
																			<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/beta/threads/runs/tool_call_delta_object.py'>tool_call_delta_object.py</a></b></td>
																			<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																		</tr>
																	</table>
																</blockquote>
															</details>
														</blockquote>
													</details>
												</blockquote>
											</details>
											<!-- chat Submodule -->
											<details>
												<summary><b>chat</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.openai.types.chat</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/chat/chat_completion.py'>chat_completion.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/chat/chat_completion_allowed_tools_param.py'>chat_completion_allowed_tools_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/chat/chat_completion_allowed_tool_choice_param.py'>chat_completion_allowed_tool_choice_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/chat/chat_completion_assistant_message_param.py'>chat_completion_assistant_message_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/chat/chat_completion_audio.py'>chat_completion_audio.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/chat/chat_completion_audio_param.py'>chat_completion_audio_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/chat/chat_completion_chunk.py'>chat_completion_chunk.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/chat/chat_completion_content_part_image.py'>chat_completion_content_part_image.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/chat/chat_completion_content_part_image_param.py'>chat_completion_content_part_image_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/chat/chat_completion_content_part_input_audio_param.py'>chat_completion_content_part_input_audio_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/chat/chat_completion_content_part_param.py'>chat_completion_content_part_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/chat/chat_completion_content_part_refusal_param.py'>chat_completion_content_part_refusal_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/chat/chat_completion_content_part_text.py'>chat_completion_content_part_text.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/chat/chat_completion_content_part_text_param.py'>chat_completion_content_part_text_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/chat/chat_completion_custom_tool_param.py'>chat_completion_custom_tool_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/chat/chat_completion_deleted.py'>chat_completion_deleted.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/chat/chat_completion_developer_message_param.py'>chat_completion_developer_message_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/chat/chat_completion_function_call_option_param.py'>chat_completion_function_call_option_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/chat/chat_completion_function_message_param.py'>chat_completion_function_message_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/chat/chat_completion_function_tool.py'>chat_completion_function_tool.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/chat/chat_completion_function_tool_param.py'>chat_completion_function_tool_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/chat/chat_completion_message.py'>chat_completion_message.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/chat/chat_completion_message_custom_tool_call.py'>chat_completion_message_custom_tool_call.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/chat/chat_completion_message_custom_tool_call_param.py'>chat_completion_message_custom_tool_call_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/chat/chat_completion_message_function_tool_call.py'>chat_completion_message_function_tool_call.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/chat/chat_completion_message_function_tool_call_param.py'>chat_completion_message_function_tool_call_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/chat/chat_completion_message_param.py'>chat_completion_message_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/chat/chat_completion_message_tool_call.py'>chat_completion_message_tool_call.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/chat/chat_completion_message_tool_call_param.py'>chat_completion_message_tool_call_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/chat/chat_completion_message_tool_call_union_param.py'>chat_completion_message_tool_call_union_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/chat/chat_completion_modality.py'>chat_completion_modality.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/chat/chat_completion_named_tool_choice_custom_param.py'>chat_completion_named_tool_choice_custom_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/chat/chat_completion_named_tool_choice_param.py'>chat_completion_named_tool_choice_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/chat/chat_completion_prediction_content_param.py'>chat_completion_prediction_content_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/chat/chat_completion_reasoning_effort.py'>chat_completion_reasoning_effort.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/chat/chat_completion_role.py'>chat_completion_role.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/chat/chat_completion_store_message.py'>chat_completion_store_message.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/chat/chat_completion_stream_options_param.py'>chat_completion_stream_options_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/chat/chat_completion_system_message_param.py'>chat_completion_system_message_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/chat/chat_completion_token_logprob.py'>chat_completion_token_logprob.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/chat/chat_completion_tool_choice_option_param.py'>chat_completion_tool_choice_option_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/chat/chat_completion_tool_message_param.py'>chat_completion_tool_message_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/chat/chat_completion_tool_param.py'>chat_completion_tool_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/chat/chat_completion_tool_union_param.py'>chat_completion_tool_union_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/chat/chat_completion_user_message_param.py'>chat_completion_user_message_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/chat/completion_create_params.py'>completion_create_params.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/chat/completion_list_params.py'>completion_list_params.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/chat/completion_update_params.py'>completion_update_params.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/chat/parsed_chat_completion.py'>parsed_chat_completion.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/chat/parsed_function_tool_call.py'>parsed_function_tool_call.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
													<!-- completions Submodule -->
													<details>
														<summary><b>completions</b></summary>
														<blockquote>
															<div class='directory-path' style='padding: 8px 0; color: #666;'>
																<code><b>⦿ venv.Lib.site-packages.openai.types.chat.completions</b></code>
															<table style='width: 100%; border-collapse: collapse;'>
															<thead>
																<tr style='background-color: #f8f9fa;'>
																	<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																	<th style='text-align: left; padding: 8px;'>Summary</th>
																</tr>
															</thead>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/chat/completions/message_list_params.py'>message_list_params.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
															</table>
														</blockquote>
													</details>
												</blockquote>
											</details>
											<!-- containers Submodule -->
											<details>
												<summary><b>containers</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.openai.types.containers</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/containers/file_create_params.py'>file_create_params.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/containers/file_create_response.py'>file_create_response.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/containers/file_list_params.py'>file_list_params.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/containers/file_list_response.py'>file_list_response.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/containers/file_retrieve_response.py'>file_retrieve_response.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
											<!-- conversations Submodule -->
											<details>
												<summary><b>conversations</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.openai.types.conversations</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/conversations/computer_screenshot_content.py'>computer_screenshot_content.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/conversations/container_file_citation_body.py'>container_file_citation_body.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/conversations/conversation.py'>conversation.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/conversations/conversation_create_params.py'>conversation_create_params.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/conversations/conversation_deleted_resource.py'>conversation_deleted_resource.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/conversations/conversation_item.py'>conversation_item.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/conversations/conversation_item_list.py'>conversation_item_list.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/conversations/conversation_update_params.py'>conversation_update_params.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/conversations/file_citation_body.py'>file_citation_body.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/conversations/input_file_content.py'>input_file_content.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/conversations/input_image_content.py'>input_image_content.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/conversations/input_text_content.py'>input_text_content.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/conversations/item_create_params.py'>item_create_params.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/conversations/item_list_params.py'>item_list_params.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/conversations/item_retrieve_params.py'>item_retrieve_params.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/conversations/lob_prob.py'>lob_prob.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/conversations/message.py'>message.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/conversations/output_text_content.py'>output_text_content.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/conversations/refusal_content.py'>refusal_content.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/conversations/summary_text_content.py'>summary_text_content.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/conversations/text_content.py'>text_content.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/conversations/top_log_prob.py'>top_log_prob.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/conversations/url_citation_body.py'>url_citation_body.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
											<!-- evals Submodule -->
											<details>
												<summary><b>evals</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.openai.types.evals</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/evals/create_eval_completions_run_data_source.py'>create_eval_completions_run_data_source.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/evals/create_eval_completions_run_data_source_param.py'>create_eval_completions_run_data_source_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/evals/create_eval_jsonl_run_data_source.py'>create_eval_jsonl_run_data_source.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/evals/create_eval_jsonl_run_data_source_param.py'>create_eval_jsonl_run_data_source_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/evals/eval_api_error.py'>eval_api_error.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/evals/run_cancel_response.py'>run_cancel_response.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/evals/run_create_params.py'>run_create_params.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/evals/run_create_response.py'>run_create_response.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/evals/run_delete_response.py'>run_delete_response.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/evals/run_list_params.py'>run_list_params.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/evals/run_list_response.py'>run_list_response.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/evals/run_retrieve_response.py'>run_retrieve_response.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
													<!-- runs Submodule -->
													<details>
														<summary><b>runs</b></summary>
														<blockquote>
															<div class='directory-path' style='padding: 8px 0; color: #666;'>
																<code><b>⦿ venv.Lib.site-packages.openai.types.evals.runs</b></code>
															<table style='width: 100%; border-collapse: collapse;'>
															<thead>
																<tr style='background-color: #f8f9fa;'>
																	<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																	<th style='text-align: left; padding: 8px;'>Summary</th>
																</tr>
															</thead>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/evals/runs/output_item_list_params.py'>output_item_list_params.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/evals/runs/output_item_list_response.py'>output_item_list_response.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/evals/runs/output_item_retrieve_response.py'>output_item_retrieve_response.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
															</table>
														</blockquote>
													</details>
												</blockquote>
											</details>
											<!-- fine_tuning Submodule -->
											<details>
												<summary><b>fine_tuning</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.openai.types.fine_tuning</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/fine_tuning/dpo_hyperparameters.py'>dpo_hyperparameters.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/fine_tuning/dpo_hyperparameters_param.py'>dpo_hyperparameters_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/fine_tuning/dpo_method.py'>dpo_method.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/fine_tuning/dpo_method_param.py'>dpo_method_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/fine_tuning/fine_tuning_job.py'>fine_tuning_job.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/fine_tuning/fine_tuning_job_event.py'>fine_tuning_job_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/fine_tuning/fine_tuning_job_integration.py'>fine_tuning_job_integration.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/fine_tuning/fine_tuning_job_wandb_integration.py'>fine_tuning_job_wandb_integration.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/fine_tuning/fine_tuning_job_wandb_integration_object.py'>fine_tuning_job_wandb_integration_object.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/fine_tuning/job_create_params.py'>job_create_params.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/fine_tuning/job_list_events_params.py'>job_list_events_params.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/fine_tuning/job_list_params.py'>job_list_params.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/fine_tuning/reinforcement_hyperparameters.py'>reinforcement_hyperparameters.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/fine_tuning/reinforcement_hyperparameters_param.py'>reinforcement_hyperparameters_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/fine_tuning/reinforcement_method.py'>reinforcement_method.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/fine_tuning/reinforcement_method_param.py'>reinforcement_method_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/fine_tuning/supervised_hyperparameters.py'>supervised_hyperparameters.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/fine_tuning/supervised_hyperparameters_param.py'>supervised_hyperparameters_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/fine_tuning/supervised_method.py'>supervised_method.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/fine_tuning/supervised_method_param.py'>supervised_method_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
													<!-- alpha Submodule -->
													<details>
														<summary><b>alpha</b></summary>
														<blockquote>
															<div class='directory-path' style='padding: 8px 0; color: #666;'>
																<code><b>⦿ venv.Lib.site-packages.openai.types.fine_tuning.alpha</b></code>
															<table style='width: 100%; border-collapse: collapse;'>
															<thead>
																<tr style='background-color: #f8f9fa;'>
																	<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																	<th style='text-align: left; padding: 8px;'>Summary</th>
																</tr>
															</thead>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/fine_tuning/alpha/grader_run_params.py'>grader_run_params.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/fine_tuning/alpha/grader_run_response.py'>grader_run_response.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/fine_tuning/alpha/grader_validate_params.py'>grader_validate_params.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/fine_tuning/alpha/grader_validate_response.py'>grader_validate_response.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
															</table>
														</blockquote>
													</details>
													<!-- checkpoints Submodule -->
													<details>
														<summary><b>checkpoints</b></summary>
														<blockquote>
															<div class='directory-path' style='padding: 8px 0; color: #666;'>
																<code><b>⦿ venv.Lib.site-packages.openai.types.fine_tuning.checkpoints</b></code>
															<table style='width: 100%; border-collapse: collapse;'>
															<thead>
																<tr style='background-color: #f8f9fa;'>
																	<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																	<th style='text-align: left; padding: 8px;'>Summary</th>
																</tr>
															</thead>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/fine_tuning/checkpoints/permission_create_params.py'>permission_create_params.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/fine_tuning/checkpoints/permission_create_response.py'>permission_create_response.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/fine_tuning/checkpoints/permission_delete_response.py'>permission_delete_response.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/fine_tuning/checkpoints/permission_retrieve_params.py'>permission_retrieve_params.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/fine_tuning/checkpoints/permission_retrieve_response.py'>permission_retrieve_response.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
															</table>
														</blockquote>
													</details>
													<!-- jobs Submodule -->
													<details>
														<summary><b>jobs</b></summary>
														<blockquote>
															<div class='directory-path' style='padding: 8px 0; color: #666;'>
																<code><b>⦿ venv.Lib.site-packages.openai.types.fine_tuning.jobs</b></code>
															<table style='width: 100%; border-collapse: collapse;'>
															<thead>
																<tr style='background-color: #f8f9fa;'>
																	<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																	<th style='text-align: left; padding: 8px;'>Summary</th>
																</tr>
															</thead>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/fine_tuning/jobs/checkpoint_list_params.py'>checkpoint_list_params.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/fine_tuning/jobs/fine_tuning_job_checkpoint.py'>fine_tuning_job_checkpoint.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
															</table>
														</blockquote>
													</details>
												</blockquote>
											</details>
											<!-- graders Submodule -->
											<details>
												<summary><b>graders</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.openai.types.graders</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/graders/label_model_grader.py'>label_model_grader.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/graders/label_model_grader_param.py'>label_model_grader_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/graders/multi_grader.py'>multi_grader.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/graders/multi_grader_param.py'>multi_grader_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/graders/python_grader.py'>python_grader.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/graders/python_grader_param.py'>python_grader_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/graders/score_model_grader.py'>score_model_grader.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/graders/score_model_grader_param.py'>score_model_grader_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/graders/string_check_grader.py'>string_check_grader.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/graders/string_check_grader_param.py'>string_check_grader_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/graders/text_similarity_grader.py'>text_similarity_grader.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/graders/text_similarity_grader_param.py'>text_similarity_grader_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
											<!-- responses Submodule -->
											<details>
												<summary><b>responses</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.openai.types.responses</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/computer_tool.py'>computer_tool.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/computer_tool_param.py'>computer_tool_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/custom_tool.py'>custom_tool.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/custom_tool_param.py'>custom_tool_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/easy_input_message.py'>easy_input_message.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/easy_input_message_param.py'>easy_input_message_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/file_search_tool.py'>file_search_tool.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/file_search_tool_param.py'>file_search_tool_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/function_tool.py'>function_tool.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/function_tool_param.py'>function_tool_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/input_item_list_params.py'>input_item_list_params.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/parsed_response.py'>parsed_response.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response.py'>response.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_audio_delta_event.py'>response_audio_delta_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_audio_done_event.py'>response_audio_done_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_audio_transcript_delta_event.py'>response_audio_transcript_delta_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_audio_transcript_done_event.py'>response_audio_transcript_done_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_code_interpreter_call_code_delta_event.py'>response_code_interpreter_call_code_delta_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_code_interpreter_call_code_done_event.py'>response_code_interpreter_call_code_done_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_code_interpreter_call_completed_event.py'>response_code_interpreter_call_completed_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_code_interpreter_call_interpreting_event.py'>response_code_interpreter_call_interpreting_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_code_interpreter_call_in_progress_event.py'>response_code_interpreter_call_in_progress_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_code_interpreter_tool_call.py'>response_code_interpreter_tool_call.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_code_interpreter_tool_call_param.py'>response_code_interpreter_tool_call_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_completed_event.py'>response_completed_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_computer_tool_call.py'>response_computer_tool_call.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_computer_tool_call_output_item.py'>response_computer_tool_call_output_item.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_computer_tool_call_output_screenshot.py'>response_computer_tool_call_output_screenshot.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_computer_tool_call_output_screenshot_param.py'>response_computer_tool_call_output_screenshot_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_computer_tool_call_param.py'>response_computer_tool_call_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_content_part_added_event.py'>response_content_part_added_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_content_part_done_event.py'>response_content_part_done_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_conversation_param.py'>response_conversation_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_created_event.py'>response_created_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_create_params.py'>response_create_params.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_custom_tool_call.py'>response_custom_tool_call.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_custom_tool_call_input_delta_event.py'>response_custom_tool_call_input_delta_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_custom_tool_call_input_done_event.py'>response_custom_tool_call_input_done_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_custom_tool_call_output.py'>response_custom_tool_call_output.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_custom_tool_call_output_param.py'>response_custom_tool_call_output_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_custom_tool_call_param.py'>response_custom_tool_call_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_error.py'>response_error.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_error_event.py'>response_error_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_failed_event.py'>response_failed_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_file_search_call_completed_event.py'>response_file_search_call_completed_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_file_search_call_in_progress_event.py'>response_file_search_call_in_progress_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_file_search_call_searching_event.py'>response_file_search_call_searching_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_file_search_tool_call.py'>response_file_search_tool_call.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_file_search_tool_call_param.py'>response_file_search_tool_call_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_format_text_config.py'>response_format_text_config.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_format_text_config_param.py'>response_format_text_config_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_format_text_json_schema_config.py'>response_format_text_json_schema_config.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_format_text_json_schema_config_param.py'>response_format_text_json_schema_config_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_function_call_arguments_delta_event.py'>response_function_call_arguments_delta_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_function_call_arguments_done_event.py'>response_function_call_arguments_done_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_function_tool_call.py'>response_function_tool_call.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_function_tool_call_item.py'>response_function_tool_call_item.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_function_tool_call_output_item.py'>response_function_tool_call_output_item.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_function_tool_call_param.py'>response_function_tool_call_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_function_web_search.py'>response_function_web_search.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_function_web_search_param.py'>response_function_web_search_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_image_gen_call_completed_event.py'>response_image_gen_call_completed_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_image_gen_call_generating_event.py'>response_image_gen_call_generating_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_image_gen_call_in_progress_event.py'>response_image_gen_call_in_progress_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_image_gen_call_partial_image_event.py'>response_image_gen_call_partial_image_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_includable.py'>response_includable.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_incomplete_event.py'>response_incomplete_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_input_content.py'>response_input_content.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_input_content_param.py'>response_input_content_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_input_file.py'>response_input_file.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_input_file_param.py'>response_input_file_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_input_image.py'>response_input_image.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_input_image_param.py'>response_input_image_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_input_item.py'>response_input_item.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_input_item_param.py'>response_input_item_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_input_message_content_list.py'>response_input_message_content_list.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_input_message_content_list_param.py'>response_input_message_content_list_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_input_message_item.py'>response_input_message_item.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_input_param.py'>response_input_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_input_text.py'>response_input_text.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_input_text_param.py'>response_input_text_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_in_progress_event.py'>response_in_progress_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_item.py'>response_item.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_item_list.py'>response_item_list.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_mcp_call_arguments_delta_event.py'>response_mcp_call_arguments_delta_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_mcp_call_arguments_done_event.py'>response_mcp_call_arguments_done_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_mcp_call_completed_event.py'>response_mcp_call_completed_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_mcp_call_failed_event.py'>response_mcp_call_failed_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_mcp_call_in_progress_event.py'>response_mcp_call_in_progress_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_mcp_list_tools_completed_event.py'>response_mcp_list_tools_completed_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_mcp_list_tools_failed_event.py'>response_mcp_list_tools_failed_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_mcp_list_tools_in_progress_event.py'>response_mcp_list_tools_in_progress_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_output_item.py'>response_output_item.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_output_item_added_event.py'>response_output_item_added_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_output_item_done_event.py'>response_output_item_done_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_output_message.py'>response_output_message.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_output_message_param.py'>response_output_message_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_output_refusal.py'>response_output_refusal.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_output_refusal_param.py'>response_output_refusal_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_output_text.py'>response_output_text.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_output_text_annotation_added_event.py'>response_output_text_annotation_added_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_output_text_param.py'>response_output_text_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_prompt.py'>response_prompt.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_prompt_param.py'>response_prompt_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_queued_event.py'>response_queued_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_reasoning_item.py'>response_reasoning_item.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_reasoning_item_param.py'>response_reasoning_item_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_reasoning_summary_part_added_event.py'>response_reasoning_summary_part_added_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_reasoning_summary_part_done_event.py'>response_reasoning_summary_part_done_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_reasoning_summary_text_delta_event.py'>response_reasoning_summary_text_delta_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_reasoning_summary_text_done_event.py'>response_reasoning_summary_text_done_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_reasoning_text_delta_event.py'>response_reasoning_text_delta_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_reasoning_text_done_event.py'>response_reasoning_text_done_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_refusal_delta_event.py'>response_refusal_delta_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_refusal_done_event.py'>response_refusal_done_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_retrieve_params.py'>response_retrieve_params.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_status.py'>response_status.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_stream_event.py'>response_stream_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_text_config.py'>response_text_config.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_text_config_param.py'>response_text_config_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_text_delta_event.py'>response_text_delta_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_text_done_event.py'>response_text_done_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_usage.py'>response_usage.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_web_search_call_completed_event.py'>response_web_search_call_completed_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_web_search_call_in_progress_event.py'>response_web_search_call_in_progress_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/response_web_search_call_searching_event.py'>response_web_search_call_searching_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/tool.py'>tool.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/tool_choice_allowed.py'>tool_choice_allowed.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/tool_choice_allowed_param.py'>tool_choice_allowed_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/tool_choice_custom.py'>tool_choice_custom.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/tool_choice_custom_param.py'>tool_choice_custom_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/tool_choice_function.py'>tool_choice_function.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/tool_choice_function_param.py'>tool_choice_function_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/tool_choice_mcp.py'>tool_choice_mcp.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/tool_choice_mcp_param.py'>tool_choice_mcp_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/tool_choice_options.py'>tool_choice_options.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/tool_choice_types.py'>tool_choice_types.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/tool_choice_types_param.py'>tool_choice_types_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/tool_param.py'>tool_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/web_search_tool.py'>web_search_tool.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/responses/web_search_tool_param.py'>web_search_tool_param.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
											<!-- shared Submodule -->
											<details>
												<summary><b>shared</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.openai.types.shared</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/shared/all_models.py'>all_models.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/shared/chat_model.py'>chat_model.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/shared/comparison_filter.py'>comparison_filter.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/shared/compound_filter.py'>compound_filter.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/shared/custom_tool_input_format.py'>custom_tool_input_format.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/shared/error_object.py'>error_object.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/shared/function_definition.py'>function_definition.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/shared/function_parameters.py'>function_parameters.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/shared/metadata.py'>metadata.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/shared/reasoning.py'>reasoning.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/shared/reasoning_effort.py'>reasoning_effort.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/shared/responses_model.py'>responses_model.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/shared/response_format_json_object.py'>response_format_json_object.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/shared/response_format_json_schema.py'>response_format_json_schema.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/shared/response_format_text.py'>response_format_text.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/shared/response_format_text_grammar.py'>response_format_text_grammar.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/shared/response_format_text_python.py'>response_format_text_python.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
											<!-- shared_params Submodule -->
											<details>
												<summary><b>shared_params</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.openai.types.shared_params</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/shared_params/chat_model.py'>chat_model.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/shared_params/comparison_filter.py'>comparison_filter.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/shared_params/compound_filter.py'>compound_filter.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/shared_params/custom_tool_input_format.py'>custom_tool_input_format.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/shared_params/function_definition.py'>function_definition.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/shared_params/function_parameters.py'>function_parameters.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/shared_params/metadata.py'>metadata.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/shared_params/reasoning.py'>reasoning.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/shared_params/reasoning_effort.py'>reasoning_effort.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/shared_params/responses_model.py'>responses_model.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/shared_params/response_format_json_object.py'>response_format_json_object.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/shared_params/response_format_json_schema.py'>response_format_json_schema.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/shared_params/response_format_text.py'>response_format_text.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
											<!-- uploads Submodule -->
											<details>
												<summary><b>uploads</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.openai.types.uploads</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/uploads/part_create_params.py'>part_create_params.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/uploads/upload_part.py'>upload_part.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
											<!-- vector_stores Submodule -->
											<details>
												<summary><b>vector_stores</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.openai.types.vector_stores</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/vector_stores/file_batch_create_params.py'>file_batch_create_params.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/vector_stores/file_batch_list_files_params.py'>file_batch_list_files_params.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/vector_stores/file_content_response.py'>file_content_response.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/vector_stores/file_create_params.py'>file_create_params.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/vector_stores/file_list_params.py'>file_list_params.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/vector_stores/file_update_params.py'>file_update_params.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/vector_stores/vector_store_file.py'>vector_store_file.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/vector_stores/vector_store_file_batch.py'>vector_store_file_batch.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/vector_stores/vector_store_file_deleted.py'>vector_store_file_deleted.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
											<!-- webhooks Submodule -->
											<details>
												<summary><b>webhooks</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.openai.types.webhooks</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/webhooks/batch_cancelled_webhook_event.py'>batch_cancelled_webhook_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/webhooks/batch_completed_webhook_event.py'>batch_completed_webhook_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/webhooks/batch_expired_webhook_event.py'>batch_expired_webhook_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/webhooks/batch_failed_webhook_event.py'>batch_failed_webhook_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/webhooks/eval_run_canceled_webhook_event.py'>eval_run_canceled_webhook_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/webhooks/eval_run_failed_webhook_event.py'>eval_run_failed_webhook_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/webhooks/eval_run_succeeded_webhook_event.py'>eval_run_succeeded_webhook_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/webhooks/fine_tuning_job_cancelled_webhook_event.py'>fine_tuning_job_cancelled_webhook_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/webhooks/fine_tuning_job_failed_webhook_event.py'>fine_tuning_job_failed_webhook_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/webhooks/fine_tuning_job_succeeded_webhook_event.py'>fine_tuning_job_succeeded_webhook_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/webhooks/response_cancelled_webhook_event.py'>response_cancelled_webhook_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/webhooks/response_completed_webhook_event.py'>response_completed_webhook_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/webhooks/response_failed_webhook_event.py'>response_failed_webhook_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/webhooks/response_incomplete_webhook_event.py'>response_incomplete_webhook_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/types/webhooks/unwrap_webhook_event.py'>unwrap_webhook_event.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
										</blockquote>
									</details>
									<!-- _extras Submodule -->
									<details>
										<summary><b>_extras</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.openai._extras</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/_extras/numpy_proxy.py'>numpy_proxy.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/_extras/pandas_proxy.py'>pandas_proxy.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/_extras/sounddevice_proxy.py'>sounddevice_proxy.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/_extras/_common.py'>_common.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
									<!-- _utils Submodule -->
									<details>
										<summary><b>_utils</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.openai._utils</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/_utils/_logs.py'>_logs.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/_utils/_proxy.py'>_proxy.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/_utils/_reflection.py'>_reflection.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/_utils/_resources_proxy.py'>_resources_proxy.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/_utils/_streams.py'>_streams.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/_utils/_sync.py'>_sync.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/_utils/_transform.py'>_transform.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/_utils/_typing.py'>_typing.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai/_utils/_utils.py'>_utils.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<!-- openai-1.101.0.dist-info Submodule -->
							<details>
								<summary><b>openai-1.101.0.dist-info</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.openai-1.101.0.dist-info</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai-1.101.0.dist-info/entry_points.txt'>entry_points.txt</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai-1.101.0.dist-info/INSTALLER'>INSTALLER</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai-1.101.0.dist-info/METADATA'>METADATA</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai-1.101.0.dist-info/RECORD'>RECORD</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai-1.101.0.dist-info/WHEEL'>WHEEL</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
									<!-- licenses Submodule -->
									<details>
										<summary><b>licenses</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.openai-1.101.0.dist-info.licenses</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/openai-1.101.0.dist-info/licenses/LICENSE'>LICENSE</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<!-- pip Submodule -->
							<details>
								<summary><b>pip</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.pip</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/py.typed'>py.typed</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/__main__.py'>__main__.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/__pip-runner__.py'>__pip-runner__.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
									<!-- _internal Submodule -->
									<details>
										<summary><b>_internal</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.pip._internal</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/build_env.py'>build_env.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/cache.py'>cache.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/configuration.py'>configuration.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/exceptions.py'>exceptions.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/main.py'>main.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/pyproject.py'>pyproject.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/self_outdated_check.py'>self_outdated_check.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/wheel_builder.py'>wheel_builder.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
											<!-- cli Submodule -->
											<details>
												<summary><b>cli</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.pip._internal.cli</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/cli/autocompletion.py'>autocompletion.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/cli/base_command.py'>base_command.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/cli/cmdoptions.py'>cmdoptions.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/cli/command_context.py'>command_context.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/cli/index_command.py'>index_command.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/cli/main.py'>main.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/cli/main_parser.py'>main_parser.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/cli/parser.py'>parser.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/cli/progress_bars.py'>progress_bars.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/cli/req_command.py'>req_command.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/cli/spinners.py'>spinners.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/cli/status_codes.py'>status_codes.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
											<!-- commands Submodule -->
											<details>
												<summary><b>commands</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.pip._internal.commands</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/commands/cache.py'>cache.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/commands/check.py'>check.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/commands/completion.py'>completion.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/commands/configuration.py'>configuration.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/commands/debug.py'>debug.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/commands/download.py'>download.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/commands/freeze.py'>freeze.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/commands/hash.py'>hash.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/commands/help.py'>help.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/commands/index.py'>index.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/commands/inspect.py'>inspect.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/commands/install.py'>install.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/commands/list.py'>list.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/commands/lock.py'>lock.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/commands/search.py'>search.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/commands/show.py'>show.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/commands/uninstall.py'>uninstall.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/commands/wheel.py'>wheel.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
											<!-- distributions Submodule -->
											<details>
												<summary><b>distributions</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.pip._internal.distributions</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/distributions/base.py'>base.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/distributions/installed.py'>installed.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/distributions/sdist.py'>sdist.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/distributions/wheel.py'>wheel.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
											<!-- index Submodule -->
											<details>
												<summary><b>index</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.pip._internal.index</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/index/collector.py'>collector.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/index/package_finder.py'>package_finder.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/index/sources.py'>sources.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
											<!-- locations Submodule -->
											<details>
												<summary><b>locations</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.pip._internal.locations</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/locations/base.py'>base.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/locations/_distutils.py'>_distutils.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/locations/_sysconfig.py'>_sysconfig.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
											<!-- metadata Submodule -->
											<details>
												<summary><b>metadata</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.pip._internal.metadata</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/metadata/base.py'>base.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/metadata/pkg_resources.py'>pkg_resources.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/metadata/_json.py'>_json.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
													<!-- importlib Submodule -->
													<details>
														<summary><b>importlib</b></summary>
														<blockquote>
															<div class='directory-path' style='padding: 8px 0; color: #666;'>
																<code><b>⦿ venv.Lib.site-packages.pip._internal.metadata.importlib</b></code>
															<table style='width: 100%; border-collapse: collapse;'>
															<thead>
																<tr style='background-color: #f8f9fa;'>
																	<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																	<th style='text-align: left; padding: 8px;'>Summary</th>
																</tr>
															</thead>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/metadata/importlib/_compat.py'>_compat.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/metadata/importlib/_dists.py'>_dists.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/metadata/importlib/_envs.py'>_envs.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
															</table>
														</blockquote>
													</details>
												</blockquote>
											</details>
											<!-- models Submodule -->
											<details>
												<summary><b>models</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.pip._internal.models</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/models/candidate.py'>candidate.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/models/direct_url.py'>direct_url.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/models/format_control.py'>format_control.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/models/index.py'>index.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/models/installation_report.py'>installation_report.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/models/link.py'>link.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/models/pylock.py'>pylock.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/models/scheme.py'>scheme.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/models/search_scope.py'>search_scope.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/models/selection_prefs.py'>selection_prefs.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/models/target_python.py'>target_python.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/models/wheel.py'>wheel.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
											<!-- network Submodule -->
											<details>
												<summary><b>network</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.pip._internal.network</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/network/auth.py'>auth.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/network/cache.py'>cache.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/network/download.py'>download.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/network/lazy_wheel.py'>lazy_wheel.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/network/session.py'>session.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/network/utils.py'>utils.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/network/xmlrpc.py'>xmlrpc.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
											<!-- operations Submodule -->
											<details>
												<summary><b>operations</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.pip._internal.operations</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/operations/check.py'>check.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/operations/freeze.py'>freeze.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/operations/prepare.py'>prepare.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
													<!-- build Submodule -->
													<details>
														<summary><b>build</b></summary>
														<blockquote>
															<div class='directory-path' style='padding: 8px 0; color: #666;'>
																<code><b>⦿ venv.Lib.site-packages.pip._internal.operations.build</b></code>
															<table style='width: 100%; border-collapse: collapse;'>
															<thead>
																<tr style='background-color: #f8f9fa;'>
																	<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																	<th style='text-align: left; padding: 8px;'>Summary</th>
																</tr>
															</thead>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/operations/build/build_tracker.py'>build_tracker.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/operations/build/metadata.py'>metadata.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/operations/build/metadata_editable.py'>metadata_editable.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/operations/build/metadata_legacy.py'>metadata_legacy.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/operations/build/wheel.py'>wheel.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/operations/build/wheel_editable.py'>wheel_editable.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/operations/build/wheel_legacy.py'>wheel_legacy.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
															</table>
														</blockquote>
													</details>
													<!-- install Submodule -->
													<details>
														<summary><b>install</b></summary>
														<blockquote>
															<div class='directory-path' style='padding: 8px 0; color: #666;'>
																<code><b>⦿ venv.Lib.site-packages.pip._internal.operations.install</b></code>
															<table style='width: 100%; border-collapse: collapse;'>
															<thead>
																<tr style='background-color: #f8f9fa;'>
																	<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																	<th style='text-align: left; padding: 8px;'>Summary</th>
																</tr>
															</thead>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/operations/install/editable_legacy.py'>editable_legacy.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/operations/install/wheel.py'>wheel.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
															</table>
														</blockquote>
													</details>
												</blockquote>
											</details>
											<!-- req Submodule -->
											<details>
												<summary><b>req</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.pip._internal.req</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/req/constructors.py'>constructors.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/req/req_dependency_group.py'>req_dependency_group.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/req/req_file.py'>req_file.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/req/req_install.py'>req_install.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/req/req_set.py'>req_set.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/req/req_uninstall.py'>req_uninstall.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
											<!-- resolution Submodule -->
											<details>
												<summary><b>resolution</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.pip._internal.resolution</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/resolution/base.py'>base.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
													<!-- legacy Submodule -->
													<details>
														<summary><b>legacy</b></summary>
														<blockquote>
															<div class='directory-path' style='padding: 8px 0; color: #666;'>
																<code><b>⦿ venv.Lib.site-packages.pip._internal.resolution.legacy</b></code>
															<table style='width: 100%; border-collapse: collapse;'>
															<thead>
																<tr style='background-color: #f8f9fa;'>
																	<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																	<th style='text-align: left; padding: 8px;'>Summary</th>
																</tr>
															</thead>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/resolution/legacy/resolver.py'>resolver.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
															</table>
														</blockquote>
													</details>
													<!-- resolvelib Submodule -->
													<details>
														<summary><b>resolvelib</b></summary>
														<blockquote>
															<div class='directory-path' style='padding: 8px 0; color: #666;'>
																<code><b>⦿ venv.Lib.site-packages.pip._internal.resolution.resolvelib</b></code>
															<table style='width: 100%; border-collapse: collapse;'>
															<thead>
																<tr style='background-color: #f8f9fa;'>
																	<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																	<th style='text-align: left; padding: 8px;'>Summary</th>
																</tr>
															</thead>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/resolution/resolvelib/base.py'>base.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/resolution/resolvelib/candidates.py'>candidates.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/resolution/resolvelib/factory.py'>factory.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/resolution/resolvelib/found_candidates.py'>found_candidates.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/resolution/resolvelib/provider.py'>provider.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/resolution/resolvelib/reporter.py'>reporter.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/resolution/resolvelib/requirements.py'>requirements.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/resolution/resolvelib/resolver.py'>resolver.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
															</table>
														</blockquote>
													</details>
												</blockquote>
											</details>
											<!-- utils Submodule -->
											<details>
												<summary><b>utils</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.pip._internal.utils</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/utils/appdirs.py'>appdirs.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/utils/compat.py'>compat.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/utils/compatibility_tags.py'>compatibility_tags.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/utils/datetime.py'>datetime.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/utils/deprecation.py'>deprecation.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/utils/direct_url_helpers.py'>direct_url_helpers.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/utils/egg_link.py'>egg_link.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/utils/entrypoints.py'>entrypoints.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/utils/filesystem.py'>filesystem.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/utils/filetypes.py'>filetypes.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/utils/glibc.py'>glibc.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/utils/hashes.py'>hashes.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/utils/logging.py'>logging.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/utils/misc.py'>misc.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/utils/packaging.py'>packaging.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/utils/retry.py'>retry.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/utils/setuptools_build.py'>setuptools_build.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/utils/subprocess.py'>subprocess.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/utils/temp_dir.py'>temp_dir.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/utils/unpacking.py'>unpacking.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/utils/urls.py'>urls.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/utils/virtualenv.py'>virtualenv.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/utils/wheel.py'>wheel.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/utils/_jaraco_text.py'>_jaraco_text.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/utils/_log.py'>_log.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
											<!-- vcs Submodule -->
											<details>
												<summary><b>vcs</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.pip._internal.vcs</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/vcs/bazaar.py'>bazaar.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/vcs/git.py'>git.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/vcs/mercurial.py'>mercurial.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/vcs/subversion.py'>subversion.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_internal/vcs/versioncontrol.py'>versioncontrol.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
										</blockquote>
									</details>
									<!-- _vendor Submodule -->
									<details>
										<summary><b>_vendor</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.pip._vendor</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/vendor.txt'>vendor.txt</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
											<!-- cachecontrol Submodule -->
											<details>
												<summary><b>cachecontrol</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.pip._vendor.cachecontrol</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/cachecontrol/adapter.py'>adapter.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/cachecontrol/cache.py'>cache.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/cachecontrol/controller.py'>controller.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/cachecontrol/filewrapper.py'>filewrapper.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/cachecontrol/heuristics.py'>heuristics.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/cachecontrol/py.typed'>py.typed</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/cachecontrol/serialize.py'>serialize.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/cachecontrol/wrapper.py'>wrapper.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/cachecontrol/_cmd.py'>_cmd.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
													<!-- caches Submodule -->
													<details>
														<summary><b>caches</b></summary>
														<blockquote>
															<div class='directory-path' style='padding: 8px 0; color: #666;'>
																<code><b>⦿ venv.Lib.site-packages.pip._vendor.cachecontrol.caches</b></code>
															<table style='width: 100%; border-collapse: collapse;'>
															<thead>
																<tr style='background-color: #f8f9fa;'>
																	<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																	<th style='text-align: left; padding: 8px;'>Summary</th>
																</tr>
															</thead>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/cachecontrol/caches/file_cache.py'>file_cache.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/cachecontrol/caches/redis_cache.py'>redis_cache.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
															</table>
														</blockquote>
													</details>
												</blockquote>
											</details>
											<!-- certifi Submodule -->
											<details>
												<summary><b>certifi</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.pip._vendor.certifi</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/certifi/core.py'>core.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/certifi/py.typed'>py.typed</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/certifi/__main__.py'>__main__.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
											<!-- dependency_groups Submodule -->
											<details>
												<summary><b>dependency_groups</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.pip._vendor.dependency_groups</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/dependency_groups/py.typed'>py.typed</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/dependency_groups/_implementation.py'>_implementation.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/dependency_groups/_lint_dependency_groups.py'>_lint_dependency_groups.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/dependency_groups/_pip_wrapper.py'>_pip_wrapper.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/dependency_groups/_toml_compat.py'>_toml_compat.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/dependency_groups/__main__.py'>__main__.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
											<!-- distlib Submodule -->
											<details>
												<summary><b>distlib</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.pip._vendor.distlib</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/distlib/compat.py'>compat.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/distlib/resources.py'>resources.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/distlib/scripts.py'>scripts.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/distlib/util.py'>util.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
											<!-- distro Submodule -->
											<details>
												<summary><b>distro</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.pip._vendor.distro</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/distro/distro.py'>distro.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/distro/py.typed'>py.typed</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/distro/__main__.py'>__main__.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
											<!-- idna Submodule -->
											<details>
												<summary><b>idna</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.pip._vendor.idna</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/idna/codec.py'>codec.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/idna/compat.py'>compat.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/idna/core.py'>core.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/idna/idnadata.py'>idnadata.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/idna/intranges.py'>intranges.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/idna/package_data.py'>package_data.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/idna/py.typed'>py.typed</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/idna/uts46data.py'>uts46data.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
											<!-- msgpack Submodule -->
											<details>
												<summary><b>msgpack</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.pip._vendor.msgpack</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/msgpack/exceptions.py'>exceptions.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/msgpack/ext.py'>ext.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/msgpack/fallback.py'>fallback.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
											<!-- packaging Submodule -->
											<details>
												<summary><b>packaging</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.pip._vendor.packaging</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/packaging/markers.py'>markers.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/packaging/metadata.py'>metadata.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/packaging/py.typed'>py.typed</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/packaging/requirements.py'>requirements.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/packaging/specifiers.py'>specifiers.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/packaging/tags.py'>tags.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/packaging/utils.py'>utils.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/packaging/version.py'>version.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/packaging/_elffile.py'>_elffile.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/packaging/_manylinux.py'>_manylinux.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/packaging/_musllinux.py'>_musllinux.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/packaging/_parser.py'>_parser.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/packaging/_structures.py'>_structures.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/packaging/_tokenizer.py'>_tokenizer.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
													<!-- licenses Submodule -->
													<details>
														<summary><b>licenses</b></summary>
														<blockquote>
															<div class='directory-path' style='padding: 8px 0; color: #666;'>
																<code><b>⦿ venv.Lib.site-packages.pip._vendor.packaging.licenses</b></code>
															<table style='width: 100%; border-collapse: collapse;'>
															<thead>
																<tr style='background-color: #f8f9fa;'>
																	<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																	<th style='text-align: left; padding: 8px;'>Summary</th>
																</tr>
															</thead>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/packaging/licenses/_spdx.py'>_spdx.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
															</table>
														</blockquote>
													</details>
												</blockquote>
											</details>
											<!-- platformdirs Submodule -->
											<details>
												<summary><b>platformdirs</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.pip._vendor.platformdirs</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/platformdirs/android.py'>android.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/platformdirs/api.py'>api.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/platformdirs/macos.py'>macos.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/platformdirs/py.typed'>py.typed</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/platformdirs/unix.py'>unix.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/platformdirs/version.py'>version.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/platformdirs/windows.py'>windows.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/platformdirs/__main__.py'>__main__.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
											<!-- pygments Submodule -->
											<details>
												<summary><b>pygments</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.pip._vendor.pygments</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/pygments/console.py'>console.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/pygments/filter.py'>filter.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/pygments/formatter.py'>formatter.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/pygments/lexer.py'>lexer.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/pygments/modeline.py'>modeline.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/pygments/plugin.py'>plugin.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/pygments/regexopt.py'>regexopt.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/pygments/scanner.py'>scanner.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/pygments/sphinxext.py'>sphinxext.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/pygments/style.py'>style.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/pygments/token.py'>token.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/pygments/unistring.py'>unistring.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/pygments/util.py'>util.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/pygments/__main__.py'>__main__.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
													<!-- formatters Submodule -->
													<details>
														<summary><b>formatters</b></summary>
														<blockquote>
															<div class='directory-path' style='padding: 8px 0; color: #666;'>
																<code><b>⦿ venv.Lib.site-packages.pip._vendor.pygments.formatters</b></code>
															<table style='width: 100%; border-collapse: collapse;'>
															<thead>
																<tr style='background-color: #f8f9fa;'>
																	<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																	<th style='text-align: left; padding: 8px;'>Summary</th>
																</tr>
															</thead>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/pygments/formatters/_mapping.py'>_mapping.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
															</table>
														</blockquote>
													</details>
													<!-- lexers Submodule -->
													<details>
														<summary><b>lexers</b></summary>
														<blockquote>
															<div class='directory-path' style='padding: 8px 0; color: #666;'>
																<code><b>⦿ venv.Lib.site-packages.pip._vendor.pygments.lexers</b></code>
															<table style='width: 100%; border-collapse: collapse;'>
															<thead>
																<tr style='background-color: #f8f9fa;'>
																	<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																	<th style='text-align: left; padding: 8px;'>Summary</th>
																</tr>
															</thead>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/pygments/lexers/python.py'>python.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/pygments/lexers/_mapping.py'>_mapping.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
															</table>
														</blockquote>
													</details>
													<!-- styles Submodule -->
													<details>
														<summary><b>styles</b></summary>
														<blockquote>
															<div class='directory-path' style='padding: 8px 0; color: #666;'>
																<code><b>⦿ venv.Lib.site-packages.pip._vendor.pygments.styles</b></code>
															<table style='width: 100%; border-collapse: collapse;'>
															<thead>
																<tr style='background-color: #f8f9fa;'>
																	<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																	<th style='text-align: left; padding: 8px;'>Summary</th>
																</tr>
															</thead>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/pygments/styles/_mapping.py'>_mapping.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
															</table>
														</blockquote>
													</details>
												</blockquote>
											</details>
											<!-- pyproject_hooks Submodule -->
											<details>
												<summary><b>pyproject_hooks</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.pip._vendor.pyproject_hooks</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/pyproject_hooks/py.typed'>py.typed</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/pyproject_hooks/_impl.py'>_impl.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
													<!-- _in_process Submodule -->
													<details>
														<summary><b>_in_process</b></summary>
														<blockquote>
															<div class='directory-path' style='padding: 8px 0; color: #666;'>
																<code><b>⦿ venv.Lib.site-packages.pip._vendor.pyproject_hooks._in_process</b></code>
															<table style='width: 100%; border-collapse: collapse;'>
															<thead>
																<tr style='background-color: #f8f9fa;'>
																	<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																	<th style='text-align: left; padding: 8px;'>Summary</th>
																</tr>
															</thead>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/pyproject_hooks/_in_process/_in_process.py'>_in_process.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
															</table>
														</blockquote>
													</details>
												</blockquote>
											</details>
											<!-- requests Submodule -->
											<details>
												<summary><b>requests</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.pip._vendor.requests</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/requests/adapters.py'>adapters.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/requests/api.py'>api.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/requests/auth.py'>auth.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/requests/certs.py'>certs.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/requests/compat.py'>compat.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/requests/cookies.py'>cookies.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/requests/exceptions.py'>exceptions.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/requests/help.py'>help.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/requests/hooks.py'>hooks.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/requests/models.py'>models.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/requests/packages.py'>packages.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/requests/sessions.py'>sessions.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/requests/status_codes.py'>status_codes.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/requests/structures.py'>structures.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/requests/utils.py'>utils.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/requests/_internal_utils.py'>_internal_utils.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/requests/__version__.py'>__version__.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
											<!-- resolvelib Submodule -->
											<details>
												<summary><b>resolvelib</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.pip._vendor.resolvelib</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/resolvelib/providers.py'>providers.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/resolvelib/py.typed'>py.typed</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/resolvelib/reporters.py'>reporters.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/resolvelib/structs.py'>structs.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
													<!-- resolvers Submodule -->
													<details>
														<summary><b>resolvers</b></summary>
														<blockquote>
															<div class='directory-path' style='padding: 8px 0; color: #666;'>
																<code><b>⦿ venv.Lib.site-packages.pip._vendor.resolvelib.resolvers</b></code>
															<table style='width: 100%; border-collapse: collapse;'>
															<thead>
																<tr style='background-color: #f8f9fa;'>
																	<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																	<th style='text-align: left; padding: 8px;'>Summary</th>
																</tr>
															</thead>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/resolvelib/resolvers/abstract.py'>abstract.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/resolvelib/resolvers/criterion.py'>criterion.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/resolvelib/resolvers/exceptions.py'>exceptions.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/resolvelib/resolvers/resolution.py'>resolution.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
															</table>
														</blockquote>
													</details>
												</blockquote>
											</details>
											<!-- rich Submodule -->
											<details>
												<summary><b>rich</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.pip._vendor.rich</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/abc.py'>abc.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/align.py'>align.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/ansi.py'>ansi.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/bar.py'>bar.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/box.py'>box.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/cells.py'>cells.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/color.py'>color.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/color_triplet.py'>color_triplet.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/columns.py'>columns.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/console.py'>console.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/constrain.py'>constrain.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/containers.py'>containers.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/control.py'>control.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/default_styles.py'>default_styles.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/diagnose.py'>diagnose.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/emoji.py'>emoji.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/errors.py'>errors.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/filesize.py'>filesize.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/file_proxy.py'>file_proxy.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/highlighter.py'>highlighter.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/json.py'>json.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/jupyter.py'>jupyter.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/layout.py'>layout.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/live.py'>live.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/live_render.py'>live_render.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/logging.py'>logging.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/markup.py'>markup.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/measure.py'>measure.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/padding.py'>padding.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/pager.py'>pager.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/palette.py'>palette.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/panel.py'>panel.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/pretty.py'>pretty.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/progress.py'>progress.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/progress_bar.py'>progress_bar.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/prompt.py'>prompt.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/protocol.py'>protocol.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/py.typed'>py.typed</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/region.py'>region.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/repr.py'>repr.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/rule.py'>rule.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/scope.py'>scope.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/screen.py'>screen.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/segment.py'>segment.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/spinner.py'>spinner.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/status.py'>status.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/style.py'>style.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/styled.py'>styled.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/syntax.py'>syntax.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/table.py'>table.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/terminal_theme.py'>terminal_theme.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/text.py'>text.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/theme.py'>theme.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/themes.py'>themes.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/traceback.py'>traceback.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/tree.py'>tree.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/_cell_widths.py'>_cell_widths.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/_emoji_codes.py'>_emoji_codes.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/_emoji_replace.py'>_emoji_replace.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/_export_format.py'>_export_format.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/_extension.py'>_extension.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/_fileno.py'>_fileno.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/_inspect.py'>_inspect.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/_log_render.py'>_log_render.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/_loop.py'>_loop.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/_null_file.py'>_null_file.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/_palettes.py'>_palettes.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/_pick.py'>_pick.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/_ratio.py'>_ratio.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/_spinners.py'>_spinners.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/_stack.py'>_stack.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/_timer.py'>_timer.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/_win32_console.py'>_win32_console.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/_windows.py'>_windows.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/_windows_renderer.py'>_windows_renderer.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/_wrap.py'>_wrap.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/rich/__main__.py'>__main__.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
											<!-- tomli Submodule -->
											<details>
												<summary><b>tomli</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.pip._vendor.tomli</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/tomli/py.typed'>py.typed</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/tomli/_parser.py'>_parser.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/tomli/_re.py'>_re.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/tomli/_types.py'>_types.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
											<!-- tomli_w Submodule -->
											<details>
												<summary><b>tomli_w</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.pip._vendor.tomli_w</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/tomli_w/py.typed'>py.typed</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/tomli_w/_writer.py'>_writer.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
											<!-- truststore Submodule -->
											<details>
												<summary><b>truststore</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.pip._vendor.truststore</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/truststore/py.typed'>py.typed</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/truststore/_api.py'>_api.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/truststore/_macos.py'>_macos.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/truststore/_openssl.py'>_openssl.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/truststore/_ssl_constants.py'>_ssl_constants.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/truststore/_windows.py'>_windows.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
											<!-- urllib3 Submodule -->
											<details>
												<summary><b>urllib3</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.pip._vendor.urllib3</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/urllib3/connection.py'>connection.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/urllib3/connectionpool.py'>connectionpool.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/urllib3/exceptions.py'>exceptions.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/urllib3/fields.py'>fields.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/urllib3/filepost.py'>filepost.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/urllib3/poolmanager.py'>poolmanager.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/urllib3/request.py'>request.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/urllib3/response.py'>response.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/urllib3/_collections.py'>_collections.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/urllib3/_version.py'>_version.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
													<!-- contrib Submodule -->
													<details>
														<summary><b>contrib</b></summary>
														<blockquote>
															<div class='directory-path' style='padding: 8px 0; color: #666;'>
																<code><b>⦿ venv.Lib.site-packages.pip._vendor.urllib3.contrib</b></code>
															<table style='width: 100%; border-collapse: collapse;'>
															<thead>
																<tr style='background-color: #f8f9fa;'>
																	<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																	<th style='text-align: left; padding: 8px;'>Summary</th>
																</tr>
															</thead>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/urllib3/contrib/appengine.py'>appengine.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/urllib3/contrib/ntlmpool.py'>ntlmpool.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/urllib3/contrib/pyopenssl.py'>pyopenssl.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/urllib3/contrib/securetransport.py'>securetransport.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/urllib3/contrib/socks.py'>socks.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/urllib3/contrib/_appengine_environ.py'>_appengine_environ.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
															</table>
															<!-- _securetransport Submodule -->
															<details>
																<summary><b>_securetransport</b></summary>
																<blockquote>
																	<div class='directory-path' style='padding: 8px 0; color: #666;'>
																		<code><b>⦿ venv.Lib.site-packages.pip._vendor.urllib3.contrib._securetransport</b></code>
																	<table style='width: 100%; border-collapse: collapse;'>
																	<thead>
																		<tr style='background-color: #f8f9fa;'>
																			<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																			<th style='text-align: left; padding: 8px;'>Summary</th>
																		</tr>
																	</thead>
																		<tr style='border-bottom: 1px solid #eee;'>
																			<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/urllib3/contrib/_securetransport/bindings.py'>bindings.py</a></b></td>
																			<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																		</tr>
																		<tr style='border-bottom: 1px solid #eee;'>
																			<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/urllib3/contrib/_securetransport/low_level.py'>low_level.py</a></b></td>
																			<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																		</tr>
																	</table>
																</blockquote>
															</details>
														</blockquote>
													</details>
													<!-- packages Submodule -->
													<details>
														<summary><b>packages</b></summary>
														<blockquote>
															<div class='directory-path' style='padding: 8px 0; color: #666;'>
																<code><b>⦿ venv.Lib.site-packages.pip._vendor.urllib3.packages</b></code>
															<table style='width: 100%; border-collapse: collapse;'>
															<thead>
																<tr style='background-color: #f8f9fa;'>
																	<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																	<th style='text-align: left; padding: 8px;'>Summary</th>
																</tr>
															</thead>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/urllib3/packages/six.py'>six.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
															</table>
															<!-- backports Submodule -->
															<details>
																<summary><b>backports</b></summary>
																<blockquote>
																	<div class='directory-path' style='padding: 8px 0; color: #666;'>
																		<code><b>⦿ venv.Lib.site-packages.pip._vendor.urllib3.packages.backports</b></code>
																	<table style='width: 100%; border-collapse: collapse;'>
																	<thead>
																		<tr style='background-color: #f8f9fa;'>
																			<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																			<th style='text-align: left; padding: 8px;'>Summary</th>
																		</tr>
																	</thead>
																		<tr style='border-bottom: 1px solid #eee;'>
																			<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/urllib3/packages/backports/makefile.py'>makefile.py</a></b></td>
																			<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																		</tr>
																		<tr style='border-bottom: 1px solid #eee;'>
																			<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/urllib3/packages/backports/weakref_finalize.py'>weakref_finalize.py</a></b></td>
																			<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																		</tr>
																	</table>
																</blockquote>
															</details>
														</blockquote>
													</details>
													<!-- util Submodule -->
													<details>
														<summary><b>util</b></summary>
														<blockquote>
															<div class='directory-path' style='padding: 8px 0; color: #666;'>
																<code><b>⦿ venv.Lib.site-packages.pip._vendor.urllib3.util</b></code>
															<table style='width: 100%; border-collapse: collapse;'>
															<thead>
																<tr style='background-color: #f8f9fa;'>
																	<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																	<th style='text-align: left; padding: 8px;'>Summary</th>
																</tr>
															</thead>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/urllib3/util/connection.py'>connection.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/urllib3/util/proxy.py'>proxy.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/urllib3/util/queue.py'>queue.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/urllib3/util/request.py'>request.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/urllib3/util/response.py'>response.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/urllib3/util/retry.py'>retry.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/urllib3/util/ssltransport.py'>ssltransport.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/urllib3/util/ssl_.py'>ssl_.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/urllib3/util/ssl_match_hostname.py'>ssl_match_hostname.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/urllib3/util/timeout.py'>timeout.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/urllib3/util/url.py'>url.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip/_vendor/urllib3/util/wait.py'>wait.py</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
															</table>
														</blockquote>
													</details>
												</blockquote>
											</details>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<!-- pip-25.2.dist-info Submodule -->
							<details>
								<summary><b>pip-25.2.dist-info</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.pip-25.2.dist-info</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip-25.2.dist-info/entry_points.txt'>entry_points.txt</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip-25.2.dist-info/INSTALLER'>INSTALLER</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip-25.2.dist-info/METADATA'>METADATA</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip-25.2.dist-info/RECORD'>RECORD</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip-25.2.dist-info/REQUESTED'>REQUESTED</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip-25.2.dist-info/top_level.txt'>top_level.txt</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip-25.2.dist-info/WHEEL'>WHEEL</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
									<!-- licenses Submodule -->
									<details>
										<summary><b>licenses</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.pip-25.2.dist-info.licenses</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip-25.2.dist-info/licenses/AUTHORS.txt'>AUTHORS.txt</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip-25.2.dist-info/licenses/LICENSE.txt'>LICENSE.txt</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
											<!-- src Submodule -->
											<details>
												<summary><b>src</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.pip-25.2.dist-info.licenses.src</b></code>
													<!-- pip Submodule -->
													<details>
														<summary><b>pip</b></summary>
														<blockquote>
															<div class='directory-path' style='padding: 8px 0; color: #666;'>
																<code><b>⦿ venv.Lib.site-packages.pip-25.2.dist-info.licenses.src.pip</b></code>
															<!-- _vendor Submodule -->
															<details>
																<summary><b>_vendor</b></summary>
																<blockquote>
																	<div class='directory-path' style='padding: 8px 0; color: #666;'>
																		<code><b>⦿ venv.Lib.site-packages.pip-25.2.dist-info.licenses.src.pip._vendor</b></code>
																	<!-- cachecontrol Submodule -->
																	<details>
																		<summary><b>cachecontrol</b></summary>
																		<blockquote>
																			<div class='directory-path' style='padding: 8px 0; color: #666;'>
																				<code><b>⦿ venv.Lib.site-packages.pip-25.2.dist-info.licenses.src.pip._vendor.cachecontrol</b></code>
																			<table style='width: 100%; border-collapse: collapse;'>
																			<thead>
																				<tr style='background-color: #f8f9fa;'>
																					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																					<th style='text-align: left; padding: 8px;'>Summary</th>
																				</tr>
																			</thead>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip-25.2.dist-info/licenses/src/pip/_vendor/cachecontrol/LICENSE.txt'>LICENSE.txt</a></b></td>
																					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																				</tr>
																			</table>
																		</blockquote>
																	</details>
																	<!-- certifi Submodule -->
																	<details>
																		<summary><b>certifi</b></summary>
																		<blockquote>
																			<div class='directory-path' style='padding: 8px 0; color: #666;'>
																				<code><b>⦿ venv.Lib.site-packages.pip-25.2.dist-info.licenses.src.pip._vendor.certifi</b></code>
																			<table style='width: 100%; border-collapse: collapse;'>
																			<thead>
																				<tr style='background-color: #f8f9fa;'>
																					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																					<th style='text-align: left; padding: 8px;'>Summary</th>
																				</tr>
																			</thead>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip-25.2.dist-info/licenses/src/pip/_vendor/certifi/LICENSE'>LICENSE</a></b></td>
																					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																				</tr>
																			</table>
																		</blockquote>
																	</details>
																	<!-- dependency_groups Submodule -->
																	<details>
																		<summary><b>dependency_groups</b></summary>
																		<blockquote>
																			<div class='directory-path' style='padding: 8px 0; color: #666;'>
																				<code><b>⦿ venv.Lib.site-packages.pip-25.2.dist-info.licenses.src.pip._vendor.dependency_groups</b></code>
																			<table style='width: 100%; border-collapse: collapse;'>
																			<thead>
																				<tr style='background-color: #f8f9fa;'>
																					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																					<th style='text-align: left; padding: 8px;'>Summary</th>
																				</tr>
																			</thead>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip-25.2.dist-info/licenses/src/pip/_vendor/dependency_groups/LICENSE.txt'>LICENSE.txt</a></b></td>
																					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																				</tr>
																			</table>
																		</blockquote>
																	</details>
																	<!-- distlib Submodule -->
																	<details>
																		<summary><b>distlib</b></summary>
																		<blockquote>
																			<div class='directory-path' style='padding: 8px 0; color: #666;'>
																				<code><b>⦿ venv.Lib.site-packages.pip-25.2.dist-info.licenses.src.pip._vendor.distlib</b></code>
																			<table style='width: 100%; border-collapse: collapse;'>
																			<thead>
																				<tr style='background-color: #f8f9fa;'>
																					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																					<th style='text-align: left; padding: 8px;'>Summary</th>
																				</tr>
																			</thead>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip-25.2.dist-info/licenses/src/pip/_vendor/distlib/LICENSE.txt'>LICENSE.txt</a></b></td>
																					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																				</tr>
																			</table>
																		</blockquote>
																	</details>
																	<!-- distro Submodule -->
																	<details>
																		<summary><b>distro</b></summary>
																		<blockquote>
																			<div class='directory-path' style='padding: 8px 0; color: #666;'>
																				<code><b>⦿ venv.Lib.site-packages.pip-25.2.dist-info.licenses.src.pip._vendor.distro</b></code>
																			<table style='width: 100%; border-collapse: collapse;'>
																			<thead>
																				<tr style='background-color: #f8f9fa;'>
																					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																					<th style='text-align: left; padding: 8px;'>Summary</th>
																				</tr>
																			</thead>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip-25.2.dist-info/licenses/src/pip/_vendor/distro/LICENSE'>LICENSE</a></b></td>
																					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																				</tr>
																			</table>
																		</blockquote>
																	</details>
																	<!-- msgpack Submodule -->
																	<details>
																		<summary><b>msgpack</b></summary>
																		<blockquote>
																			<div class='directory-path' style='padding: 8px 0; color: #666;'>
																				<code><b>⦿ venv.Lib.site-packages.pip-25.2.dist-info.licenses.src.pip._vendor.msgpack</b></code>
																			<table style='width: 100%; border-collapse: collapse;'>
																			<thead>
																				<tr style='background-color: #f8f9fa;'>
																					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																					<th style='text-align: left; padding: 8px;'>Summary</th>
																				</tr>
																			</thead>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip-25.2.dist-info/licenses/src/pip/_vendor/msgpack/COPYING'>COPYING</a></b></td>
																					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																				</tr>
																			</table>
																		</blockquote>
																	</details>
																	<!-- packaging Submodule -->
																	<details>
																		<summary><b>packaging</b></summary>
																		<blockquote>
																			<div class='directory-path' style='padding: 8px 0; color: #666;'>
																				<code><b>⦿ venv.Lib.site-packages.pip-25.2.dist-info.licenses.src.pip._vendor.packaging</b></code>
																			<table style='width: 100%; border-collapse: collapse;'>
																			<thead>
																				<tr style='background-color: #f8f9fa;'>
																					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																					<th style='text-align: left; padding: 8px;'>Summary</th>
																				</tr>
																			</thead>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip-25.2.dist-info/licenses/src/pip/_vendor/packaging/LICENSE'>LICENSE</a></b></td>
																					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																				</tr>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip-25.2.dist-info/licenses/src/pip/_vendor/packaging/LICENSE.APACHE'>LICENSE.APACHE</a></b></td>
																					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																				</tr>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip-25.2.dist-info/licenses/src/pip/_vendor/packaging/LICENSE.BSD'>LICENSE.BSD</a></b></td>
																					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																				</tr>
																			</table>
																		</blockquote>
																	</details>
																	<!-- pkg_resources Submodule -->
																	<details>
																		<summary><b>pkg_resources</b></summary>
																		<blockquote>
																			<div class='directory-path' style='padding: 8px 0; color: #666;'>
																				<code><b>⦿ venv.Lib.site-packages.pip-25.2.dist-info.licenses.src.pip._vendor.pkg_resources</b></code>
																			<table style='width: 100%; border-collapse: collapse;'>
																			<thead>
																				<tr style='background-color: #f8f9fa;'>
																					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																					<th style='text-align: left; padding: 8px;'>Summary</th>
																				</tr>
																			</thead>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip-25.2.dist-info/licenses/src/pip/_vendor/pkg_resources/LICENSE'>LICENSE</a></b></td>
																					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																				</tr>
																			</table>
																		</blockquote>
																	</details>
																	<!-- platformdirs Submodule -->
																	<details>
																		<summary><b>platformdirs</b></summary>
																		<blockquote>
																			<div class='directory-path' style='padding: 8px 0; color: #666;'>
																				<code><b>⦿ venv.Lib.site-packages.pip-25.2.dist-info.licenses.src.pip._vendor.platformdirs</b></code>
																			<table style='width: 100%; border-collapse: collapse;'>
																			<thead>
																				<tr style='background-color: #f8f9fa;'>
																					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																					<th style='text-align: left; padding: 8px;'>Summary</th>
																				</tr>
																			</thead>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip-25.2.dist-info/licenses/src/pip/_vendor/platformdirs/LICENSE'>LICENSE</a></b></td>
																					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																				</tr>
																			</table>
																		</blockquote>
																	</details>
																	<!-- pygments Submodule -->
																	<details>
																		<summary><b>pygments</b></summary>
																		<blockquote>
																			<div class='directory-path' style='padding: 8px 0; color: #666;'>
																				<code><b>⦿ venv.Lib.site-packages.pip-25.2.dist-info.licenses.src.pip._vendor.pygments</b></code>
																			<table style='width: 100%; border-collapse: collapse;'>
																			<thead>
																				<tr style='background-color: #f8f9fa;'>
																					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																					<th style='text-align: left; padding: 8px;'>Summary</th>
																				</tr>
																			</thead>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip-25.2.dist-info/licenses/src/pip/_vendor/pygments/LICENSE'>LICENSE</a></b></td>
																					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																				</tr>
																			</table>
																		</blockquote>
																	</details>
																	<!-- pyproject_hooks Submodule -->
																	<details>
																		<summary><b>pyproject_hooks</b></summary>
																		<blockquote>
																			<div class='directory-path' style='padding: 8px 0; color: #666;'>
																				<code><b>⦿ venv.Lib.site-packages.pip-25.2.dist-info.licenses.src.pip._vendor.pyproject_hooks</b></code>
																			<table style='width: 100%; border-collapse: collapse;'>
																			<thead>
																				<tr style='background-color: #f8f9fa;'>
																					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																					<th style='text-align: left; padding: 8px;'>Summary</th>
																				</tr>
																			</thead>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip-25.2.dist-info/licenses/src/pip/_vendor/pyproject_hooks/LICENSE'>LICENSE</a></b></td>
																					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																				</tr>
																			</table>
																		</blockquote>
																	</details>
																	<!-- requests Submodule -->
																	<details>
																		<summary><b>requests</b></summary>
																		<blockquote>
																			<div class='directory-path' style='padding: 8px 0; color: #666;'>
																				<code><b>⦿ venv.Lib.site-packages.pip-25.2.dist-info.licenses.src.pip._vendor.requests</b></code>
																			<table style='width: 100%; border-collapse: collapse;'>
																			<thead>
																				<tr style='background-color: #f8f9fa;'>
																					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																					<th style='text-align: left; padding: 8px;'>Summary</th>
																				</tr>
																			</thead>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip-25.2.dist-info/licenses/src/pip/_vendor/requests/LICENSE'>LICENSE</a></b></td>
																					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																				</tr>
																			</table>
																		</blockquote>
																	</details>
																	<!-- resolvelib Submodule -->
																	<details>
																		<summary><b>resolvelib</b></summary>
																		<blockquote>
																			<div class='directory-path' style='padding: 8px 0; color: #666;'>
																				<code><b>⦿ venv.Lib.site-packages.pip-25.2.dist-info.licenses.src.pip._vendor.resolvelib</b></code>
																			<table style='width: 100%; border-collapse: collapse;'>
																			<thead>
																				<tr style='background-color: #f8f9fa;'>
																					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																					<th style='text-align: left; padding: 8px;'>Summary</th>
																				</tr>
																			</thead>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip-25.2.dist-info/licenses/src/pip/_vendor/resolvelib/LICENSE'>LICENSE</a></b></td>
																					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																				</tr>
																			</table>
																		</blockquote>
																	</details>
																	<!-- rich Submodule -->
																	<details>
																		<summary><b>rich</b></summary>
																		<blockquote>
																			<div class='directory-path' style='padding: 8px 0; color: #666;'>
																				<code><b>⦿ venv.Lib.site-packages.pip-25.2.dist-info.licenses.src.pip._vendor.rich</b></code>
																			<table style='width: 100%; border-collapse: collapse;'>
																			<thead>
																				<tr style='background-color: #f8f9fa;'>
																					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																					<th style='text-align: left; padding: 8px;'>Summary</th>
																				</tr>
																			</thead>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip-25.2.dist-info/licenses/src/pip/_vendor/rich/LICENSE'>LICENSE</a></b></td>
																					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																				</tr>
																			</table>
																		</blockquote>
																	</details>
																	<!-- tomli Submodule -->
																	<details>
																		<summary><b>tomli</b></summary>
																		<blockquote>
																			<div class='directory-path' style='padding: 8px 0; color: #666;'>
																				<code><b>⦿ venv.Lib.site-packages.pip-25.2.dist-info.licenses.src.pip._vendor.tomli</b></code>
																			<table style='width: 100%; border-collapse: collapse;'>
																			<thead>
																				<tr style='background-color: #f8f9fa;'>
																					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																					<th style='text-align: left; padding: 8px;'>Summary</th>
																				</tr>
																			</thead>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip-25.2.dist-info/licenses/src/pip/_vendor/tomli/LICENSE'>LICENSE</a></b></td>
																					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																				</tr>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip-25.2.dist-info/licenses/src/pip/_vendor/tomli/LICENSE-HEADER'>LICENSE-HEADER</a></b></td>
																					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																				</tr>
																			</table>
																		</blockquote>
																	</details>
																	<!-- tomli_w Submodule -->
																	<details>
																		<summary><b>tomli_w</b></summary>
																		<blockquote>
																			<div class='directory-path' style='padding: 8px 0; color: #666;'>
																				<code><b>⦿ venv.Lib.site-packages.pip-25.2.dist-info.licenses.src.pip._vendor.tomli_w</b></code>
																			<table style='width: 100%; border-collapse: collapse;'>
																			<thead>
																				<tr style='background-color: #f8f9fa;'>
																					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																					<th style='text-align: left; padding: 8px;'>Summary</th>
																				</tr>
																			</thead>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip-25.2.dist-info/licenses/src/pip/_vendor/tomli_w/LICENSE'>LICENSE</a></b></td>
																					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																				</tr>
																			</table>
																		</blockquote>
																	</details>
																	<!-- truststore Submodule -->
																	<details>
																		<summary><b>truststore</b></summary>
																		<blockquote>
																			<div class='directory-path' style='padding: 8px 0; color: #666;'>
																				<code><b>⦿ venv.Lib.site-packages.pip-25.2.dist-info.licenses.src.pip._vendor.truststore</b></code>
																			<table style='width: 100%; border-collapse: collapse;'>
																			<thead>
																				<tr style='background-color: #f8f9fa;'>
																					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																					<th style='text-align: left; padding: 8px;'>Summary</th>
																				</tr>
																			</thead>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip-25.2.dist-info/licenses/src/pip/_vendor/truststore/LICENSE'>LICENSE</a></b></td>
																					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																				</tr>
																			</table>
																		</blockquote>
																	</details>
																	<!-- urllib3 Submodule -->
																	<details>
																		<summary><b>urllib3</b></summary>
																		<blockquote>
																			<div class='directory-path' style='padding: 8px 0; color: #666;'>
																				<code><b>⦿ venv.Lib.site-packages.pip-25.2.dist-info.licenses.src.pip._vendor.urllib3</b></code>
																			<table style='width: 100%; border-collapse: collapse;'>
																			<thead>
																				<tr style='background-color: #f8f9fa;'>
																					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																					<th style='text-align: left; padding: 8px;'>Summary</th>
																				</tr>
																			</thead>
																				<tr style='border-bottom: 1px solid #eee;'>
																					<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pip-25.2.dist-info/licenses/src/pip/_vendor/urllib3/LICENSE.txt'>LICENSE.txt</a></b></td>
																					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																				</tr>
																			</table>
																		</blockquote>
																	</details>
																</blockquote>
															</details>
														</blockquote>
													</details>
												</blockquote>
											</details>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<!-- pkg_resources Submodule -->
							<details>
								<summary><b>pkg_resources</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.pkg_resources</b></code>
									<!-- _vendor Submodule -->
									<details>
										<summary><b>_vendor</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.pkg_resources._vendor</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pkg_resources/_vendor/appdirs.py'>appdirs.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pkg_resources/_vendor/zipp.py'>zipp.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
											<!-- importlib_resources Submodule -->
											<details>
												<summary><b>importlib_resources</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.pkg_resources._vendor.importlib_resources</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pkg_resources/_vendor/importlib_resources/abc.py'>abc.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pkg_resources/_vendor/importlib_resources/readers.py'>readers.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pkg_resources/_vendor/importlib_resources/simple.py'>simple.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pkg_resources/_vendor/importlib_resources/_adapters.py'>_adapters.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pkg_resources/_vendor/importlib_resources/_common.py'>_common.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pkg_resources/_vendor/importlib_resources/_compat.py'>_compat.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pkg_resources/_vendor/importlib_resources/_itertools.py'>_itertools.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pkg_resources/_vendor/importlib_resources/_legacy.py'>_legacy.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
											<!-- jaraco Submodule -->
											<details>
												<summary><b>jaraco</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.pkg_resources._vendor.jaraco</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pkg_resources/_vendor/jaraco/context.py'>context.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pkg_resources/_vendor/jaraco/functools.py'>functools.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
											<!-- more_itertools Submodule -->
											<details>
												<summary><b>more_itertools</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.pkg_resources._vendor.more_itertools</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pkg_resources/_vendor/more_itertools/more.py'>more.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pkg_resources/_vendor/more_itertools/recipes.py'>recipes.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
											<!-- packaging Submodule -->
											<details>
												<summary><b>packaging</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.pkg_resources._vendor.packaging</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pkg_resources/_vendor/packaging/markers.py'>markers.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pkg_resources/_vendor/packaging/requirements.py'>requirements.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pkg_resources/_vendor/packaging/specifiers.py'>specifiers.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pkg_resources/_vendor/packaging/tags.py'>tags.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pkg_resources/_vendor/packaging/utils.py'>utils.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pkg_resources/_vendor/packaging/version.py'>version.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pkg_resources/_vendor/packaging/_manylinux.py'>_manylinux.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pkg_resources/_vendor/packaging/_musllinux.py'>_musllinux.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pkg_resources/_vendor/packaging/_structures.py'>_structures.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pkg_resources/_vendor/packaging/__about__.py'>__about__.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
											<!-- pyparsing Submodule -->
											<details>
												<summary><b>pyparsing</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.pkg_resources._vendor.pyparsing</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pkg_resources/_vendor/pyparsing/actions.py'>actions.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pkg_resources/_vendor/pyparsing/common.py'>common.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pkg_resources/_vendor/pyparsing/core.py'>core.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pkg_resources/_vendor/pyparsing/exceptions.py'>exceptions.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pkg_resources/_vendor/pyparsing/helpers.py'>helpers.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pkg_resources/_vendor/pyparsing/results.py'>results.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pkg_resources/_vendor/pyparsing/testing.py'>testing.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pkg_resources/_vendor/pyparsing/unicode.py'>unicode.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pkg_resources/_vendor/pyparsing/util.py'>util.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<!-- propcache Submodule -->
							<details>
								<summary><b>propcache</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.propcache</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/propcache/api.py'>api.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/propcache/py.typed'>py.typed</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/propcache/_helpers.py'>_helpers.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/propcache/_helpers_c.pyx'>_helpers_c.pyx</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/propcache/_helpers_py.py'>_helpers_py.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- propcache-0.3.2.dist-info Submodule -->
							<details>
								<summary><b>propcache-0.3.2.dist-info</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.propcache-0.3.2.dist-info</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/propcache-0.3.2.dist-info/INSTALLER'>INSTALLER</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/propcache-0.3.2.dist-info/METADATA'>METADATA</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/propcache-0.3.2.dist-info/RECORD'>RECORD</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/propcache-0.3.2.dist-info/top_level.txt'>top_level.txt</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/propcache-0.3.2.dist-info/WHEEL'>WHEEL</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
									<!-- licenses Submodule -->
									<details>
										<summary><b>licenses</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.propcache-0.3.2.dist-info.licenses</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/propcache-0.3.2.dist-info/licenses/LICENSE'>LICENSE</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/propcache-0.3.2.dist-info/licenses/NOTICE'>NOTICE</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<!-- pydantic Submodule -->
							<details>
								<summary><b>pydantic</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.pydantic</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/aliases.py'>aliases.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/alias_generators.py'>alias_generators.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/annotated_handlers.py'>annotated_handlers.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/class_validators.py'>class_validators.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/color.py'>color.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/config.py'>config.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/dataclasses.py'>dataclasses.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/datetime_parse.py'>datetime_parse.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/decorator.py'>decorator.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/env_settings.py'>env_settings.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/errors.py'>errors.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/error_wrappers.py'>error_wrappers.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/fields.py'>fields.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/functional_serializers.py'>functional_serializers.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/functional_validators.py'>functional_validators.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/generics.py'>generics.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/json.py'>json.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/json_schema.py'>json_schema.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/main.py'>main.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/mypy.py'>mypy.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/networks.py'>networks.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/parse.py'>parse.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/py.typed'>py.typed</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/root_model.py'>root_model.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/schema.py'>schema.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/tools.py'>tools.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/types.py'>types.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/type_adapter.py'>type_adapter.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/typing.py'>typing.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/utils.py'>utils.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/validate_call_decorator.py'>validate_call_decorator.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/validators.py'>validators.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/version.py'>version.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/warnings.py'>warnings.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/_migration.py'>_migration.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
									<!-- deprecated Submodule -->
									<details>
										<summary><b>deprecated</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.pydantic.deprecated</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/deprecated/class_validators.py'>class_validators.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/deprecated/config.py'>config.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/deprecated/copy_internals.py'>copy_internals.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/deprecated/decorator.py'>decorator.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/deprecated/json.py'>json.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/deprecated/parse.py'>parse.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/deprecated/tools.py'>tools.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
									<!-- experimental Submodule -->
									<details>
										<summary><b>experimental</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.pydantic.experimental</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/experimental/arguments_schema.py'>arguments_schema.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/experimental/pipeline.py'>pipeline.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
									<!-- plugin Submodule -->
									<details>
										<summary><b>plugin</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.pydantic.plugin</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/plugin/_loader.py'>_loader.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/plugin/_schema_validator.py'>_schema_validator.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
									<!-- v1 Submodule -->
									<details>
										<summary><b>v1</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.pydantic.v1</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/v1/annotated_types.py'>annotated_types.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/v1/class_validators.py'>class_validators.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/v1/color.py'>color.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/v1/config.py'>config.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/v1/dataclasses.py'>dataclasses.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/v1/datetime_parse.py'>datetime_parse.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/v1/decorator.py'>decorator.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/v1/env_settings.py'>env_settings.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/v1/errors.py'>errors.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/v1/error_wrappers.py'>error_wrappers.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/v1/fields.py'>fields.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/v1/generics.py'>generics.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/v1/json.py'>json.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/v1/main.py'>main.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/v1/mypy.py'>mypy.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/v1/networks.py'>networks.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/v1/parse.py'>parse.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/v1/py.typed'>py.typed</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/v1/schema.py'>schema.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/v1/tools.py'>tools.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/v1/types.py'>types.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/v1/typing.py'>typing.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/v1/utils.py'>utils.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/v1/validators.py'>validators.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/v1/version.py'>version.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/v1/_hypothesis_plugin.py'>_hypothesis_plugin.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
									<!-- _internal Submodule -->
									<details>
										<summary><b>_internal</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.pydantic._internal</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/_internal/_config.py'>_config.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/_internal/_core_metadata.py'>_core_metadata.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/_internal/_core_utils.py'>_core_utils.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/_internal/_dataclasses.py'>_dataclasses.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/_internal/_decorators.py'>_decorators.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/_internal/_decorators_v1.py'>_decorators_v1.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/_internal/_discriminated_union.py'>_discriminated_union.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/_internal/_docs_extraction.py'>_docs_extraction.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/_internal/_fields.py'>_fields.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/_internal/_forward_ref.py'>_forward_ref.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/_internal/_generate_schema.py'>_generate_schema.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/_internal/_generics.py'>_generics.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/_internal/_git.py'>_git.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/_internal/_import_utils.py'>_import_utils.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/_internal/_internal_dataclass.py'>_internal_dataclass.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/_internal/_known_annotated_metadata.py'>_known_annotated_metadata.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/_internal/_mock_val_ser.py'>_mock_val_ser.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/_internal/_model_construction.py'>_model_construction.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/_internal/_namespace_utils.py'>_namespace_utils.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/_internal/_repr.py'>_repr.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/_internal/_schema_gather.py'>_schema_gather.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/_internal/_schema_generation_shared.py'>_schema_generation_shared.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/_internal/_serializers.py'>_serializers.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/_internal/_signature.py'>_signature.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/_internal/_typing_extra.py'>_typing_extra.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/_internal/_utils.py'>_utils.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/_internal/_validate_call.py'>_validate_call.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic/_internal/_validators.py'>_validators.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<!-- pydantic-2.11.7.dist-info Submodule -->
							<details>
								<summary><b>pydantic-2.11.7.dist-info</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.pydantic-2.11.7.dist-info</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic-2.11.7.dist-info/INSTALLER'>INSTALLER</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic-2.11.7.dist-info/METADATA'>METADATA</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic-2.11.7.dist-info/RECORD'>RECORD</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic-2.11.7.dist-info/WHEEL'>WHEEL</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
									<!-- licenses Submodule -->
									<details>
										<summary><b>licenses</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.pydantic-2.11.7.dist-info.licenses</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic-2.11.7.dist-info/licenses/LICENSE'>LICENSE</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<!-- pydantic_core Submodule -->
							<details>
								<summary><b>pydantic_core</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.pydantic_core</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_core/core_schema.py'>core_schema.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_core/py.typed'>py.typed</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_core/_pydantic_core.pyi'>_pydantic_core.pyi</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- pydantic_core-2.33.2.dist-info Submodule -->
							<details>
								<summary><b>pydantic_core-2.33.2.dist-info</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.pydantic_core-2.33.2.dist-info</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_core-2.33.2.dist-info/INSTALLER'>INSTALLER</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_core-2.33.2.dist-info/METADATA'>METADATA</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_core-2.33.2.dist-info/RECORD'>RECORD</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_core-2.33.2.dist-info/WHEEL'>WHEEL</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
									<!-- licenses Submodule -->
									<details>
										<summary><b>licenses</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.pydantic_core-2.33.2.dist-info.licenses</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_core-2.33.2.dist-info/licenses/LICENSE'>LICENSE</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<!-- pydantic_extra_types Submodule -->
							<details>
								<summary><b>pydantic_extra_types</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.pydantic_extra_types</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_extra_types/color.py'>color.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_extra_types/coordinate.py'>coordinate.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_extra_types/country.py'>country.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_extra_types/currency_code.py'>currency_code.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_extra_types/domain.py'>domain.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_extra_types/epoch.py'>epoch.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_extra_types/isbn.py'>isbn.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_extra_types/language_code.py'>language_code.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_extra_types/mac_address.py'>mac_address.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_extra_types/mongo_object_id.py'>mongo_object_id.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_extra_types/path.py'>path.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_extra_types/payment.py'>payment.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_extra_types/pendulum_dt.py'>pendulum_dt.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_extra_types/phone_numbers.py'>phone_numbers.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_extra_types/py.typed'>py.typed</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_extra_types/routing_number.py'>routing_number.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_extra_types/s3.py'>s3.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_extra_types/script_code.py'>script_code.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_extra_types/semantic_version.py'>semantic_version.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_extra_types/semver.py'>semver.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_extra_types/timezone_name.py'>timezone_name.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_extra_types/ulid.py'>ulid.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- pydantic_extra_types-2.10.5.dist-info Submodule -->
							<details>
								<summary><b>pydantic_extra_types-2.10.5.dist-info</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.pydantic_extra_types-2.10.5.dist-info</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_extra_types-2.10.5.dist-info/INSTALLER'>INSTALLER</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_extra_types-2.10.5.dist-info/METADATA'>METADATA</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_extra_types-2.10.5.dist-info/RECORD'>RECORD</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_extra_types-2.10.5.dist-info/WHEEL'>WHEEL</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
									<!-- licenses Submodule -->
									<details>
										<summary><b>licenses</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.pydantic_extra_types-2.10.5.dist-info.licenses</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_extra_types-2.10.5.dist-info/licenses/LICENSE'>LICENSE</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<!-- pydantic_settings Submodule -->
							<details>
								<summary><b>pydantic_settings</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.pydantic_settings</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_settings/exceptions.py'>exceptions.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_settings/main.py'>main.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_settings/py.typed'>py.typed</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_settings/utils.py'>utils.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_settings/version.py'>version.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
									<!-- sources Submodule -->
									<details>
										<summary><b>sources</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.pydantic_settings.sources</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_settings/sources/base.py'>base.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_settings/sources/types.py'>types.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_settings/sources/utils.py'>utils.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
											<!-- providers Submodule -->
											<details>
												<summary><b>providers</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.pydantic_settings.sources.providers</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_settings/sources/providers/aws.py'>aws.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_settings/sources/providers/azure.py'>azure.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_settings/sources/providers/cli.py'>cli.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_settings/sources/providers/dotenv.py'>dotenv.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_settings/sources/providers/env.py'>env.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_settings/sources/providers/gcp.py'>gcp.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_settings/sources/providers/json.py'>json.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_settings/sources/providers/pyproject.py'>pyproject.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_settings/sources/providers/secrets.py'>secrets.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_settings/sources/providers/toml.py'>toml.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_settings/sources/providers/yaml.py'>yaml.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<!-- pydantic_settings-2.10.1.dist-info Submodule -->
							<details>
								<summary><b>pydantic_settings-2.10.1.dist-info</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.pydantic_settings-2.10.1.dist-info</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_settings-2.10.1.dist-info/INSTALLER'>INSTALLER</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_settings-2.10.1.dist-info/METADATA'>METADATA</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_settings-2.10.1.dist-info/RECORD'>RECORD</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_settings-2.10.1.dist-info/WHEEL'>WHEEL</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
									<!-- licenses Submodule -->
									<details>
										<summary><b>licenses</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.pydantic_settings-2.10.1.dist-info.licenses</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/pydantic_settings-2.10.1.dist-info/licenses/LICENSE'>LICENSE</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<!-- python_dotenv-1.1.1.dist-info Submodule -->
							<details>
								<summary><b>python_dotenv-1.1.1.dist-info</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.python_dotenv-1.1.1.dist-info</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/python_dotenv-1.1.1.dist-info/entry_points.txt'>entry_points.txt</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/python_dotenv-1.1.1.dist-info/INSTALLER'>INSTALLER</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/python_dotenv-1.1.1.dist-info/METADATA'>METADATA</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/python_dotenv-1.1.1.dist-info/RECORD'>RECORD</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/python_dotenv-1.1.1.dist-info/top_level.txt'>top_level.txt</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/python_dotenv-1.1.1.dist-info/WHEEL'>WHEEL</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
									<!-- licenses Submodule -->
									<details>
										<summary><b>licenses</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.python_dotenv-1.1.1.dist-info.licenses</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/python_dotenv-1.1.1.dist-info/licenses/LICENSE'>LICENSE</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<!-- PyYAML-6.0.2.dist-info Submodule -->
							<details>
								<summary><b>PyYAML-6.0.2.dist-info</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.PyYAML-6.0.2.dist-info</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/PyYAML-6.0.2.dist-info/INSTALLER'>INSTALLER</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/PyYAML-6.0.2.dist-info/LICENSE'>LICENSE</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/PyYAML-6.0.2.dist-info/METADATA'>METADATA</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/PyYAML-6.0.2.dist-info/RECORD'>RECORD</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/PyYAML-6.0.2.dist-info/top_level.txt'>top_level.txt</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/PyYAML-6.0.2.dist-info/WHEEL'>WHEEL</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- readmeai Submodule -->
							<details>
								<summary><b>readmeai</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.readmeai</b></code>
									<!-- cli Submodule -->
									<details>
										<summary><b>cli</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.readmeai.cli</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/cli/main.py'>main.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/cli/options.py'>options.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
									<!-- config Submodule -->
									<details>
										<summary><b>config</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.readmeai.config</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/config/settings.py'>settings.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
											<!-- settings Submodule -->
											<details>
												<summary><b>settings</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.readmeai.config.settings</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/config/settings/badge-list.toml'>badge-list.toml</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/config/settings/commands.toml'>commands.toml</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/config/settings/config.toml'>config.toml</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/config/settings/dev-setup.toml'>dev-setup.toml</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/config/settings/dev-tools.toml'>dev-tools.toml</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/config/settings/ignore-list.toml'>ignore-list.toml</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/config/settings/language-map.toml'>language-map.toml</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/config/settings/project-manifest.toml'>project-manifest.toml</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/config/settings/prompts.toml'>prompts.toml</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/config/settings/templates.toml'>templates.toml</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
													<!-- templates Submodule -->
													<details>
														<summary><b>templates</b></summary>
														<blockquote>
															<div class='directory-path' style='padding: 8px 0; color: #666;'>
																<code><b>⦿ venv.Lib.site-packages.readmeai.config.settings.templates</b></code>
															<table style='width: 100%; border-collapse: collapse;'>
															<thead>
																<tr style='background-color: #f8f9fa;'>
																	<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																	<th style='text-align: left; padding: 8px;'>Summary</th>
																</tr>
															</thead>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/config/settings/templates/banners.toml'>banners.toml</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/config/settings/templates/headers.toml'>headers.toml</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/config/settings/templates/quickstart.toml'>quickstart.toml</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
															</table>
														</blockquote>
													</details>
													<!-- themes Submodule -->
													<details>
														<summary><b>themes</b></summary>
														<blockquote>
															<div class='directory-path' style='padding: 8px 0; color: #666;'>
																<code><b>⦿ venv.Lib.site-packages.readmeai.config.settings.themes</b></code>
															<table style='width: 100%; border-collapse: collapse;'>
															<thead>
																<tr style='background-color: #f8f9fa;'>
																	<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
																	<th style='text-align: left; padding: 8px;'>Summary</th>
																</tr>
															</thead>
																<tr style='border-bottom: 1px solid #eee;'>
																	<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/config/settings/themes/emojis.yaml'>emojis.yaml</a></b></td>
																	<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
																</tr>
															</table>
														</blockquote>
													</details>
												</blockquote>
											</details>
										</blockquote>
									</details>
									<!-- core Submodule -->
									<details>
										<summary><b>core</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.readmeai.core</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/core/errors.py'>errors.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/core/logger.py'>logger.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/core/pipeline.py'>pipeline.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
									<!-- extractors Submodule -->
									<details>
										<summary><b>extractors</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.readmeai.extractors</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/extractors/analyzer.py'>analyzer.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/extractors/dependencies.py'>dependencies.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/extractors/metadata.py'>metadata.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/extractors/models.py'>models.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/extractors/tools.py'>tools.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
									<!-- generators Submodule -->
									<details>
										<summary><b>generators</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.readmeai.generators</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/generators/badges.py'>badges.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/generators/builder.py'>builder.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/generators/emojis.py'>emojis.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/generators/enums.py'>enums.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/generators/headers.py'>headers.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/generators/navigation.py'>navigation.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/generators/quickstart.py'>quickstart.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/generators/tables.py'>tables.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/generators/tree.py'>tree.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
											<!-- banners Submodule -->
											<details>
												<summary><b>banners</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.readmeai.generators.banners</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/generators/banners/ascii.py'>ascii.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/generators/banners/svg.py'>svg.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
											<!-- colors Submodule -->
											<details>
												<summary><b>colors</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.readmeai.generators.colors</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/generators/colors/converters.py'>converters.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/generators/colors/gradients.py'>gradients.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
										</blockquote>
									</details>
									<!-- models Submodule -->
									<details>
										<summary><b>models</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.readmeai.models</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/models/anthropic.py'>anthropic.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/models/base.py'>base.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/models/dalle.py'>dalle.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/models/enums.py'>enums.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/models/factory.py'>factory.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/models/gemini.py'>gemini.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/models/offline.py'>offline.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/models/openai.py'>openai.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/models/prompts.py'>prompts.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/models/tokens.py'>tokens.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
									<!-- parsers Submodule -->
									<details>
										<summary><b>parsers</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.readmeai.parsers</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/parsers/base.py'>base.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/parsers/cpp.py'>cpp.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/parsers/docker.py'>docker.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/parsers/factory.py'>factory.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/parsers/go.py'>go.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/parsers/gradle.py'>gradle.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/parsers/maven.py'>maven.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/parsers/npm.py'>npm.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/parsers/properties.py'>properties.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/parsers/python.py'>python.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/parsers/rust.py'>rust.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/parsers/swift.py'>swift.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
									<!-- postprocessor Submodule -->
									<details>
										<summary><b>postprocessor</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.readmeai.postprocessor</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/postprocessor/markdown_to_html.py'>markdown_to_html.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/postprocessor/response_cleaner.py'>response_cleaner.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
									<!-- preprocessor Submodule -->
									<details>
										<summary><b>preprocessor</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.readmeai.preprocessor</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/preprocessor/directory_cleaner.py'>directory_cleaner.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/preprocessor/document_cleaner.py'>document_cleaner.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/preprocessor/file_filter.py'>file_filter.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/preprocessor/ignore_handler.py'>ignore_handler.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
									<!-- retrievers Submodule -->
									<details>
										<summary><b>retrievers</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.readmeai.retrievers</b></code>
											<!-- git Submodule -->
											<details>
												<summary><b>git</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.readmeai.retrievers.git</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/retrievers/git/metadata.py'>metadata.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/retrievers/git/providers.py'>providers.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/retrievers/git/repository.py'>repository.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
										</blockquote>
									</details>
									<!-- utils Submodule -->
									<details>
										<summary><b>utils</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.readmeai.utils</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/utils/fetch_badges.py'>fetch_badges.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/utils/file_handler.py'>file_handler.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/utils/importer.py'>importer.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai/utils/resource_manager.py'>resource_manager.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<!-- readmeai-0.6.3.dist-info Submodule -->
							<details>
								<summary><b>readmeai-0.6.3.dist-info</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.readmeai-0.6.3.dist-info</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai-0.6.3.dist-info/entry_points.txt'>entry_points.txt</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai-0.6.3.dist-info/INSTALLER'>INSTALLER</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai-0.6.3.dist-info/LICENSE'>LICENSE</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai-0.6.3.dist-info/METADATA'>METADATA</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai-0.6.3.dist-info/RECORD'>RECORD</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai-0.6.3.dist-info/REQUESTED'>REQUESTED</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/readmeai-0.6.3.dist-info/WHEEL'>WHEEL</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- regex Submodule -->
							<details>
								<summary><b>regex</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.regex</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/regex/regex.py'>regex.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/regex/test_regex.py'>test_regex.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/regex/_regex_core.py'>_regex_core.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- regex-2025.7.34.dist-info Submodule -->
							<details>
								<summary><b>regex-2025.7.34.dist-info</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.regex-2025.7.34.dist-info</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/regex-2025.7.34.dist-info/INSTALLER'>INSTALLER</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/regex-2025.7.34.dist-info/METADATA'>METADATA</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/regex-2025.7.34.dist-info/RECORD'>RECORD</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/regex-2025.7.34.dist-info/top_level.txt'>top_level.txt</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/regex-2025.7.34.dist-info/WHEEL'>WHEEL</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
									<!-- licenses Submodule -->
									<details>
										<summary><b>licenses</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.regex-2025.7.34.dist-info.licenses</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/regex-2025.7.34.dist-info/licenses/LICENSE.txt'>LICENSE.txt</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<!-- requests Submodule -->
							<details>
								<summary><b>requests</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.requests</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/requests/adapters.py'>adapters.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/requests/api.py'>api.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/requests/auth.py'>auth.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/requests/certs.py'>certs.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/requests/compat.py'>compat.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/requests/cookies.py'>cookies.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/requests/exceptions.py'>exceptions.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/requests/help.py'>help.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/requests/hooks.py'>hooks.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/requests/models.py'>models.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/requests/packages.py'>packages.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/requests/sessions.py'>sessions.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/requests/status_codes.py'>status_codes.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/requests/structures.py'>structures.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/requests/utils.py'>utils.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/requests/_internal_utils.py'>_internal_utils.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/requests/__version__.py'>__version__.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- requests-2.32.5.dist-info Submodule -->
							<details>
								<summary><b>requests-2.32.5.dist-info</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.requests-2.32.5.dist-info</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/requests-2.32.5.dist-info/INSTALLER'>INSTALLER</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/requests-2.32.5.dist-info/METADATA'>METADATA</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/requests-2.32.5.dist-info/RECORD'>RECORD</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/requests-2.32.5.dist-info/top_level.txt'>top_level.txt</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/requests-2.32.5.dist-info/WHEEL'>WHEEL</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
									<!-- licenses Submodule -->
									<details>
										<summary><b>licenses</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.requests-2.32.5.dist-info.licenses</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/requests-2.32.5.dist-info/licenses/LICENSE'>LICENSE</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<!-- setuptools Submodule -->
							<details>
								<summary><b>setuptools</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.setuptools</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/archive_util.py'>archive_util.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/build_meta.py'>build_meta.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/depends.py'>depends.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/dep_util.py'>dep_util.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/discovery.py'>discovery.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/dist.py'>dist.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/errors.py'>errors.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/extension.py'>extension.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/glob.py'>glob.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/installer.py'>installer.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/launch.py'>launch.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/logging.py'>logging.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/monkey.py'>monkey.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/msvc.py'>msvc.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/namespaces.py'>namespaces.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/package_index.py'>package_index.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/py34compat.py'>py34compat.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/sandbox.py'>sandbox.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/script (dev).tmpl'>script (dev).tmpl</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/script.tmpl'>script.tmpl</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/unicode_utils.py'>unicode_utils.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/version.py'>version.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/wheel.py'>wheel.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/windows_support.py'>windows_support.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_deprecation_warning.py'>_deprecation_warning.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_entry_points.py'>_entry_points.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_imp.py'>_imp.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_importlib.py'>_importlib.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_itertools.py'>_itertools.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_path.py'>_path.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_reqs.py'>_reqs.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
									<!-- command Submodule -->
									<details>
										<summary><b>command</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.setuptools.command</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/command/alias.py'>alias.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/command/bdist_egg.py'>bdist_egg.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/command/bdist_rpm.py'>bdist_rpm.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/command/build.py'>build.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/command/build_clib.py'>build_clib.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/command/build_ext.py'>build_ext.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/command/build_py.py'>build_py.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/command/develop.py'>develop.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/command/dist_info.py'>dist_info.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/command/easy_install.py'>easy_install.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/command/editable_wheel.py'>editable_wheel.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/command/egg_info.py'>egg_info.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/command/install.py'>install.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/command/install_egg_info.py'>install_egg_info.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/command/install_lib.py'>install_lib.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/command/install_scripts.py'>install_scripts.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/command/launcher manifest.xml'>launcher manifest.xml</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/command/py36compat.py'>py36compat.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/command/register.py'>register.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/command/rotate.py'>rotate.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/command/saveopts.py'>saveopts.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/command/sdist.py'>sdist.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/command/setopt.py'>setopt.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/command/test.py'>test.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/command/upload.py'>upload.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/command/upload_docs.py'>upload_docs.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
									<!-- config Submodule -->
									<details>
										<summary><b>config</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.setuptools.config</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/config/expand.py'>expand.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/config/pyprojecttoml.py'>pyprojecttoml.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/config/setupcfg.py'>setupcfg.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/config/_apply_pyprojecttoml.py'>_apply_pyprojecttoml.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
											<!-- _validate_pyproject Submodule -->
											<details>
												<summary><b>_validate_pyproject</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.setuptools.config._validate_pyproject</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/config/_validate_pyproject/error_reporting.py'>error_reporting.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/config/_validate_pyproject/extra_validations.py'>extra_validations.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/config/_validate_pyproject/fastjsonschema_exceptions.py'>fastjsonschema_exceptions.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/config/_validate_pyproject/fastjsonschema_validations.py'>fastjsonschema_validations.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/config/_validate_pyproject/formats.py'>formats.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
										</blockquote>
									</details>
									<!-- _distutils Submodule -->
									<details>
										<summary><b>_distutils</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.setuptools._distutils</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_distutils/archive_util.py'>archive_util.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_distutils/bcppcompiler.py'>bcppcompiler.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_distutils/ccompiler.py'>ccompiler.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_distutils/cmd.py'>cmd.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_distutils/config.py'>config.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_distutils/core.py'>core.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_distutils/cygwinccompiler.py'>cygwinccompiler.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_distutils/debug.py'>debug.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_distutils/dep_util.py'>dep_util.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_distutils/dir_util.py'>dir_util.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_distutils/dist.py'>dist.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_distutils/errors.py'>errors.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_distutils/extension.py'>extension.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_distutils/fancy_getopt.py'>fancy_getopt.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_distutils/filelist.py'>filelist.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_distutils/file_util.py'>file_util.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_distutils/log.py'>log.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_distutils/msvc9compiler.py'>msvc9compiler.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_distutils/msvccompiler.py'>msvccompiler.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_distutils/py38compat.py'>py38compat.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_distutils/py39compat.py'>py39compat.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_distutils/spawn.py'>spawn.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_distutils/sysconfig.py'>sysconfig.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_distutils/text_file.py'>text_file.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_distutils/unixccompiler.py'>unixccompiler.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_distutils/util.py'>util.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_distutils/version.py'>version.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_distutils/versionpredicate.py'>versionpredicate.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_distutils/_collections.py'>_collections.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_distutils/_functools.py'>_functools.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_distutils/_macos_compat.py'>_macos_compat.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_distutils/_msvccompiler.py'>_msvccompiler.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
											<!-- command Submodule -->
											<details>
												<summary><b>command</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.setuptools._distutils.command</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_distutils/command/bdist.py'>bdist.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_distutils/command/bdist_dumb.py'>bdist_dumb.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_distutils/command/bdist_rpm.py'>bdist_rpm.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_distutils/command/build.py'>build.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_distutils/command/build_clib.py'>build_clib.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_distutils/command/build_ext.py'>build_ext.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_distutils/command/build_py.py'>build_py.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_distutils/command/build_scripts.py'>build_scripts.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_distutils/command/check.py'>check.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_distutils/command/clean.py'>clean.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_distutils/command/config.py'>config.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_distutils/command/install.py'>install.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_distutils/command/install_data.py'>install_data.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_distutils/command/install_egg_info.py'>install_egg_info.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_distutils/command/install_headers.py'>install_headers.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_distutils/command/install_lib.py'>install_lib.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_distutils/command/install_scripts.py'>install_scripts.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_distutils/command/py37compat.py'>py37compat.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_distutils/command/register.py'>register.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_distutils/command/sdist.py'>sdist.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_distutils/command/upload.py'>upload.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_distutils/command/_framework_compat.py'>_framework_compat.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
										</blockquote>
									</details>
									<!-- _vendor Submodule -->
									<details>
										<summary><b>_vendor</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.setuptools._vendor</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_vendor/ordered_set.py'>ordered_set.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_vendor/typing_extensions.py'>typing_extensions.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_vendor/zipp.py'>zipp.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
											<!-- importlib_metadata Submodule -->
											<details>
												<summary><b>importlib_metadata</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.setuptools._vendor.importlib_metadata</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_vendor/importlib_metadata/_adapters.py'>_adapters.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_vendor/importlib_metadata/_collections.py'>_collections.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_vendor/importlib_metadata/_compat.py'>_compat.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_vendor/importlib_metadata/_functools.py'>_functools.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_vendor/importlib_metadata/_itertools.py'>_itertools.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_vendor/importlib_metadata/_meta.py'>_meta.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_vendor/importlib_metadata/_text.py'>_text.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
											<!-- importlib_resources Submodule -->
											<details>
												<summary><b>importlib_resources</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.setuptools._vendor.importlib_resources</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_vendor/importlib_resources/abc.py'>abc.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_vendor/importlib_resources/readers.py'>readers.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_vendor/importlib_resources/simple.py'>simple.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_vendor/importlib_resources/_adapters.py'>_adapters.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_vendor/importlib_resources/_common.py'>_common.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_vendor/importlib_resources/_compat.py'>_compat.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_vendor/importlib_resources/_itertools.py'>_itertools.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_vendor/importlib_resources/_legacy.py'>_legacy.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
											<!-- jaraco Submodule -->
											<details>
												<summary><b>jaraco</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.setuptools._vendor.jaraco</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_vendor/jaraco/context.py'>context.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_vendor/jaraco/functools.py'>functools.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
											<!-- more_itertools Submodule -->
											<details>
												<summary><b>more_itertools</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.setuptools._vendor.more_itertools</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_vendor/more_itertools/more.py'>more.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_vendor/more_itertools/recipes.py'>recipes.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
											<!-- packaging Submodule -->
											<details>
												<summary><b>packaging</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.setuptools._vendor.packaging</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_vendor/packaging/markers.py'>markers.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_vendor/packaging/requirements.py'>requirements.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_vendor/packaging/specifiers.py'>specifiers.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_vendor/packaging/tags.py'>tags.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_vendor/packaging/utils.py'>utils.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_vendor/packaging/version.py'>version.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_vendor/packaging/_manylinux.py'>_manylinux.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_vendor/packaging/_musllinux.py'>_musllinux.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_vendor/packaging/_structures.py'>_structures.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_vendor/packaging/__about__.py'>__about__.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
											<!-- pyparsing Submodule -->
											<details>
												<summary><b>pyparsing</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.setuptools._vendor.pyparsing</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_vendor/pyparsing/actions.py'>actions.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_vendor/pyparsing/common.py'>common.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_vendor/pyparsing/core.py'>core.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_vendor/pyparsing/exceptions.py'>exceptions.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_vendor/pyparsing/helpers.py'>helpers.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_vendor/pyparsing/results.py'>results.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_vendor/pyparsing/testing.py'>testing.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_vendor/pyparsing/unicode.py'>unicode.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_vendor/pyparsing/util.py'>util.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
											<!-- tomli Submodule -->
											<details>
												<summary><b>tomli</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.setuptools._vendor.tomli</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_vendor/tomli/_parser.py'>_parser.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_vendor/tomli/_re.py'>_re.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools/_vendor/tomli/_types.py'>_types.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<!-- setuptools-65.5.0.dist-info Submodule -->
							<details>
								<summary><b>setuptools-65.5.0.dist-info</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.setuptools-65.5.0.dist-info</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools-65.5.0.dist-info/entry_points.txt'>entry_points.txt</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools-65.5.0.dist-info/INSTALLER'>INSTALLER</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools-65.5.0.dist-info/LICENSE'>LICENSE</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools-65.5.0.dist-info/METADATA'>METADATA</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools-65.5.0.dist-info/RECORD'>RECORD</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools-65.5.0.dist-info/REQUESTED'>REQUESTED</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools-65.5.0.dist-info/top_level.txt'>top_level.txt</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/setuptools-65.5.0.dist-info/WHEEL'>WHEEL</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- smmap Submodule -->
							<details>
								<summary><b>smmap</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.smmap</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/smmap/buf.py'>buf.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/smmap/mman.py'>mman.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/smmap/util.py'>util.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
									<!-- test Submodule -->
									<details>
										<summary><b>test</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.smmap.test</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/smmap/test/lib.py'>lib.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/smmap/test/test_buf.py'>test_buf.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/smmap/test/test_mman.py'>test_mman.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/smmap/test/test_tutorial.py'>test_tutorial.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/smmap/test/test_util.py'>test_util.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<!-- smmap-5.0.2.dist-info Submodule -->
							<details>
								<summary><b>smmap-5.0.2.dist-info</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.smmap-5.0.2.dist-info</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/smmap-5.0.2.dist-info/INSTALLER'>INSTALLER</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/smmap-5.0.2.dist-info/LICENSE'>LICENSE</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/smmap-5.0.2.dist-info/METADATA'>METADATA</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/smmap-5.0.2.dist-info/RECORD'>RECORD</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/smmap-5.0.2.dist-info/top_level.txt'>top_level.txt</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/smmap-5.0.2.dist-info/WHEEL'>WHEEL</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/smmap-5.0.2.dist-info/zip-safe'>zip-safe</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- sniffio Submodule -->
							<details>
								<summary><b>sniffio</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.sniffio</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/sniffio/py.typed'>py.typed</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/sniffio/_impl.py'>_impl.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/sniffio/_version.py'>_version.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
									<!-- _tests Submodule -->
									<details>
										<summary><b>_tests</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.sniffio._tests</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/sniffio/_tests/test_sniffio.py'>test_sniffio.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<!-- sniffio-1.3.1.dist-info Submodule -->
							<details>
								<summary><b>sniffio-1.3.1.dist-info</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.sniffio-1.3.1.dist-info</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/sniffio-1.3.1.dist-info/INSTALLER'>INSTALLER</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/sniffio-1.3.1.dist-info/LICENSE'>LICENSE</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/sniffio-1.3.1.dist-info/LICENSE.APACHE2'>LICENSE.APACHE2</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/sniffio-1.3.1.dist-info/LICENSE.MIT'>LICENSE.MIT</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/sniffio-1.3.1.dist-info/METADATA'>METADATA</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/sniffio-1.3.1.dist-info/RECORD'>RECORD</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/sniffio-1.3.1.dist-info/top_level.txt'>top_level.txt</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/sniffio-1.3.1.dist-info/WHEEL'>WHEEL</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- structlog Submodule -->
							<details>
								<summary><b>structlog</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.structlog</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/structlog/contextvars.py'>contextvars.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/structlog/dev.py'>dev.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/structlog/exceptions.py'>exceptions.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/structlog/processors.py'>processors.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/structlog/py.typed'>py.typed</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/structlog/stdlib.py'>stdlib.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/structlog/testing.py'>testing.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/structlog/threadlocal.py'>threadlocal.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/structlog/tracebacks.py'>tracebacks.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/structlog/twisted.py'>twisted.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/structlog/types.py'>types.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/structlog/typing.py'>typing.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/structlog/_base.py'>_base.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/structlog/_config.py'>_config.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/structlog/_frames.py'>_frames.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/structlog/_generic.py'>_generic.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/structlog/_greenlets.py'>_greenlets.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/structlog/_log_levels.py'>_log_levels.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/structlog/_native.py'>_native.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/structlog/_output.py'>_output.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/structlog/_utils.py'>_utils.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- structlog-24.4.0.dist-info Submodule -->
							<details>
								<summary><b>structlog-24.4.0.dist-info</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.structlog-24.4.0.dist-info</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/structlog-24.4.0.dist-info/INSTALLER'>INSTALLER</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/structlog-24.4.0.dist-info/METADATA'>METADATA</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/structlog-24.4.0.dist-info/RECORD'>RECORD</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/structlog-24.4.0.dist-info/WHEEL'>WHEEL</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
									<!-- licenses Submodule -->
									<details>
										<summary><b>licenses</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.structlog-24.4.0.dist-info.licenses</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/structlog-24.4.0.dist-info/licenses/LICENSE-APACHE'>LICENSE-APACHE</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/structlog-24.4.0.dist-info/licenses/LICENSE-MIT'>LICENSE-MIT</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/structlog-24.4.0.dist-info/licenses/NOTICE'>NOTICE</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<!-- tenacity Submodule -->
							<details>
								<summary><b>tenacity</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.tenacity</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tenacity/after.py'>after.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tenacity/before.py'>before.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tenacity/before_sleep.py'>before_sleep.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tenacity/nap.py'>nap.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tenacity/py.typed'>py.typed</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tenacity/retry.py'>retry.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tenacity/stop.py'>stop.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tenacity/tornadoweb.py'>tornadoweb.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tenacity/wait.py'>wait.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tenacity/_utils.py'>_utils.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
									<!-- asyncio Submodule -->
									<details>
										<summary><b>asyncio</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.tenacity.asyncio</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tenacity/asyncio/retry.py'>retry.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<!-- tenacity-8.5.0.dist-info Submodule -->
							<details>
								<summary><b>tenacity-8.5.0.dist-info</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.tenacity-8.5.0.dist-info</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tenacity-8.5.0.dist-info/INSTALLER'>INSTALLER</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tenacity-8.5.0.dist-info/LICENSE'>LICENSE</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tenacity-8.5.0.dist-info/METADATA'>METADATA</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tenacity-8.5.0.dist-info/RECORD'>RECORD</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tenacity-8.5.0.dist-info/top_level.txt'>top_level.txt</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tenacity-8.5.0.dist-info/WHEEL'>WHEEL</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- tiktoken Submodule -->
							<details>
								<summary><b>tiktoken</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.tiktoken</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tiktoken/core.py'>core.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tiktoken/load.py'>load.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tiktoken/model.py'>model.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tiktoken/py.typed'>py.typed</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tiktoken/registry.py'>registry.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- tiktoken-0.4.0.dist-info Submodule -->
							<details>
								<summary><b>tiktoken-0.4.0.dist-info</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.tiktoken-0.4.0.dist-info</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tiktoken-0.4.0.dist-info/INSTALLER'>INSTALLER</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tiktoken-0.4.0.dist-info/LICENSE'>LICENSE</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tiktoken-0.4.0.dist-info/METADATA'>METADATA</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tiktoken-0.4.0.dist-info/RECORD'>RECORD</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tiktoken-0.4.0.dist-info/top_level.txt'>top_level.txt</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tiktoken-0.4.0.dist-info/WHEEL'>WHEEL</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- tiktoken_ext Submodule -->
							<details>
								<summary><b>tiktoken_ext</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.tiktoken_ext</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tiktoken_ext/openai_public.py'>openai_public.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- tqdm Submodule -->
							<details>
								<summary><b>tqdm</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.tqdm</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tqdm/asyncio.py'>asyncio.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tqdm/auto.py'>auto.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tqdm/autonotebook.py'>autonotebook.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tqdm/cli.py'>cli.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tqdm/completion.sh'>completion.sh</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tqdm/dask.py'>dask.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tqdm/gui.py'>gui.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tqdm/keras.py'>keras.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tqdm/notebook.py'>notebook.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tqdm/rich.py'>rich.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tqdm/std.py'>std.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tqdm/tk.py'>tk.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tqdm/tqdm.1'>tqdm.1</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tqdm/utils.py'>utils.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tqdm/version.py'>version.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tqdm/_dist_ver.py'>_dist_ver.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tqdm/_main.py'>_main.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tqdm/_monitor.py'>_monitor.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tqdm/_tqdm.py'>_tqdm.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tqdm/_tqdm_gui.py'>_tqdm_gui.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tqdm/_tqdm_notebook.py'>_tqdm_notebook.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tqdm/_tqdm_pandas.py'>_tqdm_pandas.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tqdm/_utils.py'>_utils.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tqdm/__main__.py'>__main__.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
									<!-- contrib Submodule -->
									<details>
										<summary><b>contrib</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.tqdm.contrib</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tqdm/contrib/bells.py'>bells.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tqdm/contrib/concurrent.py'>concurrent.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tqdm/contrib/discord.py'>discord.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tqdm/contrib/itertools.py'>itertools.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tqdm/contrib/logging.py'>logging.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tqdm/contrib/slack.py'>slack.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tqdm/contrib/telegram.py'>telegram.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tqdm/contrib/utils_worker.py'>utils_worker.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<!-- tqdm-4.67.1.dist-info Submodule -->
							<details>
								<summary><b>tqdm-4.67.1.dist-info</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.tqdm-4.67.1.dist-info</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tqdm-4.67.1.dist-info/entry_points.txt'>entry_points.txt</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tqdm-4.67.1.dist-info/INSTALLER'>INSTALLER</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tqdm-4.67.1.dist-info/LICENCE'>LICENCE</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tqdm-4.67.1.dist-info/METADATA'>METADATA</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tqdm-4.67.1.dist-info/RECORD'>RECORD</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tqdm-4.67.1.dist-info/top_level.txt'>top_level.txt</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/tqdm-4.67.1.dist-info/WHEEL'>WHEEL</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- typing_extensions-4.15.0.dist-info Submodule -->
							<details>
								<summary><b>typing_extensions-4.15.0.dist-info</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.typing_extensions-4.15.0.dist-info</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/typing_extensions-4.15.0.dist-info/INSTALLER'>INSTALLER</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/typing_extensions-4.15.0.dist-info/METADATA'>METADATA</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/typing_extensions-4.15.0.dist-info/RECORD'>RECORD</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/typing_extensions-4.15.0.dist-info/WHEEL'>WHEEL</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
									<!-- licenses Submodule -->
									<details>
										<summary><b>licenses</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.typing_extensions-4.15.0.dist-info.licenses</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/typing_extensions-4.15.0.dist-info/licenses/LICENSE'>LICENSE</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<!-- typing_inspection Submodule -->
							<details>
								<summary><b>typing_inspection</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.typing_inspection</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/typing_inspection/introspection.py'>introspection.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/typing_inspection/py.typed'>py.typed</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/typing_inspection/typing_objects.py'>typing_objects.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/typing_inspection/typing_objects.pyi'>typing_objects.pyi</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- typing_inspection-0.4.1.dist-info Submodule -->
							<details>
								<summary><b>typing_inspection-0.4.1.dist-info</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.typing_inspection-0.4.1.dist-info</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/typing_inspection-0.4.1.dist-info/INSTALLER'>INSTALLER</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/typing_inspection-0.4.1.dist-info/METADATA'>METADATA</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/typing_inspection-0.4.1.dist-info/RECORD'>RECORD</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/typing_inspection-0.4.1.dist-info/WHEEL'>WHEEL</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
									<!-- licenses Submodule -->
									<details>
										<summary><b>licenses</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.typing_inspection-0.4.1.dist-info.licenses</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/typing_inspection-0.4.1.dist-info/licenses/LICENSE'>LICENSE</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<!-- urllib3 Submodule -->
							<details>
								<summary><b>urllib3</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.urllib3</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/urllib3/connection.py'>connection.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/urllib3/connectionpool.py'>connectionpool.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/urllib3/exceptions.py'>exceptions.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/urllib3/fields.py'>fields.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/urllib3/filepost.py'>filepost.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/urllib3/poolmanager.py'>poolmanager.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/urllib3/py.typed'>py.typed</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/urllib3/response.py'>response.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/urllib3/_base_connection.py'>_base_connection.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/urllib3/_collections.py'>_collections.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/urllib3/_request_methods.py'>_request_methods.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/urllib3/_version.py'>_version.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
									<!-- contrib Submodule -->
									<details>
										<summary><b>contrib</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.urllib3.contrib</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/urllib3/contrib/pyopenssl.py'>pyopenssl.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/urllib3/contrib/socks.py'>socks.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
											<!-- emscripten Submodule -->
											<details>
												<summary><b>emscripten</b></summary>
												<blockquote>
													<div class='directory-path' style='padding: 8px 0; color: #666;'>
														<code><b>⦿ venv.Lib.site-packages.urllib3.contrib.emscripten</b></code>
													<table style='width: 100%; border-collapse: collapse;'>
													<thead>
														<tr style='background-color: #f8f9fa;'>
															<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
															<th style='text-align: left; padding: 8px;'>Summary</th>
														</tr>
													</thead>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/urllib3/contrib/emscripten/connection.py'>connection.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/urllib3/contrib/emscripten/emscripten_fetch_worker.js'>emscripten_fetch_worker.js</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/urllib3/contrib/emscripten/fetch.py'>fetch.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/urllib3/contrib/emscripten/request.py'>request.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
														<tr style='border-bottom: 1px solid #eee;'>
															<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/urllib3/contrib/emscripten/response.py'>response.py</a></b></td>
															<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
														</tr>
													</table>
												</blockquote>
											</details>
										</blockquote>
									</details>
									<!-- http2 Submodule -->
									<details>
										<summary><b>http2</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.urllib3.http2</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/urllib3/http2/connection.py'>connection.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/urllib3/http2/probe.py'>probe.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
									<!-- util Submodule -->
									<details>
										<summary><b>util</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.urllib3.util</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/urllib3/util/connection.py'>connection.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/urllib3/util/proxy.py'>proxy.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/urllib3/util/request.py'>request.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/urllib3/util/response.py'>response.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/urllib3/util/retry.py'>retry.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/urllib3/util/ssltransport.py'>ssltransport.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/urllib3/util/ssl_.py'>ssl_.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/urllib3/util/ssl_match_hostname.py'>ssl_match_hostname.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/urllib3/util/timeout.py'>timeout.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/urllib3/util/url.py'>url.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/urllib3/util/util.py'>util.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/urllib3/util/wait.py'>wait.py</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<!-- urllib3-2.5.0.dist-info Submodule -->
							<details>
								<summary><b>urllib3-2.5.0.dist-info</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.urllib3-2.5.0.dist-info</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/urllib3-2.5.0.dist-info/INSTALLER'>INSTALLER</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/urllib3-2.5.0.dist-info/METADATA'>METADATA</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/urllib3-2.5.0.dist-info/RECORD'>RECORD</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/urllib3-2.5.0.dist-info/WHEEL'>WHEEL</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
									<!-- licenses Submodule -->
									<details>
										<summary><b>licenses</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.urllib3-2.5.0.dist-info.licenses</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/urllib3-2.5.0.dist-info/licenses/LICENSE.txt'>LICENSE.txt</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<!-- yaml Submodule -->
							<details>
								<summary><b>yaml</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.yaml</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/yaml/composer.py'>composer.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/yaml/constructor.py'>constructor.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/yaml/cyaml.py'>cyaml.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/yaml/dumper.py'>dumper.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/yaml/emitter.py'>emitter.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/yaml/error.py'>error.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/yaml/events.py'>events.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/yaml/loader.py'>loader.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/yaml/nodes.py'>nodes.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/yaml/parser.py'>parser.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/yaml/reader.py'>reader.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/yaml/representer.py'>representer.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/yaml/resolver.py'>resolver.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/yaml/scanner.py'>scanner.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/yaml/serializer.py'>serializer.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/yaml/tokens.py'>tokens.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- yarl Submodule -->
							<details>
								<summary><b>yarl</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.yarl</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/yarl/py.typed'>py.typed</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/yarl/_parse.py'>_parse.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/yarl/_path.py'>_path.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/yarl/_query.py'>_query.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/yarl/_quoters.py'>_quoters.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/yarl/_quoting.py'>_quoting.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/yarl/_quoting_c.pyx'>_quoting_c.pyx</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/yarl/_quoting_py.py'>_quoting_py.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/yarl/_url.py'>_url.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
							<!-- yarl-1.20.1.dist-info Submodule -->
							<details>
								<summary><b>yarl-1.20.1.dist-info</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages.yarl-1.20.1.dist-info</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/yarl-1.20.1.dist-info/INSTALLER'>INSTALLER</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/yarl-1.20.1.dist-info/METADATA'>METADATA</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/yarl-1.20.1.dist-info/RECORD'>RECORD</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/yarl-1.20.1.dist-info/top_level.txt'>top_level.txt</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/yarl-1.20.1.dist-info/WHEEL'>WHEEL</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
									<!-- licenses Submodule -->
									<details>
										<summary><b>licenses</b></summary>
										<blockquote>
											<div class='directory-path' style='padding: 8px 0; color: #666;'>
												<code><b>⦿ venv.Lib.site-packages.yarl-1.20.1.dist-info.licenses</b></code>
											<table style='width: 100%; border-collapse: collapse;'>
											<thead>
												<tr style='background-color: #f8f9fa;'>
													<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
													<th style='text-align: left; padding: 8px;'>Summary</th>
												</tr>
											</thead>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/yarl-1.20.1.dist-info/licenses/LICENSE'>LICENSE</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
												<tr style='border-bottom: 1px solid #eee;'>
													<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/yarl-1.20.1.dist-info/licenses/NOTICE'>NOTICE</a></b></td>
													<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
												</tr>
											</table>
										</blockquote>
									</details>
								</blockquote>
							</details>
							<!-- _distutils_hack Submodule -->
							<details>
								<summary><b>_distutils_hack</b></summary>
								<blockquote>
									<div class='directory-path' style='padding: 8px 0; color: #666;'>
										<code><b>⦿ venv.Lib.site-packages._distutils_hack</b></code>
									<table style='width: 100%; border-collapse: collapse;'>
									<thead>
										<tr style='background-color: #f8f9fa;'>
											<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
											<th style='text-align: left; padding: 8px;'>Summary</th>
										</tr>
									</thead>
										<tr style='border-bottom: 1px solid #eee;'>
											<td style='padding: 8px;'><b><a href='/venv/Lib/site-packages/_distutils_hack/override.py'>override.py</a></b></td>
											<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
										</tr>
									</table>
								</blockquote>
							</details>
						</blockquote>
					</details>
				</blockquote>
			</details>
			<!-- Scripts Submodule -->
			<details>
				<summary><b>Scripts</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ venv.Scripts</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='/venv/Scripts/activate'>activate</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='/venv/Scripts/activate.bat'>activate.bat</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='/venv/Scripts/Activate.ps1'>Activate.ps1</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='/venv/Scripts/deactivate.bat'>deactivate.bat</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<!-- Visualizer_csv Submodule -->
	<details>
		<summary><b>Visualizer_csv</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ Visualizer_csv</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='/Visualizer_csv/routes.py'>routes.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
			</table>
			<!-- controller Submodule -->
			<details>
				<summary><b>controller</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ Visualizer_csv.controller</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='/Visualizer_csv/controller/controller_analyst.py'>controller_analyst.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='/Visualizer_csv/controller/controller_cleaner.py'>controller_cleaner.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- services Submodule -->
			<details>
				<summary><b>services</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ Visualizer_csv.services</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='/Visualizer_csv/services/Analyse_csv.py'>Analyse_csv.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='/Visualizer_csv/services/execution_sql.py'>execution_sql.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='/Visualizer_csv/services/meta_data.py'>meta_data.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='/Visualizer_csv/services/pip_line_cleaner.py'>pip_line_cleaner.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<!-- Visualizer_DB Submodule -->
	<details>
		<summary><b>Visualizer_DB</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ Visualizer_DB</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='/Visualizer_DB/db_credentials.json'>db_credentials.json</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='/Visualizer_DB/routes.py'>routes.py</a></b></td>
					<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
				</tr>
			</table>
			<!-- controller Submodule -->
			<details>
				<summary><b>controller</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ Visualizer_DB.controller</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='/Visualizer_DB/controller/controller_save.py'>controller_save.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='/Visualizer_DB/controller/saveschemaMINIO.py'>saveschemaMINIO.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
			<!-- services Submodule -->
			<details>
				<summary><b>services</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ Visualizer_DB.services</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='/Visualizer_DB/services/ajoutNameJson.py'>ajoutNameJson.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='/Visualizer_DB/services/connectdb.py'>connectdb.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='/Visualizer_DB/services/elasticsearch.py'>elasticsearch.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='/Visualizer_DB/services/execute.py'>execute.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='/Visualizer_DB/services/fetch_save.py'>fetch_save.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='/Visualizer_DB/services/generateLLMprompt.py'>generateLLMprompt.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='/Visualizer_DB/services/generationJSON.py'>generationJSON.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='/Visualizer_DB/services/meta_data.py'>meta_data.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='/Visualizer_DB/services/sql.py'>sql.py</a></b></td>
							<td style='padding: 8px;'>Code>❯ REPLACE-ME</code></td>
						</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
</details>

---

## Getting Started

### Prerequisites

This project requires the following dependencies:

- **Programming Language:** Python
- **Package Manager:** Pip
- **Container Runtime:** Docker

### Installation

Build  from the source and intsall dependencies:

1. **Clone the repository:**

    ```sh
    ❯ git clone ../
    ```

2. **Navigate to the project directory:**

    ```sh
    ❯ cd 
    ```

3. **Install the dependencies:**

<!-- SHIELDS BADGE CURRENTLY DISABLED -->
	<!-- [![docker][docker-shield]][docker-link] -->
	<!-- REFERENCE LINKS -->
	<!-- [docker-shield]: https://img.shields.io/badge/Docker-2CA5E0.svg?style={badge_style}&logo=docker&logoColor=white -->
	<!-- [docker-link]: https://www.docker.com/ -->

	**Using [docker](https://www.docker.com/):**

	```sh
	❯ docker build -t / .
	```
<!-- SHIELDS BADGE CURRENTLY DISABLED -->
	<!-- [![pip][pip-shield]][pip-link] -->
	<!-- REFERENCE LINKS -->
	<!-- [pip-shield]: https://img.shields.io/badge/Pip-3776AB.svg?style={badge_style}&logo=pypi&logoColor=white -->
	<!-- [pip-link]: https://pypi.org/project/pip/ -->

	**Using [pip](https://pypi.org/project/pip/):**

	```sh
	❯ pip install -r requirements.txt
	```


### Usage

**With Docker:**
```sh
docker-compose up --build
```

**With Python:**
```sh
pip install -r requirements.txt
python main.py
```


### Testing

Run tests with:
```sh
pytest
```

---


## Roadmap

- [X] Retail data analysis and visualization
- [X] Chatbot integration
- [X] MinIO and Elasticsearch support
- [ ] Advanced LLM prompt features
- [ ] Enhanced user management

---


## Contributing

1. Fork the repository
2. Clone locally
3. Create a new branch for your feature or fix
4. Make and test your changes
5. Commit and push
6. Submit a pull request

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://LOCAL{///}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=/">
   </a>
</p>
</details>

---


## License

See the [LICENSE](LICENSE) file for details.

---


## Acknowledgments

- Thanks to all contributors and referenced open-source projects.

<div align="right">

[![][back-to-top]](#top)

</div>


[back-to-top]: https://img.shields.io/badge/-BACK_TO_TOP-151515?style=flat-square


---
