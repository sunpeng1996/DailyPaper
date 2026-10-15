---
title: Decoupled Marginal Sharpening for Training-Free Inference-Time Scaling
title_zh: 用于免训练推理时缩放的解耦边际锐化方法
authors:
- Weixin Wang
- Wei Deng
- Anderson Schneider
- Yuriy Nevmyvaka
- Pan Xu
- Andrew Bennett
affiliations:
- Duke University
- Morgan Stanley
arxiv_id: '2610.20483'
url: https://arxiv.org/abs/2610.20483
pdf_url: https://arxiv.org/pdf/2610.20483
published: '2026-10-14'
collected: '2026-10-15'
category: Reasoning
direction: LLM推理优化 · 免训练推理时缩放
tags:
- Training-Free
- Inference-Time Scaling
- LLM Reasoning
- Marginal Sharpening
- Sequential Monte Carlo
one_liner: 提出双阶段解耦边际锐化框架，免训练提升LLM推理准确率，全基准测试性能超现有方法
practical_value: '- 电商/广告Agent的多步推理场景（如复杂用户咨询应答、定制化选品推理）可直接复用双阶段锐化思路：轻度锐化保留推理路径多样性，强锐化聚合答案共识，无需微调即可提升复杂问题解决准确率

  - FAA-SMC、Island采样的路径坍塌缓解trick可迁移到生成式推荐的多候选生成环节，在有限计算预算下提升候选多样性与最终排序准确率，避免生成结果趋同

  - 免训练推理时优化范式适合无法微调大模型的业务场景（如合规要求高的电商客服、广告文案生成），仅调整采样策略即可获得可量化的效果收益'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有免训练LLM推理时幂采样方法存在两大核心痛点：一是全序列级锐化会将概率集中在少数高似然的推理-答案配对，忽略多条低似然路径共同支撑的正确答案，反而降低最终答案准确率；二是有限粒子的传统SMC采样在重复重采样时易出现路径坍塌，损失推理路径多样性，无法充分激活基础模型本身的推理能力，且无需微调、无需额外奖励模型的优化方案具备极高的业务落地价值。

### 方法关键点
- 双阶段解耦边际锐化（DMS）框架：设置独立超参数分别控制推理路径锐化强度α_Z、答案边际锐化强度α_A，先对推理路径做轻度锐化保留多路径多样性，再聚合所有路径的答案概率做更强的边际锐化，优先选择多路径共识度高的答案
- FAA-SMC采样器：结合退火幂目标调度、预测祖先重采样、局部完全适配提议机制，大幅缓解SMC采样的路径坍塌问题，提升推理路径采样效率
- 长推理场景可选Island-DMS变种：将采样粒子拆分为多个独立岛屿单独采样，进一步保留路径祖先多样性

### 关键结果
在MATH500、GPQA-Diamond、HumanEval、AIME24/25四个推理基准，Qwen3-4B、Qwen3-8B、DeepSeek-R1-Distill-Llama-8B三个基础模型上测试，对比标准解码、低温解码、Power-SMC、Marginal Sharpening四个基线，DMS在全部12组实验设置下pass@1最高，相对最优基线提升0.34~10.07个百分点，推理延迟仅为同类基线Marginal Sharpening的17%~44%。

### 核心洞见
推理时优化不需要盲目拉高单条推理路径的似然得分，保留路径多样性并聚合多路径共识的收益远高于单路径锐化的收益
