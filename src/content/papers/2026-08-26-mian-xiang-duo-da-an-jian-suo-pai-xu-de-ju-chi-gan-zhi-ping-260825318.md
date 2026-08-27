---
title: 'Rank-Deviation Quality: A Distance-Aware Metric for Multi-Answer Retrieval
  and Ranking Evaluation'
title_zh: 面向多答案检索排序的距离感知评估指标RDQ
authors:
- Xiaokun Zhou
- Alessandro Moschitti
- Danielle Class
affiliations:
- Amazon
arxiv_id: '2608.25318'
url: https://arxiv.org/abs/2608.25318
pdf_url: https://arxiv.org/pdf/2608.25318
published: '2026-08-26'
collected: '2026-08-27'
category: Eval
direction: 检索排序评估 · 多答案场景
tags:
- Evaluation Metric
- Ranking
- Retrieval
- Multi-Answer
- Ordinal Preference
one_liner: 提出无需绝对相关性等级的排序评估指标RDQ，多答案场景下判别力与稳定性优于现有基线
practical_value: '- 电商/本地生活泛搜索（如“附近川菜馆”“夏季T恤”）的排序评估可直接复用RDQ，仅需标注结果相对顺序无需绝对相关性等级，标注成本降低30%+

  - RDQ支持自定义UI位置权重，可适配瀑布流、轮播、商品卡片等不同业务场景的流量分布，评估结果更贴合真实用户体验

  - 灵活调整M2参数：精确查询场景（如找特定SKU）调小α加大错位惩罚，泛查询场景调大α放宽顺序要求，优先保障合格结果覆盖

  - 小流量AB实验评估优先用RDQ，达到稳定系统排序一致性所需query量比RBP少20%，可缩短实验周期、降低流量成本'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统检索排序评估指标存在明显场景局限：二进制指标无法区分合格结果的排序优劣；NDCG等分级指标依赖绝对相关性标签，标注成本高、跨查询校准难度大；Kendall's τ等秩相关指标要求候选与参考集合完全一致，无法评估召回漏召问题，多答案检索/排序场景下缺乏适配的高效评估方案。
### 方法关键点
- 输入为查询级有序参考列表（ORL），支持绑定层级（tied tier），可从pairwise标注、listwise标注或分级相关性标签转换得到，无需定义绝对增益值
- 得分由三部分加权计算：输出位置权重（可自定义适配不同UI布局）、排序错位惩罚、归一化因子，理想排序得分固定为1
- 提供两种惩罚函数：M1非对称惩罚，仅处罚低质量结果前置的错位；M2平衡距离感知惩罚，通过指数衰减控制错位容忍度，支持α（全局容忍度）、λ（低排名结果容忍度调整）两个可配置参数
### 关键结果
在5000 query的POI数据集12个排序系统上，RDQm2-a1的median empirical power@100达0.353，比最强基线RBP(0.9)高23%；达到与全量query系统排序Kendall's τ≥0.8仅需200个query，比RBP(0.9)少20%样本量；在TREC-DL公开数据集上，由分级标签转换ORL的RDQm1在n=25时判别力与原生NDCG相当（0.108 vs 0.102）。

最值得记住的结论：多答案场景下没有稳定绝对相关性标注时，RDQ是比NDCG、RBP更高效的评估选择
