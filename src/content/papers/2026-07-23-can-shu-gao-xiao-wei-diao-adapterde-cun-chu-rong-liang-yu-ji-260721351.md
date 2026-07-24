---
title: How Many Bits Can an Adapter Write? Measuring the Capacity and Memorization
  of Parameter-Efficient Fine-Tuning
title_zh: 参数高效微调Adapter的存储容量与记忆特性量化研究
authors:
- Kaizhen Tan
- Heqing Du
- Yang Feng
affiliations:
- Carnegie Mellon University
- Columbia University
arxiv_id: '2607.21351'
url: https://arxiv.org/abs/2607.21351
pdf_url: https://arxiv.org/pdf/2607.21351
published: '2026-07-23'
collected: '2026-07-24'
category: Training
direction: 大模型高效微调 · LoRA隐私与容量测量
tags:
- LoRA
- PEFT
- Memorization
- Privacy
- SFT
- RL
one_liner: 量化LoRA的信息存储上限，揭示容量与参数位置、基座、训练范式的关联
practical_value: '- 做业务LoRA微调时，优先将可训练参数放在注意力层而非MLP层，可在相同参数量下降低隐私泄露风险，同时控制存储成本

  - 涉及用户敏感数据的微调任务优先采用RL类训练范式而非SFT，可避免明文敏感数据被LoRA记忆泄露

  - 对外共享业务微调LoRA前，可复用论文的压缩测量框架评估存储的敏感信息量，提前规避数据泄露风险

  - 小样本SFT微调时，若数据量小于LoRA理论存储容量（1.7~2.8bit/参数），需警惕训练数据被完整记忆'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
行业长期默认LoRA是轻量技能补丁，不会泄露训练数据，但缺乏量化验证；现有隐私评估依赖事后攻击，无法提前预判泄露风险，也不清楚LoRA实际存储上限的核心影响因素。

### 方法关键点
- 基于压缩优势原理设计测量框架：模型能记忆的字符串可被更短编码压缩，压缩差值即为存储的真实信息量
- 采用随机无意义token序列校准测量，排除语义泛化干扰，确保每bit差值对应真实记忆的信息
- 定义三个核心评估指标：训练参数编码长度（物理传输的文件大小）、行为写入bit（模型似然变化量）、记忆bit（随机序列压缩差值）
- 控制变量对比参数位置、基座类型、训练范式（SFT/GRPO）对LoRA容量的影响

### 关键结果数字
LoRA每训练参数仅存储1.7~2.8bit，远低于全量微调的3.6bit；相同参数量下，MLP层LoRA的存储容量是注意力层的近2倍；基于预训练基座的LoRA记忆率达98%，基于随机初始化基座的LoRA记忆率仅29%；相同准确率下，SFT会完整记忆训练数据中的明文秘密，GRPO的记忆量与噪声无差异，无敏感数据泄露。

### 核心结论
LoRA的存储容量由参数位置、基座结构共同决定，而非仅由参数量决定，RL类微调不会明文记忆训练数据，SFT存在明确的泄露风险。
