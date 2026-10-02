---
title: 'Know When to Hold ''em: Correct-Token Retention in Uniform-State Diffusion
  Language Models'
title_zh: 均匀状态扩散语言模型的正确Token保留正则化方法
authors:
- Mojtaba Nafez
- James Henderson
affiliations:
- EPFL
- Idiap Research Institute
arxiv_id: '2610.01275'
url: https://arxiv.org/abs/2610.01275
pdf_url: https://arxiv.org/pdf/2610.01275
published: '2026-10-01'
collected: '2026-10-02'
category: Training
direction: 扩散语言模型 · 训练正则化
tags:
- Diffusion LM
- USDM
- Regularization
- Training Objective
- Text Generation
one_liner: 提出无需修改采样器的CTR-Reg正则化，解决USDM生成多样性崩溃问题
practical_value: '- 生成式推荐、电商文案生成场景若采用扩散模型做并行生成，可直接接入CTR-Reg正则化，无需修改采样逻辑即可降低生成重复率、提升多样性，同时可减少推理步数降低延迟

  - 开发自修正LLM、Agent推理模块时，可借鉴CTR-Reg思路，对已经验证正确的中间结果（如已确定的召回item、正确的思维链节点）添加保留损失，避免反复修改正确内容导致的效果震荡

  - 离散扩散类模型训练中若遇到生成结果不稳定、每步修改比例过高的问题，可参考本文的损失分解方法，定位是否存在正确样本惩罚权重不足的问题，针对性添加辅助损失'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
均匀状态扩散语言模型（USDM）支持任意去噪步骤修改任意token，具备原生自修正能力，比掩码扩散更适合高吞吐并行生成场景。但现有SOTA USDM存在严重的正确token保留缺陷：贪心尾解码时每步仍会修改173~270个（共512）位置，大量无协调修改导致生成多样性崩溃；进一步分析发现根源是NELBO训练目标对正确位置的错误预测惩罚极弱，仅占总损失的3.5%~5.2%，模型无法区分需要保留的正确token和需要修改的错误token。

### 方法关键点
- Correct-Token Retention Regularization（CTR-Reg）是无需修改采样器的轻量辅助损失，仅在前向加噪过程未被扰动的token位置生效，强化模型对正确token的预测置信度
- 适配两类USDM参数化方式：对直接预测干净token的DUO、UDLM，直接对未扰动位置加负对数似然损失；对预测分数的SEDD模型，改为对非对角线分数加软hinge损失
- 正则化权重λ取0.02即可平衡保留能力和修正能力，训练无额外计算开销

### 关键结果
实验基于OpenWebText、arXiv等6个公开语料，对比DUO、UDLM、SEDD三个SOTA USDM基线：
- CTR-Reg平均提升干净token准确率26.5个百分点，错误token修正准确率几乎不变；贪心尾解码时每步修改位置快速收敛到3~11个，无反复震荡
- 仅用5步贪心尾解码，三个模型的生成困惑度均减半：DUO从105.86降至49.57，UDLM从93.28降至44.31，SEDD从194.59降至87.19，同时生成多样性高于训练语料熵，完全避免基线的多样性崩溃问题。

> 最值得记住的一句话：自修正生成模型的核心不仅是修正错误的能力，更是保留正确结果的能力，现有训练目标往往忽略后者的信号权重。
