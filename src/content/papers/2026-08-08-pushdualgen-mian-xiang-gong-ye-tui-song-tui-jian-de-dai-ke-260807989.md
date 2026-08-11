---
title: 'PushDualGen: Enabling LLMs to Generate Semantic IDs with Interpretable Copy
  for Industrial Push Recommendation'
title_zh: PushDualGen：面向工业推送推荐的带可解释文案的Semantic ID生成框架
authors:
- Manjia Lin
- Da Li
- Yan Wang
- Yong Jin
- Zheming Ding
- Wei Yuan
- Lei Yan
- Yanan Xia
- Lu Zhang
- Fan Yang
affiliations:
- Kuaishou Technology
arxiv_id: '2608.07989'
url: https://arxiv.org/abs/2608.07989
pdf_url: https://arxiv.org/pdf/2608.07989
published: '2026-08-08'
collected: '2026-08-11'
category: GenRec
direction: 生成式推荐 · 工业推送 Semantic ID
tags:
- Generative Recommendation
- Semantic ID
- Push Recommendation
- LLM4Rec
- Interpretability
one_liner: 面向工业推送场景提出轻量生成式推荐框架，先生成Semantic ID再生成可选可解释文案兼顾效果与效率
practical_value: '- 工业级低延迟生成式推荐可采用「先生成Semantic ID再生成可选解释文案」的架构，解释环节可按需跳过，大幅降低推理overhead，适配高QPS推送/通知场景

  - Semantic ID构建可改用并行多嵌入槽量化方案，替代传统残差量化，避免层级误差累积，同时配合T2S/S2T双任务对齐LLM词汇表，冻结原词表仅优化SID特殊token，训练更稳定高效

  - 生成式召回输出的Top-N SID可通过简单加权融合进原有用户特征，无缝对接现有ANN检索链路，无需全链路重构即可快速落地获得效果收益'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业推送推荐是短视频/电商平台核心用户召回渠道，触达规模大但对延迟、准确性、可解释性要求极高；现有基于Semantic ID的生成式推荐要么黑盒不可解释，要么加CoT解释后推理成本过高，无法适配10万级QPS的工业推送场景，同时传统残差量化的Semantic ID存在层级误差累积问题，长用户行为序列也易超出LLM上下文窗口。

### 方法关键点
- 采用并行Semantic ID构建方案：每个视频对应8个独立嵌入槽，分别经K-means量化得到8个SID token，避免残差量化的层级误差，同时将用户行为序列替换为SID压缩上下文，可在有限窗口内保留更多交互信号
- 双任务对齐LLM：新增<T2S>（文本转SID）和<S2T>（SID转文本）任务微调Qwen3-0.6B，冻结原词表仅优化SID特殊token嵌入，让LLM具备理解和生成SID的能力
- 生成阶段采用先SID后文案的双输出结构，中间插入特殊分隔符，训练目标为SID预测损失加文案生成损失的加权和；合并高频n-gram为单个token，进一步降低计算成本
- 在线推理时将生成的Top20个SID编码为偏好向量，与原有用户特征加权融合后进行ANN检索，生成的文案可按需选择是否输出

### 关键实验
基于快手近10亿用户的推送点击日志训练，1.5亿用户参与14天A/B测试，对比基线为现有级联推送推荐pipeline；有效播放率相对提升8.50%，不满率相对下降37.70%，点击PV提升0.43%，DAU提升0.05%，同时长尾内容曝光占比提升0.9%，优化内容生态。

### 核心结论
生成式推荐在工业场景落地不需要追求端到端全替换，可通过轻量架构设计兼顾效果、可解释性与效率，通过信号融合的方式无缝对接现有链路大幅降低落地成本。
