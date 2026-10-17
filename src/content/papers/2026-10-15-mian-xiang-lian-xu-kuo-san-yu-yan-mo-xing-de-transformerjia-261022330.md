---
title: Designing Transformers for Continuous Diffusion Language Models
title_zh: 面向连续扩散语言模型的Transformer架构优化设计
authors:
- Weijian Luo
- Yujian Chen
- Hao Jiang
- Guang Cheng
- Tianyang Hu
affiliations:
- Polyadic Research Group
- Dots Studio, Xiaohongshu
- Peking University
- SAGA Lab, The Chinese University of Hong Kong, Shenzhen
- The University of California, Los Angeles
arxiv_id: '2610.22330'
url: https://arxiv.org/abs/2610.22330
pdf_url: https://arxiv.org/pdf/2610.22330
published: '2026-10-15'
collected: '2026-10-17'
category: LLM
direction: 连续扩散语言模型 · Transformer架构优化
tags:
- CDLM
- Transformer
- Diffusion
- LangDiT
- TextGeneration
one_liner: 提出专为CDLM优化的LangDiT架构，刷新多范式连续语言生成SOTA
practical_value: '- LangDiT的QK归一化、宽噪声条件、梯度路由校准、置信门控自训练4个优化trick，可直接迁移到扩散式生成推荐的backbone优化，降低生成PPL，提升推荐文案、物品语义生成质量

  - LangDiT为即插即用架构，无需修改原有扩散模型的训练目标、推理采样器，业务侧可低改造成本替换现有CDLM架构，适配推荐文案生成、搜索补全等场景

  - 128 NFEs低步数场景下性能提升显著，推理延迟可控，可直接落地对实时性要求高的电商实时push文案生成、搜索suggestion等在线场景'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有Continuous Diffusion Language Models (CDLM)直接复用因果LLM或图像领域DiT的Transformer架构，未针对CDLM的并行生成特性优化，生成效果与推理效率存在明显瓶颈。
### 方法关键点
提出LangDiT架构，融合4项核心优化：特征与Query-Key层归一化、宽维度噪声条件注入、似然捷径梯度路由与校准、置信门控训练阶段自条件机制，可即插即用适配不同CDLM范式，无需修改原有模型的训练目标与推理逻辑。
### 关键结果数字
在OpenWebText 1024-token无条件生成任务上：
1. 适配LangFlow范式：1024 NFEs下GenPPL达21.72，128 NFEs下GenPPL为44.72，刷新SOTA
2. 适配Plaid范式：1024 NFEs下GenPPL达11.33，128 NFEs下GenPPL为27.51，同样领先现有方案
