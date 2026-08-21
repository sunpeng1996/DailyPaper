---
title: 'FlowEvo: Self-Evolving Agents through the Co-Evolution of Workflows and Executable
  Skills'
title_zh: FlowEvo：基于工作流与可执行技能协同进化的自进化Agent框架
authors:
- Zeyu Ren
- Ling Yue
- Ran Li
- Yishu Wang
- Shengxiang Xu
- Hanmo Liu
- Shaowu Pan
- Shimin Di
affiliations:
- Southeast University
- Rensselaer Polytechnic Institute
- The Hong Kong University of Science and Technology
arxiv_id: '2607.21596'
url: https://arxiv.org/abs/2607.21596
pdf_url: https://arxiv.org/pdf/2607.21596
published: '2026-08-19'
collected: '2026-08-21'
category: Agent
direction: Agent自进化 · 工作流-技能协同进化
tags:
- Agent
- Self-Evolution
- Workflow
- Executable Skill
- Training-Free
one_liner: 无需训练的Agent框架，通过工作流与可执行技能协同进化提升效果与推理效率
practical_value: '- 可直接复用工作流转可执行技能的编译逻辑，将推荐/搜索场景中重复出现的成功交互链路（如类目导航、优惠券核销路径）封装成可调用技能，降低重复推理的token成本

  - 借鉴分层技能复用机制：兼容任务直接调用执行+相似任务做prompt上下文参考两种模式，适配电商Agent的客服、导购等不同任务场景的复用需求

  - 可直接落地负向技能抑制逻辑：通过对比验证持续淘汰会带来负迁移的技能，避免推荐/Agent系统的历史经验反而降低新场景效果

  - 该框架完全无需训练，仅需推理侧内存更新即可实现能力迭代，适合中小厂快速落地自进化Agent业务，无需额外训练资源'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM Agent单次推理生成的工作流执行后即被丢弃，无法沉淀可复用能力；已有的技能库多为离线人工构建，无法从Agent自身执行轨迹中动态迭代，导致Agent反复生成相似执行逻辑，既推高token成本，也无法实现无训练的持续能力进化。

### 方法关键点
- 训练-free的工作流-技能-工作流闭环：仅将验证通过的成功工作流编译为结构化技能，包含可执行主体、调用接口、验证测试、元数据四类信息，存入持久化技能库
- 分层技能复用路由：任务与技能匹配度达标时直接执行技能，匹配度不足时将技能作为结构化上下文引导新工作流生成，两种模式自动切换
- 技能生命周期治理：引入对比效用评估，持续跟踪每个技能的下游效果，自动抑制/淘汰带来负迁移的技能，避免技能库膨胀或引入噪声

### 关键结果
基于GPT-4o-mini统一底座，在ALFWorld、HumanEval、MBPP、GSM8K、MATH-500共5个标准基准上对比8个SOTA基线：ALFWorld准确率达85.6%，较最强基线高26.4个百分点，token消耗仅为基线的1/3；跨10个7B~671B参数底座的50组模型-数据集对比中，49组优于ExpeL基线，平均精度提升11个百分点； ablation实验显示技能复用环节贡献了41.8个点的精度提升。

> 最值得记住：Agent推理侧可执行技能积累对小参数模型的增益远高于大模型，是低成本落地高效果Agent的核心路径。
