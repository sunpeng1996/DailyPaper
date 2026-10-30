---
title: 'WorkFactory: Turning Professional Intents into Executable Work for Scalable
  Agent Training'
title_zh: WorkFactory：将专业意图转化为可执行任务以规模化训练工作Agent
authors:
- Ziyang Zeng
- Tingyang Chen
- Jia Deng
- Qiyao Wang
- Shuo Tang
- Yike Yang
- Tao Ren
- Wayne Xin Zhao
- Feng Chang
- Jujie He
affiliations:
- IQuest Research
- Zhejiang University
- Renmin University of China
- Shenzhen Institutes of Advanced Technology
- Shanghai Jiao Tong University
arxiv_id: '2610.37161'
url: https://arxiv.org/abs/2610.37161
pdf_url: https://arxiv.org/pdf/2610.37161
published: '2026-10-26'
collected: '2026-10-30'
category: Agent
direction: Agent 规模化训练任务合成框架
tags:
- AgentTraining
- TaskSynthesis
- WorkAgent
- SFT
- ScalableTraining
one_liner: 提出WorkFactory框架规模化生成可执行专业任务，训出的WorkPilot系列Agent性能大幅超越基线
practical_value: '- 做垂直领域Agent训练时可复用「信息支持图反向规划+执行探针修复」的任务生成流程，避免任务缺失必要信息或泄露答案，大幅提升训练数据质量

  - 规模化训练Agent时可参考其数据缩放结论：小参数量模型前30K任务即可获得90%以上的性能增益，优先控制数据规模而非盲目堆量可降低训练成本

  - 电商/广告运营类Agent的任务合成可借鉴其多源意图生成逻辑：从岗位职责、技能文档、真实交付物三个维度生成任务，覆盖更全面的真实业务场景

  - 收集训练用的专家轨迹时，可参考其探针+教师独立执行的流程，减少轨迹中的无效操作，提升SFT监督信号的可靠性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
工作Agent的SFT训练需要大量高质量、可执行的专业任务，但现有合成任务普遍存在信息缺失、逻辑不一致、答案提前泄露等问题，导致教师执行的轨迹质量差，无法提供有效的监督信号，亟需可规模化生成高可用专业任务的框架。

### 方法关键点
- 多源意图合成：从职业分类、公开技能文档、真实专业交付物三个维度生成多样化专业意图，经LLM评审后留存符合真实工作场景的可行意图
- 信息支持图引导环境构建：从预期输出反向推导所需信息的依赖关系与存储位置，明确区分需提供给Agent的输入信息和需Agent推导的结果，避免答案泄露
- 执行探针修复：用独立探针Agent在仅可见输入的环境下尝试执行任务，诊断缺失/矛盾的信息点，在不改变任务核心目标的前提下修复环境缺陷，仅通过探针验证的任务进入下一步
- 高质量轨迹采集：用独立教师模型在干净沙箱中执行合格任务，过滤无效/不完整轨迹后转为SFT训练数据

### 关键实验
共构建112686个覆盖612个职业的任务，对Qwen 4B、27B、35B-A3B做SFT得到WorkPilot系列模型；在4个专业工作基准上全量超过对应基线，其中WorkPilot-35B-A3B在GDPval-AA v2.1上的Elo从基线的879提升到1565，WorkPilot-27B达到1612 Elo，接近前沿大模型水平；组件消融显示信息规划+探针修复的组合相比直接任务生成能让GDPval-AA Elo提升81分。

### 核心结论
Agent训练数据的质量远重于数量，高质量可执行任务配合可靠专家轨迹，能让中等参数量模型达到接近前沿大模型的任务执行性能。
