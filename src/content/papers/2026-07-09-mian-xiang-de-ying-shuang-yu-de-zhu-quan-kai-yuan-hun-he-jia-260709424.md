---
title: A Sovereign, Open-Source Foundation Model for German and English
title_zh: 面向德英双语的主权开源混合架构30B基础模型Soofi S
authors:
- The Soofi-Team
- Benedikt Droste
- David Fitzek
- Ruben Härle
- Lukas Helff
- Maximilian Idahl
- Alex Jude
- Abbas Goher Khan
- Maurice Kraus
- Timm Ruland
affiliations:
- DFKI
- Fraunhofer IAIS
- Technische Universität Darmstadt
- Universität Würzburg
- Lamarr
arxiv_id: '2607.09424'
url: https://arxiv.org/abs/2607.09424
pdf_url: https://arxiv.org/pdf/2607.09424
published: '2026-07-09'
collected: '2026-07-13'
category: LLM
direction: 多语言开源基础模型 · MoE-Mamba混合架构
tags:
- MoE
- Mamba
- Long Context
- Open Source
- Multilingual LLM
one_liner: 开源30B MoE混合Mamba德英基础模型，单token激活3B参数，长上下文吞吐领先同类基线
practical_value: '- 架构选型可直接复用：仅保留少量注意力层+Mamba为主干+MoE稀疏激活的设计，长上下文吞吐比同能力稠密模型高8~9倍，适合电商高并发长query理解、用户长行为序列建模场景，大幅降低推理成本

  - 小语种垂域模型训练技巧：小语种数据在预训练阶段占7.2%、退火阶段提升至15.3%的加权策略，可直接迁移到电商小语种站点的垂直大模型训练，用更少的小语种数据达到更好效果

  - 二次预训练课程设计可复用：前期用大而全的混合数据打基础，学习率退火阶段切换到高质量垂直/技能数据集中优化的流程，可提升电商垂域大模型二次预训练的效果与效率

  - 长上下文扩展工程方案：仅用0.1T多域长度分桶数据微调即可将上下文窗口扩展到1M且吞吐几乎不下降，适合用户全生命周期行为序列的端到端建模'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前开源大模型存在三大落地痛点：多数仅公开权重，不披露训练数据、配方，无法复现与审计；通用多语言模型以英语为核心，德语等区域语言资源不足、效果不达预期；稠密Transformer在长上下文、高并发场景下KV cache开销随长度线性增长，部署成本极高，亟需兼顾区域语言效果、部署效率、完全开源的主权模型。
### 方法关键点
- 架构复用成熟的Nemotron 3 Nano参考设计，混合23层Mamba-2、23层MoE、仅6层GQA注意力，总参31.6B，单token仅激活3.2B参数，KV cache开销极低
- 训练采用三阶段课程学习：阶段1用20T多域混合数据（德语占7.2%）打基础，阶段2用6.58T高质量数据（德语占15.3%）搭配WSD学习率退火优化，阶段3用0.1T长度分桶数据扩展上下文至1M
- 全链路开源：公开所有训练数据统计、超参数、训练/评测代码、权重，99%训练数据可独立复现
### 关键结果
- 效果：德英基准成绩持平14~27B稠密模型，是当前最优的德英开源基础模型，代码能力在17个开源基线中排名第一，超过所有欧洲主权基线
- 效率：40K上下文、batch 32下，单B200解码TPS是14~27B稠密模型的8~9倍，上下文从4K到256K吞吐几乎无衰减
### 核心结论
混合Mamba+MoE架构可通过3B激活参数达到30B级模型效果，同时兼顾长上下文高并发部署效率，是垂域大模型落地的高性价比选择
