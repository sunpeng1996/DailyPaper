---
title: 'SplitJEPA: Learning Invariant and Variant Latent Worlds without Reconstruction'
title_zh: SplitJEPA：无需重构的不变与可变潜世界表征学习
authors:
- Ruijin Hua
- Zichuan Liu
- Zhuokai Zhao
- Yujia Zheng
affiliations:
- University of Illinois Urbana-Champaign
- Carnegie Mellon University
- University of Chicago
arxiv_id: '2610.12349'
url: https://arxiv.org/abs/2610.12349
pdf_url: https://arxiv.org/pdf/2610.12349
published: '2026-10-08'
collected: '2026-10-10'
category: Other
direction: 无重构表征学习 · 不变可变分量拆分
tags:
- JEPA
- Representation Learning
- Invariant Feature
- Disentanglement
- Latent Space
one_liner: 提出无重构的SplitJEPA架构，可直接在表征空间拆分潜态的不变与可变分量
practical_value: '- 特征工程可借鉴无重构拆分思路，拆分用户/物品表征的不变分量（长期偏好、固有属性）与可变分量（短期兴趣、场景扰动），提升跨场景推荐鲁棒性

  - 无解码器的设计可降低表征预训练的计算开销，适合大参数量召回/排序模型的预训练阶段落地

  - 电商导购Agent可基于该方法拆分用户Query的不变需求（如品类偏好）与可变约束（如预算、时效），提升多轮需求理解准确率'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有潜态不变/可变分量拆分依赖重构损失，需额外引入观测解码器，计算开销高且表征组织可信度受重构效果约束；传统JEPA虽无重构环节，但无法自动拆分潜态的不变与可变结构。
### 方法关键点
SplitJEPA架构可直接在表征空间联合学习潜态及其不变、可变分量划分，无需重构损失与观测解码器；理论证明在平稳高斯预测动力学、满秩变化条件下，可精准识别不变与可变子空间，仅存在独立块级等距变换误差。
### 关键结果
合成非线性系统、机器人操纵任务实验验证了理论正确性，相比基于重构的拆分方案，鲁棒性与训练效率均有显著提升。
