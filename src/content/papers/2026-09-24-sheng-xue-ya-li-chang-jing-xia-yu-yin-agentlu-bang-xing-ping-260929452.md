---
title: 'Voice Agents under Acoustic Stress: From Signal Degradation to Interaction
  and Action'
title_zh: 声学压力场景下语音Agent鲁棒性评估工作流TRACE
authors:
- Amir Ivry
- Kai-Wei Chang
- Lin Zhang
- Sharon Gannot
- Carlos Busso
affiliations:
- Technion - Israel Institute of Technology
- Massachusetts Institute of Technology
- Independent Researcher
- Bar-Ilan University
- Carnegie Mellon University
arxiv_id: '2609.29452'
url: https://arxiv.org/abs/2609.29452
pdf_url: https://arxiv.org/pdf/2609.29452
published: '2026-09-24'
collected: '2026-09-25'
category: Agent
direction: 语音Agent · 鲁棒性评估
tags:
- Voice Agent
- Acoustic Robustness
- Evaluation Workflow
- Task-oriented Agent
- TRACE
one_liner: 提出5步TRACE工作流，量化评估声学干扰下任务型语音Agent的交互鲁棒性与用户负担
practical_value: '- 电商语音购物助手、语音客服等语音交互类Agent上线前的鲁棒性测试，可直接复用TRACE的对照实验框架，比单纯测ASR准确率更能反映实际业务风险（如噪声场景下错下单）。

  - 语音交互体验指标可参考TRACE的分层设计：除任务完成率外，额外统计违规操作率（如下错单后取消）、用户平均额外交互轮次，全面衡量体验损耗。

  - 迭代语音前端降噪、澄清话术策略时，可采用TRACE的控制变量法，固定任务规则、用户回复逻辑对比迭代前后的效果，量化策略的业务收益。'
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

### 动机
现有语音Agent鲁棒性评估大多仅关注ASR准确率、单轮回复质量，未跟踪噪声、混响、抢话等声学干扰对全链路任务完成、中间错误操作、用户交互负担的影响，无法准确反映真实场景的业务损失与体验问题，也难以定位Agent的优化方向。

### 方法关键点
- 提出TRACE 5步可复现评估工作流：1. Task 明确定义任务目标、合法操作与禁止行为规则；2. Recording 选取真实场景的原始语音输入，标注关键信息片段；3. Acoustics 对原始语音做可控声学扰动，分为答案保留、信息缺失、场景变更三类分别设计评估逻辑；4. Comparison 同一Agent在相同任务、用户回复规则下，分别跑原始和扰动后的语音输入做对照；5. Effects 从任务完成、违规操作、恢复成功率、用户额外轮次四个维度量化打分。
- 评分做三层区分：目标达成（最终结果正确）、违规操作（中间出现错误动作如提交错误订单）、任务成功（达成目标且无违规），避免忽略可恢复但影响体验的中间错误。

### 关键结果数字
论文用快递地址填写的虚拟测试集做示例验证：当地址数字被静音扰动后，任务成功率从90%下降到60%，违规操作率从10%上升到20%，用户平均额外交互轮次从0.1上升到0.8，可精准反映声学扰动的实际业务影响。

### 核心结论
语音交互类Agent的鲁棒性评估不能仅停留在语音识别准确率层面，必须全链路跟踪声学扰动对任务结果、中间行为与用户负担的实际影响。
