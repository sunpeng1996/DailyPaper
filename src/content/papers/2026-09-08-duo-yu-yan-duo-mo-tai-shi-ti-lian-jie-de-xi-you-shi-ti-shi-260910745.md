---
title: 'Think Before You Link: Rarity, Reasoning, and Retrieval in Multilingual Entity
  Linking'
title_zh: 多语言多模态实体链接的稀有实体识别与推理检索融合框架
authors:
- Parinthapat Pengpun
- Simran Khanuja
- Graham Neubig
affiliations:
- Carnegie Mellon University
arxiv_id: '2609.10745'
url: https://arxiv.org/abs/2609.10745
pdf_url: https://arxiv.org/pdf/2609.10745
published: '2026-09-08'
collected: '2026-09-12'
category: Agent
direction: 多模态实体链接 · RAG+推理增强
tags:
- Entity Linking
- Multimodal LLM
- RAG
- Long Tail
- Multilingual
- Tool Use
one_liner: 提出多维稀有实体刻画方法，结合推理VLM与迭代检索提升多模态实体链接性能
practical_value: '- 长尾/稀有实体刻画不要仅依赖热度类指标（点击、曝光、搜索量），可补充知识图谱结构指标（实体关联数、跨语种/跨平台覆盖度等），能挖掘传统指标漏判的难例，针对性优化搜索、推荐的长尾效果

  - 做知识密集型Agent任务（商品实体链接、合规内容审核、多语种商品关联）时，不要单独用推理或单独用RAG：推理单独用解决不了长尾知识缺失，RAG单独用会引入噪声拖累头部效果，两者结合性价比最高

  - 中小参数推理模型加RAG可媲美更大参数的普通指令模型，尤其长尾场景效果更优，能降低部署成本：文中4B推理VLM加RAG效果打平8B指令VLM，稀有场景还高出5-7%

  - 多语种跨模态检索优先选用多语种语义Embedding而非BM25，非拉丁语系的召回率更高，适合跨境电商的多语言商品匹配、搜索场景'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有多语言多模态实体链接系统在稀有实体上性能骤降，但过往稀有度仅用页面访问量等热度指标定义，漏判了大量知识图谱结构稀疏、跨语种覆盖不足的文化/地域小众实体，这类实体的链接失败是现有系统的核心痛点，尤其影响跨境、垂类场景的效果。
### 方法关键点
- 提出多维稀有度刻画体系：除传统热度指标外，新增12项维基百科编辑特征、Wikidata结构特征（关联数、语种覆盖数等），不同维度稀有实体集平均重叠仅37%，能覆盖更多传统指标漏判的难例
- 免训练两阶段框架：第一阶段用带推理能力的VLM（Qwen3-VL）迭代调用维基百科检索工具，支持BM25和多语种语义Embedding两种检索模式，动态收集证据直到结果置信度达标；第二阶段从推理轨迹中抽取标准实体名称
- 控制变量实验设计：覆盖2/4/8B三个参数规模，对比推理版VLM和普通指令版VLM，验证推理、检索、模型规模各自的贡献
### 关键结果
- 实验基于多语言多模态实体链接基准MERLIN（覆盖印地语、印尼语、日语等5种语言），新增发布MERLIN-Rare稀有实体测试子集
- 最优配置8B-Think+Embed整体准确率较SOTA Cultural Pangea提升6.9%，稀有实体子集最高提升23.3%
- ablation结论：单独推理对稀有实体无明显提升，单独RAG提升稀有实体效果但拖累头部准确率，两者结合效果最优；4B推理模型加RAG效果打平8B普通指令模型，稀有场景还高5-7%
### 核心结论
对于知识密集型任务，「推理能力+迭代检索」的组合比单纯堆模型参数的性价比更高，尤其能大幅提升长尾稀有场景的性能。
