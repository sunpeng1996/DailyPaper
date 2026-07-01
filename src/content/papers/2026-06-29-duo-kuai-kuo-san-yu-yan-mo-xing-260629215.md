---
title: Multi-Block Diffusion Language Models
title_zh: 多块扩散语言模型
authors:
- Yijie Jin
- Jiajun Xu
- Yuxuan Liu
- Chenkai Xu
- Yi Tu
- Jiajun Li
- Dandan Tu
- Xiaohui Yan
- Kai Yu
- Pengfei Liu
affiliations:
- Shanghai Jiao Tong University
- Xi'an Jiao Tong University
- Huawei
arxiv_id: '2606.29215'
url: https://arxiv.org/abs/2606.29215
pdf_url: https://arxiv.org/pdf/2606.29215
published: '2026-06-29'
collected: '2026-07-01'
category: LLM
direction: 扩散语言模型 · 并行解码效率优化
tags:
- Diffusion LM
- Parallel Decoding
- KV Cache
- Teacher Forcing
- CUDA Graph
one_liner: 提出多块教师强迫后训练与块缓冲推理引擎，大幅提升扩散语言模型解码并行度且精度损失极小
practical_value: '- 生成式推荐/Agent场景用扩散模型做文案、Semantic ID生成时，可直接复用MultiTF后训练方法，仅需少量微调就能提升70%+的解码并行度，几乎不损失生成质量，适配高并发低延迟需求

  - Block Buffer静态输入适配trick可直接迁移到所有迭代式生成模型的推理引擎，解决动态输入长度无法用CUDA Graph优化的问题，把并行度转化为实际TPS提升

  - 训练-推理对齐思路可复用：针对推理时的状态特征设计对应的训练数据分布，不需要全量重训，后训练即可大幅提升特定推理模式下的效果，落地成本极低'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有Block Diffusion Language Models（BD-LMs）支持KV缓存与动态长度生成，但原生单块解码逐块串行，存在KV缓存存储气泡，无法利用块间并行度；此前的扩散强迫训练策略支持多块解码，但训练状态与实际推理场景不匹配，精度损失大，且动态输入形状无法适配CUDA Graph优化，难以将并行度转化为实际吞吐量。

### 方法关键点
- 设计多块教师强迫（MultiTF）后训练策略，构造有限长度噪声组模拟推理时的bounded运行集，搭配链式均匀噪声调度生成异质槽位噪声模式，匹配推理时的噪声分布，减少训练-推理偏移
- 采用Group-Aware Dual-Stream Mask，保证噪声组内块间可见，同时所有块依赖干净前缀上下文，兼容原有BD-LM的KV缓存逻辑
- 推理侧引入Block Buffer机制，用固定数量的槽位封装动态运行集，将动态输入转化为静态形状，支持CUDA Graph捕获回放，同时实现解码与KV缓存存储并行，保留前缀缓存复用能力

### 关键结果
在GSM8K、MATH500、MBPP+、HumanEval+基准测试：
- MBD-LLaDA2-Mini平均每前向传播生成token数（TPF）从3.47提升至6.19（+78.4%），平均精度从79.95%提升至81.03%
- 搭配DMax加速策略的MBD-LLaDA2-Mini-DMax平均TPF达9.34，仅损失1.02%精度，实际吞吐量（TPS）较基准提升19%

**最值得记住的一句话**：扩散类生成模型的并行解码收益落地，必须同时做算法侧的训练-推理状态对齐与工程侧的静态输入适配，才能把理论并行度转化为实际的吞吐量提升
