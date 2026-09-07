---
title: 'Embedding Surgery: Localized Updates for Adaptive Ranking Correction in Dense
  Retrieval'
title_zh: 嵌入手术：稠密检索中自适应排序修正的局部更新方法
authors:
- Maddalena Amendola
- Antonio Mallia
- Raffaele Perego
affiliations:
- IIT-CNR
- Seltz
- ISTI-CNR
arxiv_id: '2609.05110'
url: https://arxiv.org/abs/2609.05110
pdf_url: https://arxiv.org/pdf/2609.05110
published: '2026-09-04'
collected: '2026-09-07'
category: RecSys
direction: 稠密检索 · 反馈驱动排序自适应修正
tags:
- Dense Retrieval
- Ranking Correction
- Relevance Feedback
- ANN Index
- Embedding Adaptation
one_liner: 通过反馈驱动的局部嵌入微调实现稠密检索实时排序矫正，无需重训模型或重构向量索引
practical_value: '- 电商搜索/推荐召回bad case修复可直接复用该方案：遇到局部排序错误时，仅调整相关item的embedding即可生效，无需重训双编码器或全量重构向量索引，大幅降低bad
  case修复成本

  - 可灵活对接三类业务反馈源触发修正：运营审核的人工标注、用户点击/ dwell time等交互信号、LLM生成的伪相关性标签，适配不同业务的反馈获取能力

  - 向量索引工程实现可复用in-place更新方案：针对HNSW/IVF等主流ANN索引，小幅度embedding修改直接原地覆盖即可，无需调整索引结构，实测性能损失可忽略

  - 可与现有CoRocchio等query侧自适应方法组合使用，在可靠反馈场景下获得额外收益，同时比纯query侧方法更抗噪声反馈'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
当前稠密检索系统的文档embedding均离线预计算并存入静态索引，无法快速适配用户反馈、实时意图漂移或业务规则调整；重训双编码器+全量重构向量索引的成本极高，无法满足即时修复bad case、动态调整排序优先级的业务需求。

### 方法关键点
- 将排序修正建模为凸二次优化问题：仅调整当前query召回结果中涉及排序错误的文档embedding，最小化embedding修改幅度的同时，满足反馈给出的pairwise排序约束（如相关文档需排在非相关文档前）
- 支持三种修正模式：对称调整（相关/非相关文档embedding均微调）、仅晋升相关文档、仅降级非相关文档，实测对称模式效果最优
- 兼容三类反馈触发源：人工标注、用户交互信号、LLM生成的伪相关性标签

### 关键结果
在7个IR基准数据集上覆盖4种主流稠密检索模型测试：
- 人工标注反馈下，DL-Hard数据集nDCG@10最高相对提升60.64%，跨域Robust04数据集最高相对提升56.71%
- 1000次完美用户点击反馈下，DL-Hard最高提升25.98%，近随机噪声反馈下无性能下降
- 对56k MS MARCO查询全量修正后，HNSW/IVF索引原地更新仅0.38%的向量跨IVF簇漂移，下游任务无统计显著性能损失
- 与CoRocchio组合使用时，完美反馈下nDCG@10额外提升1pct

**最值得记住的结论**：针对检索bad case的局部修正，优先做文档embedding的微小调整，无需动模型或索引，成本极低收益显著
