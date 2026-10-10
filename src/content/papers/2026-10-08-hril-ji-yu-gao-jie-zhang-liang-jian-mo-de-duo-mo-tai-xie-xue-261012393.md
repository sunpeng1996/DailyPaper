---
title: 'HRIL: Learning Multimodal Synergy via Higher-Order Tensor Modeling'
title_zh: HRIL：基于高阶张量建模的多模态协同学习
authors:
- Qun Dai
- Liangjian Wen
- Jiang Duan
- Yong Dai
- Dongkai Wang
- Maolin Wang
- Mingjie Wang
- Jianzhuang Liu
- He Yan
- Zhao Kang
affiliations:
- 西南财经大学计算与人工智能学院
- 四川省人工智能与数字金融重点实验室
- X-Humanoid
- 香港城市大学香港科学人工智能研究院
- 电子科技大学
arxiv_id: '2610.12393'
url: https://arxiv.org/abs/2610.12393
pdf_url: https://arxiv.org/pdf/2610.12393
published: '2026-10-08'
collected: '2026-10-10'
category: Multimodal
direction: 多模态表征 · 高阶张量协同建模
tags:
- Multimodal Representation
- Tensor Decomposition
- Self-supervised Learning
- Cross-modal Interaction
- Synergy Learning
one_liner: 提出基于高阶张量的多模态协同建模框架HRIL，大幅提升协同交互主导任务的效果
practical_value: '- 电商多模态商品表征场景可引入HRIL的跨模态矩张量建模方法，捕捉文本、图像、属性跨模态协同信号，提升召回/排序阶段的表征质量

  - 多模态搜索场景可复用Tucker分解+协同感知正则的组合，避免单一模态特征主导，提升跨模态语义匹配准确率

  - Agent多模态输入理解模块可直接集成HRIL预训练的表征层，降低多输入协同推理的特征工程成本'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
自监督多模态表征学习已在多领域取得良好效果，但难以捕捉仅存在于多模态联合配置、无法从单模态独立恢复的协同信息，是跨模态任务的核心性能瓶颈。
### 方法关键点
1. 核心洞察：多模态协同信息对应模态间的高阶统计依赖，可作为联合交互建模的明确优化目标
2. 提出HRIL框架，基于模态嵌入构建经验跨矩张量表征多路交互
3. 采用Tucker分解得到核心张量，搭配协同感知正则器避免能量集中，保留高阶耦合容量以捕捉协同信号
### 关键结果
在受控协同任务和真实世界基准测试中，效果全面优于现有多模态对比学习方法，在协同交互主导的任务上提升尤为显著，代码已开源。
