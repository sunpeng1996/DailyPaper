---
title: Multimodal Semantic-Aware Contrastive Learning For False Negative Mitigation
  in 3D Medical Imaging
title_zh: 面向3D医学影像假阴性缓解的多模态语义感知对比学习
authors:
- Sara Ketabi
- Matthias W. Wagner
- Cynthia Hawkins
- Uri Tabori
- Birgit Betina Ertl-Wagner
- Farzad Khalvati
affiliations:
- University of Toronto
- The Hospital for Sick Children
- Vector Institute
- University Hospital Augsburg
arxiv_id: '2607.14995'
url: https://arxiv.org/abs/2607.14995
pdf_url: https://arxiv.org/pdf/2607.14995
published: '2026-07-16'
collected: '2026-07-20'
category: Multimodal
direction: 多模态对比学习 · 假阴性缓解
tags:
- Contrastive Learning
- Multimodal Representation
- False Negative Mitigation
- Semantic Alignment
- Pretraining
one_liner: 引入放射报告语义相似度作为引导信号，缓解多模态对比学习中的语义相似假阴性问题
practical_value: '- 电商多模态召回的对比学习训练中，可引入商品标题/详情的语义相似度作为软信号，修正负例权重，缓解同品类非配对样本被误判为负例的问题

  - 跨模态预训练阶段仅优化负例采样逻辑即可提升下游任务性能，无需改动下游任务架构，落地改造成本低

  - 多模态表征对齐训练时，可优先用文本侧语义信息作为监督信号，文本语义提取难度远低于图像侧，性价比更高'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
传统多模态Contrastive Learning（CL）默认批次内所有非配对样本为负例，当样本存在高层语义重叠时会产生大量假阴性，劣化表征质量，医疗场景该问题尤为突出。
### 方法关键点
MseaCL多模态语义感知对比学习框架基于3D脑MRI影像与放射报告儿科数据集训练，训练阶段引入放射报告间的语义相似度作为引导信号，降低语义相似非配对样本的负例权重，缓解假阴性对表征学习的干扰。
### 关键结果
作为预训练阶段部署时，下游小儿脑肿瘤分子分类任务AUC至少提升22.6%，生成的多模态表征语义对齐性、鲁棒性显著更优。
