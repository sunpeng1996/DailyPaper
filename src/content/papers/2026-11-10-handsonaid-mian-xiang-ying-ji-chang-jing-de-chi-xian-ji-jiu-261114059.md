---
title: 'HandsOnAid: Building and Evaluating an Offline First-Aid Assistant for Emergency
  Response Scenarios'
title_zh: HandsOnAid：面向应急场景的离线急救助手构建与评估
authors:
- Rezwan Islam Salvi
- Saiyma Sittul Muna
- Mushfiqur Rahman Mushfique
affiliations:
- Islamic University of Technology, Dhaka, Bangladesh
arxiv_id: '2611.14059'
url: https://arxiv.org/abs/2611.14059
pdf_url: https://arxiv.org/pdf/2611.14059
published: '2026-11-10'
collected: '2026-11-12'
category: Agent
direction: 端侧轻量Agent 离线部署优化
tags:
- SLM
- QLoRA
- On-device Deployment
- LLM-as-a-Judge
- RAG
one_liner: 基于4-bit量化Gemma 2B与QLoRA微调构建端侧离线急救助手，完成多维度安全与性能验证
practical_value: '- 端侧轻量Agent部署可复用4-bit量化+QLoRA微调方案，平衡推理速度与模型效果，适合离线场景的个性化导购/推荐助手落地

  - 多前沿LLM盲评+人工校验+隐藏质控样本的评估范式，可直接迁移到生成式推荐、Agent回答的安全性/合规性评测环节

  - 垂类小样本场景下「微调+RAG」的组合收益已被验证，可复用到电商垂直领域（3C/美妆客服、商品选购助手）的Agent优化'
score: 6
source: arxiv-cs.CL
depth: abstract
---

### 动机
无信号的偏远/灾害等应急场景无法访问云端AI服务，端侧小模型可提供急救指导，但需严格保障输出的安全性与准确性，现有方案缺乏合规性验证与端侧性能实测。
### 方法关键点
选取Gemma 2B做4-bit量化，采用QLoRA在5550条FirstAidQA问答数据集微调；对比7种配置（基础/4-bit/8-bit微调、长度下限/安全门/RAG增强版本）；构建符合ANZCOR指南的医学审核问答库，采用0-5分评分规则+12项安全否决项，引入4款前沿LLM盲评+45个隐藏质控样本校验评判可靠性，补充医学专家盲评交叉验证。
### 关键结果
微调后模型平均分较基线提升+1.08至2.34，最优4-bit微调+RAG版本得分2.51/5，与医学专家评分一致性高；Pixel 7 Pro端侧离线运行首token延迟6.86s，完整回答平均耗时14.88s
