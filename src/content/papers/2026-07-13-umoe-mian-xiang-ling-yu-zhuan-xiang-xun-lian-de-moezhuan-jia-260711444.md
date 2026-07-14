---
title: UMoE:Unlocking Every Expert in Domain-Specific Training
title_zh: UMoE：面向领域专项训练的MoE专家池全激活方法
authors:
- Xuefeng Li
- Pengfei Liu
affiliations:
- SII
- SJTU
- GAIR
arxiv_id: '2607.11444'
url: https://arxiv.org/abs/2607.11444
pdf_url: https://arxiv.org/pdf/2607.11444
published: '2026-07-13'
collected: '2026-07-14'
category: Training
direction: MoE领域训练 · 专家池重组优化
tags:
- MoE
- Domain Fine-tuning
- Expert Pruning
- Expert Expansion
- LLM Training
one_liner: 不改变MoE推理成本的专家池重组方法，剪低贡献专家后扰动扩种提升领域微调效果
practical_value: '- 电商/广告垂类MoE微调可直接复用UMoE流程：1024条领域样本做校准，先剪低贡献专家再对称扰动扩种，不改变推理架构即可提升垂类效果，无额外推理成本

  - 专家筛选优先用REAP saliency指标（门控加权的输出范数），效果优于单纯激活频率，校准数据量需求极低，适合业务侧小样本垂类适配场景

  - MoE扩种专家必须对称扰动父专家和新生成专家的MLP+路由参数，仅扰动新专家会导致其路由占比持续下降，效果反而劣于直接SFT

  - 不管训练数据量大小，UMoE增益始终为正，训练数据较少时提升更明显，适合业务侧垂类数据积累不足的场景'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
通用预训练MoE的专家池适配混合域分布，垂类微调时大量低领域相关性专家仍会获得非零路由，直接SFT仅更新专家参数不调整专家池结构，导致近40%的路由算力浪费在可无损失剪掉的冗余专家上，且现有压缩方案会改变推理架构、增加部署成本。

### 方法关键点
- 剪枝：从目标领域SFT数据中采样1024条做校准，计算每个专家的REAP saliency（路由门控权重加权的专家输出L2范数均值），每层剪掉saliency最低的50%专家
- 扩种：剩余专家每个对应生成1个新专家，复制父专家参数后对父专家和新专家的MLP权重、路由参数分别加σ=0.05的独立高斯扰动，恢复原有专家数量、模型结构、推理成本
- 直接执行标准全参数SFT，无需调整超参数，无额外训练开销

### 关键结果
覆盖2种MoE架构（Qwen3-30B-A3B、Qwen3.5-35B-A3B）、5个领域（数学、代码、科学、工具调用、Agent编码）、12个基准测试，UMoE相对直接SFT平均提升2.55个百分点：数学平均准确率升3.4，SWE-bench Verified pass@1升6.0，在高质量内部数学语料上（直接SFT已超Qwen3-30B-A3B-Thinking）仍能再提升1.36个百分点，增益随训练数据量增大始终保持为正。

> 最值得记住的一句话：直接SFT的MoE存在大量冗余路由容量，无需增加推理成本的专家池重组即可充分释放这部分能力，跨领域通用。
