---
title: Register Tokens for Bounded-State Reasoning in Diffusion Language Models
title_zh: 面向扩散语言模型有界状态推理的寄存器Token方法
authors:
- Albert Ge
- Chandan Singh
- Yufan Zhuang
- Xiaodong Liu
- Jianfeng Gao
- Frederic Sala
affiliations:
- University of Wisconsin–Madison
- Microsoft Research
- UC San Diego
arxiv_id: '2609.16372'
url: https://arxiv.org/abs/2609.16372
pdf_url: https://arxiv.org/pdf/2609.16372
published: '2026-09-13'
collected: '2026-09-17'
category: Reasoning
direction: 扩散大语言模型 · 有界状态推理
tags:
- Diffusion LLM
- Register Token
- Bounded Reasoning
- State Compression
- Long Context
one_liner: 在扩散LLM中引入固定位置寄存器Token实现跨生成块的有界连续状态推理
practical_value: '- 电商导购Agent、多轮推荐场景可复用固定位置连续寄存器设计，替代KV cache截断或离散摘要，用少量向量携带历史交互状态，降低长上下文推理时延

  - 训练时可复用prompt掩码+全块掩码的trick，迫使模型依赖压缩状态而非原始输入，可直接迁移到推荐系统的用户长期兴趣压缩建模任务

  - dLLM+寄存器的并行生成+低时延长序列组合，可用于电商营销文案、商品详情页长文本生成，相比全上下文自回归解码速度最高提升5.6倍，吞吐量更高'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
扩散大语言模型（dLLM）支持并行生成，推理速度优于自回归LLM，但跨生成块推理时需保留全量历史上下文，注意力成本随生成长度平方级增长；现有离散文本摘要、KV cache压缩方法信息损失大，无法有效承载连续推理状态，亟需固定大小的连续状态携带机制实现低时延长序列推理。
### 方法关键点
- 新增固定位置的连续寄存器Token，每生成完一个块后，通过前向传播将推理状态写入寄存器的隐层向量，清除历史生成文本后将寄存器向量作为下一生成块的输入，上下文窗口始终保持固定大小
- 训练引入两个trick避免模型绕过寄存器：以一定概率掩码后续块对原始prompt的注意力，每个块第一轮训练将所有completion token全掩码，迫使模型只能通过寄存器获取历史信息；梯度仅回传到前一个块的寄存器写入步骤，控制训练内存开销
- 支持RL优化，提出chunked diffu-GRPO算法，将奖励信号回传到寄存器更新步骤，进一步提升长horizon推理效果
### 关键结果
在LLaDA-8B、Dream-7B两个dLLM上验证，训练数据为60K数学+代码指令样本，对比离散文本携带、重建式记忆Token基线：GSM8K任务上比离散文本高8.5个点，MBPP代码任务最高提升19.5个点，长序列推理速度相比全上下文解码最高提升5.6倍，RL优化后在Countdown、LongArithmetic任务上分别提升2.6、8.1个奖励点。

最值得记住的一句话：少量连续的固定位置寄存器Token，比等量离散文本token能更高效承载推理状态，是平衡长序列推理效果和时延的可行路径。
