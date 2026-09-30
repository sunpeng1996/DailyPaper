---
title: 'Allspark: Weak to Strong Transfer via Alternating Chain of Thought'
title_zh: Allspark：基于交替思维链的弱模型到强模型能力迁移框架
authors:
- Kaizhao Liang
- Junxiong Wang
- Chen Liang
- Zhendong Wang
- Qiang Liu
affiliations:
- UT Austin
- Together AI
- Microsoft
arxiv_id: '2609.32913'
url: https://arxiv.org/abs/2609.32913
pdf_url: https://arxiv.org/pdf/2609.32913
published: '2026-09-25'
collected: '2026-09-30'
category: LLM
direction: LLM 弱到强推理能力迁移
tags:
- Weak-to-Strong Transfer
- Chain of Thought
- RL for LLM
- Cross-Model Transfer
- Reasoning
one_liner: 仅用小模型rollout训练弱教师，推理时通过交替思维链引导冻结强模型提升推理效果
practical_value: '- 可直接复用小模型RL训练的推理引导能力，无需微调业务侧大模型权重即可提升推理效果，适合电商query语义理解、商品合规校验、售后工单判定等场景，大幅降低大模型调优成本

  - 交替思维链的纯文本交互模式无需对齐tokenizer，支持跨模型族灵活组合，可使用开源小模型训练引导逻辑，配合闭源商用大模型推理，规避训练数据泄露风险

  - 可针对性优化推理任务的准确率-token成本tradeoff，在客服Agent、智能导购等对响应成本敏感的场景，通过小模型补充关键推理节点，减少大模型无效推理token消耗，同时提升结果准确率'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前大模型RL训练需要生成大量大模型rollout，计算成本极高，中小团队很难负担；现有弱到强迁移方法大多需要更新强模型权重，或者依赖强模型rollout参与训练，落地门槛高。亟需一种不需要强模型参与训练，就能把小模型学到的推理能力迁移给强模型的低成本方案。

### 方法关键点
- 训练阶段：两个同尺寸小模型副本交替生成思维链片段，一个作为可训练的弱教师，另一个冻结并生成最终答案，仅用最终答案的Reward更新弱教师的RL损失，全程不涉及任何大模型rollout
- 推理阶段：冻结训练好的弱教师，替换训练阶段的冻结小模型为任意强学生模型，二者继续交替生成思维链，强学生输出最终答案，通过纯文本交互，天然支持跨模型族、不同tokenizer的模型组合

### 关键实验
- 可控实验：Qwen3-1.7B训练的教师引导Qwen3-4B，推理任务准确率从81.2%提升到82.8%，数学任务准确率基本持平
- 大规模实验：Inkling-Small训练的教师引导同族Inkling大模型，ARC-AGI-2任务准确率从78.1%提升到81.6%，同时在10.8k token量级达到79.2%准确率，优于大模型单独在12.3k token下的78.1%准确率
- 跨模型族实验：同一教师引导Kimi K2.6，准确率提升11.5个百分点，token消耗减少7.7%；引导Nemotron 3 Ultra，中/全推理模式下准确率分别提升17.7、5.2个百分点

### 核心结论
弱模型不需要本身性能超过强模型，只要能输出有效推理引导片段，就能帮助强模型获得更好的推理效果，大幅降低大模型推理增强的落地成本
