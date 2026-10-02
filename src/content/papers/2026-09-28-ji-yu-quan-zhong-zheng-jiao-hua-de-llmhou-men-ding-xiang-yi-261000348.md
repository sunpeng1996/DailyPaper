---
title: 'Removing the NEEDLE in the Haystack: Backdoor Removal in LLMs via Weight Orthogonalisation'
title_zh: 基于权重正交化的LLM后门定向移除方法NEEDLE
authors:
- Minoo Kim
- Vasileios Lampos
- George Drayson
affiliations:
- Locai Labs
- University College London (UCL)
arxiv_id: '2610.00348'
url: https://arxiv.org/abs/2610.00348
pdf_url: https://arxiv.org/pdf/2610.00348
published: '2026-09-28'
collected: '2026-10-02'
category: LLM
direction: LLM安全 · 后门定向移除
tags:
- Backdoor Defense
- Weight Orthogonalization
- Activation Steering
- LLM Safety
- Model Editing
one_liner: 无需训练的LLM后门定向移除方法，兼顾低攻击成功率与极小的能力、安全损失
practical_value: '- 业务场景中若采用开源LLM搭建Agent、生成式推荐、智能客服系统，可直接复用NEEDLE方案移除已知后门，无需重新训练，避免模型能力下降与安全风险

  - 「激活方向估计+权重正交化+目标子空间保留」的思路可迁移到模型定向编辑场景：比如擦除LLM生成推荐文案时的敏感词倾向、修正Agent执行特定违规指令的逻辑，对主任务效果影响极小

  - 顺序逐层编辑的方法可复用在LLM对齐优化场景，无需全量SFT即可在保留核心安全能力的同时，修正特定不良生成行为，降低对齐成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM后门移除方案普遍依赖额外训练或干净参考模型，移除后门时会大幅偏移模型输出分布，导致推理能力下降、原有安全对齐机制受损；且后门激活方向与LLM拒绝子空间高度重叠，直接擦除后门会显著提升有害输出率，亟需低侵入、同时保能力保安全的后门移除方案。

### 方法关键点
- 训练-free方案，无需干净参考模型、毒化训练数据，仅需已知后门触发规则即可执行
- 先对比触发/普通输入的激活向量，估计各层后门方向；再通过有害请求的拒绝/合规响应，构建4维拒绝子空间
- 对中高层（12-34层）的注意力、MLP输出投影矩阵做顺序正交化，擦除后门方向中正交于拒绝子空间的分量，同时通过岭回归修正层间编辑带来的拒绝子空间偏移

### 关键实验
在Gemma-3-4B-IT、Qwen3-4B-Instruct两个模型上测试6种后门攻击（情感steering、定向拒绝、代码注入各2种触发类型），对比SFT、OSFT、CROW、BD-VAX四种基线：
- 平均Attack Success Rate (ASR)降至1.67%（Gemma）/5.00%（Qwen），代码注入攻击ASR达0%，远低于基线的27.75%-69.25%
- 模型相对能力损失仅0.48%/0.72%，正常输出的KL散度仅0.03/0.11，安全变化幅度小于4%，均远优于所有基线

### 核心结论
LLM定向编辑时需同时擦除目标特征分量、保留核心功能子空间，顺序逐层编辑可最小化整体分布偏移
