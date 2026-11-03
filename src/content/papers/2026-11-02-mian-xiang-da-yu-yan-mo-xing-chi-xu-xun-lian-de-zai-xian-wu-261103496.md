---
title: Online Label-Free Gradient Matching for Continual Language Model Training
title_zh: 面向大语言模型持续训练的在线无标注梯度匹配方法OLGA
authors:
- Sajjad Pakdamansavoji
- Mohammad Reza Rezaei
- Ilija Subasic
- Pedro Garzon
- Radu Paradovschi
- Zhao Chen
affiliations:
- Upwork Inc
arxiv_id: '2611.03496'
url: https://arxiv.org/abs/2611.03496
pdf_url: https://arxiv.org/pdf/2611.03496
published: '2026-11-02'
collected: '2026-11-03'
category: Training
direction: 大模型持续训练 · 无标注数据集蒸馏
tags:
- Continual Learning
- Dataset Distillation
- Gradient Matching
- Label-free Training
- Online Learning
one_liner: 提出无标注可流式梯度匹配蒸馏框架OLGA，大幅降低大模型持续训练成本
practical_value: '- 电商/推荐场景LLM持续微调可复用无标注梯度蒸馏逻辑：基于线上无标注用户行为/交互数据蒸馏出极小训练集，无需标注即可完成模型迭代，大幅降低全量重训成本

  - 流式数据更新场景借鉴cascaded merge的rehearsal memory设计：每次仅合并新到batch与现有记忆蒸馏，无需留存全量历史数据，适合推荐/广告排序模型的实时更新

  - 小样本微调场景优先用「先采样粗筛+后蒸馏」混合管线：先用低成本采样将数据压缩到中等规模再做梯度匹配蒸馏，比直接蒸馏提速30%，精度损失不到1个百分点'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
面向C端的LLM应用（电商智能客服、推荐Query理解、交互Agent等）需要持续适配用户偏好、热点话题、安全规则的分布漂移，但全量重训累计数据的成本过高。现有基于梯度匹配的数据集蒸馏方法依赖人工标注、仅支持静态数据快照、大数据量下运行效率低，无法落地到线上流式无标注场景。
### 方法关键点
- 无标注梯度匹配损失：基于冻结LLM的next-token预测概率计算PMI，抽取每个分组区分度最高的token构造软标签，替换人工标注实现无标注蒸馏
- 在线流式蒸馏架构：维护滚动rehearsal memory，每个新到batch先单独蒸馏，再和现有记忆合并重蒸馏，无需保留全量历史数据，单步计算成本恒定
- 混合压缩管线：极端压缩场景先做低成本无监督采样粗筛，将大数据集压缩到中等规模后再做梯度匹配蒸馏，平衡运行速度与精度
### 关键结果
在SST-2、IMDB等5个文本分类基准上基于phi-1.5测试：离线场景仅用5个蒸馏样本，精度比最优选择基线高10.2个百分点；在线流式场景stream-AUC比最强基线高6.6个百分点；混合管线相比纯蒸馏提速30%，平均精度损失仅0.9个百分点。
最值得记住的结论：极端压缩场景下合成蒸馏样本的信息密度远高于真实样本选择，小预算持续微调优先采用蒸馏方案，大预算场景可搭配采样降低成本
