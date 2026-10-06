---
title: 'TasteVal: Measuring the Experimental Research Taste of AI Systems Against
  Human Experts'
title_zh: TasteVal：对标人类专家的AI系统实验研究品味评估基准
authors:
- Oliver Jaffe
- Dane Sherburn
affiliations:
- P-Zero Research
arxiv_id: '2610.06824'
url: https://arxiv.org/abs/2610.06824
pdf_url: https://arxiv.org/pdf/2610.06824
published: '2026-10-05'
collected: '2026-10-06'
category: Eval
direction: 大模型能力评估 · 研究能力基准构建
tags:
- Benchmark
- LLM Evaluation
- Research Agent
- Compute Efficiency
- Task Isolation
one_liner: 提出衡量AI实验研究品味的基准TasteVal，验证前沿模型已超过人类专家基线
practical_value: '- 可复用「compute multiplier」量化思路，将推荐算法迭代能力定义为相同效果下与基线方案的算力消耗反比，优化团队算法迭代效率评估标准

  - 可直接套用「Researcher+Coder」的Agent分工架构，隔离实验设计与工程实现能力，落地推荐算法自动化迭代的多Agent系统

  - 「固定问题→迭代实验→结果反馈→预算约束」的评估闭环可复用，适配电商推荐A/B实验的自动化效果评估场景'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
现有大模型评估体系侧重通用能力，缺乏对AI系统实验研究品味（问题选择、实验设计、结果解读能力）的量化基准，无法支撑AI研发自动化的能力跟踪与进度预测。
### 方法关键点
将实验研究品味量化为compute multiplier：相同得分下，与人类专家串行实验算力消耗的反比；搭建8个AI研发相关开放式任务，采用「被测模型作为Researcher设计实验+固定Coder Agent实现并返回结果」的隔离架构，排除编码能力干扰，设置40 H100小时或120 wall-clock小时预算上限，以24位人类专家的最优成绩为基线。
### 关键结果
最优模型Opus 5.5的compute multiplier达2.3x，超过人类专家基线，单轮成本仅为专家平均的1/30；2025年12月后前沿模型compute multiplier每3个月翻一倍，远快于此前的14个月周期，最终性能每14.6个月翻一倍。
