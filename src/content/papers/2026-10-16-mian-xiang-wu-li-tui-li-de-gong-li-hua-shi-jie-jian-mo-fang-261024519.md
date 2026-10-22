---
title: Axiomatic World Modeling for Physics Reasoning
title_zh: 面向物理推理的公理化世界建模方法
authors:
- Xinye Yang
- Zhenyang Liu
- Yuxuan Wang
- Yuanyuan Lei
affiliations:
- Northwestern University
- University of Florida Department of Physics
- University of Florida Computer & Information Science and Engineering
arxiv_id: '2610.24519'
url: https://arxiv.org/abs/2610.24519
pdf_url: https://arxiv.org/pdf/2610.24519
published: '2026-10-16'
collected: '2026-10-22'
category: Reasoning
direction: LLM推理优化 · 公理化世界建模
tags:
- World Modeling
- Reasoning
- Reinforcement Learning
- LLM
- Reward Design
one_liner: 提出双层奖励的RLAWM框架，缓解LLM物理推理的建模漂移问题，大幅提升精度与泛化能力
practical_value: '- 可复用分层奖励设计到电商规则型Agent场景：先校验Agent对用户需求、业务规则的理解是否正确，再校验执行路径合规性，减少前提层面的幻觉传播

  - 建模奖励的schema抽取+规则F1打分思路，可迁移到用户意图理解模块：将query解析为结构化意图实体，和规则库匹配打分，降低意图识别错误对下游推荐/搜索的负面影响

  - 针对RL训练多样性坍塌的优化思路：不限制具体推理/生成路径，仅约束核心前提与合规性，适合生成式推荐的RL调优，兼顾规则对齐与生成多样性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM在物理推理任务中存在严重的建模漂移问题：模型会静默篡改问题参数、虚构物理定律、新增未声明假设，在与真实设定不符的内部世界模型中推理，而现有RLVR、PRM等奖励方法仅监督最终结果或步骤局部正确性，无法约束前提层的建模错误，导致推理精度低、泛化性差。

### 方法关键点
1. 提出RLAWM框架，训练阶段强制模型输出[建模]和[求解]两个结构化模块，推理阶段无额外计算开销；
2. 建模奖励$R_M$：按固定schema从模型输出的公理化世界模型中抽取三类motif，与问题真实设定计算F1得分，直接监督模型对齐问题前提；
3. 求解奖励$R_S$：将模型输出的推理伪代码转换为可执行实例，通过复用的物理规则模板校验不变量、轨迹一致性、扰动响应合理性，监督推理过程符合公理约束；
4. 联合奖励由$R_M$、$R_S$、答案正确性奖励$R_A$加权组合，共同优化模型。

### 关键实验结果
在PhysReason数据集上SubPass@1相比最强基线最高提升+12.2个点，PHYSICS数据集提升+5.2个点；奥赛级物理题零泛化性能是基线的2.45倍，跨域迁移到AIME 2026数学题比最强RLVR基线高+10个点；同时解决了传统RL方法的多样性坍塌问题，SubPass@k随采样数k增长持续提升。

### 核心结论
对于有明确公理/规则约束的推理场景，先对齐前提模型再校验执行过程的分层奖励设计，远比对步骤或结果直接打分的效果更好，且泛化性更强。
