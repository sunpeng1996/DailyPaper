---
title: 'Feyospace-v1: How the Cyber Mercury Seven Trained Frontier Cyber Models'
title_zh: Feyospace-v1：七人小团队训练前沿网络Agent模型的实践
authors:
- Zongjie Li
- Alan Z. W
- John Nicolas J
- Walter H. F
- Scott Donald L
- Gordon Y. P
- Deke X Jr
affiliations:
- Vera Praxis Lab
arxiv_id: '2609.08418'
url: https://arxiv.org/abs/2609.08418
pdf_url: https://arxiv.org/pdf/2609.08418
published: '2026-09-07'
collected: '2026-09-14'
category: Agent
direction: Agent 网络安全能力训练优化
tags:
- CyberAgent
- DataCentricTraining
- SFT
- OpenWeightModel
- AgentEvaluation
one_liner: 提出数据驱动的网络Agent训练框架，七人小团队训练出同规模最优的开源网络Agent
practical_value: '- 小团队落地Agent能力可复用其数据优先的优化思路，优先解决环境、监督数据、teacher调用成本三大瓶颈，无需盲目堆模型规模

  - 训练Agent交互轨迹数据集时可借鉴「执行验证+证据审计」的过滤机制，大幅降低SFT数据噪声，提升训练效率

  - 多LoRA/多模型合并后出现的能力衰减问题，可复用PSBreakup的修复思路，适用于电商多业务推荐模型合并的场景'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
开源大模型post-training提升Agent能力的核心瓶颈并非模型规模，而是可执行环境成本、可靠多轮监督数据、强teacher访问限制，小团队很难产出前沿Agent能力。
### 方法关键点
提出数据优先的训练框架，配套5个互补系统解决核心瓶颈：Choulea分析隐藏推理特征、SkyReal降低teacher采样成本、Hongzwang绕过teacher执行API限制、PSBreakup修复模型合并导致的能力衰减、Kreator将专家干预转化为可训练推理数据；数据引擎构建可重置的多类网络安全执行环境，轨迹经执行验证+证据审计过滤后得到164269条长上下文SFT数据。
### 关键结果数字
3个微调checkpoint相对基座在CyberGym套件平均提升23.76%，CTF套件平均提升10.49%；Feyospace-s1位列CyberGym官方榜第10，同参数量级下所有checkpoint均排第1。
