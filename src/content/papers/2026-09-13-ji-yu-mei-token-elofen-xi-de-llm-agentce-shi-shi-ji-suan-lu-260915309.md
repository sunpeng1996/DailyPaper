---
title: 'When Agents Slow Down: Understanding LLM Agents'' Test-Time Strategies via
  Elo-per-token Analysis'
title_zh: 基于每token Elo分析的LLM Agent测试时计算效率与优化研究
authors:
- Kaiyuan Liu
- Qiuyang Mang
- Bo Peng
- Wenhao Chai
- Hanchen Li
- Shreyas Pimpalgaonkar
- Luke Zettlemoyer
- Alex Dimakis
- Alvin Cheung
affiliations:
- UC Berkeley
- University of Washington
- Princeton University
- Bespoke Labs
arxiv_id: '2609.15309'
url: https://arxiv.org/abs/2609.15309
pdf_url: https://arxiv.org/pdf/2609.15309
published: '2026-09-13'
collected: '2026-09-15'
category: Agent
direction: Agent测试时策略 · 效率评估与优化
tags:
- LLM Agent
- Test-Time Scaling
- Elo Rating
- Compute Allocation
- Evaluation
one_liner: 提出Elo-per-token分析框架，揭示Agent测试时效率衰减规律，给出最优计算分配策略
practical_value: '- 电商/推荐场景的Agent（文案生成、选品优化、策略迭代类）可复用Elo-per-token框架度量不同测试时策略的token
  ROI，避免无意义的长上下文堆料

  - 长周期Agent任务（如用户画像挖掘、竞品分析）可先测量拐点预算，将总token拆为多个并行短会话，实测可提升200+Elo等效效果，降低推理成本

  - Agent策略设计需主动引入路径跳出机制（如定期重置上下文、引入外部候选方案），避免陷入局部最优解导致的效率衰减'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM Agent测试时会自适应分配计算（迭代调优、调用工具、回溯决策），但缺乏跨任务统一的性能-计算效率度量，无法指导测试时计算资源最优分配，也无法衡量Agent自适应策略相比随机采样的效率优劣。

### 方法关键点
- 提出**Elo-per-token**评估框架：基于Bradley-Terry模型对不同token预算下的任务最优解做跨任务归一化Elo打分，消除不同任务评分尺度非线性、单位不一致的问题
- 理论证明独立随机采样基准的Elo随log(计算量)线性增长，每10倍token预算提升400 Elo，作为Agent效率对比的统一基线
- 定义**scaling inflection point（缩放拐点）**：Agent边际Elo增益首次低于随机采样的token预算点，基于该点设计分配规则，将总预算拆为多个并行独立会话，每个会话跑满拐点预算后取最优解

### 关键实验结果
在4类开放基准（算法优化、GPU kernel优化、机器学习研究等）、4款主流Agent（GPT-5.5、Claude Opus 4.8、Gemini 3.5 Flash等）上测试，覆盖最高1亿token会话：
1. 所有Agent前期增益均超过随机采样，后期边际收益持续衰减，最终低于随机采样基线
2. 人类编程竞赛选手表现出超线性增益，在多天任务中显著超过饱和后的Agent
3. 基于拐点分配1亿token预算，在Polyomino Packing任务上比单长会话高+264 Elo，比10个短会话高+355 Elo

### 核心结论
当前LLM Agent的测试时策略存在路径依赖导致的效率衰减，超过拐点后拆分并行会话比拉长单会话的性价比高得多。
