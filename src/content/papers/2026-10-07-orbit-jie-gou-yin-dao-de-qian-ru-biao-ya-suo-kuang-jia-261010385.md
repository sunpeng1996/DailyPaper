---
title: 'OrBIT: Structure-Guided Embedding Compression'
title_zh: OrBIT：结构引导的嵌入表压缩框架
authors:
- Yunied Puig
- Amit Kumar Jaiswal
affiliations:
- Jay Chaudhry Software Innovation Centre
- Indian Institute of Technology (BHU)
arxiv_id: '2610.10385'
url: https://arxiv.org/abs/2610.10385
pdf_url: https://arxiv.org/pdf/2610.10385
published: '2026-10-07'
collected: '2026-10-08'
category: LLM
direction: LLM 嵌入表压缩优化
tags:
- Embedding Compression
- LLM
- Quantization
- Codec
- Orbit Dynamics
one_liner: 基于轨道动力学学习局部几何约束共享码字，实现LLM嵌入表超高压缩率
practical_value: '- 推荐/广告系统大模型的用户/物品嵌入表内存占比过高时，可复用OrBIT的轨道几何约束+残差导向码字分配思路，在保证召回/排序精度的前提下降低内存开销，适配端侧/边缘侧部署场景

  - 冗余紧帧粘合机制可直接迁移到多视角嵌入融合场景，通过重叠视图的误差抵消特性，在不增加存储成本的前提下降低2%-4%的重建误差

  - 编码器端构造的复杂轨道结构可完全编译丢弃、仅保留轻量解码器的设计思路，适合推理侧算力受限的线上推荐/广告排序链路，不会增加推理延迟'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

### 动机
LLM的嵌入表是核心内存开销来源，现有压缩方法（如PQ、AQ）均预先固定编码几何结构（坐标块、低秩子空间、无约束码本）再优化，无法自适应数据本身的结构特征，压缩率和重建精度的tradeoff存在明显瓶颈。

### 方法关键点
- 引入轨道动力学思想，从少量锚点生成轨道字典与局部支架，约束共享码字的生成空间，大幅降低码本存储开销
- 采用冗余紧帧分析系统与粘合机制，重叠视图下可抵消80%-99%的局部重建误差，进一步降低全局失真
- 基于全局残差的码字调度策略，优先给残差最大的视图分配编码预算；编码完成后所有轨道相关构造状态可完全编译丢弃，仅保留轻量解码器
- 支持支架对齐的后粘合优化，固定存储预算下可进一步降低2.7%-4.1%的重建误差

### 关键结果
在GPT-2、Llama-2-7B、Mistral-7B等4个模型的嵌入表上验证，对比PQ、OPQ、AQ等基线，GPT-2嵌入表压缩率达37.9×，7B级模型嵌入表压缩率均超23×，重建精度优于无约束加性量化（AQ），与成熟的乘积量化（PQ）基线效果相当。

**最值得记住的一句话**：不需要为了更高的压缩率牺牲重建精度，从数据中自适应学习编码几何结构的压缩框架，能在相同存储预算下取得比预先固定结构的方法更优的效果。
