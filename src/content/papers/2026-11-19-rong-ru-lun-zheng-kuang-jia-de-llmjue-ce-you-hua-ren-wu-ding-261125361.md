---
title: 'Incorporating argumentation frameworks for LLM decision-making: Task-specific
  design and evaluation'
title_zh: 融入论证框架的LLM决策优化：任务定制化设计与评估
authors:
- Bochen Han
- Anshu Xiong
- Mingyang Ma
affiliations:
- 中国科学院数学与系统科学研究院
- 中国科学院大学数学科学学院
arxiv_id: '2611.25361'
url: https://arxiv.org/abs/2611.25361
pdf_url: https://arxiv.org/pdf/2611.25361
published: '2026-11-19'
collected: '2026-11-20'
category: Reasoning
direction: LLM推理增强 · 形式化论证框架适配
tags:
- Argumentation_Framework
- LLM_Decision_Making
- Fact_Verification
- RAG
- Debate_Reasoning
one_liner: 提出四阶段论证增强LLM决策工作流，推出适配辩论/事实核查的Qnt-Arg与Qlt-Arg定制方法
practical_value: '- 做Agent多轮辩论/群体决策场景时，可复用Qnt-Arg的speaker条件化论证构建+gradual semantics打分逻辑，替代简单投票提升多Agent意见汇总准确率，尤其适合不确定度高的决策场景

  - 做RAG类事实核查/电商商品评价可信度评估时，可复用Qlt-Arg的证据可信度导向冲突排序+grounded semantics过滤逻辑，对召回的冲突评价/资讯做优先级排序，降低RAG幻觉

  - 论证增强方案必须做任务适配：辩论类用定量论证+先验打分，检索类用定性论证+证据过滤，不要盲目套用统一框架，跨任务使用会出现明显性能下降

  - 可复用论文的四阶段论证工作流（构建→评估→语义推理→决策）做现有LLM决策模块的增强，不需要全替换，可分步嵌入先验打分、证据过滤等子模块'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有LLM处理多视角冲突信息（辩论、多源检索证据）时存在确认偏差，直接推理准确率低；现有论证增强LLM方法无任务适配逻辑，跨场景性能波动大，甚至优于不使用论证框架的基线，亟需针对性设计论证框架与LLM的结合规则。

### 方法关键点
- 抽象出通用四阶段论证增强工作流：论证构建→可接受性评估→形式化语义推理→决策
- 针对辩论类决策推出Qnt-Arg：围绕发言人生成对应论证，结合决策模型输出的候选答案先验，用gradual semantics聚合论证强度与关系权重，输出最终决策
- 针对检索类事实核查推出Qlt-Arg：将召回证据作为论证，用可信度得分确定冲突证据的攻击方向，用grounded semantics筛选可接受证据，连同可信度标注一起输入LLM做最终判断

### 关键结果
- 辩论任务：在6个公开辩论数据集上，对比Direct LLM、CoT、ArgLLM等基线，Qnt-Arg总体准确率达78.41%，比最强直接基线高1.42pp，比直接LLM推理高4.03pp
- 检索事实核查任务：在3个公开数据集上，对比RAG LLM、ArgRAG等基线，带GE过滤的Qlt-Arg在所有Top5/Top10检索设置下均优于RAG LLM，AVeriTeC Top10准确率达80.50%，DeepFact-Bench Top5准确率达87.50%

### 最值得记住的一句话
形式化论证框架与LLM结合必须做任务适配，没有通用的最优方案，要根据任务特性选择论证构建逻辑、语义规则与模型分工。
