---
title: 'Flash-BoN: Instant Drafts for Inference-Time Scaling in Diffusion Models'
title_zh: Flash-BoN：面向扩散模型推理时缩放的候选快速生成方法
authors:
- Ruchit Rawal
- Reza Shirkavand
- Sayak Paul
- Yuxin Wen
- Heng Huang
- Yizheng Chen
- Tom Goldstein
- Gowthami Somepalli
affiliations:
- University of Maryland, College Park
- Hugging Face
arxiv_id: '2607.04461'
url: https://arxiv.org/abs/2607.04461
pdf_url: https://arxiv.org/pdf/2607.04461
published: '2026-07-04'
collected: '2026-07-10'
category: Multimodal
direction: 多模态生成 · 扩散模型推理优化
tags:
- Diffusion Models
- Inference Optimization
- Best-of-N
- Text-to-Image
- Scaling
one_liner: 结合三类生成加速策略与多级验证，在固定墙钟预算下显著提升扩散模型推理时缩放性能
practical_value: '- 电商图文生成、文案生成等生成类业务做推理优化时，不要盲目上复杂的中间引导策略，可先测试简单BoN的墙钟效率，往往性价比更高

  - 可复用「低成本粗筛候选+高成本精修」架构：生成候选时用截断步长、跳层等trick降低单候选开销，再用轻量验证器筛选最优后精修，平衡时延和生成效果

  - 方案对比不要仅参考NFEs等抽象指标，必须以实际业务的墙钟时延为基准做评估，避免出现实验室指标好看但业务落地效果差的问题'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
现有扩散模型推理时缩放方法聚焦中间去噪步的引导验证，默认生成成本固定，且仅用NFEs评估效率忽略验证开销，导致效率排名失真；实测墙钟下简单BoN效果已超过不少复杂引导方法，说明算力投给更多候选探索性价比更高。
### 方法关键点
1. 结合步长截断、层跳过、激活代理三类互补加速trick，单模型仅需一次优化得到低成本候选生成配置，批量生成粗draft
2. 多级验证筛选最优候选，再做全质量精修
### 关键结果
固定墙钟预算下，3个基准、3个模型规模下均超过所有基线，大模型规模下AUC提升8%；和提示优化等正交技术结合可额外提升16%AUC，还能加速RL后训练收敛。
