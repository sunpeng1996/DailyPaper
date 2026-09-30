---
title: Learning from Teacher Continuations at Student States
title_zh: 基于学生状态下教师续写的在线大模型蒸馏方法OLIVE
authors:
- Haojin Wang
- Dylan Zhang
- Huaibo Chen
- Suhao Yu
- Yihang Sun
- Zhanyang Jin
- Jiaying Ye
- Dianqi Li
- Prasanna Sattigeri
- Kamal Youcef-Toumi
affiliations:
- University of Illinois at Urbana-Champaign
- Massachusetts Institute of Technology
- University of Pennsylvania
- University of Washington
- IBM
arxiv_id: '2609.36246'
url: https://arxiv.org/abs/2609.36246
pdf_url: https://arxiv.org/pdf/2609.36246
published: '2026-09-27'
collected: '2026-09-30'
category: Training
direction: 大模型知识蒸馏 · 在线训练优化
tags:
- Knowledge Distillation
- Online Training
- LLM Agent
- Reasoning
- Black-box Distillation
one_liner: 提出仅依赖教师生成文本的在线蒸馏框架OLIVE，解决现有蒸馏方法的协变量偏移、监督碎片化等缺陷
practical_value: '- 电商导购/客服Agent蒸馏可直接复用OLIVE范式：让学生Agent先跑前k步交互，用黑盒API教师（如GPT-4o、内部大模型）续写正确路径，仅对教师部分算CE损失，无需获取教师logit，大幅降低蒸馏成本

  - 生成式推荐小模型蒸馏可采用在线刷新学生前缀的设计，避免离线SFT的协变量偏移，同时将通用能力遗忘控制在1%以内，保留小模型原有合规文案生成、语义理解等能力

  - 工程上可借鉴异步OLIVE实现：将学生前缀生成与教师续写任务并行调度，可降低训练 idle 时间20%+，适配算力有限的业务训练场景

  - 复杂Query理解、多轮会话推荐等需要小模型具备推理能力的场景，优先选用OLIVE替代传统OPD，师生能力差距较大时仍能有效蒸馏，不会出现OPD训不动的问题'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有LLM蒸馏存在三大痛点：离线SFT用固定教师轨迹存在序列协变量偏移，长序列下错误累加，还易导致学生原有能力遗忘；token级OPD依赖学生原始生成序列，学生前缀出错后后续监督完全无效，监督碎片化严重；分布匹配类蒸馏需要获取教师token概率，无法对接仅返回生成文本的黑盒API教师，在长链推理、长 horizon Agent 任务上效果受限。
### 方法关键点
- 核心流程：每轮训练让当前学生生成k长度前缀（推理任务为token数，Agent任务为交互轮次），教师基于前缀自动续写M长度内容，仅对教师续写部分计算掩码CE损失更新学生，前缀部分不参与损失计算；
- 异步优化：学生生成下一批前缀和教师生成当前批续写并行执行，通过异步深度d控制策略陈旧度，大幅降低训练 idle 时间；
- 多场景适配：无需改动核心逻辑即可同时支持单-turn长推理、多-turn Agent 交互任务。
### 关键实验
在RLVE推理数据集上，比OPD、离线SFT的Pass@8高6~8个点；在AgentGym的5个Agent任务上，平均成功率比OPD高7~22个点，其中师生能力差距极大的ScienceWorld任务，从OPD的0%成功率提升到7.5%；异步实现比同步版本训练时间降低23.8%，GPU耗时与OPD相当但效果显著更优；对比离线SFT不会出现训练 plateau，ScienceWorld任务最终性能高13%，通用能力平均遗忘仅0.9%。
### 核心结论
蒸馏的效果不仅取决于监督的形式，更取决于监督是否锚定在学生当前实际访问的状态，且随学生演化动态刷新
