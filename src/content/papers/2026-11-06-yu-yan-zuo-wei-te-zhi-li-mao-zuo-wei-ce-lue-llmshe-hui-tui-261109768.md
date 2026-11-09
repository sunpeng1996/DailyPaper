---
title: 'Language as Trait, Politeness as Strategy: Controlled Tests of Linguistic
  Effects in LLM Social-Deduction Agents'
title_zh: 语言作为特质、礼貌作为策略：LLM社会推理Agent的语言效应对照测试
authors:
- Yuchen Li
- Lisa Liu
- Runqi Zou
- Shuxuan Kuang
- Qingquan Zhang
- Julian Togelius
affiliations:
- Lingnan University
- New York University
arxiv_id: '2611.09768'
url: https://arxiv.org/abs/2611.09768
pdf_url: https://arxiv.org/pdf/2611.09768
published: '2026-11-06'
collected: '2026-11-09'
category: Agent
direction: LLM多Agent交互行为影响因素研究
tags:
- LLM Agents
- Multi-Agent Interaction
- Linguistic Feature
- Controlled Experiment
- Social Deduction
one_liner: 通过狼人杀多Agent对照实验验证语言复杂度、礼貌度几乎不影响其他LLM Agent的交互决策
practical_value: '- 做电商客服Agent、群聊带货Agent时，无需过度优化话术的礼貌度、复杂程度，核心传递清楚信息即可，节省话术调优成本

  - 多Agent协同任务（如投放策略复盘、选品评审Agent群）设计时，无需为Agent额外增加礼貌表达模块，降低推理开销

  - 多Agent交互效果评估时，可优先聚焦核心信息准确性，暂时排除话术风格类混淆变量，提升评估效率'
score: 7
source: arxiv-cs.CL
depth: abstract
---

### 动机
现有研究证实LLM对不同语言风格的回复存在偏见，但语言复杂度、礼貌度等非语义特征在长期多Agent交互场景下对决策的影响尚未得到量化验证。
### 方法关键点
基于LURK狼人杀多Agent框架，固定每轮发言的核心语义不变，仅改写发言的语言复杂度、礼貌策略，通过checkpoint重放做严格对照实验，控制其他变量完全一致。
### 关键结果数字
累计30场游戏、4335次重放实验显示：两种语言特征调整均未显著影响其他Agent对发言者的信任度，经多重比较校正后对投票、夜间行动等决策无显著影响；未校正的最大效应仅为偏离中性改写的语言风格会带来4pp的投票变动；自然交互中88%的面子威胁类发言均为直接表达，与角色无关。
