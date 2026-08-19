---
title: 'EvoTS-Agent: A Self-Evolving LLM Agent for Financial Time Series Change Point
  Detection'
title_zh: EvoTS-Agent：面向金融时间序列变点检测的自进化LLM智能体
authors:
- Lei Jiang
- Ye Wei
- Xinyu Xi
- Jordan Langham-Lopez
- Yifan Bao
- Raad Khraishi
- Yihao Ang
- Anthony K. H. Tung
- Lukasz Szpruch
- Hao Ni
affiliations:
- Alan Turing Institute
- University of Oxford
- National University of Singapore
- NatWest AI Research
- University of Edinburgh
arxiv_id: '2608.17933'
url: https://arxiv.org/abs/2608.17933
pdf_url: https://arxiv.org/pdf/2608.17933
published: '2026-08-18'
collected: '2026-08-19'
category: Agent
direction: Agent 自进化时序任务优化
tags:
- LLM Agent
- Time Series
- Change Point Detection
- Self-Evolution
- Auto Tuning
one_liner: 提出验证引导的自进化LLM Agent，通过三类进化算子实现金融时序变点检测效果优于现有同类Agent
practical_value: '- 可复用「验证反馈+三类进化算子（优化现有方案/切换策略/重组优质方案）」的架构，解决推荐/广告场景下非平稳时序指标的异常检测、分布漂移检测问题

  - 先做探索性数据分析刻画数据集特征再初始化候选模型的流程，可迁移到多场景自适应调参Agent的设计中，降低无效试错成本

  - 全流程可执行轨迹进化的设计思路，能提升业务Agent的执行成功率，可复用在需要自动调优模型/特征的生产场景'
score: 7
source: arxiv-cs.AI
depth: abstract
---

### 动机
金融时间序列具有非平稳、统计特性异质的特点，没有单一无监督变点检测算法能在不同资产、不同市场状态下保持稳定表现，传统流程重度依赖专家完成模型选择、特征设计、超参调优，扩展性和适配性受限。
### 方法关键点
1. 先执行定制化探索性数据分析，刻画数据集特征，初始化候选检测模型；
2. 基于三类互补算子进化可执行实验轨迹：Revision迭代优化当前最优方案，进度停滞时Alternative Strategy探索全新建模方向，Recombination整合高表现轨迹的互补优势；
3. 全程用验证反馈引导轨迹进化，自适应匹配不同数据集的统计特性。
### 关键结果
在4个基准数据集上效果持续优于现有LLM-based Agent，所有测试的骨干LLM上执行成功率达100%
