---
title: Transformer-Guided Swarm Intelligence for Frugal Neural Architecture Search
title_zh: 基于Transformer引导群智能的低资源神经网络架构搜索框架
authors:
- Romain Amigon
affiliations:
- Université du Québec à Chicoutimi (UQAC)
arxiv_id: '2607.11826'
url: https://arxiv.org/abs/2607.11826
pdf_url: https://arxiv.org/pdf/2607.11826
published: '2026-07-13'
collected: '2026-07-15'
category: Training
direction: 低资源NAS · Transformer+群智能混合优化
tags:
- NAS
- Transformer
- Reinforcement Learning
- Swarm Intelligence
- Frugal AI
one_liner: 结合Transformer RL控制器与人工蜂群算法，实现消费级GPU上的低资源高效NAS
practical_value: '- 推荐/广告小模型轻量化场景可复用「全局Transformer RL搜索+局部启发式微调」的混合优化框架，大幅降低小参数模型搜参成本

  - 模型训练/超参搜索时可借鉴动态熵机制，检测到性能停滞时强制探索新结构/超参数组合，缓解早熟收敛问题

  - 边缘端部署的推荐/推理模型搜参可引入参数/深度惩罚项，在精度损失可控前提下最大化压缩模型体积，降低推理开销'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
传统NAS需数千GPU日的海量计算资源，落地门槛极高，同时存在早熟收敛、模型臃肿、元启发式方法冷启动等痛点，无法在消费级硬件上使用。
### 方法关键点
1. 混合搜索框架：结合RL训练的自回归Transformer控制器（负责全局宏观结构搜索）与人工蜂群（ABC）算法（负责局部微观结构调优），解决元启发式冷启动问题；
2. 动态熵机制：RL阶段检测到性能停滞时强制探索新拓扑，避免早熟收敛；
3. 引入网络深度惩罚项，主动抑制模型参数膨胀。
### 关键结果
在RTX 3060消费级GPU上仅用3小时搜索，得到CIFAR-10数据集上精度84.85%的模型，参数仅~17.4万，远小于ResNet-20基线；迁移到不平衡信用卡欺诈检测表格数据，F1达0.71，参数仅~4600。
