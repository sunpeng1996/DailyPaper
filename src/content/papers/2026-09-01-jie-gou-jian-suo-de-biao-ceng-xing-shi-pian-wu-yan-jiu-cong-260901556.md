---
title: 'Retrieved but not ranked: surface-form bias in structural retrieval, from
  mathematics to agent trajectories'
title_zh: 结构检索的表层形式偏误研究：从数学问题到智能体轨迹
authors:
- Nabira Rashid
- Manolis Kellis
affiliations:
- Independent
- MIT CSAIL
arxiv_id: '2609.01556'
url: https://arxiv.org/abs/2609.01556
pdf_url: https://arxiv.org/pdf/2609.01556
published: '2026-09-01'
collected: '2026-09-02'
category: Eval
direction: 结构检索评估 · 表层偏误诊断
tags:
- Structural Retrieval
- Surface Form Bias
- Reranking
- LLM-as-Judge
- Embedding Retrieval
- Agent Trajectory
one_liner: 跨数学与智能体轨迹双领域验证嵌入检索表层偏误，提出低成本词汇重排序诊断工具
practical_value: '- 做RAG/检索系统时，可先用低成本词汇重排序控制判断业务场景的表层变异类型：词汇重排序效果下降说明是对抗性变异（如商品标题恶意蹭关键词），效果提升则是偶发变异（如用户query改写），提前优化检索策略。

  - 结构匹配类检索任务（如Agent历史轨迹复用、同款不同描述的商品召回）不要完全依赖嵌入排序，加LLM重排序层可覆盖5%~76%的可恢复排序缺口。

  - LLM重排序选型不要盲目跨域复用效果结论：不同领域、不同query风格下最优LLM judge差异极大，甚至会出现效果排名反转，必须在业务数据上做小流量验证。

  - 上线RAG系统前必须验证检索增益的实际下游效果：如果业务使用的LLM零-shot能力已经接近天花板，即使检索精度再高也不会带来明显效果提升，避免做无用功。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有嵌入检索基准大多默认文本表层形式与语义一致，但结构检索场景（如同解法不同表述的数学题、同流程不同物体的智能体轨迹）下两者完全分离，此前单域研究无法区分偏误来自模型本身还是基准构造，亟需统一框架下的系统性验证。
### 方法关键点
- 跨两个完全无关领域采用统一测试协议：数学领域用MathNet-Retrieve的500条查询、11.7万条语料，分易/难两个伪装层级；智能体轨迹领域用ALFWorld衍生的118条查询、336条轨迹，分不同物体、不同物体+容器两个严格度层级。
- 统一Pipeline：先用嵌入模型召回全库Top10，再分别用朴素词汇重排序、3款独立LLM judge重排序，核心指标为可恢复缺口闭合率（重排序后Hit@1提升 / 嵌入召回Top10到Top1的潜在提升空间），所有结果带bootstrap 95%置信区间。
- 下游配对实验：对比零-shot、恶意检索、黄金检索三种条件下数学求解器的效果，定位检索增益的约束条件。
### 关键结果
- 数学领域难伪装层级下，两款生产级嵌入模型严格Hit@1均为0%，95.2%~99.8%的错排是因为Top1词汇相似度高于正确答案；词汇重排序拉低效果，LLM重排序可恢复5%~63%的缺口。
- 智能体轨迹领域要求黄金匹配不同物体+容器时，三款嵌入模型Hit@1全部低于随机概率；词汇重排序可闭合26%~36%的缺口，LLM重排序可闭合43%~76%的缺口。
- 下游实验中，黄金检索与恶意检索的求解效果无统计差异（McNemar p=0.678），核心原因是求解器零-shot在可完成问题上准确率达97%~100%，留给检索的提升空间几乎为0。

**最值得记住的结论**：嵌入检索永远优先匹配字面表层内容而非底层结构，没有通用的最优重排序方案，一切效果都要结合业务场景的表层变异类型验证。
