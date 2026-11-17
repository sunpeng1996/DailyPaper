---
title: 'MAGE: Meta-path Adaptive Graph Evidence for Transferable Multimodal Graph
  Learning'
title_zh: MAGE：面向可迁移多模态图学习的元路径自适应图证据框架
authors:
- Haiyang Jiang
- Tong Chen
- Xinyi Gao
- Hao Wang
- Hongzhi Yin
affiliations:
- The University of Queensland
- Alibaba Group
arxiv_id: '2611.20449'
url: https://arxiv.org/abs/2611.20449
pdf_url: https://arxiv.org/pdf/2611.20449
published: '2026-11-16'
collected: '2026-11-17'
category: LLM
direction: 多模态图学习 · LLM跨域迁移
tags:
- Multimodal Graph
- Cross-domain Transfer
- Meta-path
- Instruction Tuning
- Multimodal LLM
one_liner: 提出无需目标域参数更新的元路径自适应多模态图跨域迁移学习框架
practical_value: '- 电商商品/用户异构图跨场景迁移时，可复用MAMP模块沿元路径自适应聚合多模态邻居信息，减少新场景冷启动标注成本

  - 多模态LLM做图相关推理（如商品类目预测、关联推荐）时，可借鉴EGIT的证据选择逻辑，仅将相关邻域信息注入prompt，降低输入长度、减少幻觉

  - 跨域多模态图任务可直接复用该框架，无需目标域参数微调，降低新场景上线成本'
score: 7
source: arxiv-cs.IR
depth: abstract
---

### 动机
多模态图融合文本、视觉属性与关系结构，在电商、社交等场景应用广泛，但现有模型跨域泛化性差：不同节点、不同域的邻域跨模态交互逻辑、预测所需邻域信息差异大，自适应跨模态邻域融合、目标专属证据选择是两大核心痛点。
### 方法关键点
提出MAGE框架，包含两个互补模块：
1. Meta-path Adaptive Multimodal Propagation（MAMP）：沿异质元路径自适应聚合邻域信息，压缩为图感知软Token
2. Evidence-Guided Instruction Tuning（EGIT）：为每个查询筛选相关邻域证据，将图感知表示注入冻结multimodal LLM的指令
### 关键结果
在3个源图、4个未见过的目标图上测试，节点分类、链接预测的跨域迁移表现显著优于基线，全程无需目标域参数更新。
