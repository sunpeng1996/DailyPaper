---
title: Spectral Rewiring for Exploration, Purification, and Model Merging
title_zh: 面向模型探索、能力提纯与专家合并的谱重布线方法
authors:
- Zhilong Zhang
- Hongli Yu
- Huan-ang Gao
- Hanlin Wu
- Yuxuan Song
- Wei-Ying Ma
- Ya-Qin Zhang
- Hao Zhou
affiliations:
- Institute for AI Industry Research (AIR), Tsinghua University
- SIA-Lab of Tsinghua AIR and ByteDance Seed
arxiv_id: '2607.03065'
url: https://arxiv.org/abs/2607.03065
pdf_url: https://arxiv.org/pdf/2607.03065
published: '2026-07-02'
collected: '2026-07-17'
category: Training
direction: 大模型后训练优化 · 谱投影编辑
tags:
- Spectral Projection
- Model Merging
- Reinforcement Learning
- Reasoning
- Low-Rank Adaptation
one_liner: 提出基于预训练模型SVD子空间的SAR方法，免训练提升RL后大模型推理性能、跨域兼容性与合并效果
practical_value: '- 多域LLM精调/RL后可复用SAR思路，将更新投影到基模型SVD子空间，仅保留0.5%~1%核心参数即可保留99%以上下游性能，同时降低多任务冲突，适合电商多场景（推荐/客服/营销）统一大模型的轻量化部署

  - 模型合并场景可替换原有TA/TIES等基线，先将各领域专家的增量更新做谱投影提纯，再合并可实现跨域性能超过单域最优专家，适合快速集成商品理解、营销文案生成、订单处理等垂直领域专家能力

  - Agent推理优化场景，可对RL后模型做SAR处理，提升高k采样下的Pass@k性能，无需重新训练即可提升电商智能导购、代码Agent等场景的多轮探索成功率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前RL后训练已成为LLM提升推理能力的标准方案，但全参数更新存在两个核心痛点：一是推理性能提前饱和，高k采样下探索能力下降；二是多域训练或模型合并时跨域干扰严重，容易出现某类能力提升时其他能力被抑制的问题，亟需无需重训练的后编辑方法解决上述问题。
### 方法关键点
- 提出Subspace-Aligned Rewiring（SAR）方法，核心假设RL带来的推理增益完全集中在预训练基模型的SVD谱子空间内，将RL后的全参数更新分解为子空间内有效分量和正交冗余分量
- 具体流程：先对基模型每层注意力、MLP线性层做SVD分解得到谱坐标，再提取RL模型和基模型的参数增量，将增量投影到基模型的SVD子空间得到重布线矩阵M，最终用M重构得到仅保留有效推理分量的模型
- 全程无训练开销，无需调整嵌入层、归一化层、输出头参数
### 关键结果
- 覆盖1.5B~32B多尺度模型，在AIME数学推理、LiveCodeBench代码、IFEval指令跟随等基准测试，对比全RL基线、TIES/DARE+TIES等模型合并基线
- 仅用0.58%总参数的重布线矩阵即可保留99%以上的RL后推理性能，高k采样下Pass@k超过全RL基线，AIME 25 Pass@16从88.33%提升到91.71%
- 多域模型提纯场景，32B模型上同时提升编码性能（LCB v5+1.48%、v6+0.95%）、数学探索能力，指令跟随效果几乎无损失
- 跨域专家合并场景，1.5B、14B尺度下合并后模型均超过单域最优专家的数学、编码双域性能
### 核心结论
RL对大模型推理能力的提升本质是对基模型已有 latent 能力的重布线，而非新增能力，仅需提取极少量谱空间核心更新即可实现比全参数更新更好的下游效果。
