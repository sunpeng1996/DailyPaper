---
title: 'AgentSSL: Can MLE Agents Leverage Unlabeled Data?'
title_zh: AgentSSL：MLE智能体利用无标注数据的半监督学习框架研究
authors:
- Ethan Lin
- Akanksha Sarkar
- Ziang Liu
- Kristin Branson
- Jennifer J. Sun
affiliations:
- Cornell University
- Howard Hughes Medical Institute
arxiv_id: '2611.17323'
url: https://arxiv.org/abs/2611.17323
pdf_url: https://arxiv.org/pdf/2611.17323
published: '2026-11-12'
collected: '2026-11-13'
category: Agent
direction: Agent 半监督学习程序自动搜索
tags:
- Agent
- Semi-Supervised Learning
- Program Search
- MLE Agent
- Low-Resource Learning
one_liner: 提出AgentSSL将SSL转化为程序搜索问题，12个场景中8个优于人工设计的SOTA基线
practical_value: '- 电商推荐冷启动/低标注场景可复用AgentSSL思路：将半监督策略的组合优化转化为程序搜索问题，无需人工针对场景调参，自动适配商品/用户数据分布

  - 低资源场景下标注预算分配可参考结论：当无监督选择指标失效时，将50%标注预算用于候选模型选择，比全量用于训练的精度提升最高可达26%

  - 生成式推荐/LLM4Rec低资源微调场景，可直接复用本文的8种无监督指标集成方案，作为模型排序的代理目标，降低对验证集的依赖

  - 智能体设计可复用经验：优先选greedy搜索策略平衡精度与速度，需探索更多SSL组合方案时选择进化搜索提升策略多样性'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有MLE智能体仅在全监督场景下验证效果，实际业务（如电商冷启动、科学计算）中普遍存在标注稀缺、无标注数据丰富的情况，而传统SSL方法需要大量人工针对场景调参，落地成本高，亟需探索智能体自动发现适配场景的SSL策略的可行性。

### 方法关键点
- 提出AgentSSL两阶段框架：第一阶段程序发现，基于LLM生成可执行的SSL程序，用无监督指标或少量标注的噪声验证信号作为反馈迭代优化；第二阶段程序选择，从候选池中选最优程序，支持无监督选择、主动标注选择两种模式。
- 覆盖全SSL方法搜索空间：支持伪标签、一致性正则、自训练、对比学习等10类经典与现代SSL方法的组合与适配，内置greedy、MCTS、进化三种搜索策略。
- 开源ProgramSelectBench基准：包含16977个人工/智能体生成的SSL程序，覆盖10000+GPU小时的计算结果，用于低标注场景下程序选择方法的评估。

### 关键结果
在6个SSL基准数据集12个低标注设置下，对比FixMatch、SoftMatch、FineSSL等6个人工设计的SOTA基线，AgentSSL在8个设置下性能更优，最高提升21.8%；当无监督选择指标失效时，将50%标注预算用于主动选择，比全量用于训练的精度最高提升26.07%；在真实生态检测任务中，仅用10%标注的AgentSSL效果接近全量标注的专家基线。

### 最值得记住的一句话
随着智能体生成候选程序的成本不断降低，半监督学习的核心瓶颈已经从策略设计转向低标注场景下的最优策略选择。
