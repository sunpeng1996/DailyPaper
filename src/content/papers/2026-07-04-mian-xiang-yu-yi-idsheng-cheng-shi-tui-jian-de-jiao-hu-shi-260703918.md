---
title: 'Beyond Item Order: Temporal Gap Tokenization for Generative Recommendation
  with Semantic IDs'
title_zh: 面向语义ID生成式推荐的交互时间间隔Token化方法
authors:
- Chengkai Huang
- Tianqi Gao
- Hongtao Huang
- Quan Z. Sheng
- Lina Yao
affiliations:
- University of New South Wales
- Macquarie University
- CSIRO’s Data61
- Independent Researcher
arxiv_id: '2607.03918'
url: https://arxiv.org/abs/2607.03918
pdf_url: https://arxiv.org/pdf/2607.03918
published: '2026-07-04'
collected: '2026-07-07'
category: GenRec
direction: 生成式推荐 · 交互时序间隙建模
tags:
- Generative Recommendation
- Semantic ID
- Sequential Recommendation
- Temporal Modeling
- Tokenization
one_liner: 提出轻量时序增强框架ChronoSID，为语义ID生成式推荐引入交互间隔建模
practical_value: '- 可直接复用时间间隔离散化trick：按log尺度将交互间隔分为<1h、1h-1d、1d-1w、1w-1mo、≥1mo共5个固定区间，生成gap
  token交错插入Semantic ID序列作为编码器输入，几乎不增加解码成本，适配所有SID类生成式推荐架构

  - 物品预训练阶段可叠加TA-FAMAE辅助损失：在原有掩码特征重构目标外增加时间间隔预测辅助任务，默认权重λ=0.1，无需修改原有量化流程即可增强物品表示的时序相关性

  - 回流用户场景优先适配：长交互间隔场景下增益更显著，可直接叠加到现有冷启动/回流用户召回链路，不需要重构SID生成全流程

  - 部署成本低：训练overhead仅7%-29%，推理latency增加约25%，性能提升稳定，适合线上业务快速迭代上线'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有Semantic ID（SID）类生成式推荐仅将用户行为序列建模为静态物品ID的有序拼接，完全忽略交互之间的时间间隔；而数据显示用户同品类购买率随交互间隔增长显著下降，间隔信息直接反映兴趣连续性与漂移程度，时序信息的缺失大幅限制了生成式推荐的效果，尤其是长间隔回流用户的预测准确性。

### 方法关键点
- 两阶段时序增强设计，完全兼容现有SID生成范式，不改动量化流程：
  1. 表示层：提出TA-FAMAE预训练目标，在原有掩码特征重构任务基础上增加辅助的交互间隔预测损失（默认权重λ=0.1），正则化物品表示的时序相关性
  2. 序列层：将交互间隔按log尺度离散为5个固定gap token，与每个物品的SID三元组交错作为T5编码器输入，解码器仍生成目标物品SID，不增加解码负担

### 关键实验结果
在8个Amazon品类数据集上对比ReSID、TIGER等SID生成式基线及SASRec、BERT4Rec等传统序列推荐模型，所有数据集上性能均最优：相比基线ReSID，R@5最高提升11.5%（Industrial & Scientific领域），长间隔（≥1个月）回流场景增益更突出；训练overhead仅7%-29%，推理latency增加约25%，对热门/冷门物品均有提升，冷门物品N@10最高提升13.59%。

### 核心结论
低成本的时间间隔token注入即可为SID类生成式推荐带来全场景稳定增益，无需重构架构即可适配业务中用户兴趣漂移、回流召回等典型场景。
