---
title: 'Multi-Decoder OneRec: Controllable Generative Retrieval for Multi-Objective
  Industrial Recommendation'
title_zh: Multi-Decoder OneRec：面向工业多目标推荐的可控生成式召回
authors:
- You Wang
- Zhao Liu
- Guoping Tang
- Yiqing Yang
- Shuo Su
- Jing Liu
- Naifu Zhou
- Xiaoyou Zhou
- Wei Jiang
- Jian Liang
affiliations:
- Kuaishou Technology
arxiv_id: '2607.26500'
url: https://arxiv.org/abs/2607.26500
pdf_url: https://arxiv.org/pdf/2607.26500
published: '2026-07-29'
collected: '2026-07-30'
category: GenRec
direction: 生成式推荐 · 多目标可控召回
tags:
- Generative Retrieval
- Semantic ID
- LoRA
- Multi-Objective Recommendation
- Constrained Beam Search
one_liner: 基于共享基座+LoRA分目标专家+配额约束波束搜索的工业级多目标生成式召回框架
practical_value: '- 架构选型：可复用共享用户编码器+通用Semantic ID生成基座，每个新增目标仅需添加轻量LoRA专家+专属BOS+SID嵌入残差，参数增量仅20%，大幅降低多目标建模的迭代和维护成本

  - 训练trick：采用梯度隔离策略，基座仅用曝光样本NTP更新，各目标专家仅接收自身监督信号的梯度，同时加KL正则锚定通用SID分布，避免生成非法ID和负迁移

  - 推理优化：上线MD-CBS策略，按业务优先级给各分目标分配召回配额，已生成的SID前缀（可配置粒度）对后续路径做屏蔽，在固定召回预算下最大化候选互补性，避免预算浪费

  - 目标适配：连续反馈类目标（如观看时长、GMV、转化）不要用二值化SFT，改用基于用户历史归一化的相对奖励做RL优化，能充分利用细粒度反馈信号提升效果'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业推荐传统多路线召回为每个业务目标配置独立通路和配额，虽可控但随目标增多会出现建模、训练、部署严重碎片化问题；单解码器生成式召回实现了统一建模，但不同目标策略耦合，候选重叠度高，无法同时满足多目标优化和配额可控的核心需求。
### 方法关键点
- 架构：共享用户上下文编码器+通用解码器基座，每个目标对应独立LoRA专家，仅新增专属BOS、SID嵌入残差、LoRA参数，梯度隔离避免不同目标更新相互干扰
- 训练：基座用全曝光样本NTP更新；离散反馈目标（点赞、长看）用过滤后样本SFT更新对应专家；连续反馈目标（观看时长）用用户历史归一化的相对奖励做KL正则化的RL优化
- 推理：MD-CBS按业务优先级给各目标分配召回配额，已生成的SID前缀（默认全ID层级）对后续路径屏蔽，最后通用解码器补全剩余配额，最大化候选多样性
- 开源Kwai26数据集：包含13.1亿条item级记录、3185万Item-ID、2503万有效Semantic ID，配套标准拆分和评测协议
### 关键结果
离线Kwai26数据集相同512召回预算下，较单解码器OneRec基线，4个Recall@512指标提升1.69%~5.62%；巴西快手生产A/B测试，单设备使用时长+0.37%、7日留存+0.19%、新内容冷启动效果+2.09%，全量业务指标显著提升。
**最值得记住的结论**：生成式召回可以通过「共享基座+隔离专家+协同解码」的设计，同时实现统一建模、目标可控、候选互补三大工业级核心需求。
