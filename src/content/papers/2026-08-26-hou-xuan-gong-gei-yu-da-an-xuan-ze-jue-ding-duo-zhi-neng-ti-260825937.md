---
title: Candidate supply and answer selection shape the value of LLM judging in multi-agent
  systems
title_zh: 候选供给与答案选择决定多智能体系统中LLM裁判的价值
authors:
- Jia-Hao Ji
- Sijie Li
- Jiabei Cheng
- Zixi She
- Jin-Tai Yu
- Zhiyuan Yuan
affiliations:
- 复旦大学华山医院
- 复旦大学类脑智能科学与技术研究院
- 上海交通大学自动化与智能感知学院
- 上海人工智能科学研究院
arxiv_id: '2608.25937'
url: https://arxiv.org/abs/2608.25937
pdf_url: https://arxiv.org/pdf/2608.25937
published: '2026-08-26'
collected: '2026-08-27'
category: Agent
direction: 多智能体推理 · LLM裁判优化
tags:
- Multi-Agent
- LLM Judge
- Answer Selection
- Reasoning
- Cost Efficiency
one_liner: 拆解多智能体推理的生成-选择瓶颈，明确LLM裁判生效的适用场景与成本边界
practical_value: '- 多Agent召回/生成场景可复用「候选供给率+LLM裁判+混合排序」架构：当候选池优质内容占比<62.5%时引入LLM裁判，收益优于纯多数投票；占比更高时直接用投票降低成本

  - 小候选池场景（如query改写、短文案生成，候选数≤6）优先加LLM裁判ROI最高；候选数≥16时新增裁判边际收益为负，可直接扩容候选池走投票

  - LLM裁判可靠性不是静态指标，需结合业务场景的生成模型、候选质量分布实测，不能直接套用通用基准得分

  - 电商搜索/推荐多路召回结果聚合场景，可参考rank-power加权规则，结合召回频率与LLM打分，平衡共识稳定性与小众优质内容召回率'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有多智能体系统常出现「已生成正确答案但最终输出错误」的问题，且优化时同时改动生成、通信、选择模块，无法归因性能收益，LLM裁判的适用边界也不清晰，导致多Agent落地的成本与收益无法量化。

### 方法关键点
- 将多智能体推理拆解为候选生成、信息演化、终端选择三个独立阶段，定义`pgen`为单问题全候选库的正确答案占比，量化候选供给水平
- 构建离线排名基准，用`rank AUC`衡量LLM裁判的排序可靠性，通过固定候选池重放排除动态通信干扰，单独评估选择规则效果
- 提出rank-power加权混合选择规则，通过参数`t`调节LLM裁判排序与候选频率的权重，平衡投票的统计稳定性与裁判的内容识别能力

### 关键结果
实验覆盖MMLU-Pro、GPQA、MedXpertQA、MuSR、HLE共5个基准，16278个问题，81390个固定候选池：纯多数投票准确率63.82%，混合规则（t=2~4）准确率达70.82~70.95%，相对提升7pp；候选池大小k=2时LLM裁判比多数投票高13.52pp，k=16时收益降为-0.34pp，边际成本从每千次正确$0.1涨到$6.28；当`pgen`<0.625时LLM裁判平均增益6~7.9pp，`pgen`>0.625时反而比投票低3.22pp。

最值得记住的一句话：多智能体系统的性能瓶颈往往不是生成能力不足，而是少数优质候选被多数错误选项淹没，LLM裁判的价值只在优质候选存在但占比偏低的场景下才会兑现。
