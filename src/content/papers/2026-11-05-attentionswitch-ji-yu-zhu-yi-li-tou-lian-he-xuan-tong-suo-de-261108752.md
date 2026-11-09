---
title: 'AttentionSwitch: Jailbreak Defense for LLMs via Joint Learning of Sparse Attention-Head
  Selection and Scaling'
title_zh: AttentionSwitch：基于注意力头联合选通缩放的LLM越狱防御
authors:
- Doniyorkhon Obidov
- Honggang Yu
- Xiaolong Guo
- Kaichen Yang
affiliations:
- Michigan Technological University
- Miami University
- Lehigh University
arxiv_id: '2611.08752'
url: https://arxiv.org/abs/2611.08752
pdf_url: https://arxiv.org/pdf/2611.08752
published: '2026-11-05'
collected: '2026-11-09'
category: LLM
direction: LLM安全 · 越狱攻击防御
tags:
- Jailbreak Defense
- Attention Head
- Sparse Intervention
- Low-data Learning
- LLM Safety
one_liner: 冻结LLM下联合优化注意力头选择与动态缩放，低数据场景越狱防御效果优于现有方案
practical_value: '- 电商/广告Agent安全防护可快速复用：无需全量SFT，仅新增万级参数即可实现越狱防御，不破坏原模型生成能力，仅在prefill阶段干预，线上生成
  latency 增加不足3%，适合高并发场景落地

  - 推荐系统Transformer bad case优化可借鉴：针对违规内容排序、敏感推荐等问题，无需全量重训，仅选择20-30%的attention头做动态缩放，即可快速修正bad
  case，同时保留原有推荐效果

  - 小样本模型对齐可复用优化范式：用Gumbel-Softmax实现离散选择（如选干预头、选特征）和干预强度的联合优化，比先选点再优化的两步法效果提升4%以上，适合小样本场景下的定制化对齐

  - 低代价安全对齐选型参考：仅需30条标注样本即可实现96%+的攻击拒答率，远优于同数据量下LoRA-SFT的效果，适合资源不足的中小团队快速做模型安全加固'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
现有LLM越狱防御方案存在两大痛点：全量SFT/RLHF成本高、易发生灾难性遗忘，大幅降低原模型性能；先选干预点再优化干预强度的两步法割裂了两者的关联，属于次优方案，低数据场景下效果极差。
### 方法关键点
- 冻结原LLM全部权重，仅新增两个轻量模块：稀疏attention头选择掩码、query关联的头输出缩放因子，总参数量仅为万级，占原模型参数占比不足0.0004%
- 缩放因子由当前头的query向量预测，对整个头输出做统一标量缩放，仅改变表征幅度不改变方向，最大程度保留原模型的语义理解与生成能力
- 用Gumbel-Softmax实现Top-K头选择的可微松弛，支持头选择和缩放的端到端联合优化；训练分三阶段：全头初始化缩放参数、联合优化选点与缩放、固定选点后微调缩放参数
### 关键实验
在Llama-3.1、DeepSeek、Vicuna等5款主流开源LLM上测试，对比SFT、LoRA-SFT、ASGuard、DDPO等基线：30条小样本训练时，攻击拒答率（ARR）达96.58%，比SFT高0.44pct，benign通过率（BPR）达97.68%，远高于SFT的24.64%，MMLU几乎无下降；120条样本时ARR达99.05%，生成延迟仅比原模型高5ms左右。
### 核心结论
对Transformer的稀疏注意力头做联合选通和动态缩放，是低代价平衡模型原生能力与安全对齐的有效路径。
