---
title: Values Shape What Self-Improving Coding Agents Build
title_zh: 施瓦茨价值观对自改进编码Agent性能与输出的影响
authors:
- Jason Liang
- Dylan Waldner
- Risto Miikkulainen
affiliations:
- Cognizant AI Lab
arxiv_id: '2611.23067'
url: https://arxiv.org/abs/2611.23067
pdf_url: https://arxiv.org/pdf/2611.23067
published: '2026-11-17'
collected: '2026-11-18'
category: Agent
direction: 自改进Agent 价值对齐与行为引导
tags:
- Self-improving Agent
- Value Alignment
- LLM Agent
- Code Generation
- Schwartz Values
one_liner: 验证固定价值观指令可显著改变自改进编码Agent的性能表现与生成代码的结构特征
practical_value: '- 自改进Agent的system prompt中可加入简洁的价值导向指令引导迭代路径，比如推荐系统召回策略迭代Agent可设置「优先尝试新结构」的开放型价值观提升泛化能力

  - 禁止Agent自行修改核心价值指令，实验显示开放价值修改会抹平不同价值观的性能差异，导致最优策略性能下降

  - 价值指令的措辞需人工设计验证，从文献自动蒸馏的价值观无性能增益，不同措辞框架（规则/结果/品格导向）效果差异显著

  - 任务开放度越高（如完全可编辑的推荐排序模型结构迭代），价值观引导效果越明显，仅调参场景价值引导作用有限'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有自改进Agent仅围绕任务结果优化，开放场景下缺乏对Agent优化路径的约束，易偏离设计者预期，此前无受控实验验证简洁价值指令对自改进Agent行为与性能的独立影响。

### 方法关键点
- 基于施瓦茨人类价值观理论设计4类价值指令：开放探索、保守稳定、自我提升、自我超越，与无价值观、无关文本安慰剂两组对照做对比
- 自改进循环每轮重置工作区并重新注入固定价值指令与安全规则，仅保留Agent提交的代码变更，禁止Agent修改核心指令
- 覆盖6类编码任务：ALE-Bench、圆形装箱、实体匹配、2048游戏、符号回归、SZ-俄罗斯方块，每类任务用独立的开发集与离线held-out集评估

### 关键结果数字
- 跨任务平均来看，开放探索价值观的held-out性能较无价值观组提升0.38个Cliff's δ，保守稳定价值观下降0.27个δ，二者头对头对比效果量达0.58个δ，统计显著性p<0.001
- 允许Agent自行修改价值观时，不同价值观的性能差异缩小3倍，最优的开放探索组性能显著下降，最差的保守组性能上升；从AI文献蒸馏的价值观无任何性能增益
- 开放探索组生成的代码复杂度平均比保守组高27%，held-out得分与代码复杂度的相关性远高于与API成本、运行时间的相关性

### 最值得记住的一句话
对于开放迭代的自改进Agent，人工设计的简洁价值指令是低成本、高收益的行为引导手段，其效果远好于自动蒸馏或允许Agent自行修改价值观。
