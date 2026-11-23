---
title: 'Beyond Math, Code, and Logic: Do Reasoning Models Transfer to Scientific Argumentation?'
title_zh: 超越数学、代码与逻辑：推理模型能否迁移至科学论证场景
authors:
- Buse Sibel Korkmaz
- Antonio del Rio Chanona
affiliations:
- Amazon AGI
- Imperial College London
arxiv_id: '2611.27722'
url: https://arxiv.org/abs/2611.27722
pdf_url: https://arxiv.org/pdf/2611.27722
published: '2026-11-20'
collected: '2026-11-23'
category: LLM
direction: LLM推理 · 科学领域能力迁移
tags:
- Reasoning
- Scientific NLP
- Chain-of-Thought
- RLHF
- Multi-task Learning
one_liner: 系统评测LLM科学论证能力短板，提出推理感知训练框架让小模型追平前沿大模型表现
practical_value: '- 做垂直领域小模型时，可复用「推理感知蒸馏+多任务SFT+分权重RL」的三段式训练范式，无需盲目堆参数量即可逼近大模型效果，适合业务端低成本部署

  - 多任务训练时做样本均衡避免大任务梯度淹没有价值的小任务信号，该技巧可直接复用在电商多目标排序、多场景推荐训练中

  - RL阶段复合奖励加乘门控机制的设计，可迁移到Agent回复生成、商品文案生成、评论回复等场景，兼顾正确性、事实一致性和格式合规性

  - 分层拆解任务的评测思路，可复用在推荐系统能力评估上，从识别、生成到跨上下文推理分层拆解，避免单指标评估的片面性'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
当前推理型LLM在数学、代码、逻辑基准上表现优异，但科学论证场景需要领域方法论知识、证据强度评估、跨长上下文逻辑链维系能力，现有评测体系完全未覆盖该场景，且通用推理能力无法直接迁移，导致学术助理类Agent无法完成审稿回复、证据核验、观点辩论等高价值任务，存在明确能力缺口。

### 方法关键点
- 构建覆盖7项科学论证任务的分层评测体系：分为论点挖掘（声明检测、证据检测等4项分类任务）、论证生成（审稿 rebuttal生成、会议元综述生成2项生成任务）、跨语篇推理（多证据合成问答）三类，覆盖从识别到生成再到复杂推理的全能力维度
- 三段式训练框架：1）推理感知知识蒸馏：用Gemini 2.5 Flash作为教师，生成带<reasoning>标签的结构化推理链标注数据，强制推理过程绑定上下文、不直接泄露分类标签；2）多任务SFT：均衡各任务样本量，同时对推理链和最终答案计算交叉熵损失，避免大任务梯度淹没小任务信号；3）复合奖励GRPO训练：奖励包含答案正确性、逻辑一致性、证据归因、格式合规4部分，加乘门控机制强制满足推理深度和上下文覆盖要求，避免模型投机取巧刷指标

### 关键实验
在NSF-SciFy、SciFact、DISAPERE、ARIES等7个公开科学NLP数据集上评测，对比Llama3.2 1B/3B/8B、OpenAI o3、Gemini 2.5 Flash等基线，训练后的3B模型在立场检测任务上准确率超过o3（65% vs 49.5%）， rebuttal生成BERTScore达到0.85追平o3，参数规模仅为后者的几十分之一；移除CoT监督时复杂跨语篇任务BERTScore下降超40%，验证了推理脚手架的核心价值。

### 核心结论
有效的科学论证不是模型规模增大后的涌现能力，必须通过显式的推理感知训练才能获得。
