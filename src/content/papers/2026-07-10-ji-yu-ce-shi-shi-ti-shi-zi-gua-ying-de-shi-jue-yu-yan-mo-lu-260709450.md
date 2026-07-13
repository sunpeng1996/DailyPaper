---
title: Robustifying Vision-Language Models via Test-Time Prompt Adaptation
title_zh: 基于测试时提示自适应的视觉语言模型鲁棒性提升方法
authors:
- Xingyu Zhu
- Huanshen Wu
- Shuo Wang
- Beier Zhu
- Jiannan Ge
- Jiaheng Zhang
- Long Chen
affiliations:
- National University of Singapore
- University of Science and Technology of China
- The Hong Kong University of Science and Technology
arxiv_id: '2607.09450'
url: https://arxiv.org/abs/2607.09450
pdf_url: https://arxiv.org/pdf/2607.09450
published: '2026-07-10'
collected: '2026-07-13'
category: Multimodal
direction: 多模态模型 · 测试时自适应鲁棒优化
tags:
- VLM
- Test-Time Adaptation
- Adversarial Robustness
- Prompt Learning
- Optimal Transport
one_liner: RITA测试时提示自适应框架通过分布对齐与动态缓存提升VLM对抗鲁棒性且不损失干净样本精度
practical_value: '- 电商多模态搜索/推荐场景可复用分布对齐思路，解决模糊低质商品图、拼写错误query等扰动样本的跨模态匹配偏差问题

  - 在线推理场景可借鉴动态缓存机制，逐步积累可靠样本特征优化匹配效果，无需重新训练即可适配线上分布漂移

  - 多模态RAG/Agent的输入鲁棒性优化可复用「增强视图分布保留语义」的观察，降低噪声输入、恶意输入的干扰'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
预训练VLM（如CLIP）零样本泛化能力优异，但对抗扰动下性能骤降；现有测试时自适应方法依赖样本级置信度启发式规则，忽略数据内在分布结构，无法区分高置信度对抗误判与真实语义一致性，鲁棒性受限。

### 方法关键点
1. 核心观察：对抗扰动结构脆弱，整体表征虽被破坏，但增强视图的分布仍保留语义完整性；
2. RITA框架实现从样本级估计到分布级对齐的范式转换，采用最优传输将增强视觉特征分布与文本原型对齐，缓解对抗离群点，纠正跨模态语义偏移；
3. 引入动态缓存逐步积累测试流中的可靠线索，支持在线效果优化。

### 关键结果
多组实验验证，RITA可大幅提升VLM对抗鲁棒性，同时完全不损失干净样本的预测准确率。
