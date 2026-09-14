---
title: 'Beyond Top-k Skill Retrieval: Diversity-Aware Skill Routing for LLM Agents'
title_zh: 超越Top-k技能检索：面向LLM Agent的多样性感知技能路由
authors:
- Wang Wei
- Tiankai Yang
- Samyadeep Basu
- Hongjie Chen
- Yue Zhao
- Zhengzhong Tu
- Xiyang Hu
- Franck Dernoncourt
- Ryan A. Rossi
- Hoda Eldardiry
affiliations:
- Virginia Tech
- University of Southern California
- Adobe Research
- Dolby Labs
- Texas A&M University
arxiv_id: '2609.05824'
url: https://arxiv.org/abs/2609.05824
pdf_url: https://arxiv.org/pdf/2609.05824
published: '2026-09-04'
collected: '2026-09-14'
category: Agent
direction: Agent技能路由 · 多样性感知子集选择
tags:
- LLM Agent
- Skill Routing
- DPP
- Diversity-aware Retrieval
- Reranking
one_liner: 提出基于DPP与查询残差核的多样性感知技能路由框架，提升多技能任务的技能集覆盖效果
practical_value: '- 电商Agent工具/技能库路由场景可直接复用DSR的「检索+重排+DPP子集选择」pipeline，替换原有top-k选技能逻辑，适配多步骤客服、智能运营等复合任务

  - 推荐/搜索的多样性重排场景可借鉴查询残差核设计：先移除物品/内容表征中与query对齐的分量再算相似度，避免误惩罚同query相关的互补内容

  - 工程实现上，DPP贪心MAP推理配合增量Cholesky更新，仅在召回的top-50候选上计算，额外开销极低， latency敏感的在线业务也可落地'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM Agent技能路由多采用独立打分的top-k检索逻辑，当技能库规模达数万级、用户请求需要多个互补技能时，易返回大量冗余技能浪费有限上下文窗口，甚至遗漏任务必需的非重叠技能；普通多样性重排方法会将和查询共同相关的互补技能误判为冗余施加惩罚，无法满足多步骤任务需求。
### 方法关键点
- 沿用成熟的检索-重排pipeline：先用双编码器从全量技能库召回top-M候选，再用点wise重排器输出每个候选的相关性质量分
- 提出查询残差多样性核：先移除技能表征中与查询对齐的分量，混合原始表征后再计算技能间相似度，避免惩罚同查询相关的互补技能
- 基于DPP建模子集选择目标，采用贪心MAP算法+增量Cholesky更新高效生成兼顾相关性与非冗余的技能集，最终按质量分排序输出
### 关键实验
基于SkillRouter基准（包含8万+候选技能、75个专家标注查询，其中51个为多技能查询），对比强基线SkillRouter：全查询集Recall@20从0.754提升至0.768，Full Coverage@20从0.560提升至0.573；多技能查询收益更显著，Recall@20从0.704升至0.739，Full Coverage@20从0.458升至0.492，@50截断下Full Coverage提升达9.3个百分点。
### 核心结论
技能路由不应仅被视为相关性排序问题，更要作为互补技能集的选择问题来优化。
