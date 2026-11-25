---
title: 'InstructReplay: Replaying Assistant Turns to Preserve General Behavior During
  Factual Fine-Tuning'
title_zh: InstructReplay：事实微调时重放助手回复以保留通用能力
authors:
- Xiaofeng Shi
- Qian Kou
- Hua Zhou
affiliations:
- Beijing Academy of Artificial Intelligence (BAAI)
arxiv_id: '2611.32918'
url: https://arxiv.org/abs/2611.32918
pdf_url: https://arxiv.org/pdf/2611.32918
published: '2026-11-23'
collected: '2026-11-25'
category: Training
direction: LLM事实微调 灾难性遗忘缓解
tags:
- Fine-tuning
- Catastrophic Forgetting
- Knowledge Injection
- Instruction Tuning
- Replay Learning
one_liner: 提出重放初始模型通用指令回复的InstructReplay，大幅降低事实微调时的通用能力遗忘
practical_value: '- 垂类LLM微调（如电商客服、广告文案生成、Agent规则注入）可直接复用该方案：准备1w条覆盖业务常用通用能力（指令遵循、推理、格式生成等）的prompt，让初始模型预生成回复作为重放缓存，训练时加λ=0.25的KL重放损失，就能将通用能力遗忘从28%降到2.4%，同时不影响垂类事实学习效果

  - 工程上可做轻量化改造：用hard token匹配（交叉熵损失）替代全词表KL散度计算，无需每步对frozen模型做前向推理，训练成本仅翻倍，遗忘率仅比原版高0.7个点，性价比极高

  - 若业务用LoRA做低资源微调，可搭配该重放方案，事实学习效果比纯LoRA高10个点以上，同时避免纯LoRA仍存在的13%左右的通用能力损失'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
指令微调LLM注入垂类新事实时，标准微调会严重损伤通用能力：生成类基准（指令遵循、数学、推理、代码）平均下降35分，响应长度至少减半，而基于似然的MMLU基准几乎无变化。核心原因是微调数据的短答案让模型倾向输出极简回复，破坏了原有的指令遵循、思维链等助手行为，现有重放方法未明确核心优化因子。
### 方法关键点
- 预构建重放缓存：冻结初始模型M0，让其回答9600条覆盖指令遵循、数学、推理、代码、翻译的通用指令，保存所有回复作为缓存，不使用数据集自带的通用答案
- 混合损失训练：总损失 = 垂类事实QA的交叉熵损失 + λ=0.25的重放损失，重放损失计算当前模型与M0在重放回复每个前缀的next token分布的KL散度，每步等比例采样垂类数据和重放数据更新
- 控制变量验证：对比重放上下文、目标类型、回复来源三类变量对效果的影响
### 关键结果
- 跨3个4B级模型（SmolLM3-3B、Qwen3-4B、Phi-4-mini）、2个垂类域（生物医学、工程能源）测试，InstructReplay将5个通用基准的平均遗忘从28.1分降至2.4分，事实学习效果与标准微调差距不超过2分
- 在所有6组实验中，效果优于Naive SFT、LoRA-SFT、RAFT等7种现有适配方法；重放上下文的影响远大于损失形式：通用指令上下文比BOS无模板采样的遗忘低6.8分，模型自生成回复比第三方数据集答案的遗忘低4.4分

仅需让初始模型预先生成1万条通用指令回复作为重放缓存，就能以极低的额外成本，基本消除事实微调带来的通用能力损失。
