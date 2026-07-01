---
title: 'The Organizational Behavior of Agentic AI: Collective Intelligence in Human-Agent
  Workflows'
title_zh: 智能体AI的组织行为：人-Agent工作流中的集体智能
authors:
- Canhui Liu
affiliations:
- University College London
arxiv_id: '2606.30986'
url: https://arxiv.org/abs/2606.30986
pdf_url: https://arxiv.org/pdf/2606.30986
published: '2026-06-29'
collected: '2026-07-01'
category: Agent
direction: 多Agent协作 · 人-Agent工作流优化
tags:
- MultiAgent
- Human-Agent Collaboration
- Collective Intelligence
- Contextual Transaction Cost
- Agent Architecture
one_liner: 提出上下文交易成本框架，验证Agent原生协作架构效率远高于模仿人类的组织形式
practical_value: '- 搭建业务多Agent系统不要直接模仿人类团队的层级/委员会/流水线架构，优先选择blackboard共享内存、自适应元组织两类Agent原生架构，可大幅降低上下文损耗

  - Agent调度可直接复用Contextual Transaction Cost (CTC)量化公式，加权计入token消耗、语义漂移、交接损耗、验证成本，替代单纯用输出质量做调度的逻辑

  - 多Agent系统不需要堆数量提多样性，优先做模型异构、检索源异构、工具能力异构，避免伪多样性带来的冗余成本，开源模型场景下收益更明显

  - 人-Agent协作业务（如电商审核、工单处理、素材生产）要做明确接口层，强制Agent输出带溯源证据的trace，对齐人类问责需求，不要盲目上多Agent流程'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
当前多Agent系统常照搬人类组织的层级、委员会、流水线等形态，但Agent不具备人类的动机、身份、信任等社会属性，盲目模仿往往带来大量无意义的上下文损耗，反而降低协作效率；同时行业缺乏统一的量化框架解释人-Agent协作的效率差异，难以指导落地设计。

### 方法关键点
- 提出**Contextual Transaction Cost (CTC)** 作为核心机制，量化Agent间上下文传递的token开销、交接损耗、压缩损失、语义漂移、验证成本、治理成本之和，构建集体效率评估指标，同时纳入任务质量、成功率、全链路成本；
- 覆盖三类实验：8000个合成知识工作任务的仿真对比7类Agent组织形态、4类真实LLM任务（代码修复、长文档QA、法律审核、文献综述）的trace分析、鲁棒性校验（prompt变体、开源模型、无prompt DQN调度器）。

### 关键实验结果
- 仿真实验中，Agent原生架构（自适应元组织、blackboard共享内存）比人类模仿型架构（流水线、层级、委员会）效率高395.26%，自适应架构相对单Agent效率提升89.24%，委员会类模仿架构效率反而比单Agent低90%以上；
- 真实LLM任务中，商业大模型单Agent效率最高，复杂高风险任务下blackboard架构质量高2.2个百分点但CTC提升10倍；开源模型场景下自适应架构相对单Agent质量提升7.32个百分点；
- 结构化共享内存协作支持最多10个Agent的有效规模，自由文本辩论类协作最优规模仅为1个Agent。

### 核心结论
多Agent系统的效率不取决于组织形态和Agent数量，而取决于上下文传递的损耗是否低于分工、并行、验证带来的收益。
