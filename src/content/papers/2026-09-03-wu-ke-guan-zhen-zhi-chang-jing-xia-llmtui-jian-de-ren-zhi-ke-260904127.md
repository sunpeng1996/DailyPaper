---
title: 'Epistemic Warrant for LLM Recommendations: Characterizing the Basis for Reliance
  When Ground Truth Is Unavailable'
title_zh: 无客观真值场景下LLM推荐的认知可靠性分级评估框架
authors:
- Shai Vardi
- João Sedoc
affiliations:
- University of South Florida
- New York University
arxiv_id: '2609.04127'
url: https://arxiv.org/abs/2609.04127
pdf_url: https://arxiv.org/pdf/2609.04127
published: '2026-09-03'
collected: '2026-09-04'
category: Eval
direction: LLM推荐 · 无真值可靠性评估
tags:
- LLM Reliability
- Recommendation Evaluation
- Epistemic Warrant
- Ground Truth Free
- LLM Trust
one_liner: 提出四层认知担保分级体系，无客观真值时量化单条LLM推荐的可依赖程度
practical_value: '- 电商导购/相似商品推荐等无明确最优解的场景，可复用T0-T3四层测试框架评估单条LLM推荐的可靠性，降低低质量推荐的透出率

  - 做LLM-as-a-Judge的排序/标注任务时，可叠加认知担保分数过滤低可靠性的Judge结果，实验显示加入担保后对人群共识的解释度比仅用 verbalized
  confidence 平均提升11%

  - Agent业务决策模块可内置该分级逻辑：Strong Warrant结果直接执行，Basic/Conditional Warrant结果加人工复核，No Warrant结果触发兜底策略，降低决策风险'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
当下LLM被广泛应用于业务决策、推荐、LLM-as-a-Judge等场景，但大量场景不存在即时可验证的客观真值，现有方法要么评估模型整体的鲁棒性、置信度，要么关注用户对模型的信任程度，缺少针对单条推荐的可依赖程度的量化方法，也无法明确推荐的适用边界，用户很难判断是否该采信某条具体的LLM输出。

### 方法关键点
- 从认知理论引入epistemic warrant（认知担保）概念，根据推荐的稳定性和适用范围分为4个非补偿式等级：无担保、条件担保、基础担保、强担保
- 设计四层分层测试：T0测相同prompt重复生成的偏好稳定性，T1测语义等价改写（如选项换序、同义替换）下的偏好不变性，T2测合理子场景下的偏好一致性，T3测扩展相关场景下的偏好一致性，前一级测试不通过直接归为低等级，高等级无法补偿低等级的失败
- 搭建自动化流水线：用辅助LLM自动生成各层测试用的改写prompt，批量测试目标LLM的偏好变化，自动映射到4级担保等级

### 关键结果
基于100条无真值的二选一推荐prompt（覆盖22个领域），测试OpenAI、Anthropic、Llama三个系列共7款LLM：
- 人工标注验证生成的测试prompt层级匹配度达72%~98%，符合设计预期
- 担保等级和人群共识正相关，6款模型达到统计显著，强担保推荐的人群共识匹配度比无担保高40%以上
- 担保等级提供的信息显著独立于verbalized confidence和决策难度，加入担保后对人群共识的解释度平均提升11%

最值得记住的一句话：LLM推荐的可依赖程度不能只看模型表达的置信度，要从重复稳定性、改写鲁棒性、场景适用范围三个维度综合评估，才能在无真值场景下有效降低决策风险。
