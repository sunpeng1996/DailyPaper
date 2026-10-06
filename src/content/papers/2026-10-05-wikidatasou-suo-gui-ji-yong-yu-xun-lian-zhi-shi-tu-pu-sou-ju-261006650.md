---
title: 'Wikidata Search Traces: A Dataset for Training Knowledge Graph Search Agents'
title_zh: Wikidata搜索轨迹：用于训练知识图谱搜索Agent的数据集
authors:
- Mohamed Chenene
- Carlos Rosas-Hinostroza
- Pierre-Carl Langlais
- Anastasia Stasenko
affiliations:
- PleIAs
- Lattice, ENS-PSL
- Sorbonne Center for Artificial Intelligence
- Sciences Po Médialab
- Paris Dauphine-PSL
arxiv_id: '2610.06650'
url: https://arxiv.org/abs/2610.06650
pdf_url: https://arxiv.org/pdf/2610.06650
published: '2026-10-05'
collected: '2026-10-06'
category: Agent
direction: 知识图谱搜索Agent · 数据集与RLM框架
tags:
- Knowledge Graph
- Search Agent
- RLM
- Multi-hop QA
- Dataset
one_liner: 构建10235条知识图谱探索轨迹数据集与RLM框架，单GPU开源模型多跳问答超GPT-6-luna
practical_value: '- 多跳搜索类Agent可复用RLM框架设计：将检索结果存在Python持久态而非全部塞进LLM上下文，大幅降低长上下文信息损耗，提升多跳任务准确率

  - 构建业务域搜索轨迹训练集时，可借鉴「嵌套条件扩展+leave-one-out必要性校验」方法，确保每条线索对定位唯一答案有效，避免无效训练样本

  - 知识检索类Agent选型可优先验证「单GPU开源大模型+优化执行框架」组合，成本远低于闭源API，效果可超过同等闭源模型'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前知识图谱问答依赖LLM记忆对长尾实体准确率极低，传统语义解析方案无法处理多跳探索类需求；训练知识图谱搜索Agent面临两大痛点：一是缺少记录探索过程的标注训练数据，二是主流工具调用框架直接将大量图谱检索结果塞入上下文，严重降低LLM推理准确率。

### 方法关键点
- 多跳问题生成：围绕固定答案实体迭代将命名实体替换为嵌套条件，每次扩展做双重校验：所有条件组合仍唯一指向答案，移除任意单条件都会引入额外答案，保证线索必要性
- RLM执行框架：给模型提供持久化Python REPL环境，图谱检索结果存储在Python变量而非LLM上下文，仅通过子调用读取所需证据，避免长上下文信息丢失
- 数据集构建：生成10235条可用于训练的搜索轨迹，覆盖单实体、多跳两类问题，配套冻结的2026年2月Wikidata快照与13个图谱操作工具

### 关键结果
在100道测试题（50单实体+50多跳）上对比RLM框架与原生工具调用效果：gpt-6-luna总准确率从49%提升到61%，多跳准确率翻倍；单H100部署的Qwen3.8-27B总准确率从60%提升到74%，超过闭源gpt-6-luna表现，单query成本仅约0.04美元。

### 核心结论
结构化知识搜索类任务的能力瓶颈很大程度不在模型本身，而在检索结果管理与执行框架设计，合适的框架可让开源小模型超过闭源大模型
