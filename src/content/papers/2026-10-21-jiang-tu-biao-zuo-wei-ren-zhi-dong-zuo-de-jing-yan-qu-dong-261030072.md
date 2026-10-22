---
title: Charts as Epistemic Actions for Experience-Driven Agentic Data Analysis
title_zh: 将图表作为认知动作的经验驱动智能体数据分析框架
authors:
- Xinzhe Wang
- Xudong Weng
- Zang Li
- Shaolei Zhang
affiliations:
- Tencent
- Renmin University of China
arxiv_id: '2610.30072'
url: https://arxiv.org/abs/2610.30072
pdf_url: https://arxiv.org/pdf/2610.30072
published: '2026-10-21'
collected: '2026-10-22'
category: Agent
direction: Agent 数据分析推理优化
tags:
- Data Agent
- Chart Reasoning
- Experience Distillation
- ReAct
- Knowledge Base
one_liner: 无微调LLM参数，通过蒸馏轨迹经验让数据Agent按需调用图表提升分析性能
practical_value: '- 电商运营/商品分析类Agent可复用「场景-表征方式」匹配规则：时序/异常分析用图表、精确数值核对用文本，直接提升分析准确率

  - 无参数微调的受控轨迹蒸馏+验证门构建领域经验库的方案，可直接迁移到业务Agent能力迭代，大幅降低训练成本

  - 做电商数据看板自动生成、用户增长分析报告产品时，可直接复用论文中图表/文本适用场景划分结论，优化可视化选型逻辑'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有ReAct架构数据Agent的推理完全依赖文本表征，而人类分析师会通过图表发现文本摘要遗漏的趋势、异常特征；当前Agent即便被开放绘图权限，也不会自主根据场景按需调用，存在明显的能力与使用gap。
### 方法关键点
- 构建PROBEBENCH含200个受控分析任务，验证得图表在时序变化、模式识别、异常检测类任务上表现优于文本，精确数值查询、条件验证类任务文本表现更优
- 提出CHARTMIND框架，全程不改动LLM参数，从多条件受控轨迹中蒸馏两类经验：分析经验Eana指导操作选型与验证，表征经验Erepr指导何时调用文本/图表或二者结合
- 引入轨迹裁判对结果打分、对步骤做有效性标注，只有提升验证集性能的经验才通过验证 gate 进入冻结知识库，推理阶段Agent按需读取经验库决策
### 关键结果
在DAComp-DA、DDR-Bench、DSBench三个公开基准、4款LLM backbone上测试，相比匹配基线整体得分提升1.0~5.46分，可视化指标平均提升7.48分，原本几乎不使用图表的GPT-5.6 Luna的可视化得分提升达19.95分。
### 核心结论
图表不是数据分析的最终输出产物，而是可嵌入推理循环的核心认知动作，合理匹配场景选择表征方式能在无微调前提下大幅提升Agent分析能力
