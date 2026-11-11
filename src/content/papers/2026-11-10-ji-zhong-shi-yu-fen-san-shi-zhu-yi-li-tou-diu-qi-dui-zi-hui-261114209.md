---
title: Breakdown of Autoregressive Multi-Step Reasoning Under Concentrated vs. Diffuse
  Attention Head Dropout
title_zh: 集中式与分散式注意力头丢弃对自回归多步推理的影响分析
authors:
- Karol Struniawski
affiliations:
- Warsaw University of Life Sciences – SGGW
arxiv_id: '2611.14209'
url: https://arxiv.org/abs/2611.14209
pdf_url: https://arxiv.org/pdf/2611.14209
published: '2026-11-10'
collected: '2026-11-11'
category: Reasoning
direction: 大模型多步推理 · 鲁棒性分析
tags:
- LLM
- Multi-Step Reasoning
- Attention Head Dropout
- Robustness
- GSM8K
one_liner: 对比两类等预算注意力头丢弃策略，证实集中式突发丢弃会大幅降低LLM多步推理准确率
practical_value: '- 排查Agent/生成式推荐链路的LLM推理故障时，优先检查是否存在集中式注意力层失效（如量化误差、硬件故障、流量峰值导致的局部计算异常），这类故障对CoT推理的影响远大于均匀分布的随机噪声

  - 部署电商智能导购、复杂query理解等高稳定性要求的LLM服务时，故障模拟测试需新增集中式注意力丢弃的测试case，仅测试均匀噪声会显著低估线上故障的实际影响

  - 高可用生成式推荐链路（如Semantic ID生成、用户意图推理）的冗余设计，优先保障单步注意力计算的完整性，比分散资源做多步备份的投入产出比更高'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM鲁棒性研究多基于均匀i.i.d.噪声假设，但实际推理场景中常出现集中式注意力头失效（如硬件局部故障、量化误差集中、流量峰值导致的局部计算资源不足），而自回归推理的链式依赖特性可能放大这类集中故障的影响，两类故障模式的效果差异尚未被明确量化。

### 方法关键点
- 测试两个8B开源模型：Qwen3-8B、LLaMA-3.1-8B-Instruct，实验仅屏蔽模型上层的注意力头，避免干扰底层语义表征
- 对比两种等预算的注意力丢弃策略：集中式突发丢弃（短时间内屏蔽大量注意力头）、分散式i.i.d.丢弃（头屏蔽均匀分布在所有推理步），通过分层分位数匹配保证两组总丢弃头数完全一致
- 新增因子分解实验，拆分单步丢弃密度、多步连续丢弃两个变量的独立影响，采用配对McNemar检验做显著性验证

### 关键结果
- 基准参数B=0.10下，Qwen3-8B在集中式丢弃下GSM8K准确率为78.8%，比分散式的91.2%低12.4pp；LLaMA-3.1-8B-Instruct从84.0%降到76.8%，低7.2pp，两者均达统计显著性
- 因子分解实验显示，Qwen上单步高密丢弃带来10.0pp的准确率下降，是主要影响因素，多步连续丢弃的叠加效应统计上不显著
- Qwen的故障90%以上是推导过程错误，LLaMA的故障有22.2%是输出格式缺失

### 核心结论
自回归多步推理对集中式单点注意力故障的敏感度远高于同等量级的分散式噪声，故障抗性优化要优先保障单步的注意力计算完整性。
