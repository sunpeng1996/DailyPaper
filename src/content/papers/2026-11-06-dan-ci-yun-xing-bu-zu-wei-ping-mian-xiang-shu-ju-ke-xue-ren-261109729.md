---
title: 'One Run Is Not Enough: A Monte Carlo Protocol for Evaluating LLM Reliability
  on Data Science Tasks'
title_zh: 单次运行不足为凭：面向数据科学任务的LLM可靠性蒙特卡洛评估方案
authors:
- Wenqi Ni
- Ozan Evkaya
- Miguel de Carvalho
affiliations:
- University of Edinburgh
arxiv_id: '2611.09729'
url: https://arxiv.org/abs/2611.09729
pdf_url: https://arxiv.org/pdf/2611.09729
published: '2026-11-06'
collected: '2026-11-09'
category: Eval
direction: 大语言模型评估 · 可靠性度量
tags:
- LLM Evaluation
- Monte Carlo
- Benchmark
- Reliability
- Data Science
one_liner: 提出DS-QA基准与三层评估框架，采用百次重复蒙特卡洛协议评测数据科学场景下的LLM可靠性
practical_value: '- 开发电商用户分析、营销归因、AB实验分析类LLM Agent时，不要仅验证单次输出准确率，需增加多次重复调用的一致性校验规则，避免随机错误导致业务决策偏差

  - 评估LLM代码生成能力（如推荐特征工程、人群圈选代码自动生成）时，可复用三层评估框架：先校验运行时长、冗余度等通用属性，再测可执行性、准确率等粗粒度指标，最后叠加业务自定义指标

  - LLM输出词冗余度每升0.1对应token消耗升0.013，可在Prompt中增加输出长度约束，既降低推理成本，也能减少输出波动'
score: 7
source: arxiv-cs.LG
depth: abstract
---

### 动机
现有LLM数据科学任务基准仅评估单次输出质量，忽略重复调用的一致性，无法度量真实落地场景下的可靠性，无法支撑高 stakes 决策类场景的选型。

### 方法关键点
1. 构建DS-QA基准，包含100道英国大学数据科学/统计试题，覆盖16个数据集、易/中/难3档难度
2. 设计三层评估体系：通用属性层（运行时长、冗余度、文本相似度）、粗粒度指标层（准确率、代码可执行性、完整性）、任务专属指标层
3. 采用蒙特卡洛评估协议，对同Prompt重复测试100次，同步评估输出质量与运行一致性

### 关键结果数字
数据可视化、监督学习类任务输出波动极大，中高难度下一致性问题尤为突出；词冗余度每提升0.1，token冗余度对应提升约0.013
