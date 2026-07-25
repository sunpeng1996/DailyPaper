---
title: Inference-Time Scaling of Diffusion Models via Progressive Seed Pruning
title_zh: 基于渐进式种子剪枝的扩散模型推理时算力优化方法
authors:
- Rogerio Guimaraes
- Pietro Perona
affiliations:
- California Institute of Technology
arxiv_id: '2607.21591'
url: https://arxiv.org/abs/2607.21591
pdf_url: https://arxiv.org/pdf/2607.21591
published: '2026-07-23'
collected: '2026-07-25'
category: Multimodal
direction: 多模态生成 · 推理阶段算力优化
tags:
- Diffusion Model
- Flow Matching
- Inference Optimization
- Progressive Seed Pruning
- Prompt Alignment
one_liner: 固定算力下通过渐进剪枝劣质种子提升扩散类生成模型的prompt对齐度与生成质量
practical_value: '- 电商生成式素材（主图/短视频）场景可复用PSP策略，固定算力下提升素材与商品卖点的对齐度，降低无效生成成本

  - 生成式推荐候选召回/文案生成环节，可参考早期轻量打分思路，先淘汰大量低质初始候选，把算力集中到高潜力项上

  - LLM+Agent多路径推理场景，可借鉴渐进剪枝框架，总推理步数固定前提下提前剪枝低回报分支，提升输出质量'
score: 6
source: arxiv-cs.CV
depth: abstract
---

### 动机
扩散/流匹配模型已成为多模态生成主流，但推理时算力缩放方案成熟度远低于 autoregressive LLM；现有种子搜索类方法全程维持固定内存占用，固定算力下资源利用效率低，生成质量受初始随机种子影响极大。
### 方法关键点
Progressive Seed Pruning（PSP）策略打破全程固定内存约束，推理前期并行生成大量种子，对中间去噪结果做轻量打分，逐步剪枝劣质生成轨迹，仅保留高潜力种子完成全流程去噪，总模型调用次数保持固定。
### 关键结果
相同算力约束下，相比best-of-N、重要性采样、树搜索等基线，PSP在扩散、流匹配两类backbone上均稳定提升奖励引导选择效果，GenEval自动评分更高，人类评估的prompt对齐度优于所有基线。
