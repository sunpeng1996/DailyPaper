---
title: Latent Residual Reasoning for Ranking in Generative Recommendation
title_zh: 面向生成式推荐排序的隐式残差推理框架Refiner
authors:
- Haihan Shi
- Ruidong Han
- Wenjie Wang
- Shangyu Chen
- Sunhao Dai
- Yongqi Li
- Yangyang Li
- Fei Jiang
- Wei Lin
- Fuli Feng
affiliations:
- 中国科学技术大学
- 美团
- 中国人民大学
- 香港理工大学
- Academy of Cyber
arxiv_id: '2610.36890'
url: https://arxiv.org/abs/2610.36890
pdf_url: https://arxiv.org/pdf/2610.36890
published: '2026-10-27'
collected: '2026-10-28'
category: GenRec
direction: 生成式推荐 · 隐式推理排序优化
tags:
- Generative Recommendation
- Latent Reasoning
- LoRA
- Ranking
- Residual Learning
one_liner: 提出基于LoRA微调的Refiner框架，无需重训已部署生成式排序模型即可提升排序效果
practical_value: '- 已上线生成式排序模型可直接复用该框架做增量优化，冻结原模型仅训练LoRA模块+新增推理预测头，无需全量重训，不破坏原有基线效果，上线风险极低

  - 排序打分优化采用残差修正思路比直接重训打分头效果更优，每步推理仅输出当前打分的修正量，适合对已有成熟排序模型做效果增益

  - 可复用历史查询设计，从用户长序列中抽取少量浓缩的历史查询Token作为全局用户上下文，仅增加极微推理延迟即可提升冷启动用户/长尾物品的排序效果

  - 工程上可根据流量latency要求灵活配置推理步数，1-2步推理即可获得大部分收益，平衡效果和耗时，适合大流量线上推荐场景'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有生成式推荐排序模型普遍采用单步直接预测的「快思考」范式，难以满足多候选细粒度打分需求；基于LLM的显式推理方案计算开销大，无法适配工业界广泛部署的非文本ID类推荐模型；已有的隐式推理方案大多针对召回阶段优化，未对齐排序阶段的细粒度打分目标，且需要全量重训模型，难以在已上线系统落地。

### 方法关键点
- 残差推理机制：不直接输出全量打分，每步推理仅输出上一步打分的修正量，多步累加得到最终排序分，对齐排序目标
- 历史查询设计：从用户行为序列中抽取少量浓缩Token作为全局用户上下文，复用于所有推理步骤，增强候选打分的用户感知
- 参数高效微调方案：冻结预训练生成式排序backbone全部参数，仅新增LoRA模块和推理专属预测头训练，适配已部署模型，上线成本极低

### 关键实验
在Steam、MovieLens10M两个公开数据集，以及美团7000万用户的工业级数据集上测试，对比xDeepFM、DIN、MTGR、ReaRec等基线：公开数据集上CTR GAUC最高提升4.3%；工业数据集上CTR GAUC提升1.6‰、CTCVR GAUC提升2.1‰，均达到统计显著；线上A/B测试PV-CTR提升0.75%，GMV提升0.46%，针对长序列用户、长尾冷启动物品的增益更明显。

### 最值得记住的一句话
已上线的成熟推荐系统的效果优化，不一定要推翻原有架构全量重训，通过参数高效微调引入轻量化隐式推理做残差打分修正，是投入产出比极高的优化路径。
