---
title: Strategy-Aware Parameter-Efficient Adaptation for LLM-based Auto-Bidding
title_zh: 面向大语言模型自动出价的策略感知参数高效适配方法
authors:
- Songyue Cai
- Lianyu Wang
- Shan Gu
- Ziru Xu
- Jian Xu
- Xiaofeng Zhu
- Bo Zheng
affiliations:
- Hainan University
- Taobao & Tmall Group of Alibaba
arxiv_id: '2607.24232'
url: https://arxiv.org/abs/2607.24232
pdf_url: https://arxiv.org/pdf/2607.24232
published: '2026-07-27'
collected: '2026-07-28'
category: RecSys
direction: 广告自动出价 · LLM参数高效微调
tags:
- Auto-bidding
- LoRA
- MoE
- Parameter-Efficient Fine-Tuning
- LLM4Rec
one_liner: 提出SAGE框架，通过三个模块实现LLM自动出价的参数高效微调，参数量不足全微调的10%，性能领先现有方法
practical_value: '- 轨迹类时序任务可复用时间+语义双分解位置编码方案：用无参正弦编码做时序位置，仅给3类（RTG/state/action）语义token单独加可训练embedding，参数少、支持变长序列，效果优于传统可训练位置编码

  - 多模态融合可采用gated cross-attention替代直接拼接：将结构化轨迹作为query，文本指令作为KV做跨模态对齐，既避免输入长度膨胀，又能降低跨模态空间差异带来的融合损耗

  - 多约束场景可采用约束gated MoE LoRA方案：冻结LLM主干，用约束条件作为路由信号动态切换LoRA专家，仅需不到10%全微调参数量即可达到甚至超越全微调效果，大幅降低训练和部署成本

  - 小参数量LLM适配垂直任务性价比更高：实验显示0.5B Qwen效果优于1.5B/3B版本，垂直场景无需盲目追求大模型，小模型+高效适配方案即可满足业务需求'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有LLM-based自动出价方法存在三个核心痛点：一是轨迹位置编码仅考虑时序依赖、忽略同时间步不同token的语义差异，编码能力弱；二是轨迹与文本模态直接拼接融合，特征空间未对齐且输入长度大幅膨胀，计算开销高；三是依赖全微调更新LLM所有参数，易遗忘预训练知识，适配新约束场景的成本极高。

### 方法关键点
1. **位置增强模块**：拆分时序+语义双维度位置编码，时序用无参正弦编码支持变长轨迹，语义仅为RTG/state/action三类token分配独立可训练embedding，参数量极低；
2. **文本对齐模块**：采用gated cross-attention做跨模态融合，结构化轨迹作为query检索任务描述文本的KV，对齐特征空间的同时不增加输入序列长度；
3. **约束gated LoRA模块**：冻结LLM主干，将广告主约束条件编码为门控信号，路由选择MoE结构的LoRA专家，仅微调少量参数即可适配不同约束下的出价策略。

### 关键实验结果
在阿里公开的AuctionNet大规模自动出价基准上测试，对比DT、CQL等传统RL方法，以及SFT、GRPO、LLM-DT等LLM基线：100%预算下，稠密数据集得分比最优传统基线DT-score高4.49%，稀疏数据集得分高7.83%；对比最优LLM基线LLM-DT，稠密数据集得分高6.4%，稀疏数据集高10.15%；仅需全微调8.3%的参数量即可达到上述效果。

### 核心结论
LLM适配广告等垂直决策任务时，针对性的模态对齐+参数高效微调方案，效果和性价比远高于通用全微调范式。
