---
title: Can AI agents conduct open-ended AI research? Early evidence from two case
  studies
title_zh: AI Agent能否开展开放式AI研究？两个案例研究的早期证据
authors:
- Peter Kirgis
- Sayash Kapoor
- Andrew Schwartz
- Stephan Rabanser
- David Africa
- Konstantinos Voudouris
- Viet Nguyen
- Toby Pilditch
- Magda Dubois
- Harry Coppock
affiliations:
- Princeton University
- UK AI Security Institute
- University of Toronto
- UC Berkeley
- Stanford University
arxiv_id: '2607.27191'
url: https://arxiv.org/abs/2607.27191
pdf_url: https://arxiv.org/pdf/2607.27191
published: '2026-07-28'
collected: '2026-07-30'
category: Agent
direction: AI Agent 科研能力评估
tags:
- AI Agent
- Autonomous Research
- Evaluation
- Shadow Evaluation
- LLM Capability
one_liner: 提出影子评估范式，验证当前前沿AI Agent仅能完成AI研究工程环节，无法产出顶会级原创成果
practical_value: '- 做长周期Agent任务优化时，可对标文中5种故障模式（研究判断不足、缺乏创意解法、回溯能力差、资源感知弱、指令漂移）针对性加约束，比如强制探索期最小步数、预算使用率阈值告警、定期重置核心指令避免漂移

  - 落地Agent自迭代、自主优化类业务时，不要高估大模型顶层决策能力，需在方向选择、成果验收等关键节点加入人类审核，避免Agent在无价值方向消耗资源

  - 做Agent业务能力评估时，可复用影子评估思路：选取未公开的真实业务问题，由业务专家评审输出质量，比通用benchmark更贴合实际业务需求'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前业界对AI自主研发的爆发式增长预期强烈，但现有AI Agent开放式科研能力评估存在明显缺陷：窄任务验证仅能覆盖可量化目标，无法适配开放式研究需求；顶会盲审随机性高、评审质量参差不齐，无法准确衡量Agent的真实科研能力，亟需更可靠的评估范式。
### 方法关键点
- 提出**影子评估（Shadow Evaluation）**范式：选取2篇未公开的NeurIPS 2026投稿核心研究问题，给前沿Agent充足资源（6天时间、$3000 API额度、GPU算力、VM、公网访问权限），由原论文作者按顶会标准评审Agent输出
- 测试两类AI研究任务：LLM persona结构与可控性研究、表格基础模型分布偏移检测器设计
- 补充鲁棒性验证：更换底座模型（Claude Opus 4.8 → GPT-5.6 Sol Ultra）和Agent脚手架（OpenClaw → Codex），验证结论一致性
### 关键结果
- 两个任务的Agent输出均被原作者明确拒稿，整体得分分别为2/6、1/6，仅原创性得分相对较高（3/4、2/4），质量、清晰度、研究意义均不达顶会要求
- Agent可独立完成全部工程环节（文献调研、GPU环境调试、上百次实验、LaTeX排版），但存在5种共性故障模式，更换模型与脚手架后故障模式可完全复现
- Agent仅使用不到50%的API预算、40%的GPU预算，提前数小时结束任务，无法有效利用资源、响应评审反馈调整核心研究方向
> 最值得记住的结论：当前前沿AI Agent已经具备AI研究的工程执行能力，但距离独立完成开放式原创研究仍存在根本性的能力缺口
