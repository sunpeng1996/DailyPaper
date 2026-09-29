---
title: Measuring and Mitigating Identity-Cue Preference Drift in LLM-based Recommender
  Systems
title_zh: LLM推荐系统中身份特征偏好漂移的度量与缓解方法
authors:
- Zhuoxiong Gan
- Qiang Dong
affiliations:
- University of Electronic Science and Technology of China
arxiv_id: '2609.34229'
url: https://arxiv.org/abs/2609.34229
pdf_url: https://arxiv.org/pdf/2609.34229
published: '2026-09-28'
collected: '2026-09-29'
category: GenRec
direction: 生成式推荐 · 偏好漂移缓解
tags:
- LLM4Rec
- Prompt Bias
- Post-hoc Reranking
- Preference Drift
- Fairness
one_liner: 提出无训练的PromptShift框架，度量并缓解LLM推荐中身份提示引发的偏好漂移
practical_value: '- 线上LLM推荐可直接复用PromptShift后序重排逻辑，无需微调LLM，仅通过历史交互构建分人群item热度表即可落地，开发成本极低

  - 可复用Drift、SliceShift两个指标做线上巡检，快速识别prompt中身份属性（如性别、年龄、消费层级）带来的非预期推荐偏移

  - 用户分群干预强度可自适应：对历史偏好贴合群体特征的用户保留原LLM排序，对偏好小众的用户压低群体热门item权重，平衡个性化与公平性

  - 对合规要求高的电商场景，可基于该框架避免身份特征导致的推荐刻板印象，降低合规风险'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
LLM推荐系统多依赖用户交互历史生成结果，但prompt中嵌入的用户身份属性（如性别、年龄）会在用户行为完全不变的情况下，让推荐结果偏向对应人群的共性模式，现有方法既无法量化这种漂移的幅度和方向，也没有低开销的缓解方案，还无法与普通prompt措辞带来的波动区分开，严重影响推荐的个性化准确性与公平性。

### 方法关键点
- 设计两个漂移度量指标：Drift（用RBO计算带身份提示的推荐列表和仅用历史的基准列表的排序差异，度量漂移幅度）、SliceShift（计算列表中item在对应身份人群的相对热度差，度量漂移是否朝向群体共性），同时引入同义改写prompt作为基线，排除普通prompt措辞敏感度的干扰
- 训练无关的自适应后序重排策略：基于历史交互构建身份分组-item热度表，根据用户历史行为在所属群体的主流程度动态调整重排权重，在原LLM排序和逆群体热度信号间做插值，仅调整排序后段，保留头部高置信结果
- 提出Difficulty@K指标，奖励命中群体中冷门且排序靠前的相关item，更精准衡量小众偏好挖掘能力

### 关键实验结果
在MovieLens 1M、Last.fm 1K两个数据集上，用GPT-5.6 Terra、Gemini 3.1 Pro、Qwen3-8B三个LLM验证，相比原始带身份提示的推荐结果，PromptShift将宏观平均SliceShift降低62.42%，同时Difficulty@20提升22.3%、HitRate@20提升5.0%、MRR@20提升5.4%，仅NDCG@20略有下降（1.8%）。

最值得记住的结论：LLM推荐的prompt中加入的客观身份属性并非中性输入，即使不给出任何偏好引导，也会系统性地让推荐结果偏向所属群体的共性模式，这一偏移可通过无训练的后处理手段低成本缓解。
