---
title: 'Not Until the Evidence Says So: Teaching LLM Investigators When to Close a
  Case'
title_zh: 面向调查类任务的LLM证据依赖型结案决策校准方案与数据集Nautil
authors:
- Tingzhu Bi
- Ping Wang
- Meng Ma
affiliations:
- Peking University
arxiv_id: '2610.03190'
url: https://arxiv.org/abs/2610.03190
pdf_url: https://arxiv.org/pdf/2610.03190
published: '2026-10-02'
collected: '2026-10-05'
category: Agent
direction: Agent 调查任务决策校准优化
tags:
- LLM Agent
- Decision Calibration
- SFT
- RL
- Dataset
- Evidence Grounding
one_liner: 提出Nautil数据集与训练框架，让LLM调查员仅在证据充足时结案，大幅降低过度断言率
practical_value: '- 做电商售后纠纷判定、商品合规审核、虚假交易识别等需要证据支撑的Agent任务时，可复用三维评估体系：决策准确率（对比分类基准排除shortcut）、证据依赖性（反事实删除核心凭证看决策是否变化）、输出质量校验，避免模型靠数据集分布作弊

  - 训练需要「无法判定/拒绝回答」能力的Agent时，必须在SFT数据中加入足够的无法判定负例，否则模型会倾向于强行输出结论，过度断言率可达90%以上

  - RL优化时优先用可量化的硬规则奖励（比如仅奖励决策正确性），不要轻易加入LLM打分的软奖励，否则容易出现策略崩溃（比如为了拿高分永远选择不结案）'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有LLM在调查类任务（故障排查、事故分析、纠纷判定等）中，即使能找到可能的原因，也普遍存在过度断言问题，会在证据不足时强行结案；而现有拒答研究均为单轮给定上下文的场景，不支持多轮证据检索后的结案决策判断，且评估时容易被数据集shortcut（比如案件来源直接决定标签）干扰，无法验证模型是否真的基于证据决策。

### 方法关键点
- 构建Nautil数据集：包含731个经审计的多领域调查案件（航空、铁路、化工、服务器故障等），每个案件有完整调查轨迹、分布外测试集、反事实证据版本，标签为官方是否确定原因
- 两阶段训练：首先用LoRA对Qwen3.5-9B做SFT，学习调查流程与正确结案决策；再用仅针对结案正确性的GRPO强化学习（RLVR）进一步提升准确率，避免软奖励导致的策略崩溃
- 三维评估体系：1）结案准确率（对比仅用案件来源的基准，排除shortcut）；2）证据依赖性（删除结论核心证据看结案率下降幅度，验证是否真的依赖证据）；3）结论质量校验（判断是否过度断言、是否有证据支撑）

### 关键结果
- SFT后9B模型过度断言率从97%降至35%，既正确又无过度断言的结论占比从3%升至43%，优于前沿模型Gemini 3.8 Flash的9%
- RLVR后结案平衡准确率从69.2%升至83.3%，与人类教师水平相当，同来源内准确率从60.4%升至74.1%，证明不是靠来源shortcut
- 反事实测试中，删除核心证据后SFT模型结案率下降26个百分点，远高于基线模型的6个百分点和Gemini的7个百分点，证明决策高度依赖证据

**最值得记住的一句话**：LLM的事实正确性和知道何时无法给出结论是两个独立的能力，后者需要专门的训练和针对性的评估体系来保障，不会随通用能力提升自然涌现。
