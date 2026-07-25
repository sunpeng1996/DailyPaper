---
title: Robostral Navigate
title_zh: Robostral Navigate：面向大规模部署的单目视觉机器人导航大模型
authors:
- Arjun Majumdar
- Avinash Sooriyarachchi
- Benjamin Tibi
- Chris Bamford
- Elliot Chane-Sane
- Guillaume Lample
- Khyathi Raghavi Chandu
- Ludovic Ho Fuh
- Mathieu Poiree
- Olivier Duchenne
affiliations:
- Mistral AI
arxiv_id: '2607.20785'
url: https://arxiv.org/abs/2607.20785
pdf_url: https://arxiv.org/pdf/2607.20785
published: '2026-07-21'
collected: '2026-07-25'
category: Other
direction: 具身机器人导航 · 多模态大模型训练优化
tags:
- Multimodal-LLM
- Embodied-AI
- Prefix-Caching
- Training-Optimization
- Navigation
one_liner: 仅输入单目RGB的8B多模态导航大模型，跨机器人机身泛化，训练成本降22倍且达SOTA性能
practical_value: '- prefix-caching训练方案将长序列episode打包为单训练序列，可直接复用至序列推荐、会话式Agent的长上下文训练，大幅降低token消耗与训练时长

  - 树状注意力掩码避免模型依赖历史真值输入、强制基于当前上下文预测的思路，可优化推荐系统的OOD泛化能力，减少训练/推理分布偏移

  - 大规模模拟生成数据替代真实采样的思路，可迁移到电商冷启动、广告新场景测试，降低真实样本采集成本与风险'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有机器人导航系统依赖深度传感器、多摄rig或预建地图，硬件部署成本高、跨机身泛化性差，训练周期长达数月，难以规模化落地。
### 方法关键点
1. 8B参数vision-language模型，仅输入单目RGB图像流，直接在图像空间预测下一路标点，无需适配机器人专属坐标，跨轮式、足式、飞行机器人无需重校准；
2. 生成35万模拟场景共240万条轨迹，降低真实数据采集依赖；
3. 提出prefix-caching训练范式，整episode打包为单训练序列，训练token量减少22x，训练周期从数月压缩到数天；搭配树状注意力掩码、RL优化提升探索恢复能力。
### 关键结果
R2R-CE基准成功率77.4%，超最优单目方案10.5pp、最优深度/多摄方案5.3pp；RxR-CE基准成功率75.1%，优于所有单目基线。
