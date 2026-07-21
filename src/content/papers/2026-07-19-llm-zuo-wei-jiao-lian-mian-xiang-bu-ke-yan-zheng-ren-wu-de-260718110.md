---
title: 'LLM-as-a-Coach: Experiential Learning for Non-Verifiable Tasks'
title_zh: LLM 作为教练：面向不可验证任务的经验学习框架
authors:
- Tianzhu Ye
- Li Dong
- Guanheng Chen
- He Zhu
- Xun Wu
- Shaohan Huang
- Furu Wei
affiliations:
- Microsoft Research
- Tsinghua University
- Peking University
arxiv_id: '2607.18110'
url: https://arxiv.org/abs/2607.18110
pdf_url: https://arxiv.org/pdf/2607.18110
published: '2026-07-19'
collected: '2026-07-21'
category: Training
direction: 大模型后训练 · 经验学习对齐
tags:
- LLM Alignment
- Experiential Learning
- RLHF
- On-Policy Distillation
- Reward Hacking
one_liner: 将LLM-as-Judge改造为LLM-as-Coach，用高带宽经验知识替代标量奖励优化不可验证任务
practical_value: '- 电商推荐/广告文案生成这类无明确标准答案的不可验证任务，可替换现有RLHF的标量奖励，用LLM-as-Coach生成可迁移的优化指引做训练，提升文案质量的同时降低奖励hack概率

  - 业务场景的LLM微调可复用经验蒸馏+on-policy上下文蒸馏的范式：先让Coach基于业务定制的rubrics提炼通用优化经验，再通过token级反向KL将经验内化到模型，推理无需额外上下文，无推理
  overhead

  - 若计算资源有限，可先从ablation中的Multiple-Choice模式切入：预设10类左右业务场景的优化方向（比如更抓眼球、更符合平台规范、更高转化率），让Coach直接输出分类标签做低带宽优化，平衡效果和成本'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有基于LLM-as-Judge的RLHF方法会把多维度评估压缩为单一标量奖励，丢弃了丰富的文本反馈信息，尤其在不可验证开放任务（比如文案生成、创意推荐）中，标量奖励的信息瓶颈会导致高分响应无法区分，还容易出现奖励hack，泛化性差。

### 方法关键点
- 把原有LLM-as-Judge改造为LLM-as-Coach：基于rubrics评估响应后，额外输出通用可迁移的经验知识，而非仅返回标量分数，反馈带宽是1-10分制的5000倍以上
- 采用on-policy上下文蒸馏做优化：将经验知识作为上下文输入teacher模型，最小化policy模型与上下文引导的teacher模型的token级反向KL散度，把经验内化到policy参数，推理无需携带Coach或经验上下文
- 支持两种teacher设置：固定初始冻结checkpoint作为teacher，或迭代更新每轮训练后的policy作为teacher，迭代模式加通用领域样本混合可缓解OOD能力遗忘

### 关键实验
训练用WildChat-IF的7500条真实用户指令，分别在Qwen3-8B、OLMo-3-7B两款模型上验证，对比baseline为基于GRPO的rubric RL。结果显示，EL在分布内WildChat测试集得分平均比RL高0.8~1.1分，在分布外AlpacaEval-v2、WildBench等基准上平均win rate提升2~6.2个百分点，同时缓解奖励hack，泛化性显著优于RL。

最值得记住的一句话：对于多维度、无标准答案的不可验证任务，高带宽的可迁移经验指导比低带宽的标量奖励，能带来更有效、更通用的模型优化效果
