---
title: 'COGENT: A Modular Cognitive Architecture for Agentic User Simulation'
title_zh: COGENT：面向智能体用户模拟的模块化认知架构
authors:
- Yikun Chi
- Adam Davies
- Debarati Das
- Lin Ai
- Scott Counts
affiliations:
- Stanford University
- Microsoft
arxiv_id: '2611.31559'
url: https://arxiv.org/abs/2611.31559
pdf_url: https://arxiv.org/pdf/2611.31559
published: '2026-11-23'
collected: '2026-11-25'
category: Agent
direction: Agent 认知架构 · 用户行为模拟
tags:
- User Simulation
- Cognitive Architecture
- LLM Agent
- Behavior Fidelity
- Interactive System
one_liner: 基于认知理论搭建模块化可干预用户模拟架构，大幅提升人类交互行为拟合保真度
practical_value: '- 搭建用户模拟系统时可复用模块化拆解思路，不用依赖超长Prompt堆人设，拆分为感知、记忆、用户属性、意图、动作选择5个独立模块，仅修改对应组件即可调整模拟行为，比如调整frustration属性就能模拟不同耐心的电商用户，无需重写整体Prompt

  - 评估交互类Agent（电商导购Agent、客服Agent等）时，用该架构模拟用户比通用计算机用Agent的动作拟合精度高6个百分点，可降低模拟用户与真实用户的偏差，提升评测结果可信度

  - 做电商用户路径流失分析时，可复用该架构的认知拆解逻辑，将用户点击序列对应到感知、记忆、决策模块，定位流失原因是未感知到入口、无操作流程记忆还是意图未匹配

  - 产品无障碍优化阶段，替换感知模块即可模拟色弱、视力障碍等用户的交互行为，无需大量招募真实用户，降低前期验证成本'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有LLM用户模拟方案存在两类核心缺陷：一是单一人设Prompt无明确认知机制，可干预性、可解释性极差，无法追溯行为成因；二是通用计算机用Agent仅优化任务完成率，不拟合人类真实行为路径，与真实用户行为偏差大，无法支撑交互体验评估、界面优化、Agent评测等场景的需求。
### 方法关键点
- 参考ACT-R认知理论与Norman行动循环，拆解为感知、认知、控制、动作推理、执行5个独立模块，模块间通过记忆库、情境模型、用户属性三个共享存储交互，边界清晰可独立替换
- 支持三类可追溯干预：编辑记忆库调整用户知识储备、修改用户属性（谨慎度、挫败感等稳定特质/动态状态）、替换单个处理模块，单变量调整可直接对应到行为变化
- 动作决策全链路可溯源，明确区分动作来自记忆中的预设流程、界面感知到的控件，还是探索性操作
### 关键实验
- AgentNetBench（100项桌面交互任务）：COGENT人类动作预测准确率达59.8%，比面向用户模拟的基线CUA-USER高6.1个百分点，动作类型分布JS距离仅0.0445，远低于基线的0.121
- A11y-CUA（43项无障碍交互任务）：COGENT与人类动作序列的归一化Levenshtein距离为0.511，比基线CUA-USER低16.5%
- SENSE-42：用户内部状态关联结构与人类自我报告的秩相关系数达0.86，匹配度极高
### 核心结论
用户模拟的核心不是完成任务，而是复现人类完成任务的路径与认知逻辑，模块化认知架构相比单一人设Prompt可实现更高保真、更可控的用户模拟
