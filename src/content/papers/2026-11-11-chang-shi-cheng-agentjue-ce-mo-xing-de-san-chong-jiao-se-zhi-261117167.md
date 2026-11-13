---
title: Actor, Judge, or Teacher? Understanding Decision Models in Long-Horizon Agents
title_zh: 长时程Agent决策模型的三种角色：执行者、裁判与教师的能力解析
authors:
- Haochen Liu
- Qianhao Zhu
- Zixuan Wang
- Dingming Li
- Tongbo Chen
- Peng Qiu
- Yingqi Qu
- Weiming Lu
- Jun Xiao
- Yongliang Shen
affiliations:
- Zhejiang University
- Baidu Inc.
arxiv_id: '2611.17167'
url: https://arxiv.org/abs/2611.17167
pdf_url: https://arxiv.org/pdf/2611.17167
published: '2026-11-11'
collected: '2026-11-13'
category: Agent
direction: 长时程Agent · 决策模型多角色复用
tags:
- Decision Model
- Long-Horizon Agent
- GRPO
- LLM-as-Judge
- Reinforcement Learning
one_liner: 揭示决策模型执行能力差仍可做优质教师，给出最优裁判与教师配置方案
practical_value: '- 做Agent训练的模型选型时，无需优先评估监督模型的执行能力，先测其全轨迹下单步贡献的打分能力即可，可大幅降低选型成本

  - 给GRPO等强化学习框架做步级监督时，优先采用「全轨迹上下文+单步贡献提问」的决策模型打分配置，比仅用最终结果奖励的效果提升显著，可直接复用在电商导购、搜索交互Agent的训练流程中

  - 小参数Agent采用低成本决策模型的过程监督训练，效果可超过仅用结果奖励训练的大参数模型，落地时可大幅降低推理侧成本

  - 若需决策模型作为在线执行者，不要仅依赖提示词标注依赖关系，直接将目标拆为有序子目标输入，效果远好于增加依赖提示'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
过往决策模型大多仅被用作Agent的实时行动执行者，表现不佳就直接被淘汰，其作为裁判、训练教师的价值完全被低估；同时长时程Agent的GRPO训练长期缺乏低成本步级奖励信号，仅靠最终结果奖励的信用分配粒度过粗，效果天花板低。

### 方法关键点
- 将同一款决策模型映射为三种角色对比：Actor（实时选择下一步动作）、Judge（给历史轨迹的动作打分，变量为2种上下文：仅看动作前轨迹Prefix/看全轨迹Hindsight，2种提问：任务最终是否成功Value/该动作是否推进目标Progress）、Teacher（打分结果加权进GRPO的优势函数，作为步级监督信号训练策略）
- 覆盖3款专用决策模型（JEV、Decider v1.2、GPT Decisions）、3款通用LLM的适配版本，在ALFWorld、WebShop两个长时程任务基准上做控制变量验证

### 关键实验结果
- 作为Actor时，所有模型在有顺序依赖的子目标任务上表现暴跌，JEV在无依赖任务成功率70.8%，有依赖任务仅14.7%，增加依赖提示的提升最多仅5.2%
- 作为Judge时，全轨迹+Progress提问的配置下，JEV对里程碑动作和无效动作的打分差达0.36，是Value提问配置的7倍，可精准区分动作价值
- 作为Teacher时，JEV采用最优配置训练Qwen2.5-1.5B，ALFWorld成功率从72.8%提升至82.9%，WebShop从56.8%提升至71.4%，单轮训练API成本仅22~30美元，训出的1.5B模型效果超过仅用结果奖励训练的7B模型

**最值得记住的一句话：决策模型的执行能力完全不代表其训练监督价值，只要提问与上下文配置合理，执行表现拉胯的模型也能教出远超自身水平的Agent**
