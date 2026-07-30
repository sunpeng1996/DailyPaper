---
title: 'SkillRise: Agentic Reinforcement Learning for Cross-Task Skill Evolution'
title_zh: SkillRise：面向跨任务技能演化的智能体强化学习框架
authors:
- Zhiyuan Yao
- Yuxin Chen
- Zhengxi Lu
- Zishan Xu
- Yueqing Sun
- Yifu Guo
- Yuquan Lu
- Zhengzhou Cai
- Kangning Zhang
- Zhuowen Han
affiliations:
- Zhejiang University
- National University of Singapore
- Shanghai Jiao Tong University
- Meituan
arxiv_id: '2607.26784'
url: https://arxiv.org/abs/2607.26784
pdf_url: https://arxiv.org/pdf/2607.26784
published: '2026-07-28'
collected: '2026-07-30'
category: Agent
direction: Agent 跨任务技能演化强化学习
tags:
- Agentic RL
- Cross-task Transfer
- Skill Evolution
- Policy Optimization
- LLM Agent
one_liner: 端到端强化学习框架实现LLM智能体跨任务技能自动提取与复用，兼顾性能与训练效率
practical_value: '- 电商导购Agent、搜索推荐多场景优化可复用跨任务序列构造方法：将同品类/同需求族的任务按难度排序，让智能体从简单任务积累的技能迁移到复杂任务，提升多场景泛化性

  - 做技能提取类RL优化时可复用解耦信用分配机制：任务求解用当前任务reward监督，技能整理用后续任务的discounted reward监督，避免多阶段归因难问题，同时省去复杂的skill
  bank管理开销

  - 电商场景交互Agent可直接复用论文的技能提炼prompt模板：将交互轨迹抽象为通用操作流程、避坑点，过滤实例化冗余信息，可直接提升跨商品类别的任务成功率

  - 轻量化Agent部署可优先尝试该范式：SkillRise性能增益随模型规模放大更明显，1.7B到4B规模即可比基线高3-6个百分点，适配业务侧小模型落地需求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM Agent的强化学习大多将任务视为独立episode，浪费可复用的共性经验；已有的技能学习方法要么仅适配单任务重复训练，要么采用技能提取、检索、执行多阶段耦合的pipeline，归因难度高、训练开销大，无法支撑智能体跨任务持续进化。
### 方法关键点
- 跨任务序列构造：将同任务族的差异化实例按难度从低到高排序，为技能迁移提供清晰的学习信号
- 单策略双角色轮动：同一LLM策略交替执行「当前任务求解」和「技能文档更新」，仅靠动态演化的文本技能文档传递跨任务信息，无需额外外部记忆库、检索模块
- 解耦跨任务信用分配：任务求解阶段仅用当前任务reward监督，技能整理阶段用后续所有任务的discounted reward监督，再基于同序列位置、同角色的分组计算相对优势做PPO优化，避免两类任务的学习信号混淆
### 关键结果
在ALFWorld、WebShop（电商导购基准）、ScienceWorld三个基准测试，基于Qwen3-4B骨干，对比ReAct、Reflexion、GRPO、GiGPO等基线，Pass@1分别达到85.9%、84.4%、54.6%，较最强基线GiGPO分别高出2.3、7.1、8.5个百分点；训练开销仅为多阶段技能学习pipeline的1/4~1/6，测试时相关任务序列越长性能越高，且跨任务训练得到的技能策略可直接适配单任务多轮重试场景，Pass@3较基线最高提升14.2个百分点。
### 最值得记住
跨任务技能学习不需要复杂的多阶段管理pipeline，端到端监督技能整理对后续任务的增益即可实现高效的技能迁移与智能体持续进化
