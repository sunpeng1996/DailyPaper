---
title: 'DPE-Rec: Diversity-Preserving and Efficient Diffusion Language Model Recommendation
  for Bundle Construction'
title_zh: DPE-Rec：保多样性的高效扩散语言模型组合推荐框架
authors:
- Pingchuan Ma
- Bohan Jiang
- Chengshuai Zhao
- Dawei Li
- Zhen Tan
- Huan Liu
affiliations:
- Arizona State University
- Stevens Institute of Technology
arxiv_id: '2610.34700'
url: https://arxiv.org/abs/2610.34700
pdf_url: https://arxiv.org/pdf/2610.34700
published: '2026-10-26'
collected: '2026-10-27'
category: GenRec
direction: 生成式推荐 · 扩散LLM 组合构建
tags:
- Diffusion-LLM
- Bundle-Recommendation
- Semantic-ID
- GRPO
- Trajectory-Distillation
- Generative-RecSys
one_liner: 提出语义分叉感知GRPO与伪轨迹蒸馏，提升扩散式组合推荐的多样性与推理效率
practical_value: '- 基于Semantic ID的生成式推荐可复用层级温度调优trick：高熵语义分叉层（首token）用高采样温度保多样性，低熵精细化匹配层用低温度控精度，无需修改模型架构即可提升效果

  - 扩散LLM落地高并发场景可复用伪轨迹蒸馏方案：将训练分布从随机掩码的超大空间收敛到推理实际访问的轨迹子空间，可实现1个数量级的推理加速，精度损失<3%

  - 电商组合推荐（凑单、套装、穿搭）场景优先选择扩散LLM而非自回归LLM：双向注意力的归纳偏差更适配无序生成需求，搭配GRPO对齐后效果优于传统判别式推荐方法'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
扩散语言模型（DLM）天生适配无序的组合推荐（电商打包、歌单生成、穿搭搭配）任务，但现有落地存在两个核心痛点：一是置信度引导解码优先解低熵的语义精细化token，推迟高熵的语义分叉决策，导致生成物品相似度高、多样性不足；二是单步多token并行解码易生成非法Semantic ID，要么推理步数多 latency 高，要么精度损失大，无法适配高并发电商场景。
### 方法关键点
- 语义分叉感知GRPO：诱导自回归rollout优先解决语义分叉（Semantic ID首token），给分叉层设置更高采样温度（0.6）、精细化层设低温度（0.2），保留探索空间的同时不改变原有双向注意力架构
- 伪轨迹蒸馏：用单token解码的高质量教师轨迹构造训练样本，将原扩散训练的随机掩码大空间收敛到推理实际访问的轨迹子空间，让学生模型支持可靠的单步多token解码
- 生成后执行Semantic ID合法性校验与去重，确保推荐物品无重复、均在候选 catalog 内
### 关键实验
在Spotify歌单、POG/IQON3000穿搭3类数据集上对比GRU4Rec、BERT4Rec、DiffGRM、DDBC等9个SOTA基线，常规版本平均推荐性能提升63%；Fast版本平均推理速度比现有生成式推荐方法快25.6×，精度损失仅约2.5%。
### 核心洞察
扩散LLM做无序生成任务时，灵活的任意顺序解码反而可能是性能陷阱，优先解决高熵的粗粒度语义决策才能平衡探索与效率。
