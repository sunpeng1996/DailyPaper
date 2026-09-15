---
title: 'Don''t Send What You Don''t Need: Question-Guided Token Pruning as a Privacy
  Defense for Vision-Language Models'
title_zh: 按需传输：基于问题引导Token剪枝的视觉语言模型隐私防御方法
authors:
- Md Khalid Syfullah
- Alvi Ataur Khalil
affiliations:
- Southern Illinois University Carbondale
- Transformative Innovation for Trustworthy AI and Network Security (TITANS) Lab
arxiv_id: '2609.15671'
url: https://arxiv.org/abs/2609.15671
pdf_url: https://arxiv.org/pdf/2609.15671
published: '2026-09-14'
collected: '2026-09-15'
category: Multimodal
direction: 多模态大模型 · 隐私防御与Token剪枝
tags:
- VLM
- Token Pruning
- Privacy Defense
- VQA
- Split Learning
- Federated Learning
one_liner: 提出轻量问题引导视觉Token剪枝框架QPriv-VL，降低分布式VQA传输开销同时抵御多类隐私攻击
practical_value: '- 多模态电商搜索/拍立淘场景，可复用跨模态相似度计算逻辑对视觉Token定向剪枝，大幅降低边缘端到云端的传输带宽开销

  - 隐私敏感的多模态推荐（如用户上传图搜同款）场景，可复用DINOv2无监督敏感Token识别方案，无需标注即可降低用户隐私泄露风险

  - 分布式多模态Agent部署时，可借鉴轻量DTP模块设计，单前向pass同时输出剪枝比例和保留掩码，几乎不增加推理延迟'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
分布式VQA的联邦/拆分学习架构虽可保留原生数据在本地，但全量视觉Token传输不仅带宽成本高，还易被逆向攻击泄露隐私，现有固定比例剪枝无法同时平衡任务效用、传输成本与隐私防护需求。

### 方法关键点
1. 提出QPriv-VL剪枝框架，在Token跨模型分区传输前执行剪枝，原生适配FL/SL/USL三类分布式架构；
2. 核心为轻量DTP模块，单前向pass即可同时输出样本级动态剪枝比例和Token级保留掩码；
3. 剪枝规则同时结合视觉块与问题嵌入的跨模态相似度（效用维度）、DINOv2冻结特征输出的敏感信号（隐私维度），无需敏感标注即可优先保留问题相关块、过滤敏感块。

### 关键结果数字
仅用40%原始Token预算即可维持与固定比例剪枝相当甚至更优的VQA精度；VQA-RAD数据集上成员推理攻击成功率从0.99降至0.76~0.79，FSHA/FORA重建PSNR低于固定比例剪枝基线，敏感块优先剔除比达1.20±0.18。
