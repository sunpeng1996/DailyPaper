---
title: 'Cultural Awareness is Represented but Not Decoded: Tracing Mythological Knowledge
  across 18 Open-Source LLMs'
title_zh: 文化感知已表征但未被解码：18款开源LLM的神话知识溯源
authors:
- Iaroslav Chelombitko
- Ekaterina Chelombitko
- Mika Hämäläinen
affiliations:
- DataSpike
- Metropolia University of Applied Sciences
- Neapolis University Pafos
arxiv_id: '2608.02486'
url: https://arxiv.org/abs/2608.02486
pdf_url: https://arxiv.org/pdf/2608.02486
published: '2026-08-03'
collected: '2026-08-05'
category: LLM
direction: LLM文化表征与偏见分析
tags:
- LLM
- Cultural Bias
- Model Probing
- Knowledge Representation
- Cross-cultural Evaluation
one_liner: 揭示开源LLM文化偏见根源为解码器输出偏差而非内部表征缺失，配套相关数据集与工具
practical_value: '- 跨境电商多区域Agent/LLM应用可优先针对输出层做LoRA校准小众文化输出，比全量微调成本低、效率高，无需改动模型内部表征

  - 小语种市场的推荐文案生成、客服Agent场景，优先用目标地区母语构造Prompt，可大幅提升本土文化相关内容的输出准确率

  - 跨文化内容/知识推荐场景，可复用线性探测+激活补丁方法定位模型知识断层位置，针对性做RAG补全或微调，降低优化成本'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
开源LLM预训练语料被英文与西方文化内容主导，输出存在显著文化偏见，芬兰、斯拉夫、中国等非主导文化圈的神话等本土知识召回准确率极低，此前研究未明确偏见产生于表征阶段还是输出阶段。
### 方法关键点
基于Thompson motif跨文化平行实体基准，覆盖8个架构族的18款开源LLM，采用线性探测、logit lens、激活补丁、输出抽取4种手段，定位文化偏见的产生环节。
### 关键结果
1. 残差流对不同文化的区分度远高于名称字符串基线，证明LLM已学习到小众文化的内部表征；
2. 解码器会将小众文化实体token映射到主流文化对应实体，错误根源在输出层而非表征环节；
3. 用目标文化母语提问比英语提问的输出准确率显著更高，解码器的文化知识触发受Prompt语言门控。
