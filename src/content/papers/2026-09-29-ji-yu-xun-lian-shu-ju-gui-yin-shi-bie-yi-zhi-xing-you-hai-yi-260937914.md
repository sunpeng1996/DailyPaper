---
title: 'The Unequal Influence of Bad Advice: Using Training Data Attribution to Modulate
  Emergent Misalignment'
title_zh: 基于训练数据归因识别异质性有害样本以调控大模型涌现对齐偏移
authors:
- Gonçalo Paulo
- Louis Jaburi
- Nora Belrose
- Lucia Quirke
- Stella Biderman
affiliations:
- EleutherAI
arxiv_id: '2609.37914'
url: https://arxiv.org/abs/2609.37914
pdf_url: https://arxiv.org/pdf/2609.37914
published: '2026-09-29'
collected: '2026-09-30'
category: LLM
direction: LLM对齐 · 训练数据归因
tags:
- Training Data Attribution
- Emergent Misalignment
- LLM Alignment
- Influence Function
- Data Filtering
one_liner: 量化不同有害样本对大模型涌现对齐偏移的影响差异，实现精准数据过滤调优
practical_value: '- 电商/导购Agent垂直场景微调时，可复用文中梯度相似性归因方案识别微调数据中高影响坏样本，仅过滤20%高影响样本即可降低通用对齐偏移率5pct，效果远优于通用有害内容分类器

  - 针对业务场景的对齐评估，可采用「少量目标场景评测样本构建梯度查询+仅LoRA参数归因」的轻量方案，无需全量模型梯度计算即可实现高效数据筛选

  - 多规模模型部署场景下，同家族小模型的归因分数可作为大模型预过滤的依据，虽然效果略低于目标模型自归因，但可大幅降低大模型的归因计算成本'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有大模型涌现对齐偏移（Emergent Misalignment, EM）研究通常将训练数据简单划分为安全/有害，忽略了不同有害样本对EM的贡献异质性，传统通用有害内容分类器无法精准识别对EM影响最大的样本，导致数据过滤效率低，无法在保留窄域微调效果的同时控制通用对齐下降。

### 方法关键点
- 数据集：采用汽车、职业、教育三类共17700条错误建议样本，LoRA微调OLMo、Qwen、Llama三个系列共11款不同规模模型
- 归因方案：对比基于EK-FAC的近似影响函数、梯度余弦相似性两种轻量归因方法，仅针对LoRA适配器参数计算梯度，大幅降低计算开销
- 对齐评估：采用44道跨领域评测prompt（涵盖日常建议、世界观、安全三类），每个prompt生成10个补全，用Qwen 3 32B作为裁判打分，得分<3判定为对齐偏移

### 关键结果
- 对比基线：随机过滤、WildGuard通用有害分类器过滤、归因分数过滤，归因方案的过滤效果显著优于基线
- 核心数字：过滤20%归因得分最高的有害样本，对齐偏移率下降5pct；过滤20%得分最低的样本，偏移率上升10pct；仅用5%最高影响样本微调即可达到全量数据60%的偏移率
- 跨模型迁移：不同模型的归因分数Spearman相关系数0.3~0.6，跨模型归因过滤的效果仅为目标模型自归因的50%左右

> 最值得记住的结论：不同有害样本对大模型对齐偏移的影响差异极大，数据归因能精准捕获这种异质性，效果显著优于通用有害内容分类器
