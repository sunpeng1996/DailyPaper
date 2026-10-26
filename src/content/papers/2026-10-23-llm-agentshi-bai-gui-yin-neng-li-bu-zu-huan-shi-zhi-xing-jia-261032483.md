---
title: 'When Agents Fail: Model or Harness--Who''s to Blame?'
title_zh: LLM Agent失败归因：能力不足还是执行框架Harness的问题
authors:
- Shao Zhang
- Hangfan Zhang
- Yuanyuan Shi
- Hao Li
- Min-Le Su
- Kangcong Li
- Jingping Wang
- Chunjiang Mu
- Chen Zhang
- Yang Chen
affiliations:
- Shanghai Artificial Intelligence Laboratory
arxiv_id: '2610.32483'
url: https://arxiv.org/abs/2610.32483
pdf_url: https://arxiv.org/pdf/2610.32483
published: '2026-10-23'
collected: '2026-10-26'
category: Agent
direction: Agent性能评估 · 模型-Harness适配
tags:
- LLM Agent
- Agent Evaluation
- Harness
- Model-Harness Fit
- VCR
one_liner: 提出模型-Harness交互评估框架，量化二者对Agent性能与失败的独立贡献
practical_value: '- 落地Agent应用时不要仅单独测试模型能力，要搭配目标业务Harness做交叉评估，避免误判模型性能或Harness适配性

  - 可直接复用VCR（Valid Completion Rate）指标区分任务失败、执行异常、结果提交失败三类问题，快速定位Agent故障根因

  - 搭建跨模型兼容的Agent系统时优先选择Cross-Model Fit高的Harness（如论文验证的OpenCode），大幅降低多模型适配成本

  - 优化Agent资源消耗时不要仅看Token吞吐量，要结合任务成功率，避免低Token消耗对应提前终止的无效请求'
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM Agent benchmark大多评估固定模型+Harness的端到端性能，无法区分失败来自模型能力不足、还是Harness的执行/交互缺陷，也无法量化二者适配性，导致Agent优化方向不明确。

### 方法关键点
- 提出5个互补评估指标：Valid Completion Rate（VCR，衡量正常结束且可被评估的请求占比）、Model-Harness Fit（特定模型下Harness的任务达成效率）、Cross-Model Fit（Harness跨模型的通用适配性）、Interaction Residuals（模型-Harness配对的特有优劣势）、Token Load（全链路Token消耗，含失败请求）
- 设计交叉评估框架：固定任务、资源限制等外部条件，独立替换模型和Harness做配对测试，分离二者的独立影响

### 关键结果
测试4个通用Harness（OpenCode/Codex CLI/Pi CLI/DeepAgents）、4个主流LLM，覆盖6类Agent基准（代码、终端、多模态任务等），共111种配置、52168条轨迹：
1. OpenCode的Cross-Model Fit达87.48，跨模型适配性排名第一
2. DeepSeek V4 Flash的跨Harness平均VCR最高，达91.3%~93.98%
3. 仅更换Harness可让同模型的任务排名完全反转，部分高VCR配置存在10%~40%的动作执行缺口，导致任务成功率极低

### 核心结论
Agent失败不只是模型的问题，40%以上的性能差异来自Harness设计及模型-Harness的适配性，优化时必须做联合评估
