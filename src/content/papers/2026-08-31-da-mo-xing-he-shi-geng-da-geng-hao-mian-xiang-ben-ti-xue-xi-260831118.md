---
title: When Does Bigger Help? A Controlled Study of LLM Scale for Ontology Learning
title_zh: 大模型何时更大更好？面向本体学习的LLM规模效应对照研究
authors:
- Hamed Babaei Giglou
- Sören Auer
- Jennifer D'Souza
affiliations:
- TIB Leibniz Information Centre for Science and Technology, Hannover, Germany
- L3S Research Center, Leibniz University of Hannover, Hannover, Germany
arxiv_id: '2608.31118'
url: https://arxiv.org/abs/2608.31118
pdf_url: https://arxiv.org/pdf/2608.31118
published: '2026-08-31'
collected: '2026-09-02'
category: Eval
direction: 大模型评测 · 本体学习任务选型
tags:
- LLM
- Ontology Learning
- MoE
- Model Benchmarking
- Parameter Scaling
one_liner: 通过13款不同规模架构LLM的对照测试，明确本体学习任务下的模型选型规律
practical_value: '- 电商商品类目/知识图谱构建的术语分类任务，优先选27B级稠密模型即可获得最高精度收益，无需盲目上线更大参数模型

  - 层级类目关系挖掘任务优先选用大参数MoE模型，非分类关系抽取任务不要盲目堆模型规模，需额外优化prompt或任务范式

  - LLM选型不要唯参数论，模型架构、迭代血缘对效果的影响往往超过参数量，同参数规模优先选择更新迭代的模型系列'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有研究未明确LLM规模对本体学习（OL）任务的影响规律，缺乏标准化的选型参考依据。
### 方法关键点
控制所有无关变量，测试13款来自Qwen3.5/3.6系列的稠密、MoE模型及GPT闭源模型，固定embedding、RAG配置、prompt、解码策略，在生物医学、材料科学4类本体数据集上，测试术语分类、taxonomy发现、非分类关系抽取三类任务表现。
### 关键结果数字
稠密Qwen3.5系列参数量提升主要优化精度而非召回，9B到27B参数区间提升幅度最大；27B稠密模型术语分类效果超过更大参数稀疏模型，大参数MoE在taxonomy发现任务上开源模型表现最优；非分类关系抽取在所有规模下表现均较差，架构与模型血缘对效果的影响超过参数量本身，单纯看参数大小不是OL任务选型的充分标准。
