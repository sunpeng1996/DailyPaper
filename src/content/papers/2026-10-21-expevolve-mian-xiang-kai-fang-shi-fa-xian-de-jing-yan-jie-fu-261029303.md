---
title: 'ExpEvolve: Structuring and Reusing Experience for Open-Ended Discovery'
title_zh: 'ExpEvolve: 面向开放式发现的经验结构化复用框架'
authors:
- Yongqiang Chen
- Chenxi Liu
- Deyu Zou
- Zhenhao Chen
- Tongliang Liu
- Bo Han
- Kun Zhang
affiliations:
- MBZUAI
- Carnegie Mellon University
- Hong Kong Baptist University
- The Chinese University of Hong Kong
- The University of Sydney
arxiv_id: '2610.29303'
url: https://arxiv.org/abs/2610.29303
pdf_url: https://arxiv.org/pdf/2610.29303
published: '2026-10-21'
collected: '2026-10-22'
category: Agent
direction: 演化Agent · 经验复用与探索效率优化
tags:
- LLM Agent
- Evolutionary Algorithm
- Experience Reuse
- Multi-armed Bandit
- Scientific Discovery
one_liner: 从演化生成的程序中抽取高层想法因子指导探索，样本效率最高提升5倍
practical_value: '- 演化类Agent的经验复用不要只停留在整段代码/文案级，可通过对比高低分样本自动抽取可复用的高层策略因子（如推荐召回策略、广告出价规则），大幅提升样本效率

  - 可参考双槽位探索机制：固定比例槽位做随机探索保证多样性，剩余槽位用Multi-armed Bandit调度已验证的有效策略，平衡探索和业务收益

  - 效果停滞时的破局方法：自动识别当前高分样本的共有特征，强制在后续生成中屏蔽这些特征做差异化探索，避免陷入局部最优

  - 抽取的高层策略因子和LLM/具体任务解耦，可直接迁移到其他同类型演化场景，降低跨场景适配成本'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

### 动机
现有基于LLM的演化编码Agent（如AI Scientist）的程序突变多依赖表层启发式，缺乏持久控制单元，易陷入低层次细节修改，样本效率极低；科学发现本质是想法的叠加复用，现有方案无法抽象高层有效想法指导演化，导致搜索效率低、易陷入局部最优。
### 方法关键点
- 定义可跨程序复用的高层「想法因子」：即解释程序得分差异的可解释机制属性（如优化策略、初始化方法），通过对比当前因子无法解释的高低分程序对，由LLM自动提取候选因子并验证有效性后存入记忆库
- 双层探索-利用机制：固定比例槽位沿用基线的随机探索保证多样性，剩余槽位将想法因子转化为编辑动作，用Multi-armed Bandit（UCB策略）调度动作引导LLM生成程序，奖励按同代随机探索的得分标准化消除跨代偏差
- 停滞期主动探索：当连续多代无效果提升时，自动识别当前高分样本共有的背景因子，屏蔽依赖这些因子的动作，强制探索差异化策略打破局部最优
### 关键结果
- 测试集：11个开放式数学发现任务、MLS-Bench的6个机器学习任务
- 对比基线：SCS、ShinkaEvolve、OpenRSI
- 核心指标：相同200次评估预算下，样本效率最高提升5.0×；在所有数学任务上效果超过基线，适配DeepSeek、GLM、Gemini等4款LLM均稳定增益；集成到OpenRSI后在6个MLE任务上全部取得效果提升，最高提升0.109

演化类Agent的效率提升核心是从低层次的样本复用升级到高层可解释的策略因子复用，而不是盲目增加搜索预算。
