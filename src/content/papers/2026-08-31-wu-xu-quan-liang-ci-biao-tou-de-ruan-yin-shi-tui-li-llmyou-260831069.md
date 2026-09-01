---
title: A Model with No Head and Many Thoughts
title_zh: 无需全量词表头的软隐式推理LLM优化方法
authors:
- Nikita Koriagin
- Yaroslav Aksenov
- George Bredis
- Gleb Gerasimov
- Nikita Balagansky
- Daniil Gavrilov
affiliations:
- Yandex
- T-Tech
arxiv_id: '2608.31069'
url: https://arxiv.org/abs/2608.31069
pdf_url: https://arxiv.org/pdf/2608.31069
published: '2026-08-31'
collected: '2026-09-01'
category: Reasoning
direction: LLM软推理 · 词表头压缩效率优化
tags:
- Soft-Thinking
- Chain-of-Thought
- GRPO
- LoRA
- Reasoning Acceleration
one_liner: 用轻量隐空间投影替代推理阶段全量词表头，提升多采样推理效率与高k pass@k
practical_value: '- 电商Agent多轮推理（如需求拆解、优惠组合计算）场景可复用SLT轻量投影头设计，将推理阶段全量词表投影替换为领域专属小尺寸（K=8d左右）投影头，降低推理时延，尤其适配需要多rollout选优的场景

  - 训练侧可复用「领域高频token初始化投影头+LoRA联合训练」模式，无需全量微调LLM，仅新增少量参数即可适配领域推理需求，冻结主干保留通用能力，适合多业务域LLM部署

  - 多采样生成场景（如推荐理由多样性生成、搜索query改写多候选生成）可复用Gumbel-Softmax引入受控随机性的思路，平衡单样本精度与多样本覆盖度，提升高k下的召回/准确率

  - 部署可设计「投影头开关」机制，领域内任务开投影头降本提效，跨域任务关投影头回退到标准推理无性能损失，适配电商多场景混合部署需求'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
现有软思考方法虽优于离散CoT推理，但每步需过全量词表LM头，计算成本高，且中间推理状态被限制在离散token语义空间，长推理链时延瓶颈显著，多rollout RL训练成本极高。

### 方法关键点
- 推理阶段替换LM头为轻量隐空间投影器：由编码器（隐藏态映射到K维logits，K≪V）+解码器（K维混合权重映射回embedding空间）组成，仅最终答案生成保留标准LM头
- 投影器用目标领域高频token对应的LM头、embedding表行初始化，训练时和LoRA联合优化，无需全量微调主干
- 基于Gumbel-Softmax在K维空间采样引入随机性，复用SofT-GRPO策略梯度方法，可计算合法per-step似然用于RL更新
- 推理停止用软embedding与</think>或\boxed token的余弦相似度阈值判断，自动切换到标准解码输出答案

### 关键结果
在5个数学推理数据集（AIME2024/2025、AMC23、MATH-500、GSM8K）测试：
- 对比SofT-GRPO，DeepSeek-Qwen-1.5B平均pass@32从85.18提升到86.22，LLaMA-3.2-3B从57.06提升到60.70
- 推理步计算量降低约5倍，端到端吞吐量提升3%~25%，推理token量降低约7%，多rollout场景收益更显著
- 跨域场景关闭投影头即可回退到标准软思考性能，无精度损失

最值得记住的一句话：将推理过程与最终输出的词表投影解耦，用领域专属小尺寸隐空间做推理，是兼顾效率、效果与通用性的可行路径
