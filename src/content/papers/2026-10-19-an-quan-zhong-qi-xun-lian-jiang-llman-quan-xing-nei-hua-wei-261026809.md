---
title: 'Safety Mid-Training: Internalizing LLM Safety as a Foundational Capability'
title_zh: 安全中期训练：将LLM安全性内化为基础能力
authors:
- Zhengyue Zhao
- Liwei Jiang
- Yejin Choi
- Chaowei Xiao1
affiliations:
- Johns Hopkins University
- University of Washington
- Stanford University
arxiv_id: '2610.26809'
url: https://arxiv.org/abs/2610.26809
pdf_url: https://arxiv.org/pdf/2610.26809
published: '2026-10-19'
collected: '2026-10-20'
category: LLM
direction: LLM安全对齐 · 中期训练范式
tags:
- LLM Safety
- Mid-Training
- Alignment
- Safety Utility Tradeoff
- Self-Generation
one_liner: 在预训练与后训练之间新增安全中期训练阶段，通过共享推理结构联合优化安全与通用能力，缓解安全-效用权衡
practical_value: '- 做LLM驱动的电商Agent/生成式推荐时，可复用「共享推理结构」范式，把合规要求（广告禁用语、假货规避等）与通用推理任务联合训练，避免后续业务微调时合规性快速下降

  - 小参数垂域LLM微调时，可采用self-generation+轻量judge过滤的方式构造训练数据，无需依赖大模型蒸馏即可获得接近的效果，降低训练成本

  - 业务需要频繁做下游任务微调时，可在预训练后、业务SFT前加入少量中期训练，把核心业务约束（用户隐私保护、内容合规等）内化为模型基础能力，减少后续微调时的约束遗忘

  - 训练数据配比可参考论文结论，安全/约束类数据占比25%左右能平衡合规性与通用能力，避免过度拒绝正常用户请求'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM安全对齐主要放在后训练阶段，或混入预训练数据，存在两个核心痛点：一是后续做无安全数据的业务微调时，安全能力会快速遗忘；二是安全训练通常会损失模型通用能力，安全-效用权衡难以平衡，本质是安全被当成了独立于通用能力的附加补丁。

### 方法关键点
- 新增「安全中期训练」阶段，位于预训练和SFT/RLHF之间，将安全视为与通用推理共享底层结构的基础能力，共享结构包含意图理解、知识/约束应用、后果推理三个核心模块
- 采用self-generation构造训练数据：用待训练的基模型自主生成结构化知识文档和推理链，再用judge模型过滤出符合忠实性、一致性、安全要求的样本，无需依赖外部大模型蒸馏
- 训练时将安全样本和通用样本按统一格式混合，用标准因果语言建模损失联合训练

### 关键实验
在Qwen3 1.7B/4B/8B、Llama3.2 1B/3B共5个模型上验证，使用185K prompt、200M mid-training token训练：
1. 无SFT时，平均攻击成功率（ASR）相对基模型下降72%~81%，同时通用能力显著提升
2. 后续做纯通用SFT（无任何安全数据）时，中期训练后的模型ASR仅上升2~3个百分点，远低于基线的10~20个百分点，通用能力不受损失
3. 后续做无安全奖励的GRPO训练时，中期训练后的模型安全能力几乎无下降，且能让RL最终达到更高的安全-效用前沿

### 核心结论
不要把安全当成后训练阶段加的补丁，要把它和通用推理用统一的结构联合训练，才能让安全成为不会被后续微调轻易洗掉的基础能力
