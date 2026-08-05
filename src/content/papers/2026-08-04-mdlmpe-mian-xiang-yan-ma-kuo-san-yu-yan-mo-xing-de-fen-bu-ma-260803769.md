---
title: 'MDLMPE: Distribution Aware Positional Encoding for Masked Diffusion Language
  Models'
title_zh: MDLMPE：面向掩码扩散语言模型的分布感知位置编码
authors:
- Tong Ling
- Hang Lei
- Feng Xiao
- Changhui Sun
- Jiahang Xie
- Hao Liu
- Lu Liu
- Yanlong Du
affiliations:
- University Chinese Academic of Science
- HUJING Digital Media & Entertainment Group
- State Key Laboratory for Novel Software Technology, Nanjing University
- School of Data Science, Fudan University
arxiv_id: '2608.03769'
url: https://arxiv.org/abs/2608.03769
pdf_url: https://arxiv.org/pdf/2608.03769
published: '2026-08-04'
collected: '2026-08-05'
category: LLM
direction: LLM位置编码优化 · 掩码扩散模型
tags:
- Positional Encoding
- RoPE
- Masked Diffusion Language Model
- LLaDA
- DREAM
one_liner: 针对掩码扩散语言模型动态非连续掩码特点，提出分布感知位置编码，在RoPE基础上全面提升多场景性能
practical_value: '- 落地MDLM做生成式推荐/电商文案并行生成时，可直接用MDLMPE替换原有RoPE，无需改动主模型结构，仅通过SFT即可获得1-3pp的任务精度提升，适配低延迟生成场景

  - 动态掩码场景（如迭代式用户偏好补全、多轮Agent上下文动态填充）的位置编码设计，可复用「二进制掩码状态+高斯局部加权+余弦基投影」范式，显式将上下文可见性融入位置表示

  - 预训练模型增量适配时，可参考MDLMPE的渐进式激活策略：10%~90%训练步线性打开新增模块权重，避免破坏预训练表示，大幅降低适配风险

  - 用块扩散做长文本生成（如商品长描述、搜索结果长文案聚合）时，MDLMPE无需额外改造即可适配块级掩码模式，直接提升长序列生成一致性'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
掩码扩散语言模型（MDLM）支持并行生成、双向上下文建模，是替代自回归模型降本提效的核心方向，但传统RoPE等位置编码仅感知绝对/相对位置，无法适配MDLM去噪过程中动态变化、非连续的掩码分布：同一个位置的语义上下文会随周边掩码的揭示范式不断变化，传统位置编码无法捕捉这种结构，成为MDLM的性能瓶颈。
### 方法关键点
- 构造二进制可用性序列标记每个位置是否为掩码态，用目标中心的截断高斯加权聚合局部掩码分布，区分近远上下文贡献，默认窗口占序列长度3/16，高斯σ为窗口的1/4
- 用RoPE对齐的余弦基投影将加权后的掩码分布转换为分布感知特征，分两条路径注入：一条以门控残差方式加到Token embedding，另一条通过轻量MLP映射为角度偏移，调制一半RoPE的相位，保留另一半RoPE确保预训练兼容
- 训练时10%~90%步长线性激活MDLMPE调整模块，完全不改动原模型隐藏层、Tokenizer、降噪调度器，可直接适配现有预训练MDLM checkpoint
### 关键结果
在LLaDA-8B、DREAM-7B两个主流MDLM上验证，对比基线RoPE：SFT阶段MMLU最高提升1.6pp，HellaSwag最高提升2.8pp，HumanEval最高提升2.4pp；100M参数从零训练时，零样本困惑度最高比RoPE低16.3%；块扩散场景下，不同块大小的任务精度平均提升0.5~2pp。
### 核心结论
MDLM的位置编码不仅要感知位置顺序，还要显式建模当前去噪步的掩码分布结构，才能最大化双向建模的优势。
