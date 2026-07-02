---
title: 'Diffusion-GR2: Diffusion Generative Reasoning Re-ranker'
title_zh: Diffusion-GR2：基于扩散模型的生成式推理重排序器
authors:
- Zhuoxuan Zhang
- Kangqi Ni
- Yuhang Chen
- Mingfu Liang
- Xiaohan Wei
- Yunchen Pu
- Fei Tian
- Chonglin Sun
- Frank Shyu
- Adam
affiliations:
- Meta AI
- UNC Chapel Hill
arxiv_id: '2607.01170'
url: https://arxiv.org/abs/2607.01170
pdf_url: https://arxiv.org/pdf/2607.01170
published: '2026-07-01'
collected: '2026-07-02'
category: GenRec
direction: 生成式推荐 · 重排序推理加速
tags:
- Generative Re-ranking
- Diffusion LLM
- Semantic ID
- Inference Acceleration
- On-policy Distillation
one_liner: 将自回归生成式推理重排序器转换为块扩散结构，吞吐量提升2.4-3.5倍同时精度接近基线
practical_value: '- 生成式推理重排序场景下，可直接复用AR转块扩散的三步转换流程（CFT→OPD→RL），在精度损失可接受的前提下大幅提升推理吞吐量，降低线上推理成本

  - 解决扩散模型生成结构化序列（如候选ID排列）的重复/漏选/出界问题时，优先采用AR预训练权重初始化+针对性微调的方案，比外挂约束解码器效果更好，无额外推理开销

  - 非自回归序列模型知识蒸馏时，可引入on-policy distillation，在模型自身生成的轨迹上用AR教师做稠密监督，大幅降低训练推理分布 mismatch
  带来的精度损失'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
生成式推理重排序器通过先输出CoT再对候选重排，精度远超传统重排，但自回归解码需要逐token生成，长推理链导致推理延迟极高，无法满足线上高并发需求；块扩散语言模型可并行解码多个位置大幅提升速度，但直接替换AR解码器会出现两个精度缺口：一是结构缺口，并行解码会输出重复、漏选、超出候选集的ID，无法生成有效排列；二是分布缺口，在固定教师轨迹上微调与推理时自身解码分布不一致，存在残余精度损失，急需兼顾速度与精度的转换方案。

### 方法关键点
- 转换微调（CFT）：用已训练好的AR GR2权重初始化块扩散模型，在重排数据上做掩码扩散微调，迁移AR模型生成有效排列的能力，无需外挂约束解码器即可输出合法候选排列，解决结构缺口
- 同策略蒸馏（OPD）：让扩散模型基于自身的块扩散解码分布生成轨迹，用冻结的AR教师模型对这些轨迹提供逐token的稠密监督，最小化两者的前向KL散度，解决训练推理分布不匹配的分布缺口
- 强化学习优化：在OPD输出的策略基础上，基于重排奖励（目标item排名提升幅度+格式奖励）做PPO风格的轨迹级强化学习，进一步缩小和AR基线的精度差

### 关键实验
在Amazon Beauty数据集上测试，基线为自回归GR2重排器；最终Diffusion-GR2的Recall@1达0.2951，仅比AR基线的0.2960低0.0009，精度基本持平；解码吞吐量达172-246 tok/s，是AR基线71 tok/s的2.4-3.5倍，调整置信度阈值τ可灵活平衡速度与精度。

最值得记住的一句话：自回归模型转扩散式并行解码的精度损失可通过「结构适配微调+同策略蒸馏+任务专属RL」的三步流程几乎完全恢复，是生成式推荐模型线上部署降本提效的可行路径。
