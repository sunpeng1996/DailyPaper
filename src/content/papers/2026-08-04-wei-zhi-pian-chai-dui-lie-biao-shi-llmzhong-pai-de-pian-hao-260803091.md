---
title: Position Bias Undermines Preference Consistency in Listwise LLM-Based Reranking
title_zh: 位置偏差对列表式LLM重排的偏好一致性影响研究
authors:
- Ethan Bito
- Yongli Ren
- Estrid He
affiliations:
- RMIT University
arxiv_id: '2608.03091'
url: https://arxiv.org/abs/2608.03091
pdf_url: https://arxiv.org/pdf/2608.03091
published: '2026-08-04'
collected: '2026-08-05'
category: RecSys
direction: LLM推荐重排·位置偏差与一致性评估
tags:
- LLM4Rec
- Listwise Reranking
- Position Bias
- Ranking Consistency
- Permutation Invariance
one_liner: 提出三级偏好一致性评估框架，证明仅修正边际位置曝光无法保证LLM列表重排的排列不变性
practical_value: '- 评估LLM重排器不能仅依赖HR、nDCG等效果指标，需补充PPI、GPI、LOC三类一致性指标，避免推荐结果随候选输入顺序随机波动损害用户体验

  - 位置偏差 mitigation 方案可按需选型：对一致性要求高的场景优先选SGS方案，对效果要求高且允许一定结果波动的场景可选STELLALW方案

  - 不要迷信边际曝光平坦等价于解决了位置偏差：即使曝光曲线完全平坦，也可能存在严重的偏好不一致问题，必须做排列扰动测试验证鲁棒性

  - 工程上可直接复用开源的InvariRank评估工具，快速检测现有LLM重排模块的排列一致性水平'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
LLM作为列表式重排器已成为两阶段推荐pipeline的常用方案，但候选集作为无序集合，其序列化输入的顺序扰动会导致重排结果波动，违反排序函数的基本有效性假设。现有位置偏差研究多关注最终排序效果或边际位置曝光差异，未从偏好结构层面量化扰动影响，也未明确效果、曝光偏差与排列一致性的关联。

### 方法关键点
- 构建三级一致性评估体系：1) Pairwise Preference Instability（PPI）：衡量候选配对偏好随输入位置的波动幅度；2) Global Preference Inconsistency（GPI）：量化多排列下的偏好系统与最优全局排序的匹配度；3) Listwise Output Consistency（LOC）：用Kendall’s τ统计不同排列下输出排序的相似度
- 新增边际位置曝光偏差指标，对比其与三类一致性指标的关联性
- 重排结果直接从候选标记的token log概率提取，消除解码随机性和解析误差的干扰

### 关键实验
基于MovieLens-32M、Amazon Books数据集，测试3款主流开源指令微调LLM，对比4种重排方案：
- STELLALW的HR@5比Zero-shot最高提升6.9pct，但PPI最高达0.89（为最优方案SGS的4倍以上），LOC最低仅0.06，一致性表现最差
- SGS的PPI最低至0.19，LOC最高达0.83，一致性表现最优，同时HR@5略优于Zero-shot
- 三类一致性指标的排名高度对齐，但与HR@5、边际曝光偏差结果完全解耦

### 核心结论
仅提升推荐相关性或平坦边际位置曝光，无法保证LLM列表重排的偏好稳定性和输出一致性，必须同时评估效果和排列一致性两类指标。
