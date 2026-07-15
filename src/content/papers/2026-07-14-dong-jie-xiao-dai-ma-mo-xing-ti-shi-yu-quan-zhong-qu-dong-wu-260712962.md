---
title: Form, Not Content? A Preregistered, Placebo-Controlled Evaluation of Learned
  Error-Conditioned Self-Repair Through Prompts and Weights in Frozen Small Code Models
title_zh: 冻结小代码模型提示与权重驱动错误自修复的安慰剂对照评估
authors:
- Mehmet Iscan
arxiv_id: '2607.12962'
url: https://arxiv.org/abs/2607.12962
pdf_url: https://arxiv.org/pdf/2607.12962
published: '2026-07-14'
collected: '2026-07-15'
category: Eval
direction: LLM自修复能力 · 安慰剂对照评估
tags:
- LLM Evaluation
- Self-Repair
- Small Language Model
- Code LLM
- Placebo Control
one_liner: 提出PoPE安慰剂对照评估框架，验证冻结小代码模型错误驱动自修复有效性
practical_value: '- 评估业务中LLM纠错、错误修复类优化效果时，可复用PoPE的安慰剂对照思路，排除格式、结构等无关因素干扰，避免误判优化收益

  - 本地部署小参数量LLM做搜索query改写纠错、推荐文案/广告生成错误修复时，不要盲目引入错误特征做微调，先做对照验证实际增益，减少无效投入

  - 做LoRA适配业务纠错场景时，可参考本文的消融设计，加入内容消融的安慰剂组做对照，确认优化效果确实来自目标特征而非训练噪声'
score: 6
source: arxiv-cs.LG
depth: abstract
---

### 动机
当前冻结小参数代码LLM本地部署场景下，自修复能力的评估普遍缺乏安慰剂对照，无法区分修复增益是来自错误内容本身还是任务无关的格式、结构信息，评估结论可信度不足。
### 方法关键点
提出PoPE（Popperian Placebo-controlled Evaluation）评估框架，将执行错误反馈与仅保留结构、消融任务相关内容/打乱错误分配的安慰剂组做对照，分别在两个通道测试自修复效果：1）提示通道：直接在prompt中加入错误信息；2）权重通道：用小样本训练adapter适配错误特征，测试0.5-1.5B冻结代码模型，每组最多生成4次修复结果。
### 关键结果
- 提示通道：40个难例集中，内容消融的安慰剂组解锁12个，真实错误反馈组仅解锁10个，无显著增益，判定机制无效
- 权重通道：错误内容adapter与无干预基线均解锁8个（p=1.0），错误随机打乱的安慰剂组反而解锁10个，未验证错误内容对自修复的增益
