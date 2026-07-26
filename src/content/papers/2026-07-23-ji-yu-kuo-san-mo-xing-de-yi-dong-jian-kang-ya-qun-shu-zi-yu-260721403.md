---
title: 'A Diffusion-Model Subpopulation Digital Twin for Mobile Health Deployment:
  A Case Study on the HeartSteps Intervention'
title_zh: 基于扩散模型的移动健康亚群数字孪生：HeartSteps干预案例研究
authors:
- Ziping Xu
- Yuyi Chang
- Chenshun Ni
- Nithin Sugavanam
- Asim H. Gazi
- Pedja Klasnja
- Emre Ertin
- Susan A. Murphy
affiliations:
- University of North Carolina at Chapel Hill
- The Ohio State University
- Harvard University
- University of Michigan
arxiv_id: '2607.21403'
url: https://arxiv.org/abs/2607.21403
pdf_url: https://arxiv.org/pdf/2607.21403
published: '2026-07-23'
collected: '2026-07-26'
category: Other
direction: 数字孪生 · 时序扩散模型仿真验证
tags:
- Digital Twin
- Conditional Diffusion Model
- Time Series Generation
- Simulation
- Pre-deployment Validation
one_liner: 提出时序一致的条件扩散模型亚群数字孪生，支撑干预算法预部署验证
practical_value: '- 可复用「预训练+小样本微调+推理时领域知识校准」三段式迁移范式，适配新场景小数据下的用户行为仿真建模需求

  - 时序扩散模型的因果一致性约束（未来不影响过去）可直接迁移到推荐/广告的用户行为序列生成任务，避免生成序列逻辑矛盾

  - 新算法上线前的数字孪生仿真验证思路，可用于A/B测试前的候选算法粗筛，降低线上实验的用户体验损伤与流量成本'
score: 4
source: arxiv-cs.LG
depth: abstract
---

### 动机
移动健康场景的个性化干预算法直接上线易造成用户负担与流失，缺乏低成本、高仿真的预部署验证环境。

### 方法关键点
提出JITAI-Twins亚群数字孪生框架，核心是满足时序因果一致性的条件时序扩散模型（生成的历史序列不受未来行为影响），采用三段式适配流程：
1. 大规模通用观测数据预训练
2. 相关人群少量历史干预数据微调
3. 推理阶段结合领域专家知识校准目标亚群特征

### 关键结果
在HeartSteps v2~v4多轮运动建议干预任务验证中，该方法对目标亚群的时序行为模式、用户间异质性的还原效果显著优于传统简易模拟器，可完全支撑新算法上线前的效果预校验。
