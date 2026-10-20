---
title: Competing Learning in Hybrid Architectures
title_zh: 混合架构大模型的竞争学习现象与优化训练方法
authors:
- Xingyu Shen
- Yingfa Chen
- Ziqing Qiao
- Chaojun Xiao
- Xu Han
- Zhiyuan Liu
affiliations:
- Tsinghua University
arxiv_id: '2610.26830'
url: https://arxiv.org/abs/2610.26830
pdf_url: https://arxiv.org/pdf/2610.26830
published: '2026-10-18'
collected: '2026-10-20'
category: Training
direction: 混合架构LLM 预训练分工优化
tags:
- Hybrid-LLM
- Pre-training
- Competing-Learning
- Attention
- Recurrent-Layer
- BLD
one_liner: 揭示混合架构递归与注意力层的竞争学习现象，提出分阶段训练策略BLD提升多任务性能
practical_value: '- 自研垂域混合架构LLM（如电商商品理解、客服对话大模型）时，可复用BLD分阶段训练策略：前期冻结RNN/SSM类递归层，让注意力层优先学习长程商品属性、多轮对话上下文的检索能力，降低长上下文任务幻觉

  - 搭建混合RNN+Attention的长序列用户行为建模模块时，可借鉴竞争学习结论，阶段性冻结RNN层避免其过早抢占短程行为信号，让注意力层充分学习跨月/跨季度的长程用户兴趣依赖，提升推荐召回准确率

  - 开发Agent长上下文记忆模块时，可通过该训练方法诱导更多注意力检索头生成，提升历史任务指令、外部召回工具返回信息的召回准确率，增强Agent任务执行的上下文一致性'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
当前混合架构（线性递归层+softmax注意力层）LLM兼顾推理效率与表达能力，是Kimi K3、GLM-5.3-Flash等前沿开源模型的主流选型，但原生全参数预训练无法实现组件间的最优分工：递归层对短程模式的学习速度更快，会提前抢占检索类任务的学习信号，抑制注意力层长程检索能力的发育，导致架构设计的互补性无法充分发挥，最终模型在长上下文理解、信息召回类任务上表现不及预期。
### 方法关键点
- 设计合成检索任务Spaced Retrieval与层检索能力归因指标，验证竞争学习现象：先掌握特定功能的层会降低对应任务的预测误差，进而削弱其他层的同类学习信号；自然语言训练中短程模式占比更高，递归层（KDA/GDN/GLA）会优先掌握检索能力，抑制注意力层的长程检索学习
- 提出BLD（Better Layer Division）分阶段训练策略：预训练前约1/10 token量阶段冻结所有递归层参数，仅训练注意力层与嵌入层，让注意力层先建立检索能力优势，后续解冻全量参数完成预训练，主动引导组件分工：注意力负责长程检索、递归负责短程模式建模
### 关键结果
在180M~1B参数的三类主流混合架构LLM上验证，对比原生全参数预训练：
1. 召回类任务平均准确率提升4~15pp，RULER长上下文基准平均得分最高提升13pp
2. LongPPL长上下文困惑度最高降低58%，长序列尾端token预测损失显著下降
3. 常识推理平均准确率提升1~3pp，全阶段训练损失普遍更低

**最值得记住的结论**：混合架构的性能上限不仅取决于组件选型，更取决于训练过程中不同模块的功能分工是否匹配设计目标，阶段性冻结学习速度更快的组件可主动引导最优分工，实现无额外架构修改的性能增益
