---
title: 'MultiAgent-OPD: End-to-End Training of Hierarchical Multi-Agent Systems with
  On-Policy Distillation'
title_zh: MultiAgent-OPD：基于On-Policy蒸馏的层次多智能体端到端训练
authors:
- Yuhan Sun
- Jiaxin Zhao
- Yongdong Luo
- Yibo Hu
- Meiguang Jin
- Junfeng Ma
- Weixun Wang
- Weihang Pan
- Zhongan Bi
affiliations:
- Alibaba Group
- Zhejiang University
arxiv_id: '2610.23234'
url: https://arxiv.org/abs/2610.23234
pdf_url: https://arxiv.org/pdf/2610.23234
published: '2026-10-19'
collected: '2026-10-26'
category: Agent
direction: 多智能体训练 · On-Policy蒸馏
tags:
- Multi-Agent
- On-Policy Distillation
- GRPO
- Hierarchical Agent
- Reinforcement Learning
one_liner: 提出两阶段训练框架，用任务训练Teacher为搜索子Agent提供token级监督，端到端优化层次多智能体团队
practical_value: '- 做电商导购/搜索多Agent链路（需求理解+召回+文案生成）时，可复用两阶段训练思路：先训简单的检索-生成级联链路作为Teacher，再给层次系统的检索子Agent做token级OPD监督，避免仅用最终转化/点击奖励导致检索行为坍缩

  - 共享参数的多角色Agent训练时，不同角色可分配差异化奖励信号：规划类Leader用全局业务目标（GMV/转化率）奖励，检索/召回子Agent用预训练Teacher的局部蒸馏信号，生成类角色用候选内容正确性奖励，各角色更新共享参数时无冲突

  - 搜索类Agent的RL训练中，避免直接给检索子Agent分配全局最终奖励，易出现检索行为消失的训练坍缩，用任务适配后的Teacher做局部过程监督，训练稳定性和最终效果提升显著'
score: 8
source: huggingface-daily
depth: full_pdf
---

#### 动机
层次多Agent系统（Leader分配任务、子Agent执行）端到端训练存在核心信用分配难题：最终全局反馈只能间接指导子Agent的中间行为，用LLM Judge为子Agent打分又受限于Judge自身的推理偏差，且无法为序列决策提供token级细粒度指导，直接用全局奖励训练子Agent极易出现行为坍缩（比如检索Agent放弃搜索直接生成内容）。
#### 方法关键点
- 两阶段训练框架：Stage I 先训练简单的Searcher-Answerer级联链路，用答案正确性作为奖励，训练完成后冻结为Teacher模型；Stage II 端到端训练Leader-Searcher-Answerer层次多Agent团队，三个角色共享同一套LLM参数，通过角色prompt切换身份
- 角色差异化优势分配：Leader用团队最终成功奖励+少量搜索行为bonus做GRPO优化，Answerer用候选答案正确性奖励做GRPO优化；Searcher不使用全局最终奖励，改为用冻结Teacher对其生成的token做On-Policy蒸馏，将Teacher与当前学生策略的log概率差作为token级优势信号
#### 关键实验结果
在7个公开QA数据集上测试，MultiAgent-OPD的macro avg@4达38.68%，比用Prompted LLM Judge做子Agent监督的方案高4.06个百分点，比级联训练的C-MAS+RL高2.61个百分点；同时macro pass@4达48.73%，4次尝试全正确的比例达29.27%。消融实验证明，若直接给Searcher分配全局最终奖励，会出现检索行为完全消失的训练坍缩，macro avg@4骤降至17.78%。
#### 核心结论
在层次多Agent系统中，用简单链路预训练的任务专属Teacher给执行类子Agent提供细粒度局部过程监督，比仅用全局最终奖励或通用LLM Judge的训练效果更好、稳定性更高
